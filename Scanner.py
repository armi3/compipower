import re
import Token


def get_program(file_name, d):
    file = open(file_name, 'r')
    program_string = file.read()
    if d:
        print("\n\nprogram_string = \n", program_string)
    return program_string


def split_program(program_string, d):
    regex = r'class Program|{|}|\[|\]|,|;|=|\-|\+|\-=|\!|<|>|<=|>=|==|\!=|\+=|\*|\/|\&\&|\|\||%|\/\/|\"|\'|\\|\'|\"|\n|\t|\)|\(|int|boolean|if|for|return|break|continue|callout|true|false|void|else|0[x|X][\w|\d]+|\d+|[\w][\w\d_]+|[\w]+'
    lexemes = re.findall(regex, program_string)
    if d:
        print("\n\nstring_stream = \n", lexemes)
        print(type(lexemes))
    return lexemes


def tokenize(lexemes, d):
    token_stream = []

    for lexeme in lexemes:
        if lexeme != ('\n' or '\t'):
            if lexeme == 'true':
                token = "TRUE"
                token_type = "bool_literal"
            elif lexeme == 'false':
                token = "FALSE"
                token_type = "bool_literal"
            elif lexeme == '=':
                token = 'EQUALS'
                token_type = 'assign_op'
            elif re.match(r'0[x|X][\w|\d]+', lexeme):
                token = int(lexeme, 16)
                token_type = 'hex_literal'
            elif re.match(r'\d+', lexeme):
                token = int(lexeme)
                token_type = 'decimal_literal'
            # aquí van los demás elifs, algunos usarán regex otros no
            else:
                token = 'ID'
                token_type = 'string_literal'

            tokenized = Token.Token(lexeme, token, token_type)
            print('\n\nlexema: ', tokenized.lexeme, '\ntoken: ', tokenized.token, '\ntype: ', tokenized.token_type, '\nobj: ', type(tokenized))
    return token_stream


def scan(file_name, d):
    program_string = get_program(file_name, d)
    lexemes = split_program(program_string, d)
    token_stream = tokenize(lexemes, d)
    return token_stream


