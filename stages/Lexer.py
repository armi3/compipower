from model import Token, MinDFA


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
    lexemes = []
    line_nums = []
    line_num = 0

    for line in program_lines:
        line_length = len(line)
        print('\nline length: ', line_length)
        candidate_lexeme = ''

        for i in range(line_length):
            if i == 0:
                state_type, state = MinDFA.start(line[i], 1)
            else:
                state_type, state = MinDFA.start(line[i], state)
            print('i: ', i, ', line[i]: ', repr(line[i]), ', state_type: ', state_type, ', next state: ', str(state))

            if (i + 1 == line_length) and state_type == 'continue':
                state_type, state = MinDFA.start('(', state)

            if state_type == 'continue':
                candidate_lexeme = candidate_lexeme + line[i]
            elif state_type == 'accept_final':
                lexemes.append(candidate_lexeme)
                print('line: ', line_num,
                      ', i: ', i,
                      ', appended: ', repr(candidate_lexeme), '\n')
                line_nums.append(line_num)
                candidate_lexeme = line[i]
            elif state_type == 'not_accept':
                candidate_lexeme = ''
        line_num += 1

    if d:
        print("\n\nlexemes_stream = ", lexemes)
        print("lexemes_line_nums = ", line_nums)
        print(type(lexemes))

    # remove empties '' and maybe ' '
    print('len(lexemes): ', len(lexemes))
    print('len(line_nums): ', len(line_nums))

    new_lists_length = len(lexemes)
    i = 0
    while i < new_lists_length:
        print('i: ', i)
        if lexemes[i] in ['', ' ', '\t']:
            print('hubo pop')
            lexemes.pop(i)
            line_nums.pop(i)
            new_lists_length -= 1
            print('new_lists_length: ', new_lists_length)
        else:
            i += 1

    # print if debug is on
    if d:
        print("\n\nlexemes_stream = ", lexemes)
        print("lexemes_line_nums = ", line_nums)
        print(type(lexemes))
    return lexemes, line_nums


def find_lexical_errors(program_lines, lexemes, line_nums):
    # transform program lines: smash w/o spaces
    program_lines_smashed = []
    for line in program_lines:
        line_smashed = line.replace(" ", "").replace("\n", "").replace("\t", "")
        program_lines_smashed.append(line_smashed)

    program_lines_smashed = list(filter(lambda a: a != '', program_lines_smashed))

    # make equivalent lines from lexemes & line_nums: smash, then remove spaces
    line_counter = 0
    this_line = ''
    lexemes_lines = []
    lexemes_lines_smashed = []

    for i in range(len(lexemes)):
        if line_nums[i] == line_counter:
            this_line = this_line + lexemes[i]
        else:
            lexemes_lines.append(this_line)
            this_line = ''
            line_counter = line_nums[i]
            this_line = this_line + lexemes[i]
        if i == len(lexemes) - 1:
            lexemes_lines.append(this_line)

    for line in lexemes_lines:
        line_smashed = line.replace(" ", "")
        lexemes_lines_smashed.append(line_smashed)

    print('program_lines_smashed: ', program_lines_smashed)
    print('lexemes_lines_smashed: ', lexemes_lines_smashed)

    # compare lines
    lines_with_lexical_errors = []
    for i in range(len(program_lines_smashed)):
        if lexemes_lines_smashed[i] == program_lines_smashed[i]:
            pass
        else:
            lines_with_lexical_errors.append(i)

    # print errors
    if len(lines_with_lexical_errors) > 0:
        print('\nLexical errors found in the following program lines:')
        for i in range(len(lines_with_lexical_errors)):
            print('LEXERROR: Line ', lines_with_lexical_errors[i])
            print(program_lines[lines_with_lexical_errors[i]])
        return True
    else:
        print('\nNo lexical errors where found. Congrats!')
        return False


