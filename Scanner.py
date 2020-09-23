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
            elif re.match(r'\w', lexeme):
                token = 'CHAR'
                token_type = 'char_literal'
            elif re.match(r'(\w|_)(\d|\w|_)*', lexeme):
                token = 'ID'
                token_type = 'string_literal' # ID
            elif lexeme == '+=':
                token = 'PLUS_EQUALS'
                token_type = 'assign op'
            elif lexeme == '-=':
                token = 'MINUS_EQUALS'
                token_type = 'assign op'
            elif lexeme == 'int':
                token = 'KW_INT'
                token_type = 'reserved_word'
            elif lexeme == 'boolean':
                token = 'KW_BOOL'
                token_type = 'reserved_word'
            elif lexeme == 'callout':
                token = 'KW_CALLOUT'
                token_type = 'reserved_word'
            elif lexeme == 'void':
                token = 'KW_VOID'
                token_type = 'reserved_word'
            elif lexeme == 'if':
                token = 'KW_IF'
                token_type = 'reserved_word'
            elif lexeme == 'else':
                token = 'KW_ELSE'
                token_type = 'reserved_word'
            elif lexeme == 'for':
                token = 'KW_FOR'
                token_type = 'reserved_word'
            elif lexeme == 'return':
                token = 'KW_RETURN'
                token_type = 'reserved_word'
            elif lexeme == 'break':
                token = 'KW_BREAK'
                token_type = 'reserved_word'
            elif lexeme == 'continue':
                token = 'KW_CONTINUE'
                token_type = 'reserved_word'
            elif lexeme == ')':
                token = 'PARENTHESIS_R'
                token_type = 'decaf_grammar'
            elif lexeme == '(':
                token = 'PARENTHESIS_L'
                token_type = 'decaf_grammar'
            elif lexeme == '[':
                token = 'BRACKET_L'
                token_type = 'decaf_grammar'
            elif lexeme == ']':
                token = 'BRACKET_R'
                token_type = 'decaf_grammar'
            elif lexeme == '{':
                token = 'BRACE_L'
                token_type = 'decaf_grammar'
            elif lexeme == '}':
                token = 'BRACE_R'
                token_type = 'decaf_grammar'
            elif lexeme == ';':
                token = 'SEMICOLON'
                token_type = 'decaf_grammar'
            elif lexeme == '!':
                token = 'NEGATION'
                token_type = 'decaf_grammar'
            elif lexeme == '+':
                token = 'PLUS'
                token_type = 'arith_op'
            elif lexeme == '-':
                token = 'MINUS'
                token_type = 'arith_op'
            elif lexeme == '*':
                token = 'MULT'
                token_type = 'arith_op'
            elif lexeme == '/':
                token = 'DIV'
                token_type = 'arith_op'
            elif lexeme == '%':
                token = 'MOD'
                token_type = 'arith_op'
            elif lexeme == '||':
                token = 'OR'
                token_type = 'cond_op'
            elif lexeme == '&&':
                token = 'AND'
                token_type = 'cond_op'
            elif lexeme == '>':
                token = 'GREATER_THAN'
                token_type = 'rel_op'
            elif lexeme == '<':
                token = 'LESS_THAN'
                token_type = 'rel_op'
            elif lexeme == '<=':
                token = 'LESS_EQUALS_THAN'
                token_type = 'rel_op'
            elif lexeme == '>=':
                token = 'GREATER_EQUALS_THAN'
                token_type = 'rel_op'
            elif lexeme == '==':
                token = 'EQUALS_EQUALS'
                token_type = 'eq_op'
            elif lexeme == '!=':
                token = 'NEG_EQUALS'
                token_type = 'eq_op'
            else:
                token = 'STRING'
                token_type = 'string_literal'

            tokenized = Token.Token(lexeme, token, token_type)
            print('\n\nlexema: ', tokenized.lexeme, '\ntoken: ', tokenized.token, '\ntype: ', tokenized.token_type, '\nobj: ', type(tokenized))
    return token_stream


def scan(file_name, d):
    program_string = get_program(file_name, d)
    lexemes = split_program(program_string, d)
    token_stream = tokenize(lexemes, d)
    return token_stream


