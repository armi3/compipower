import re
import Token
from itertools import repeat


def get_program(file_name, d):
    file = open(file_name, 'r')
    program_lines = file.readlines()
    if d:
        print("\n\nprogram_lines = ", program_lines)
        count = 1
        for line in program_lines:
            print("Line{}: {}".format(count, line.strip()))
            count += 1
    return program_lines


def split_program(program_lines, d):
    reg_exp = r'class Program|{|}|\[|\]|,|;|==|\-=|\+=|\-|\!=|<=|>=|<|>|=|\!|\+|\*|\/|\&\&|\|\||%|\/\/|\"|\'|\\|\'|\"|\n|\t|\)|\(|int|boolean|if|for|return|break|continue|callout|true|false|void|else|0[x|X][\w|\d]+|\d+|[\w][\w\d_]+|[\w]+'
    lexemes = []
    line_nums = []
    line_num = 0
    for line in program_lines:
        line_lexemes = re.findall(reg_exp, line)
        for lexeme in line_lexemes:
            lexemes.append(lexeme)
        line_num += 1
        line_nums.extend(repeat(line_num, len(line_lexemes)))

    if d:
        print("\n\nlexemes_stream = ", lexemes)
        print("\n\nlexemes_line_nums = ", line_nums)
        print(type(lexemes))
    return lexemes, line_nums


def tokenize(lexemes, line_nums, d):
    token_stream = []

    count = 0
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
            elif re.match(r'\w', lexeme):
                token = 'CHAR'
                token_type = 'char_literal'
            elif re.match(r'(\w|_)(\d|\w|_)*', lexeme):
                token = 'ID'
                token_type = 'string_literal'
            elif lexeme == '+=':
                token = 'PLUS_EQUALS'
                token_type = 'assign_op'
            elif lexeme == '-=':
                token = 'MINUS_EQUALS'
                token_type = 'assign_op'
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

            tokenized = Token.Token(lexeme, token, token_type, line_nums[count])
            print('\n\nlexeme: ', tokenized.lexeme, '\ntoken: ', tokenized.token, '\ntype: ', tokenized.token_type,
                  '\nline_num: ', tokenized.line_num, '\nobj: ', type(tokenized))
            token_stream.append(tokenized)
        count += 1
    return token_stream


def scan(file_name, d):
    program_lines = get_program(file_name, d)
    lexemes, line_nums = split_program(program_lines, d)
    token_stream = tokenize(lexemes, line_nums, d)
    return token_stream
