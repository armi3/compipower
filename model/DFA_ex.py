col1 = 'x'
col2 = '*'
col3 = '='
col4 = '$'
col5 = 'S'
col6 = 'E'
col7 = 'V'


def start(token, state):
    if state == 1:
        state_type, next_state = state1(token)
    elif state == 2:
        state_type, next_state = state2(token)
    elif state == 3:
        state_type, next_state = state3(token)
    elif state == 4:
        state_type, next_state = state4(token)
    elif state == 5:
        state_type, next_state = state5(token)
    elif state == 6:
        state_type, next_state = state6(token)
    elif state == 7:
        state_type, next_state = state7(token)
    elif state == 8:
        state_type, next_state = state8(token)
    elif state == 9:
        state_type, next_state = state9(token)
    elif state == 10:
        state_type, next_state = state10(token)
    else:
        return 'error', 1
    return state_type, next_state


def state1(c):
    if c == col1:
        state_type = 'shift'
        next_state = 8
    elif c == col2:
        state_type = 'shift'
        next_state = 6
    elif c == col5:
        state_type = 'goto'
        next_state = 2
    elif c == col6:
        state_type = 'goto'
        next_state = 5
    elif c == col7:
        state_type = 'goto'
        next_state = 3
    else:
        state_type = 'error'
        next_state = 1
    return state_type, next_state


def state2(c):
    if c == col4:
        state_type = 'accept'
        next_state = 1
    else:
        state_type = 'error'
        next_state = 1
    return state_type, next_state


def state3(c):
    if c == col3:
        state_type = 'shift'
        next_state = 4
    elif c == col4:
        state_type = 'reduce'
        next_state = 3
    else:
        state_type = 'error'
        next_state = 1
    return state_type, next_state


def state4(c):
    if c == col1:
        state_type = 'shift'
        next_state = 8
    elif c == col2:
        state_type = 'shift'
        next_state = 6
    elif c == col6:
        state_type = 'goto'
        next_state = 9
    elif c == col7:
        state_type = 'goto'
        next_state = 7
    else:
        state_type = 'error'
        next_state = 1
    return state_type, next_state


def state5(c):
    if c == col4:
        state_type = 'reduce'
        next_state = 2
    else:
        state_type = 'error'
        next_state = 1
    return state_type, next_state


def state6(c):
    if c == col1:
        state_type = 'shift'
        next_state = 8
    elif c == col2:
        state_type = 'shift'
        next_state = 6
    elif c == col6:
        state_type = 'goto'
        next_state = 10
    elif c == col7:
        state_type = 'goto'
        next_state = 7
    else:
        state_type = 'error'
        next_state = 1
    return state_type, next_state


def state7(c):
    if c == col3:
        state_type = 'reduce'
        next_state = 3
    elif c == col4:
        state_type = 'reduce'
        next_state = 3
    else:
        state_type = 'error'
        next_state = 1
    return state_type, next_state


def state8(c):
    if c == col3:
        state_type = 'reduce'
        next_state = 4
    elif c == col4:
        state_type = 'reduce'
        next_state = 4
    else:
        state_type = 'error'
        next_state = 1
    return state_type, next_state


def state9(c):
    if c == col4:
        state_type = 'reduce'
        next_state = 1
    else:
        state_type = 'error'
        next_state = 1
    return state_type, next_state


def state10(c):
    if c == col3:
        state_type = 'reduce'
        next_state = 5
    elif c == col4:
        state_type = 'reduce'
        next_state = 5
    else:
        state_type = 'error'
        next_state = 1
    return state_type, next_state
