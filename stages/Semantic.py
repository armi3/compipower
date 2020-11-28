import json
from nested_lookup import nested_lookup
from stages import Parser

simples_list = []
semantic_errors = []
referenced_locations_ids = []
referenced_locations_lines = []
new_scope_lines = []


def get_nested_simples(ast, list_name, simple_name, d):
    if list_name in ast:
        get_nested_simples(ast[list_name], list_name, simple_name, d)

    if simple_name in ast:
        simples_list.append(ast[simple_name])


def restructure_nested_lists(ast, list_name, simple_name, d):
    global simples_list
    if list_name in ast:
        get_nested_simples(ast, list_name, simple_name, d)

        if d and len(simples_list) > 0:
            print('\n🐣 Nested {}:'.format(list_name))
            for element in simples_list:
                print(element)

        ast[list_name] = {}
        new_list = {}

        for i in range(0, len(simples_list)):
            new_list[i] = simples_list[i]

        ast[list_name] = new_list
        simples_list = []

        if d and ast[list_name]:
            print("🐣 New AST['{}'] = {}\n".format(list_name, ast[list_name]))
    return ast


def restructure_deeply_nested_lists(ast, list_name, simple_name, d):
    for key, content in ast.items():
        if key == list_name and content != {}:
            ast = restructure_nested_lists(ast, list_name, simple_name, d)
        elif type(content) is dict:
            restructure_deeply_nested_lists(ast[key], list_name, simple_name, d)
    return ast


def reorganize_ast(ast, d):
    print('✂️ Reorganizing and trimming the AST for analysis ... ')

    ast = restructure_nested_lists(ast, 'method_decl_list', 'method_decl', d)
    ast = restructure_nested_lists(ast, 'field_decl_list', 'field_decl', d)
    ast = restructure_deeply_nested_lists(ast, 'statement_list', 'statement', d)
    ast = restructure_deeply_nested_lists(ast, 'method_arg_list', 'method_arg', d)
    ast = restructure_deeply_nested_lists(ast, 'callout_arg_list', 'callout_arg', d)

    if d:
        print('\n🌳 Trimmed AST = {}\n'.format(ast))
    return ast


def check_main(ast, d):
    print("🧠️ Checking if there's one main method at most ...")
    results = nested_lookup(key='id', document=ast, wild=False)
    if d and results:
        print("💬 Every id: {}".format(results))
    if 'RW_MAIN' in results:
        print("✅ Passed check_main!")
    else:
        print("❌ Failed check_main!")
        semantic_errors.append("More than one main method declared.")


def check_voids(ast, d):
    for key, content in ast.items():
        if type(content) is dict and 'var_type' in content and ast[key]['var_type'] == 'RW_VOID':
            results = nested_lookup(key='return_expr', document=content, wild=False)
            if d and results:
                print("💬 Every return_expr: {}".format(results))
            if not results:
                print("✅ Method in line {} passed check_voids!".format(ast[key]['line_num']))
            else:
                print("❌ Method in line {} failed check_voids!".format(ast[key]['line_num']))
                semantic_errors.append(
                    "Method declared as void in line {} but has a return statement.".format(ast[key]['line_num']))
        elif type(content) is dict:
            check_voids(ast[key], d)


def check_return_types(ast, d):
    pass


def check_referenced(ast, d):
    for key, content in ast.items():
        if type(content) is dict and 'location' in content:
            this_location_id = content['location']['id']
            referenced_locations_ids.append(this_location_id)
            referenced_locations_lines.append(content['location']['line_num'])
            if d:
                print('💬 this_location_id:   {}'.format(this_location_id))
                print('💬 location line:      {}'.format(content['location']['line_num']))
        elif type(content) is dict:
            check_referenced(ast[key], d)


def check_declared(ast, d):
    check_referenced(ast, d)
    global referenced_locations_lines
    global referenced_locations_ids
    if d:
        print('💬 referenced_locations_ids:   {}'.format(referenced_locations_ids))
        print('💬 referenced_locations_lines: {}'.format(referenced_locations_ids))
    results = nested_lookup(key='field_decl', document=ast, wild=True)

    for i in range(0, len(referenced_locations_ids)):
        declared = False

        for j in range(0, len(results)):
            if 'id' in results[j]:
                if referenced_locations_ids[i] == results[j]['id']:
                    print("✅ Location in line {} with id '{}' passed check_declared!".format(
                        referenced_locations_lines[i], referenced_locations_ids[i]))
                    declared = True
            elif 0 in results[j]:
                for key, content in results[j].items():
                    if d and content:
                        print('💬 content in results[j].items():  ', content)
                    if 'id' in content:
                        if referenced_locations_ids[i] == content['id']:
                            print("✅ Location in line {} with id '{}' passed check_declared!".format(
                                referenced_locations_lines[i], referenced_locations_ids[i]))
                            declared = True
                    elif 'id_list' in content:
                        for key2 in content['id_list']:
                            if referenced_locations_ids[i] == content['id_list'][key2]:
                                print("✅ Location in line {} with id '{}' passed check_declared!".format(
                                    referenced_locations_lines[i], referenced_locations_ids[i]))
                                declared = True
    if not declared:
        print("❌ Location in line {} with id '{}' failed check_declared!".format(referenced_locations_lines[i],
                                                                                 referenced_locations_ids[i]))
        semantic_errors.append("Location referenced in line {} with id '{}' was not declared properly.".format(
            referenced_locations_lines[i], referenced_locations_ids[i]))


