from model import DFA_parser, Token
from stages import Lexer
import json


def syntax_analysis(token_stream, build_ast, d):
    token_stream.append(Token.Token('$', '$', '', 0))  # append $
    for current_token in token_stream:  # pop comments
        if current_token.token == 'COMMENT':
            if d:
                print('Comment in line ', current_token.line_num, ' was popped.')
            token_stream.remove(current_token)

    state_stack = [0]
    token_stack = []
    full_token_stack = []
    dict_stack = []

    state_type = ''
    state = 0
    dfa_input = ''
    syntax_error = False
    decaf_class = {}

    i = 0
    input_length = len(token_stream)
    while i < input_length:
        if d and not build_ast:
            print('\n🧮 i: ', i,
                  '\n(this) dfa_input:      ', dfa_input,
                  '\n(this) state:          ', state)
        if i == 0:
            state_type, state = DFA_parser.start(token_stream[i].token, 0)
        else:
            state_type, state = DFA_parser.start(dfa_input, state)
        if d and not build_ast:
            print('(result) state_type:   ', state_type,
                  '\n(result) state:        ', state)

        if state_type == 'shift':
            # add token to stack
            token_stack.append(token_stream[i].token)
            full_token_stack.append(token_stream[i])
            # add next state to stack
            state_stack.append(state)
            i += 1
            dfa_input = token_stream[i].token

        elif state_type == 'reduce':
            # reduce each case by foot
            # r0   $accept -> class $end
            if state == 0:
                # pop
                token_stack.pop()  # $end
                token_stack.pop()  # class
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('accept')
                # variable state used as production number

            # r1 class -> RW_CLASS ID BRACE_L BRACE_R
            elif state == 1:
                # pop
                token_stack.pop()  # BRACE_R
                token_stack.pop()  # BRACE_L
                token_stack.pop()  # ID
                token_stack.pop()  # RW_CLASS
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('class')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # BRACE_R
                    full_token_stack.pop()  # BRACE_L
                    id = full_token_stack.pop()  # ID
                    full_token_stack.pop()  # RW_CLASS
                    decaf_class['id'] = id.lexeme

            # r2 class -> RW_CLASS ID BRACE_L field_decl_list BRACE_R
            elif state == 2:
                # pop
                token_stack.pop()  # BRACE_R
                token_stack.pop()  # field_decl_list
                token_stack.pop()  # BRACE_L
                token_stack.pop()  # ID
                token_stack.pop()  # RW_CLASS
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('class')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # BRACE_R
                    full_token_stack.pop()  # BRACE_L
                    id = full_token_stack.pop()  # ID
                    full_token_stack.pop()  # RW_CLASS
                    decaf_class['id'] = id.lexeme
                    decaf_class['field_decl_list'] = dict_stack.pop()

            # r3 class -> RW_CLASS ID BRACE_L method_decl_list BRACE_R
            elif state == 3:
                # pop
                token_stack.pop()  # BRACE_R
                token_stack.pop()  # method_decl_list
                token_stack.pop()  # BRACE_L
                token_stack.pop()  # ID
                token_stack.pop()  # RW_CLASS
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('class')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # BRACE_R
                    full_token_stack.pop()  # BRACE_L
                    id = full_token_stack.pop()  # ID
                    full_token_stack.pop()  # RW_CLASS
                    decaf_class['id'] = id.lexeme
                    decaf_class['method_decl_list'] = dict_stack.pop()

            # r4 class -> RW_CLASS ID BRACE_L field_decl_list method_decl_list BRACE_R
            elif state == 4:
                # pop
                token_stack.pop()  # BRACE_R
                token_stack.pop()  # method_decl_list
                token_stack.pop()  # field_decl_list
                token_stack.pop()  # BRACE_L
                token_stack.pop()  # ID
                token_stack.pop()  # RW_CLASS
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('class')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # BRACE_R
                    full_token_stack.pop()  # BRACE_L
                    id = full_token_stack.pop()  # ID
                    full_token_stack.pop()  # RW_CLASS
                    decaf_class['id'] = id.lexeme
                    decaf_class['method_decl_list'] = dict_stack.pop()
                    decaf_class['field_decl_list'] = dict_stack.pop()

            # r5 field_decl_list -> field_decl_list field_decl
            elif state == 5:
                # pop
                token_stack.pop()  # field_decl
                token_stack.pop()  # field_decl_list
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('field_decl_list')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    field_decl = dict_stack.pop()  # field_decl
                    sub_field_decl_list = dict_stack.pop()  # field_decl_list
                    field_decl_list = {'field_decl_list': sub_field_decl_list, 'field_decl': field_decl}
                    dict_stack.append(field_decl_list)

            # r6 field_decl_list -> field_decl
            elif state == 6:
                # pop
                token_stack.pop()  # field_decl
                state_stack.pop()
                # reduction
                token_stack.append('field_decl_list')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    field_decl = dict_stack.pop()  # field_decl
                    field_decl_list = {'field_decl': field_decl}
                    dict_stack.append(field_decl_list)

            # r7 method_decl_list -> method_decl_list method_decl
            elif state == 7:
                # pop
                token_stack.pop()  # method_decl
                token_stack.pop()  # method_decl_list
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('method_decl_list')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    method_decl = dict_stack.pop()  # method_decl
                    sub_method_decl_list = dict_stack.pop()  # method_decl_list
                    method_decl_list = {'method_decl_list': sub_method_decl_list,
                                        'method_decl': method_decl}
                    dict_stack.append(method_decl_list)

            # r8 method_decl_list -> method_decl
            elif state == 8:
                # pop
                token_stack.pop()  # method_decl
                state_stack.pop()
                # reduction
                token_stack.append('method_decl_list')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    method_decl = dict_stack.pop()  # method_decl
                    method_decl_list = {'method_decl': method_decl}
                    dict_stack.append(method_decl_list)

            # r9 field_decl -> var_type ID SEMICOLON
            elif state == 9:
                # pop
                token_stack.pop()  # SEMICOLON
                token_stack.pop()  # ID
                token_stack.pop()  # var_type
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('field_decl')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # SEMICOLON
                    id = full_token_stack.pop()  # ID
                    var_type = dict_stack.pop()  # var_type
                    field_decl = {'var_type': var_type,
                                  'id': id.lexeme,
                                  'line_num': id.line_num}
                    dict_stack.append(field_decl)

            # field_decl -> var_type id_list SEMICOLON
            elif state == 10:
                # pop
                token_stack.pop()  # SEMICOLON
                token_stack.pop()  # id_list
                token_stack.pop()  # var_type
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('field_decl')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # SEMICOLON
                    id_list = dict_stack.pop()  # id_list
                    var_type = dict_stack.pop()  # var_type
                    field_decl = {'var_type': var_type,
                                  'id_list': id_list}
                    dict_stack.append(field_decl)

            # id_list -> ID COMMA ID
            elif state == 11:
                # pop
                token_stack.pop()  # ID
                token_stack.pop()  # COMMA
                token_stack.pop()  # ID
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('id_list')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    id2 = full_token_stack.pop()  # ID
                    full_token_stack.pop()  # SEMICOLON
                    id1 = full_token_stack.pop()  # ID
                    id_list = {1: id1.lexeme,
                               2: id2.lexeme,
                               'line_num': id1.line_num}
                    dict_stack.append(id_list)

            # var_type -> VT_INTEGER
            elif state == 12:
                # pop
                token_stack.pop()  # VT_INTEGER
                state_stack.pop()
                # reduction
                token_stack.append('var_type')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # VT_INTEGER
                    dict_stack.append('VT_INTEGER')

            # var_type -> VT_BOOLEAN
            elif state == 13:
                # pop
                token_stack.pop()  # VT_BOOLEAN
                state_stack.pop()
                # reduction
                token_stack.append('var_type')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # VT_BOOLEAN
                    dict_stack.append('VT_BOOLEAN')

            # method_decl -> var_type ID PARENTHESIS_L PARENTHESIS_R block
            elif state == 14:
                # pop
                token_stack.pop()  # block
                token_stack.pop()  # PARENTHESIS_R
                token_stack.pop()  # PARENTHESIS_L
                token_stack.pop()  # ID
                token_stack.pop()  # var_type
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('method_decl')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    block = dict_stack.pop()  # block
                    full_token_stack.pop()  # PARENTHESIS_R
                    full_token_stack.pop()  # PARENTHESIS_L
                    id = full_token_stack.pop()  # ID
                    var_type = dict_stack.pop()  # var_type
                    method_decl = {'var_type': var_type,
                                   'id': id.lexeme,
                                   'block': block,
                                   'line_num': id.line_num}
                    dict_stack.append(method_decl)

            # method_decl -> var_type ID PARENTHESIS_L method_arg_list PARENTHESIS_R block
            elif state == 15:
                # pop
                token_stack.pop()  # block
                token_stack.pop()  # PARENTHESIS_R
                token_stack.pop()  # method_arg_list
                token_stack.pop()  # PARENTHESIS_L
                token_stack.pop()  # ID
                token_stack.pop()  # var_type
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('method_decl')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    block = dict_stack.pop()  # block
                    full_token_stack.pop()  # PARENTHESIS_R
                    method_arg_list = dict_stack.pop()  # method_arg_list
                    full_token_stack.pop()  # PARENTHESIS_L
                    id = full_token_stack.pop()  # ID
                    var_type = dict_stack.pop()  # var_type
                    method_decl = {'var_type': var_type,
                                   'id': id.lexeme,
                                   'method_arg_list': method_arg_list,
                                   'block': block,
                                   'line_num': id.line_num}
                    dict_stack.append(method_decl)

            # method_decl -> RW_VOID ID PARENTHESIS_L PARENTHESIS_R block
            elif state == 16:
                # pop
                token_stack.pop()  # block
                token_stack.pop()  # PARENTHESIS_R
                token_stack.pop()  # PARENTHESIS_L
                token_stack.pop()  # ID
                token_stack.pop()  # RW_VOID
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('method_decl')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    block = dict_stack.pop()  # block
                    full_token_stack.pop()  # PARENTHESIS_R
                    full_token_stack.pop()  # PARENTHESIS_L
                    id = full_token_stack.pop()  # ID
                    full_token_stack.pop()  # RW_VOID
                    method_decl = {'var_type': 'RW_VOID',
                                   'id': id.lexeme,
                                   'block': block,
                                   'line_num': id.line_num}
                    dict_stack.append(method_decl)

            # method_decl -> RW_VOID ID PARENTHESIS_L method_arg_list PARENTHESIS_R block
            elif state == 17:
                # pop
                token_stack.pop()  # block
                token_stack.pop()  # PARENTHESIS_R
                token_stack.pop()  # method_arg_list
                token_stack.pop()  # PARENTHESIS_L
                token_stack.pop()  # ID
                token_stack.pop()  # RW_VOID
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('method_decl')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    block = dict_stack.pop()  # block
                    full_token_stack.pop()  # PARENTHESIS_R
                    method_arg_list = dict_stack.pop()  # method_arg_list
                    full_token_stack.pop()  # PARENTHESIS_L
                    id = full_token_stack.pop()  # ID
                    full_token_stack.pop()  # RW_VOID
                    method_decl = {'var_type': 'RW_VOID',
                                   'id': id.lexeme,
                                   'method_arg_list': method_arg_list,
                                   'block': block,
                                   'line_num': id.line_num}
                    dict_stack.append(method_decl)

            # r18 method_decl -> RW_VOID RW_MAIN PARENTHESIS_L PARENTHESIS_R block
            elif state == 18:
                # pop
                token_stack.pop()  # block
                token_stack.pop()  # PARENTHESIS_R
                token_stack.pop()  # PARENTHESIS_L
                token_stack.pop()  # RW_MAIN
                token_stack.pop()  # RW_VOID
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('method_decl')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    block = dict_stack.pop()  # block
                    full_token_stack.pop()  # PARENTHESIS_R
                    full_token_stack.pop()  # PARENTHESIS_L
                    rw_main = full_token_stack.pop()  # RW_MAIN
                    full_token_stack.pop()  # RW_VOID
                    method_decl = {'var_type': 'RW_VOID',
                                   'id': 'RW_MAIN',
                                   'block': block,
                                   'line_num': rw_main.line_num}
                    dict_stack.append(method_decl)

            # r19 method_arg_list -> method_arg_list COMMA method_arg
            elif state == 19:
                # pop
                token_stack.pop()  # method_arg
                token_stack.pop()  # COMMA
                token_stack.pop()  # method_arg_list
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('method_arg_list')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    method_arg = dict_stack.pop()  # method_arg
                    full_token_stack.pop()  # COMMA
                    sub_method_arg_list = dict_stack.pop()  # method_arg_list
                    method_arg_list = {'method_arg_list': sub_method_arg_list,
                                       'method_arg': method_arg}
                    dict_stack.append(method_arg_list)

            # r20 method_arg_list -> method_arg
            elif state == 20:
                # pop
                token_stack.pop()  # method_arg
                state_stack.pop()
                # reduction
                token_stack.append('method_arg_list')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    method_arg = dict_stack.pop()  # method_arg
                    method_arg_list = {'method_arg': method_arg}
                    dict_stack.append(method_arg_list)

            # r21 method_arg -> var_type ID
            elif state == 21:
                # pop
                token_stack.pop()  # ID
                token_stack.pop()  # var_type
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('method_arg')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    id = full_token_stack.pop()  # ID
                    var_type = dict_stack.pop()  # var_type
                    method_arg = {'id': id.lexeme,
                                  'var_type': var_type}
                    dict_stack.append(method_arg)

            # r22 block -> BRACE_L BRACE_R
            elif state == 22:
                # pop
                token_stack.pop()  # BRACE_R
                token_stack.pop()  # BRACE_L
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('block')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # BRACE_R
                    full_token_stack.pop()  # BRACE_L
                    block = {}
                    dict_stack.append(block)

            # r23 block -> BRACE_L var_list BRACE_R
            elif state == 23:
                # pop
                token_stack.pop()  # BRACE_R
                token_stack.pop()  # var_list
                token_stack.pop()  # BRACE_L
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('block')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # BRACE_R
                    var_list = dict_stack.pop()  # var_list
                    full_token_stack.pop()  # BRACE_L
                    block = {'var_list': var_list}
                    dict_stack.append(block)

            # r24 block -> BRACE_L statement_list BRACE_R
            elif state == 24:
                # pop
                token_stack.pop()  # BRACE_R
                token_stack.pop()  # statement_list
                token_stack.pop()  # BRACE_L
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('block')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # BRACE_R
                    statement_list = dict_stack.pop()  # statement_list
                    full_token_stack.pop()  # BRACE_L
                    block = {'statement_list': statement_list}
                    dict_stack.append(block)

            # r25 block -> BRACE_L var_list statement_list BRACE_R
            elif state == 25:
                # pop
                token_stack.pop()  # BRACE_R
                token_stack.pop()  # statement_list
                token_stack.pop()  # var_list
                token_stack.pop()  # BRACE_L
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('block')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # BRACE_R
                    statement_list = dict_stack.pop()  # statement_list
                    var_list = dict_stack.pop()  # var_list
                    full_token_stack.pop()  # BRACE_L
                    block = {'var_list': var_list,
                             'statement_list': statement_list}
                    dict_stack.append(block)

            # r26 var_list -> field_decl_list
            elif state == 26:
                # pop
                token_stack.pop()  # field_decl_list
                state_stack.pop()
                # reduction
                token_stack.append('var_list')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    field_decl_list = dict_stack.pop()  # field_decl_list
                    var_list = field_decl_list
                    dict_stack.append(var_list)

            # r27 statement_list -> statement_list statement
            elif state == 27:
                # pop
                token_stack.pop()  # statement
                token_stack.pop()  # statement_list
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('statement_list')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    statement = dict_stack.pop()  # statement
                    sub_statement_list = dict_stack.pop()  # statement_list
                    statement_list = {'statement_list': sub_statement_list,
                                      'statement': statement}
                    dict_stack.append(statement_list)

            # r28 statement_list -> statement
            elif state == 28:
                # pop
                token_stack.pop()  # statement
                state_stack.pop()
                # reduction
                token_stack.append('statement_list')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    statement = dict_stack.pop()  # statement
                    statement_list = statement
                    dict_stack.append(statement_list)

            # r29 statement -> location assign_op expr SEMICOLON
            elif state == 29:
                # pop
                token_stack.pop()  # SEMICOLON
                token_stack.pop()  # expr
                token_stack.pop()  # assign_op
                token_stack.pop()  # location
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('statement')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    semicolon = full_token_stack.pop()  # SEMICOLON
                    expr = dict_stack.pop()  # expr
                    assign_op = dict_stack.pop()  # assign_op
                    location = dict_stack.pop()  # location
                    statement = {'statement_type': 'assignment',
                                 'location': location,
                                 'assign_op': assign_op,
                                 'expr': expr,
                                 'line_num': semicolon.line_num}
                    dict_stack.append(statement)

            # r30 statement -> method_call SEMICOLON
            elif state == 30:
                # pop
                token_stack.pop()  # SEMICOLON
                token_stack.pop()  # method_call
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('statement')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # SEMICOLON
                    method_call = dict_stack.pop()  # method_call
                    statement = {'statement_type': 'method_call',
                                 'method_call': method_call}
                    dict_stack.append(statement)

            # r31 statement -> RW_IF PARENTHESIS_L expr PARENTHESIS_R block
            elif state == 31:
                # pop
                token_stack.pop()  # block
                token_stack.pop()  # PARENTHESIS_R
                token_stack.pop()  # expr
                token_stack.pop()  # PARENTHESIS_L
                token_stack.pop()  # RW_IF
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('statement')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    block = dict_stack.pop()  # block
                    parenthesis = full_token_stack.pop()  # PARENTHESIS_R
                    expr = dict_stack.pop()  # expr
                    full_token_stack.pop()  # PARENTHESIS_L
                    full_token_stack.pop()  # RW_IF
                    statement = {'statement_type': 'if',
                                 'line_num': parenthesis.line_num,
                                 'condition': expr,
                                 'block': block}
                    dict_stack.append(statement)

            # r32 statement -> RW_IF PARENTHESIS_L expr PARENTHESIS_R block RW_ELSE block
            elif state == 32:
                # pop
                token_stack.pop()  # block
                token_stack.pop()  # RW_ELSE
                token_stack.pop()  # block
                token_stack.pop()  # PARENTHESIS_R
                token_stack.pop()  # expr
                token_stack.pop()  # PARENTHESIS_L
                token_stack.pop()  # RW_IF
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('statement')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    block_else = dict_stack.pop()  # block (else)
                    full_token_stack.pop()  # RW_ELSE
                    block = dict_stack.pop()  # block
                    full_token_stack.pop()  # PARENTHESIS_R
                    expr = dict_stack.pop()  # expr
                    parenthesis = full_token_stack.pop()  # PARENTHESIS_L
                    full_token_stack.pop()  # RW_IF
                    statement = {'statement_type': 'if',
                                 'line_num': parenthesis.line_num,
                                 'condition': expr,
                                 'block': block,
                                 'else': block_else}
                    dict_stack.append(statement)

            # r33 statement -> RW_FOR ID ASSIGN expr COMMA expr block
            # for i=2, i>1 (el update se hace, o no, adentro)
            elif state == 33:
                # pop
                token_stack.pop()  # block
                token_stack.pop()  # expr
                token_stack.pop()  # COMMA
                token_stack.pop()  # expr
                token_stack.pop()  # ASSIGN
                token_stack.pop()  # ID
                token_stack.pop()  # RW_FOR
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('statement')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    block = dict_stack.pop()  # block
                    continuation_test = dict_stack.pop()  # expr
                    full_token_stack.pop()  # COMMA
                    initialization_expr = dict_stack.pop()  # expr
                    full_token_stack.pop()  # ASSIGN
                    id = full_token_stack.pop()  # ID
                    full_token_stack.pop()  # RW_FOR
                    initialization = {'id': id.lexeme,
                                      'expr': initialization_expr}
                    statement = {'statement_type': 'for',
                                 'initialization': initialization,
                                 'continuation_test': continuation_test,
                                 'block': block,
                                 'line_num': id.line_num}
                    dict_stack.append(statement)

            # r34 statement -> RW_RETURN SEMICOLON
            elif state == 34:
                # pop
                token_stack.pop()  # SEMICOLON
                token_stack.pop()  # RW_RETURN
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('statement')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # SEMICOLON
                    full_token_stack.pop()  # RW_RETURN
                    statement = {'statement_type': 'return'}
                    dict_stack.append(statement)

            # r35 statement -> RW_RETURN expr SEMICOLON
            elif state == 35:
                # pop
                token_stack.pop()  # SEMICOLON
                token_stack.pop()  # expr
                token_stack.pop()  # RW_RETURN
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('statement')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # SEMICOLON
                    expr = dict_stack.pop()  # expr
                    full_token_stack.pop()  # RW_RETURN
                    statement = {'statement_type': 'return',
                                 'return_expr': expr}
                    dict_stack.append(statement)

            # r36 statement -> RW_BREAK SEMICOLON
            elif state == 36:
                # pop
                token_stack.pop()  # SEMICOLON
                token_stack.pop()  # RW_BREAK
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('statement')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # SEMICOLON
                    full_token_stack.pop()  # RW_BREAK
                    statement = {'statement_type': 'break'}
                    dict_stack.append(statement)

            # r37 statement -> RW_CONTINUE SEMICOLON
            elif state == 37:
                # pop
                token_stack.pop()  # SEMICOLON
                token_stack.pop()  # RW_CONTINUE
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('statement')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # SEMICOLON
                    full_token_stack.pop()  # RW_CONTINUE
                    statement = {'statement_type': 'continue'}
                    dict_stack.append(statement)

            # r38 location -> ID
            elif state == 38:
                # pop
                token_stack.pop()  # ID
                state_stack.pop()
                # reduction
                token_stack.append('location')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    id = full_token_stack.pop()  # ID
                    location = {'id': id.lexeme,
                                'line_num': id.line_num}
                    dict_stack.append(location)

            # r39 location -> ID BRACKET_L expr BRACKET_R
            elif state == 39:
                # pop
                token_stack.pop()  # BRACKET_R
                token_stack.pop()  # expr
                token_stack.pop()  # BRACKET_L
                token_stack.pop()  # ID
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('location')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # BRACKET_R
                    expr = dict_stack.pop()  # expr
                    full_token_stack.pop()  # BRACKET_L
                    id = full_token_stack.pop()  # ID
                    location = {'id': id.lexeme,
                                'in_array': True,
                                'index_expr': expr,
                                'line_num': id.line_num}
                    dict_stack.append(location)

            # r40 assign_op -> ASSIGN
            elif state == 40:
                # pop
                token_stack.pop()  # ASSIGN
                state_stack.pop()
                # reduction
                token_stack.append('assign_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # ASSIGN
                    dict_stack.append('ASSIGN')

            # Abner Bab
            # r41 assign_op -> PLUS_ASSIGN
            elif state == 41:
                # pop
                token_stack.pop()  # PLUS_ASSIGN
                state_stack.pop()
                # reduction
                token_stack.append('assign_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # PLUS_ASSIGN
                    dict_stack.append('PLUS_ASSIGN')

            # r42 assign_op -> MINUS_ASSIGN
            elif state == 42:
                # pop
                token_stack.pop()  # MINUS_ASSIGN
                state_stack.pop()
                # reduction
                token_stack.append('assign_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # MINUS_ASSIGN
                    dict_stack.append('MINUS_ASSIGN')

            # r43 expr -> location
            elif state == 43:
                # pop
                token_stack.pop()  # location
                state_stack.pop()
                # reduction
                token_stack.append('expr')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    expr = dict_stack.pop()  # location
                    dict_stack.append(expr)

            # r44 expr -> method_call
            elif state == 44:
                # pop
                token_stack.pop()  # method_call
                state_stack.pop()
                # reduction
                token_stack.append('expr')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    expr = dict_stack.pop()  # method_call
                    dict_stack.append(expr)

            # r45 expr -> literal
            elif state == 45:
                # pop
                token_stack.pop()  # literal
                state_stack.pop()
                # reduction
                token_stack.append('expr')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    expr = dict_stack.pop()  # literal
                    dict_stack.append(expr)

            # r46 expr -> expr bin_op expr
            elif state == 46:
                # pop
                token_stack.pop()  # expr
                token_stack.pop()  # bin_op
                token_stack.pop()  # expr
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('expr')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    expr2 = dict_stack.pop()  # expr2
                    bin_op = dict_stack.pop()  # bin_op
                    expr1 = dict_stack.pop()  # expr1
                    expr = {'left_expr': expr1,
                            'bin_op': bin_op,
                            'right_expr': expr2}
                    dict_stack.append(expr)

            # r47   expr -> MINUS expr
            elif state == 47:
                # pop
                token_stack.pop()  # expr
                token_stack.pop()  # MINUS
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('expr')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    expr = dict_stack.pop()  # expr
                    full_token_stack.pop()  # MINUS
                    expr = {'expr': expr,
                            'un_op': 'MINUS'}
                    dict_stack.append(expr)

            # r48   expr -> NEGATION expr
            elif state == 48:
                # pop
                token_stack.pop()  # expr
                token_stack.pop()  # NEGATION
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('expr')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    expr = dict_stack.pop()  # expr
                    full_token_stack.pop()  # NEGATION
                    expr = {'expr': expr,
                            'un_op': 'NEGATION'}
                    dict_stack.append(expr)

            # r49 expr -> BRACE_L expr BRACE_R
            elif state == 49:
                # pop
                token_stack.pop()  # BRACE_R
                token_stack.pop()  # expr
                token_stack.pop()  # BRACE_L
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('expr')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # BRACE_R
                    expr = dict_stack.pop()  # expr
                    full_token_stack.pop()  # BRACE_L
                    dict_stack.append(expr)

            # r50 method_call -> ID PARENTHESIS_L expr_list PARENTHESIS_R
            elif state == 50:
                # pop
                token_stack.pop()  # PARENTHESIS_R
                token_stack.pop()  # expr_list
                token_stack.pop()  # PARENTHESIS_L
                token_stack.pop()  # ID
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('method_call')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # PARENTHESIS_R
                    expr_list = dict_stack.pop()  # expr_list
                    full_token_stack.pop()  # PARENTHESIS_L
                    id = full_token_stack.pop()  # ID
                    method_call = {'method_id': id.lexeme,
                                   'method_args': expr_list,
                                   'line_num': id.line_num}
                    dict_stack.append(method_call)

            # r51 method_call -> ID PARENTHESIS_L PARENTHESIS_R
            elif state == 51:
                # pop
                token_stack.pop()  # PARENTHESIS_R
                token_stack.pop()  # PARENTHESIS_L
                token_stack.pop()  # ID
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('method_call')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # PARENTHESIS_R
                    full_token_stack.pop()  # PARENTHESIS_L
                    id = full_token_stack.pop()  # ID
                    method_call = {'method_id': id.lexeme,
                                   'line_num': id.line_num}
                    dict_stack.append(method_call)

            # r52 method_call -> RW_CALLOUT PARENTHESIS_L PARENTHESIS_R
            elif state == 52:
                # pop
                token_stack.pop()  # PARENTHESIS_R
                token_stack.pop()  # PARENTHESIS_L
                token_stack.pop()  # RW_CALLOUT
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('method_call')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # PARENTHESIS_R
                    full_token_stack.pop()  # PARENTHESIS_L
                    rw_callout = full_token_stack.pop()  # RW_CALLOUT
                    method_call = {'method_id': 'empty_callout',
                                   'line_num': rw_callout.line_num}
                    dict_stack.append(method_call)

            # r53 method_call -> RW_CALLOUT PARENTHESIS_L STRING_LITERAL PARENTHESIS_R
            elif state == 53:
                # pop
                token_stack.pop()  # PARENTHESIS_R
                token_stack.pop()  # STRING_LITERAL
                token_stack.pop()  # PARENTHESIS_L
                token_stack.pop()  # RW_CALLOUT
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('method_call')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # PARENTHESIS_R
                    id = full_token_stack.pop()  # STRING_LITERAL
                    full_token_stack.pop()  # PARENTHESIS_L
                    rw_callout = full_token_stack.pop()  # RW_CALLOUT
                    method_call = {'method_id': id.lexeme,
                                   'line_num': id.line_num}
                    dict_stack.append(method_call)

            # r54 method_call -> RW_CALLOUT PARENTHESIS_L STRING_LITERAL COMMA callout_arg_list PARENTHESIS_R
            elif state == 54:
                # pop
                token_stack.pop()  # PARENTHESIS_R
                token_stack.pop()  # callout_arg_list
                token_stack.pop()  # COMMA
                token_stack.pop()  # STRING_LITERAL
                token_stack.pop()  # PARENTHESIS_L
                token_stack.pop()  # RW_CALLOUT
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('method_call')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    full_token_stack.pop()  # PARENTHESIS_R
                    callout_arg_list = dict_stack.pop()  # callout_arg_list
                    full_token_stack.pop()  # COMMA
                    id = full_token_stack.pop()  # STRING_LITERAL
                    full_token_stack.pop()  # PARENTHESIS_L
                    rw_callout = full_token_stack.pop()  # RW_CALLOUT
                    method_call = {'method_id': id.lexeme,
                                   'method_args': callout_arg_list,
                                   'line_num': id.line_num}
                    dict_stack.append(method_call)

            # r55 expr_list -> expr_list COMMA expr
            elif state == 55:
                # pop
                token_stack.pop()  # expr
                token_stack.pop()  # COMMA
                token_stack.pop()  # expr_list
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('expr_list')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    expr = dict_stack.pop()  # expr
                    full_token_stack.pop()  # COMMA
                    sub_expr_list = dict_stack.pop()  # expr_list
                    expr_list = {'expr_list': sub_expr_list,
                                 'expr': expr}
                    dict_stack.append(expr_list)

            # r56 expr_list -> expr
            elif state == 56:
                # pop
                token_stack.pop()  # expr
                state_stack.pop()
                # reduction
                token_stack.append('expr_list')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    expr_list = dict_stack.pop()  # expr
                    dict_stack.append(expr_list)

            # r57 literal -> TRUE_LITERAL
            elif state == 57:
                # pop
                token_stack.pop()  # TRUE_LITERAL
                state_stack.pop()
                # reduction
                token_stack.append('literal')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_literal = full_token_stack.pop()  # TRUE_LITERAL
                    literal = {'literal_type': sub_literal.token_type,
                               'lexeme': sub_literal.lexeme,
                               'line_num': sub_literal.line_num}
                    dict_stack.append(literal)

            # r58 literal -> FALSE_LITERAL
            elif state == 58:
                # pop
                token_stack.pop()  # FALSE_LITERAL
                state_stack.pop()
                # reduction
                token_stack.append('literal')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_literal = full_token_stack.pop()  # TRUE_LITERAL
                    literal = {'literal_type': sub_literal.token_type,
                               'lexeme': sub_literal.lexeme,
                               'line_num': sub_literal.line_num}
                    dict_stack.append(literal)

            # r59 literal -> DECIMAL_LITERAL
            elif state == 59:
                # pop
                token_stack.pop()  # DECIMAL_LITERAL
                state_stack.pop()
                # reduction
                token_stack.append('literal')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_literal = full_token_stack.pop()  # TRUE_LITERAL
                    literal = {'literal_type': sub_literal.token_type,
                               'lexeme': sub_literal.lexeme,
                               'line_num': sub_literal.line_num}
                    dict_stack.append(literal)

            # r60 literal -> HEXADECIMAL_LITERAL
            elif state == 60:
                # pop
                token_stack.pop()  # HEXADECIMAL_LITERAL
                state_stack.pop()
                # reduction
                token_stack.append('literal')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_literal = full_token_stack.pop()  # TRUE_LITERAL
                    literal = {'literal_type': sub_literal.token_type,
                               'lexeme': sub_literal.lexeme,
                               'line_num': sub_literal.line_num}
                    dict_stack.append(literal)

            # r61 bin_op -> MOD
            elif state == 61:
                # pop
                token_stack.pop()  # MOD
                state_stack.pop()
                # reduction
                token_stack.append('bin_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_bin_op = full_token_stack.pop()
                    bin_op = {'bin_op_type': sub_bin_op.token_type,
                              'bin_op': sub_bin_op.token}
                    dict_stack.append(bin_op)

            # r62 bin_op -> DIV
            elif state == 62:
                # pop
                token_stack.pop()  # DIV
                state_stack.pop()
                # reduction
                token_stack.append('bin_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_bin_op = full_token_stack.pop()
                    bin_op = {'bin_op_type': sub_bin_op.token_type,
                              'bin_op': sub_bin_op.token}
                    dict_stack.append(bin_op)

            # r63 bin_op -> MULT
            elif state == 63:
                # pop
                token_stack.pop()  # MULT
                state_stack.pop()
                # reduction
                token_stack.append('bin_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_bin_op = full_token_stack.pop()
                    bin_op = {'bin_op_type': sub_bin_op.token_type,
                              'bin_op': sub_bin_op.token}
                    dict_stack.append(bin_op)

            # r64 bin_op -> MINUS
            elif state == 64:
                # pop
                token_stack.pop()  # MINUS
                state_stack.pop()
                # reduction
                token_stack.append('bin_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_bin_op = full_token_stack.pop()
                    bin_op = {'bin_op_type': sub_bin_op.token_type,
                              'bin_op': sub_bin_op.token}
                    dict_stack.append(bin_op)

            # r65 bin_op -> SUM
            elif state == 65:
                # pop
                token_stack.pop()  # SUM
                state_stack.pop()
                # reduction
                token_stack.append('bin_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_bin_op = full_token_stack.pop()
                    bin_op = {'bin_op_type': sub_bin_op.token_type,
                              'bin_op': sub_bin_op.token}
                    dict_stack.append(bin_op)

            # r66 bin_op -> GREATER_THAN
            elif state == 66:
                # pop
                token_stack.pop()  # GREATER_THAN
                state_stack.pop()
                # reduction
                token_stack.append('bin_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_bin_op = full_token_stack.pop()
                    bin_op = {'bin_op_type': sub_bin_op.token_type,
                              'bin_op': sub_bin_op.token}
                    dict_stack.append(bin_op)

            # r67 bin_op -> LESS_THAN
            elif state == 67:
                # pop
                token_stack.pop()  # LESS_THAN
                state_stack.pop()
                # reduction
                token_stack.append('bin_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_bin_op = full_token_stack.pop()
                    bin_op = {'bin_op_type': sub_bin_op.token_type,
                              'bin_op': sub_bin_op.token}
                    dict_stack.append(bin_op)

            # r68 bin_op -> GREATER_EQUALS_THAN
            elif state == 68:
                # pop
                token_stack.pop()  # GREATER_EQUALS_THAN
                state_stack.pop()
                # reduction
                token_stack.append('bin_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_bin_op = full_token_stack.pop()
                    bin_op = {'bin_op_type': sub_bin_op.token_type,
                              'bin_op': sub_bin_op.token}
                    dict_stack.append(bin_op)

            # r69 bin_op -> LESS_EQUALS_THAN
            elif state == 69:
                # pop
                token_stack.pop()  # LESS_EQUALS_THAN
                state_stack.pop()
                # reduction
                token_stack.append('bin_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_bin_op = full_token_stack.pop()
                    bin_op = {'bin_op_type': sub_bin_op.token_type,
                              'bin_op': sub_bin_op.token}
                    dict_stack.append(bin_op)

            # r70 bin_op -> EQUALS
            elif state == 70:
                # pop
                token_stack.pop()  # EQUALS
                state_stack.pop()
                # reduction
                token_stack.append('bin_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_bin_op = full_token_stack.pop()
                    bin_op = {'bin_op_type': sub_bin_op.token_type,
                              'bin_op': sub_bin_op.token}
                    dict_stack.append(bin_op)

            # r71 bin_op -> NOT_EQUALS
            elif state == 71:
                # pop
                token_stack.pop()  # NOT_EQUALS
                state_stack.pop()
                # reduction
                token_stack.append('bin_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_bin_op = full_token_stack.pop()
                    bin_op = {'bin_op_type': sub_bin_op.token_type,
                              'bin_op': sub_bin_op.token}
                    dict_stack.append(bin_op)

            # r72 bin_op -> AND
            elif state == 72:
                # pop
                token_stack.pop()  # AND
                state_stack.pop()
                # reduction
                token_stack.append('bin_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_bin_op = full_token_stack.pop()
                    bin_op = {'bin_op_type': sub_bin_op.token_type,
                              'bin_op': sub_bin_op.token}
                    dict_stack.append(bin_op)

            # r73 bin_op -> OR
            elif state == 73:
                # pop
                token_stack.pop()  # OR
                state_stack.pop()
                # reduction
                token_stack.append('bin_op')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    sub_bin_op = full_token_stack.pop()
                    bin_op = {'bin_op_type': sub_bin_op.token_type,
                              'bin_op': sub_bin_op.token}
                    dict_stack.append(bin_op)

            # r74 callout_arg_list -> callout_arg_list COMMA callout_arg
            elif state == 74:
                # pop
                token_stack.pop()  # callout_arg
                token_stack.pop()  # COMMA
                token_stack.pop()  # callout_arg_list
                state_stack.pop()
                state_stack.pop()
                state_stack.pop()
                # reduction
                token_stack.append('callout_arg_list')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    callout_arg = dict_stack.pop()
                    full_token_stack.pop()
                    sub_callout_arg_list = dict_stack.pop()
                    callout_arg_list = {'callout_arg_list': sub_callout_arg_list,
                                        'callout_arg': callout_arg}
                    dict_stack.append(callout_arg_list)

            # r75 callout_arg_list -> callout_arg
            elif state == 75:
                # pop
                token_stack.pop()  # callout_arg
                state_stack.pop()
                # reduction
                token_stack.append('callout_arg_list')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    callout_arg_list = dict_stack.pop()
                    dict_stack.append(callout_arg_list)

            # r76 callout_arg -> STRING_LITERAL
            elif state == 76:
                # pop
                token_stack.pop()  # STRING_LITERAL
                state_stack.pop()
                # reduction
                token_stack.append('callout_arg')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    string_literal = full_token_stack.pop()
                    dict_stack.append(string_literal.lexeme)

            # r77 callout_arg -> expr
            elif state == 77:
                # pop
                token_stack.pop()  # expr
                state_stack.pop()
                # reduction
                token_stack.append('callout_arg')
                # variable state used as production number
                # -----------------------
                if build_ast:
                    expr = dict_stack.pop()
                    dict_stack.append(expr)

            # the last state becomes the next state
            state = state_stack[-1]
            dfa_input = token_stack[-1]

        elif state_type == 'goto':
            state_stack.append(state)
            dfa_input = token_stream[i].token

        elif state_type == 'error':
            print('‼️ Syntax error in line ' + str(token_stream[i].line_num) + '.')
            syntax_error = True
            i = input_length  # exits while

        elif state_type == 'accept':
            if not build_ast:
                print('✅ Syntax accepted!')
            elif d and build_ast:
                print('🌳 Current AST:\n')
                print(json.dumps(decaf_class, indent=2))
            i = input_length  # exits while

        if d and state_type not in ['error', 'accept'] and not build_ast:
            print('(next) state:          ', str(state),
                  '\n(next) dfa_input:      ', dfa_input)
            print('(end) state_stack:     ', state_stack)
            print('(end) token_stack:     ', token_stack)

    return syntax_error, decaf_class


def parse(file_name, debug_list):
    token_stream = Lexer.scan(file_name, debug_list)
    if token_stream:
        print('\n🔍 Analyzing syntaxis ... ')
        debug_parser = debug_list[1]
        syntax_error, ast = syntax_analysis(token_stream, False, debug_parser)
        if not syntax_error:
            print('🌳 Building AST ... ')
            syntax_error, ast = syntax_analysis(token_stream, True, debug_parser)
            print('➡️ Passing AST to next phase ... ')
            return ast
        else:
            return {}
    else:
        return {}
