col1 = ['!', '-', '<', '=', '>', '+']
col2 = ['"']
col3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
col4 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', ')', '%', ',', '-', '.', '/', '0', ';', ' ', '[', '\\', ']', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '{', '}', '(', '+', '\t', '*']
col5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '%', ',', '-', '.', '/', '0', ' ', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '+', '*']
col6 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
col7 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
col8 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']
col9 = [')', '%', ',', ';', ' ', '[', ']', '{', '}', '(', '\n', '\t', '*']
col10 = ['&']
col11 = ['.']
col12 = ['/']
col13 = ['0']
col14 = ['=']
col15 = ['|']
col16 = ['_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
col17 = ['x', 'X']
all_possible_chars = ['!', '-', '<', '=', '>', '+', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ')', '%', ',', ';', ' ', '[', ']', '{', '}', '(', '*', '&', '.', '/', '|', '\n', '\t', '"', '\\']


def start(c, state):
    if c in all_possible_chars:
        if state == 1:
            state_type, next_state = state1(c)
        elif state == 2:
            state_type, next_state = state2(c)
        elif state == 3:
            state_type, next_state = state3(c)
        elif state == 4:
            state_type, next_state = state4(c)
        elif state == 5:
            state_type, next_state = state5(c)
        elif state == 6:
            state_type, next_state = state6(c)
        elif state == 7:
            state_type, next_state = state7(c)
        elif state == 8:
            state_type, next_state = state8(c)
        elif state == 9:
            state_type, next_state = state9(c)
        elif state == 10:
            state_type, next_state = state10(c)
        elif state == 11:
            state_type, next_state = state11(c)
        elif state == 12:
            state_type, next_state = state12(c)
        elif state == 13:
            state_type, next_state = state13(c)
        elif state == 14:
            state_type, next_state = state14(c)
        elif state == 15:
            state_type, next_state = state15(c)
        elif state == 16:
            state_type, next_state = state16(c)
    else:
        return 'not_accept', 1

    return state_type, next_state


def state1(c):
    state_type = 'continue'
    if c in col1:
        next_state = 4
    elif c in col2:
        next_state = 10
    elif c in col3:
        next_state = 6
    elif c in col9:
        next_state = 3
    elif c in col10:
        next_state = 13
    elif c in col12:
        next_state = 14
    elif c in col13:
        next_state = 15
    elif c in col15:
        next_state = 16
    elif c in col16:
        next_state = 2
    else:
        state_type = 'accept_final'
        next_state = 1
    return state_type, next_state


def state2(c):
    if c in col7:
        state_type = 'continue'
        next_state = 2
    else:
        state_type, next_state = state1(c)
        state_type = 'accept_final'
    return state_type, next_state


def state3(c):
    state_type, next_state = state1(c)
    return 'accept_final', next_state


def state4(c):
    if c in col14:
        state_type = 'continue'
        next_state = 3
    else:
        state_type, next_state = state1(c)
        state_type = 'accept_final'
    return state_type, next_state


def state5(c):
    state_type = 'continue'
    if c in col2:
        next_state = 3
    elif c in col4:
        next_state = 5
    else:
        state_type = 'not_accept'
        next_state = 1
    return state_type, next_state


def state6(c):
    if c in col6:
        state_type = 'continue'
        next_state = 6
    elif c in col11:
        state_type = 'continue'
        next_state = 7
    else:
        state_type, next_state = state1(c)
        state_type = 'accept_final'
    return state_type, next_state


def state7(c):
    state_type = 'continue'
    if c in col6:
        next_state = 11
    else:
        state_type = 'not_accept'
        next_state = 1
    return state_type, next_state


def state8(c):
    if c in col5:
        state_type = 'continue'
        next_state = 8
    else:
        state_type, next_state = state1(c)
        state_type = 'accept_final'
    return state_type, next_state


def state9(c):
    if c in col8:
        state_type = 'continue'
        next_state = 12
    else:
        state_type = 'not_accept'
        next_state = 1
    return state_type, next_state


def state10(c):
    if c in col4:
        state_type = 'continue'
        next_state = 5
    else:
        state_type = 'not_accept'
        next_state = 1
    return state_type, next_state


def state11(c):
    state_type = 'continue'
    if c in col6:
        next_state = 11
    else:
        state_type, next_state = state1(c)
        state_type = 'accept_final'
    return state_type, next_state


def state12(c):
    if c in col8:
        state_type = 'continue'
        next_state = 12
    else:
        state_type, next_state = state1(c)
        state_type = 'accept_final'
    return state_type, next_state


def state13(c):
    if c in col10:
        state_type = 'continue'
        next_state = 3
    else:
        state_type = 'not_accept'
        next_state = 1
    return state_type, next_state


def state14(c):
    if c in col12:
        state_type = 'continue'
        next_state = 8
    else:
        state_type, next_state = state1(c)
        state_type = 'accept_final'
    return state_type, next_state


def state15(c):
    state_type = 'continue'
    if c in col6:
        next_state = 6
    elif c in col11:
        next_state = 7
    elif c in col17:
        next_state = 9
    else:
        state_type, next_state = state1(c)
        state_type = 'accept_final'
    return state_type, next_state


def state16(c):
    if c in col15:
        state_type = 'continue'
        next_state = 3
    else:
        state_type = 'not_accept'
        next_state = 1
    return state_type, next_state