def remove_id_lists1(ast, d):
    # for id_lists inside the field_decl_list
    new_field_decls = []
    print('✂️ Flattening field declarations in the AST ... ')
    for key, content in ast['field_decl_list'].items():
        if d:
            print("🔑 Field declaration {}:       '{}'".format(key, content))
        if 'id_list' in content:
            for k, id in ast['field_decl_list'][key]['id_list'].items():
                if type(k) is int:
                    new_field_decl = {'var_type': ast['field_decl_list'][key]['var_type'],
                                      'id': id,
                                      'line_num': ast['field_decl_list'][key]['id_list']['line_num']}
                    new_field_decls.append(new_field_decl)
                    if d:
                        print("     🔑 Nested id           = {}:'{}'".format(k, id))
                        print('     ✨ As new field_decl   = {}'.format(new_field_decl))
        elif 'id' in content:
            new_field_decls.append(content)
    ast['field_decl_list'].clear()
    for i in range(0, len(new_field_decls)):
        ast['field_decl_list'][i] = new_field_decls[i]
    if d:
        print("\n✨ Flattened AST['field_decl_list'] = {}".format(ast['field_decl_list']))
        print("✨ Current AST = {}\n".format(ast))
    return ast


def remove_id_lists2(ast, d):
    # for id_lists inside a field_decl in a var_list
    print('✂️ Flattening local variable declarations in the AST ... ')
    for key, content in ast['method_decl_list'].items():
        new_var_decls = []

        if d:
            print('🔑 Method key: {}'.format(key))

        if 'block' in content:
            if 'var_list' in content['block']:
                # will only have one id or one id_list (two ids)
                if d:
                    print("     🔑 Method has local variables declared. ")
                    print("     🔑 Method['id']     =  {}".format(content['id']))
                    print("     🔑 Method['block']  =  {}".format(content['block']))

                if 'id_list' in content['block']['var_list']['field_decl']:
                    for k in content['block']['var_list']['field_decl']['id_list']:
                        if type(k) is int:
                            new_var_decl = {'var_type': content['block']['var_list']['field_decl']['var_type'],
                                            'id': content['block']['var_list']['field_decl']['id_list'][k],
                                            'line_num': content['block']['var_list']['field_decl']['id_list']['line_num']}
                            new_var_decls.append(new_var_decl)
                    if d:
                        print('     ✨ New var_decls[]  =  {}\n'.format(new_var_decls))
                    content['block']['var_list'].clear()
                    for i in range(0, len(new_var_decls)):
                        content['block']['var_list'][i] = new_var_decls[i]

                elif 'id' in content['block']['var_list']['field_decl']:
                    new_var_decl = content['block']['var_list']['field_decl']
                    content['block']['var_list'].clear()
                    content['block']['var_list'][0] = new_var_decl
                    if d:
                        print('     ✨ New var_decl     =  {}\n'.format(new_var_decl))
            else:
                if d:
                    print("     🔐 Method has no local variables declared.\n")
    return ast


def build_symbol_table(ast, d):
    print('💬 Building symbol table ... ')
    get_new_scope_lines(ast, d)


def get_new_scope_lines(ast, d):
    for key, content in ast.items():
        if key == list_name and content != {}:
            ast = restructure_nested_lists(ast, list_name, simple_name, d)
        elif type(content) is dict:
            restructure_deeply_nested_lists(ast[key], list_name, simple_name, d)
    return new_scope_lines


def check_uniqueness(ast, d):
    pass


def check_assign_types(ast, d):
    pass


def semantic(file_name, debug_list):
    ast = Parser.parse(file_name, debug_list)
    if ast:
        print('\n🧠️ Starting semantic analysis ... ')
        debug_semantic = debug_list[2]
        reorganized_ast = reorganize_ast(ast, debug_semantic)

        check_main(reorganized_ast, debug_semantic)
        print("🧠️ Checking if void methods have no return statements ...")
        check_voids(reorganized_ast, debug_semantic)
        check_return_types(reorganized_ast, debug_semantic)
        print("🧠️ Checking if every instance was declared ...")
        check_declared(reorganized_ast, debug_semantic)

        reorganized_ast = remove_id_lists1(reorganized_ast, debug_semantic)
        reorganized_ast = remove_id_lists2(reorganized_ast, debug_semantic)
        print('🌳 A lovely, slimmer and decorated AST = {}'.format(reorganized_ast))

        print("🧠️ Starting type and scope analysis ...")
        symbol_table = build_symbol_table(reorganized_ast, debug_semantic)
        check_uniqueness(reorganized_ast, debug_semantic)
        check_assign_types(reorganized_ast, debug_semantic)

        if len(semantic_errors) == 0:
            print('➡️ Passing decorated AST to next phase ... ')
            return reorganized_ast
        else:
            print('🛠 The following semantic errors were detected:')
            for i in range(0, len(semantic_errors)):
                print('{}:    {}'.format(i, semantic_errors[i]))
            return {}
    else:
        return {}