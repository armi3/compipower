from model import Token
from archives import DFA_ex

# token_stream = Lexer.scan('../examples/example2.dcf', True)
# print('\nmmmm token:', token_stream[0].token)

# x = x
token_stream = []
token_stream.append(Token.Token('', 'x', '', 0))
token_stream.append(Token.Token('', '=', '', 0))
token_stream.append(Token.Token('', 'x', '', 0))

token_stream.append(Token.Token('$', '$', '', 0))

input_length = len(token_stream)

for i in range(0, input_length):
    print(token_stream[i].token)

state_stack = [1]
token_stack = []

state_type = ''
state = 0
dfa_input = ''
i = 0

successful_parsing = False

while i < input_length:
    if i == 0:
        state_type, state = DFA_ex.start(token_stream[i].token, 1)
    else:
        state_type, state = DFA_ex.start(dfa_input, state)

    print('\ni: ', i,
          ', token_stream[i].token: ', repr(token_stream[i].token),
          ', state_type: ', state_type,
          ', state:', state)

    # if (i + 1 == input_length) and state_type == 'shift':
    #     state_type, state = DFA.start('(', state)

    if state_type == 'shift':
        # add token to stack
        token_stack.append(token_stream[i].token)
        # add next state to stack
        state_stack.append(state)
        i += 1
        dfa_input = token_stream[i].token

    elif state_type == 'reduce':
        # reduce each case by foot
        # r1    S → V = E
        if state == 1:
            # pop
            token_stack.pop()  # E
            token_stack.pop()  # =
            token_stack.pop()  # V
            state_stack.pop()
            state_stack.pop()
            state_stack.pop()
            # reduction
            token_stack.append('S')
            # variable state used as production number
            # the last state becomes the next state
            state = state_stack[-1]

        # r2    S → E
        elif state == 2:
            # pop
            token_stack.pop()  # E
            state_stack.pop()
            # reduction
            token_stack.append('S')
            # variable state used as production number
            # the last state becomes the next state
            state = state_stack[-1]

        # r3    E → V
        elif state == 3:
            # pop
            token_stack.pop()  # V
            state_stack.pop()
            # reduction
            token_stack.append('E')
            # variable state used as production number
            # the last state becomes the next state
            state = state_stack[-1]

        # r4    V → x
        elif state == 4:
            # pop
            token_stack.pop()  # x
            state_stack.pop()
            # reduction
            token_stack.append('V')
            # variable state used as production number
            # the last state becomes the next state
            state = state_stack[-1]

        # r5    V → * E
        elif state == 5:
            # pop
            token_stack.pop()  # E
            token_stack.pop()  # *
            state_stack.pop()
            state_stack.pop()
            # reduction
            token_stack.append('V')
            # variable state used as production number
            # the last state becomes the next state
            state = state_stack[-1]

        dfa_input = token_stack[-1]

    elif state_type == 'goto':
        state_stack.append(state)
        dfa_input = token_stream[i].token

    elif state_type == 'error':
        print('\nSyntax error in line ' + str(token_stream[i].line_num) + '.')
        i = input_length

    elif state_type == 'accept':
        print('\nSyntax accepted. Building AST...')
        successful_parsing = True
        i = input_length

    # print stacks
    print('next state: ', str(state), ', dfa_input: ', dfa_input)
    print('state_stack: ', state_stack)
    print('token_stack: ', token_stack)

if successful_parsing:
    pass
