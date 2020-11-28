import anytree as at
import json
import anytree
from anytree import Node, RenderTree
from anytree.dotexport import RenderTreeGraph
from anytree.exporter import UniqueDotExporter
from anytree.exporter import DotExporter
import anytree.exporter as atex
import uuid

# Tree in JSON format
output = {
    'id': 'Program',
    'method_decl_list': {
        0: {
            'var_type': 'RW_VOID',
            'id': 'RW_MAIN',
            'block': {
                'var_list': {
                    0: {
                        'var_type': 'VT_INTEGER',
                        'id': 'w',
                        'line_num': 5
                    },
                    1: {
                        'var_type': 'VT_INTEGER',
                        'id': 'uwu',
                        'line_num': 5
                    }
                },
                'statement_list': {
                    0: {
                        'statement_type': 'assignment',
                        'location': {
                            'id': 'y',
                            'line_num': 7
                        },
                        'assign_op': 'ASSIGN',
                        'expr': {
                            'literal_type': 16,
                            'lexeme': '3',
                            'line_num': 7
                        },
                        'line_num': 7
                    },
                    1: {
                        'statement_type': 'assignment',
                        'location': {
                            'id': 'w',
                            'line_num': 8
                        },
                        'assign_op': 'ASSIGN',
                        'expr': {
                            'literal_type': 16,
                            'lexeme': '4',
                            'line_num': 8
                        },
                        'line_num': 8
                    },
                    2: {
                        'statement_type': 'assignment',
                        'location': {
                            'id': 'w',
                            'line_num': 9
                        },
                        'assign_op': 'ASSIGN',
                        'expr': {
                            'method_id': 'gcd',
                            'method_args': {
                                'expr_list': {
                                    'expr_list': {
                                        'id': 'x',
                                        'line_num': 9
                                    },
                                    'expr': {
                                        'expr': {
                                            'id': 'y',
                                            'line_num': 9
                                        },
                                        'un_op': 'MINUS'
                                    }
                                },
                                'expr': {
                                    'id': 'z',
                                    'line_num': 9
                                }
                            },
                            'line_num': 9
                        },
                        'line_num': 9
                    },
                    3: {
                        'statement_type': 'assignment',
                        'location': {
                            'id': 'z',
                            'line_num': 10
                        },
                        'assign_op': 'ASSIGN',
                        'expr': {
                            'literal_type': 15,
                            'lexeme': 'false',
                            'line_num': 10
                        },
                        'line_num': 10
                    },
                    4: {
                        'statement_type': 'assignment',
                        'location': {
                            'id': 'z',
                            'line_num': 11
                        },
                        'assign_op': 'ASSIGN',
                        'expr': {
                            'method_id': 'hvf',
                            'line_num': 11
                        },
                        'line_num': 11
                    }
                }
            },
            'line_num': 4
        },
        1: {
            'var_type': 'VT_INTEGER',
            'id': 'gcd',
            'method_arg_list': {
                0: {
                    'id': 'a',
                    'var_type': 'VT_INTEGER'
                },
                1: {
                    'id': 'b',
                    'var_type': 'VT_INTEGER'
                },
                2: {
                    'id': 'h',
                    'var_type': 'VT_BOOLEAN'
                }
            },
            'block': {
                'var_list': {
                    0: {
                        'var_type': 'VT_INTEGER',
                        'id': 'c',
                        'line_num': 15
                    }
                },
                'statement_list': {
                    0: {
                        'statement_type': 'return',
                        'return_expr': {
                            'id': 'c',
                            'line_num': 21
                        }
                    }
                }
            },
            'line_num': 14
        },
        2: {
            'var_type': 'VT_BOOLEAN',
            'id': 'hvf',
            'block': {
                'statement_list': {

                }
            },
            'line_num': 24
        },
        3: {
            'var_type': 'VT_BOOLEAN',
            'id': 'the_empty_method',
            'block': {
                'var_list': {
                    0: {
                        'var_type': 'VT_BOOLEAN',
                        'id': 'var_empty',
                        'line_num': 29
                    }
                }
            },
            'line_num': 28
        }
    },
    'field_decl_list': {
        0: {
            'var_type': 'VT_INTEGER',
            'id': 'x',
            'line_num': 1
        },
        1: {
            'var_type': 'VT_INTEGER',
            'id': 'y',
            'line_num': 1
        },
        2: {
            'var_type': 'VT_BOOLEAN',
            'id': 'f',
            'line_num': 2
        },
        3: {
            'var_type': 'VT_BOOLEAN',
            'id': 'g',
            'line_num': 2
        },
        4: {
            'var_type': 'VT_BOOLEAN',
            'id': 'z',
            'line_num': 3
        }
    }
}

superArray = []


def tree_builder(d, p_uid='root', l=0):
    for i, (k, v) in enumerate(d.items()):
        node_uid = uuid.uuid1()
        node = nodes[k] = at.Node(
            name=node_uid,
            key=k,
            parent=nodes[p_uid]
        )
        if isinstance(v, dict):
            node.an_attr = ''
            tree_builder(v, k, l + 1)
        else:
            node.an_attr = v


root = at.Node(name='root', key='root', an_attr='')
nodes = {'root': root}
tree_builder(output)


for pre, fill, node in at.RenderTree(root):
    print("%s%s|%s" % (pre, node.key, node.an_attr))

atex.DotExporter(
    root, nodeattrfunc=lambda n: 'label="{}\n{}"'.format(n.key, n.an_attr)
).to_picture("graph_t.png")