def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def tokenize(lexemes, line_nums, d):
    token_stream = []

    count = 0
    for lexeme in lexemes:
        token = ''
        token_type = 0
        # only 1 comparison
        if lexeme == '!':
            token = 'NEGATION'
            token_type = 1

        elif lexeme == ';':
            token = 'SEMICOLON'
            token_type = 2

        elif lexeme == ',':
            token = 'COMMA'
            token_type = 2

        elif lexeme == '{':
            token = 'BRACE_L'
            token_type = 3

        elif lexeme == '}':
            token = 'BRACE_R'
            token_type = 3

        elif lexeme == '(':
            token = 'PARENTHESIS_L'
            token_type = 4

        elif lexeme == ')':
            token = 'PARENTHESIS_R'
            token_type = 4

        elif lexeme == '[':
            token = 'BRACKET_L'
            token_type = 5

        elif lexeme == ']':
            token = 'BRACKET_R'
            token_type = 5

        elif lexeme[0] == '"':
            token = 'STRING_LITERAL'
            token_type = 6

        # simple comparisons
        elif lexeme[0:2] == '//':
            token = 'COMMENT'
            token_type = 7

        elif lexeme == '=':
            token = 'ASSIGN'
            token_type = 8

        elif lexeme == '+=':
            token = 'PLUS_ASSIGN'
            token_type = 8

        elif lexeme == '-=':
            token = 'MINUS_ASSIGN'
            token_type = 8

        elif lexeme == '%':
            token = 'MOD'
            token_type = 9

        elif lexeme == '/':
            token = 'DIV'
            token_type = 9

        elif lexeme == '*':
            token = 'MULT'
            token_type = 9

        elif lexeme == '-':
            token = 'MINUS'
            token_type = 9

        elif lexeme == '+':
            token = 'SUM'
            token_type = 9

        elif lexeme == '>':
            token = 'GREATER_THAN'
            token_type = 10

        elif lexeme == '<':
            token = 'LESS_THAN'
            token_type = 10

        elif lexeme == '>=':
            token = 'GREATER_EQUALS_THAN'
            token_type = 10

        elif lexeme == '<=':
            token = 'LESS_EQUALS_THAN'
            token_type = 10

        elif lexeme == '==':
            token = 'EQUALS'
            token_type = 11

        elif lexeme == '!=':
            token = 'NOT_EQUALS'
            token_type = 11

        elif lexeme == '&&':
            token = 'AND'
            token_type = 12

        elif lexeme == '||':
            token = 'OR'
            token_type = 12

        # complex comparisons
        elif lexeme == 'class':
            token = 'RW_CLASS'
            token_type = 13

        elif lexeme == 'void':
            token = 'RW_VOID'
            token_type = 13

        elif lexeme == 'if':
            token = 'RW_IF'
            token_type = 13

        elif lexeme == 'else':
            token = 'RW_ELSE'
            token_type = 13

        elif lexeme == 'for':
            token = 'RW_FOR'
            token_type = 13

        elif lexeme == 'return':
            token = 'RW_RETURN'
            token_type = 13

        elif lexeme == 'break':
            token = 'RW_BREAK'
            token_type = 13

        elif lexeme == 'continue':
            token = 'RW_CONTINUE'
            token_type = 13

        elif lexeme == 'callout':
            token = 'RW_CALLOUT'
            token_type = 13

        elif lexeme == 'int':
            token = 'VT_INTEGER'
            token_type = 14

        elif lexeme == 'boolean':
            token = 'VT_BOOLEAN'
            token_type = 14

        elif lexeme == 'true':
            token = 'TRUE_LITERAL'
            token_type = 15

        elif lexeme == 'false':
            token = 'FALSE_LITERAL'
            token_type = 15

        elif is_float(lexeme):
            token = 'DECIMAL_LITERAL'
            token_type = 16

        elif lexeme[0:2] == ('0x' or '0X') and is_hex(lexeme):
            token = 'HEXADECIMAL_LITERAL'
            token_type = 17

        else:
            token = 'ID'
            token_type = 18

        tokenized = Token.Token(lexeme, token, token_type, line_nums[count])
        print('\n\nlexeme: ', tokenized.lexeme, '\ntoken: ', tokenized.token, '\ntoken_type: ', tokenized.token_type,
              '\nline_num: ', tokenized.line_num, '\nobj: ', type(tokenized))
        token_stream.append(tokenized)
        count += 1

    return token_stream


def scan(file_name, d):
    program_lines = get_program(file_name, d)
    lexemes, line_nums = split_program(program_lines, d)
    lexical_errors = find_lexical_errors(program_lines, lexemes, line_nums)
    if not lexical_errors:
        token_stream = tokenize(lexemes, line_nums, d)
        return token_stream
    else:
        return []
