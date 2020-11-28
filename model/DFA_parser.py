col1 = '$'
col2 = 'AND'
col3 = 'ASSIGN'
col4 = 'BRACE_L'
col5 = 'BRACE_R'
col6 = 'BRACKET_L'
col7 = 'BRACKET_R'
col8 = 'COMMA'
col9 = 'DECIMAL_LITERAL'
col10 = 'DIV'
col11 = 'EQUALS'
col12 = 'FALSE_LITERAL'
col13 = 'GREATER_EQUALS_THAN'
col14 = 'GREATER_THAN'
col15 = 'HEXADECIMAL_LITERAL'
col16 = 'ID'
col17 = 'LESS_EQUALS_THAN'
col18 = 'LESS_THAN'
col19 = 'MINUS'
col20 = 'MINUS_ASSIGN'
col21 = 'MOD'
col22 = 'MULT'
col23 = 'NEGATION'
col24 = 'NOT_EQUALS'
col25 = 'OR'
col26 = 'PARENTHESIS_L'
col27 = 'PARENTHESIS_R'
col28 = 'PLUS_ASSIGN'
col29 = 'RW_BREAK'
col30 = 'RW_CALLOUT'
col31 = 'RW_CLASS'
col32 = 'RW_CONTINUE'
col33 = 'RW_ELSE'
col34 = 'RW_FOR'
col35 = 'RW_IF'
col36 = 'RW_MAIN'
col37 = 'RW_RETURN'
col38 = 'RW_VOID'
col39 = 'SEMICOLON'
col40 = 'STRING_LITERAL'
col41 = 'SUM'
col42 = 'TRUE_LITERAL'
col43 = 'VT_BOOLEAN'
col44 = 'VT_INTEGER'
col45 = 'assign_op'
col46 = 'bin_op'
col47 = 'block'
col48 = 'callout_arg'
col49 = 'callout_arg_list'
col50 = 'class'
col51 = 'expr'
col52 = 'expr_list'
col53 = 'field_decl'
col54 = 'field_decl_list'
col55 = 'id_list'
col56 = 'literal'
col57 = 'location'
col58 = 'method_arg'
col59 = 'method_arg_list'
col60 = 'method_call'
col61 = 'method_decl'
col62 = 'method_decl_list'
col63 = 'statement'
col64 = 'statement_list'
col65 = 'var_list'
col66 = 'var_type'


def start(token, state):
    if state == 0:
        state_type, next_state = state0(token)
    elif state == 1:
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
    elif state == 11:
        state_type, next_state = state11(token)
    elif state == 12:
        state_type, next_state = state12(token)
    elif state == 13:
        state_type, next_state = state13(token)
    elif state == 14:
        state_type, next_state = state14(token)
    elif state == 15:
        state_type, next_state = state15(token)
    elif state == 16:
        state_type, next_state = state16(token)
    elif state == 17:
        state_type, next_state = state17(token)
    elif state == 18:
        state_type, next_state = state18(token)
    elif state == 19:
        state_type, next_state = state19(token)
    elif state == 20:
        state_type, next_state = state20(token)
    elif state == 21:
        state_type, next_state = state21(token)
    elif state == 22:
        state_type, next_state = state22(token)
    elif state == 23:
        state_type, next_state = state23(token)
    elif state == 24:
        state_type, next_state = state24(token)
    elif state == 25:
        state_type, next_state = state25(token)
    elif state == 26:
        state_type, next_state = state26(token)
    elif state == 27:
        state_type, next_state = state27(token)
    elif state == 28:
        state_type, next_state = state28(token)
    elif state == 29:
        state_type, next_state = state29(token)
    elif state == 30:
        state_type, next_state = state30(token)
    elif state == 31:
        state_type, next_state = state31(token)
    elif state == 32:
        state_type, next_state = state32(token)
    elif state == 33:
        state_type, next_state = state33(token)
    elif state == 34:
        state_type, next_state = state34(token)
    elif state == 35:
        state_type, next_state = state35(token)
    elif state == 36:
        state_type, next_state = state36(token)
    elif state == 37:
        state_type, next_state = state37(token)
    elif state == 38:
        state_type, next_state = state38(token)
    elif state == 39:
        state_type, next_state = state39(token)
    elif state == 40:
        state_type, next_state = state40(token)
    elif state == 41:
        state_type, next_state = state41(token)
    elif state == 42:
        state_type, next_state = state42(token)
    elif state == 43:
        state_type, next_state = state43(token)
    elif state == 44:
        state_type, next_state = state44(token)
    elif state == 45:
        state_type, next_state = state45(token)
    elif state == 46:
        state_type, next_state = state46(token)
    elif state == 47:
        state_type, next_state = state47(token)
    elif state == 48:
        state_type, next_state = state48(token)
    elif state == 49:
        state_type, next_state = state49(token)
    elif state == 50:
        state_type, next_state = state50(token)
    elif state == 51:
        state_type, next_state = state51(token)
    elif state == 52:
        state_type, next_state = state52(token)
    elif state == 53:
        state_type, next_state = state53(token)
    elif state == 54:
        state_type, next_state = state54(token)
    elif state == 55:
        state_type, next_state = state55(token)
    elif state == 56:
        state_type, next_state = state56(token)
    elif state == 57:
        state_type, next_state = state57(token)
    elif state == 58:
        state_type, next_state = state58(token)
    elif state == 59:
        state_type, next_state = state59(token)
    elif state == 60:
        state_type, next_state = state60(token)
    elif state == 61:
        state_type, next_state = state61(token)
    elif state == 62:
        state_type, next_state = state62(token)
    elif state == 63:
        state_type, next_state = state63(token)
    elif state == 64:
        state_type, next_state = state64(token)
    elif state == 65:
        state_type, next_state = state65(token)
    elif state == 66:
        state_type, next_state = state66(token)
    elif state == 67:
        state_type, next_state = state67(token)
    elif state == 68:
        state_type, next_state = state68(token)
    elif state == 69:
        state_type, next_state = state69(token)
    elif state == 70:
        state_type, next_state = state70(token)
    elif state == 71:
        state_type, next_state = state71(token)
    elif state == 72:
        state_type, next_state = state72(token)
    elif state == 73:
        state_type, next_state = state73(token)
    elif state == 74:
        state_type, next_state = state74(token)
    elif state == 75:
        state_type, next_state = state75(token)
    elif state == 76:
        state_type, next_state = state76(token)
    elif state == 77:
        state_type, next_state = state77(token)
    elif state == 78:
        state_type, next_state = state78(token)
    elif state == 79:
        state_type, next_state = state79(token)
    elif state == 80:
        state_type, next_state = state80(token)
    elif state == 81:
        state_type, next_state = state81(token)
    elif state == 82:
        state_type, next_state = state82(token)
    elif state == 83:
        state_type, next_state = state83(token)
    elif state == 84:
        state_type, next_state = state84(token)
    elif state == 85:
        state_type, next_state = state85(token)
    elif state == 86:
        state_type, next_state = state86(token)
    elif state == 87:
        state_type, next_state = state87(token)
    elif state == 88:
        state_type, next_state = state88(token)
    elif state == 89:
        state_type, next_state = state89(token)
    elif state == 90:
        state_type, next_state = state90(token)
    elif state == 91:
        state_type, next_state = state91(token)
    elif state == 92:
        state_type, next_state = state92(token)
    elif state == 93:
        state_type, next_state = state93(token)
    elif state == 94:
        state_type, next_state = state94(token)
    elif state == 95:
        state_type, next_state = state95(token)
    elif state == 96:
        state_type, next_state = state96(token)
    elif state == 97:
        state_type, next_state = state97(token)
    elif state == 98:
        state_type, next_state = state98(token)
    elif state == 99:
        state_type, next_state = state99(token)
    elif state == 100:
        state_type, next_state = state100(token)
    elif state == 101:
        state_type, next_state = state101(token)
    elif state == 102:
        state_type, next_state = state102(token)
    elif state == 103:
        state_type, next_state = state103(token)
    elif state == 104:
        state_type, next_state = state104(token)
    elif state == 105:
        state_type, next_state = state105(token)
    elif state == 106:
        state_type, next_state = state106(token)
    elif state == 107:
        state_type, next_state = state107(token)
    elif state == 108:
        state_type, next_state = state108(token)
    elif state == 109:
        state_type, next_state = state109(token)
    elif state == 110:
        state_type, next_state = state110(token)
    elif state == 111:
        state_type, next_state = state111(token)
    elif state == 112:
        state_type, next_state = state112(token)
    elif state == 113:
        state_type, next_state = state113(token)
    elif state == 114:
        state_type, next_state = state114(token)
    elif state == 115:
        state_type, next_state = state115(token)
    elif state == 116:
        state_type, next_state = state116(token)
    elif state == 117:
        state_type, next_state = state117(token)
    elif state == 118:
        state_type, next_state = state118(token)
    elif state == 119:
        state_type, next_state = state119(token)
    elif state == 120:
        state_type, next_state = state120(token)
    elif state == 121:
        state_type, next_state = state121(token)
    elif state == 122:
        state_type, next_state = state122(token)
    elif state == 123:
        state_type, next_state = state123(token)
    elif state == 124:
        state_type, next_state = state124(token)
    elif state == 125:
        state_type, next_state = state125(token)
    elif state == 126:
        state_type, next_state = state126(token)
    elif state == 127:
        state_type, next_state = state127(token)
    elif state == 128:
        state_type, next_state = state128(token)
    elif state == 129:
        state_type, next_state = state129(token)
    elif state == 130:
        state_type, next_state = state130(token)
    elif state == 131:
        state_type, next_state = state131(token)
    elif state == 132:
        state_type, next_state = state132(token)
    elif state == 133:
        state_type, next_state = state133(token)
    elif state == 134:
        state_type, next_state = state134(token)
    elif state == 135:
        state_type, next_state = state135(token)
    elif state == 136:
        state_type, next_state = state136(token)
    elif state == 137:
        state_type, next_state = state137(token)
    elif state == 138:
        state_type, next_state = state138(token)
    elif state == 139:
        state_type, next_state = state139(token)
    elif state == 140:
        state_type, next_state = state140(token)
    elif state == 141:
        state_type, next_state = state141(token)
    elif state == 142:
        state_type, next_state = state142(token)
    elif state == 143:
        state_type, next_state = state143(token)
    elif state == 144:
        state_type, next_state = state144(token)
    elif state == 145:
        state_type, next_state = state145(token)
    elif state == 146:
        state_type, next_state = state146(token)
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state0(c):
    if c in col31:
        state_type = 'shift'
        next_state = 2
    elif c in col50:
        state_type = 'goto'
        next_state = 1
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state1(c):
    if c in col1:
        state_type = 'accept'
        next_state = 0
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state2(c):
    if c in col16:
        state_type = 'shift'
        next_state = 3
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state3(c):
    if c in col4:
        state_type = 'shift'
        next_state = 4
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state4(c):
    if c in col5:
        state_type = 'shift'
        next_state = 5
    elif c in col38:
        state_type = 'shift'
        next_state = 11
    elif c in col43:
        state_type = 'shift'
        next_state = 13
    elif c in col44:
        state_type = 'shift'
        next_state = 12
    elif c in col53:
        state_type = 'goto'
        next_state = 8
    elif c in col54:
        state_type = 'goto'
        next_state = 6
    elif c in col61:
        state_type = 'goto'
        next_state = 9
    elif c in col62:
        state_type = 'goto'
        next_state = 7
    elif c in col66:
        state_type = 'goto'
        next_state = 10
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state5(c):
    if c in col1:
        state_type = 'reduce'
        next_state = 1
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state6(c):
    if c in col5:
        state_type = 'shift'
        next_state = 14
    elif c in col38:
        state_type = 'shift'
        next_state = 11
    elif c in col43:
        state_type = 'shift'
        next_state = 13
    elif c in col44:
        state_type = 'shift'
        next_state = 12
    elif c in col53:
        state_type = 'goto'
        next_state = 16
    elif c in col61:
        state_type = 'goto'
        next_state = 9
    elif c in col62:
        state_type = 'goto'
        next_state = 15
    elif c in col66:
        state_type = 'goto'
        next_state = 10
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state7(c):
    if c in col5:
        state_type = 'shift'
        next_state = 17
    elif c in col38:
        state_type = 'shift'
        next_state = 11
    elif c in col43:
        state_type = 'shift'
        next_state = 13
    elif c in col44:
        state_type = 'shift'
        next_state = 12
    elif c in col61:
        state_type = 'goto'
        next_state = 18
    elif c in col66:
        state_type = 'goto'
        next_state = 19
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state8(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 6
    elif c in col16:
        state_type = 'reduce'
        next_state = 6
    elif c in col29:
        state_type = 'reduce'
        next_state = 6
    elif c in col30:
        state_type = 'reduce'
        next_state = 6
    elif c in col32:
        state_type = 'reduce'
        next_state = 6
    elif c in col34:
        state_type = 'reduce'
        next_state = 6
    elif c in col35:
        state_type = 'reduce'
        next_state = 6
    elif c in col37:
        state_type = 'reduce'
        next_state = 6
    elif c in col38:
        state_type = 'reduce'
        next_state = 6
    elif c in col43:
        state_type = 'reduce'
        next_state = 6
    elif c in col44:
        state_type = 'reduce'
        next_state = 6
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state9(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 8
    elif c in col38:
        state_type = 'reduce'
        next_state = 8
    elif c in col43:
        state_type = 'reduce'
        next_state = 8
    elif c in col44:
        state_type = 'reduce'
        next_state = 8
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state10(c):
    if c in col16:
        state_type = 'shift'
        next_state = 20
    elif c in col55:
        state_type = 'goto'
        next_state = 21
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state11(c):
    if c in col16:
        state_type = 'shift'
        next_state = 22
    elif c in col36:
        state_type = 'shift'
        next_state = 23
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state12(c):
    if c in col16:
        state_type = 'reduce'
        next_state = 12
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state13(c):
    if c in col16:
        state_type = 'reduce'
        next_state = 13
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state14(c):
    if c in col1:
        state_type = 'reduce'
        next_state = 2
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state15(c):
    if c in col5:
        state_type = 'shift'
        next_state = 24
    elif c in col38:
        state_type = 'shift'
        next_state = 11
    elif c in col43:
        state_type = 'shift'
        next_state = 13
    elif c in col44:
        state_type = 'shift'
        next_state = 12
    elif c in col61:
        state_type = 'goto'
        next_state = 18
    elif c in col66:
        state_type = 'goto'
        next_state = 19
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state16(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 5
    elif c in col16:
        state_type = 'reduce'
        next_state = 5
    elif c in col29:
        state_type = 'reduce'
        next_state = 5
    elif c in col30:
        state_type = 'reduce'
        next_state = 5
    elif c in col32:
        state_type = 'reduce'
        next_state = 5
    elif c in col34:
        state_type = 'reduce'
        next_state = 5
    elif c in col35:
        state_type = 'reduce'
        next_state = 5
    elif c in col37:
        state_type = 'reduce'
        next_state = 5
    elif c in col38:
        state_type = 'reduce'
        next_state = 5
    elif c in col43:
        state_type = 'reduce'
        next_state = 5
    elif c in col44:
        state_type = 'reduce'
        next_state = 5
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state17(c):
    if c in col1:
        state_type = 'reduce'
        next_state = 3
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state18(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 7
    elif c in col38:
        state_type = 'reduce'
        next_state = 7
    elif c in col43:
        state_type = 'reduce'
        next_state = 7
    elif c in col44:
        state_type = 'reduce'
        next_state = 7
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state19(c):
    if c in col16:
        state_type = 'shift'
        next_state = 25
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state20(c):
    if c in col8:
        state_type = 'shift'
        next_state = 28
    elif c in col26:
        state_type = 'shift'
        next_state = 27
    elif c in col39:
        state_type = 'shift'
        next_state = 26
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state21(c):
    if c in col39:
        state_type = 'shift'
        next_state = 29
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state22(c):
    if c in col26:
        state_type = 'shift'
        next_state = 30
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state23(c):
    if c in col26:
        state_type = 'shift'
        next_state = 31
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state24(c):
    if c in col1:
        state_type = 'reduce'
        next_state = 4
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state25(c):
    if c in col26:
        state_type = 'shift'
        next_state = 27
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state26(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 9
    elif c in col16:
        state_type = 'reduce'
        next_state = 9
    elif c in col29:
        state_type = 'reduce'
        next_state = 9
    elif c in col30:
        state_type = 'reduce'
        next_state = 9
    elif c in col32:
        state_type = 'reduce'
        next_state = 9
    elif c in col34:
        state_type = 'reduce'
        next_state = 9
    elif c in col35:
        state_type = 'reduce'
        next_state = 9
    elif c in col37:
        state_type = 'reduce'
        next_state = 9
    elif c in col38:
        state_type = 'reduce'
        next_state = 9
    elif c in col43:
        state_type = 'reduce'
        next_state = 9
    elif c in col44:
        state_type = 'reduce'
        next_state = 9
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state27(c):
    if c in col27:
        state_type = 'shift'
        next_state = 32
    elif c in col43:
        state_type = 'shift'
        next_state = 13
    elif c in col44:
        state_type = 'shift'
        next_state = 12
    elif c in col58:
        state_type = 'goto'
        next_state = 34
    elif c in col59:
        state_type = 'goto'
        next_state = 33
    elif c in col66:
        state_type = 'goto'
        next_state = 35
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state28(c):
    if c in col16:
        state_type = 'shift'
        next_state = 36
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state29(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 10
    elif c in col16:
        state_type = 'reduce'
        next_state = 10
    elif c in col29:
        state_type = 'reduce'
        next_state = 10
    elif c in col30:
        state_type = 'reduce'
        next_state = 10
    elif c in col32:
        state_type = 'reduce'
        next_state = 10
    elif c in col34:
        state_type = 'reduce'
        next_state = 10
    elif c in col35:
        state_type = 'reduce'
        next_state = 10
    elif c in col37:
        state_type = 'reduce'
        next_state = 10
    elif c in col38:
        state_type = 'reduce'
        next_state = 10
    elif c in col43:
        state_type = 'reduce'
        next_state = 10
    elif c in col44:
        state_type = 'reduce'
        next_state = 10
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state30(c):
    if c in col27:
        state_type = 'shift'
        next_state = 37
    elif c in col43:
        state_type = 'shift'
        next_state = 13
    elif c in col44:
        state_type = 'shift'
        next_state = 12
    elif c in col58:
        state_type = 'goto'
        next_state = 34
    elif c in col59:
        state_type = 'goto'
        next_state = 38
    elif c in col66:
        state_type = 'goto'
        next_state = 35
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state31(c):
    if c in col27:
        state_type = 'shift'
        next_state = 39
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state32(c):
    if c in col4:
        state_type = 'shift'
        next_state = 41
    elif c in col47:
        state_type = 'goto'
        next_state = 40
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state33(c):
    if c in col8:
        state_type = 'shift'
        next_state = 43
    elif c in col27:
        state_type = 'shift'
        next_state = 42
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state34(c):
    if c in col8:
        state_type = 'reduce'
        next_state = 20
    elif c in col27:
        state_type = 'reduce'
        next_state = 20
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state35(c):
    if c in col16:
        state_type = 'shift'
        next_state = 44
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state36(c):
    if c in col39:
        state_type = 'reduce'
        next_state = 11
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state37(c):
    if c in col4:
        state_type = 'shift'
        next_state = 41
    elif c in col47:
        state_type = 'goto'
        next_state = 45
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state38(c):
    if c in col8:
        state_type = 'shift'
        next_state = 43
    elif c in col27:
        state_type = 'shift'
        next_state = 46
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state39(c):
    if c in col4:
        state_type = 'shift'
        next_state = 41
    elif c in col47:
        state_type = 'goto'
        next_state = 47
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state40(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 14
    elif c in col38:
        state_type = 'reduce'
        next_state = 14
    elif c in col43:
        state_type = 'reduce'
        next_state = 14
    elif c in col44:
        state_type = 'reduce'
        next_state = 14
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state41(c):
    if c in col5:
        state_type = 'shift'
        next_state = 48
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col29:
        state_type = 'shift'
        next_state = 58
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col32:
        state_type = 'shift'
        next_state = 59
    elif c in col34:
        state_type = 'shift'
        next_state = 56
    elif c in col35:
        state_type = 'shift'
        next_state = 55
    elif c in col37:
        state_type = 'shift'
        next_state = 57
    elif c in col43:
        state_type = 'shift'
        next_state = 13
    elif c in col44:
        state_type = 'shift'
        next_state = 12
    elif c in col53:
        state_type = 'goto'
        next_state = 8
    elif c in col54:
        state_type = 'goto'
        next_state = 51
    elif c in col57:
        state_type = 'goto'
        next_state = 53
    elif c in col60:
        state_type = 'goto'
        next_state = 54
    elif c in col63:
        state_type = 'goto'
        next_state = 52
    elif c in col64:
        state_type = 'goto'
        next_state = 50
    elif c in col65:
        state_type = 'goto'
        next_state = 49
    elif c in col66:
        state_type = 'goto'
        next_state = 60
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state42(c):
    if c in col4:
        state_type = 'shift'
        next_state = 41
    elif c in col47:
        state_type = 'goto'
        next_state = 63
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state43(c):
    if c in col43:
        state_type = 'shift'
        next_state = 13
    elif c in col44:
        state_type = 'shift'
        next_state = 12
    elif c in col58:
        state_type = 'goto'
        next_state = 64
    elif c in col66:
        state_type = 'goto'
        next_state = 35
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state44(c):
    if c in col8:
        state_type = 'reduce'
        next_state = 21
    elif c in col27:
        state_type = 'reduce'
        next_state = 21
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state45(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 16
    elif c in col38:
        state_type = 'reduce'
        next_state = 16
    elif c in col43:
        state_type = 'reduce'
        next_state = 16
    elif c in col44:
        state_type = 'reduce'
        next_state = 16
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state46(c):
    if c in col4:
        state_type = 'shift'
        next_state = 41
    elif c in col47:
        state_type = 'goto'
        next_state = 65
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state47(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 18
    elif c in col38:
        state_type = 'reduce'
        next_state = 18
    elif c in col43:
        state_type = 'reduce'
        next_state = 18
    elif c in col44:
        state_type = 'reduce'
        next_state = 18
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state48(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 22
    elif c in col16:
        state_type = 'reduce'
        next_state = 22
    elif c in col29:
        state_type = 'reduce'
        next_state = 22
    elif c in col30:
        state_type = 'reduce'
        next_state = 22
    elif c in col32:
        state_type = 'reduce'
        next_state = 22
    elif c in col33:
        state_type = 'reduce'
        next_state = 22
    elif c in col34:
        state_type = 'reduce'
        next_state = 22
    elif c in col35:
        state_type = 'reduce'
        next_state = 22
    elif c in col37:
        state_type = 'reduce'
        next_state = 22
    elif c in col38:
        state_type = 'reduce'
        next_state = 22
    elif c in col43:
        state_type = 'reduce'
        next_state = 22
    elif c in col44:
        state_type = 'reduce'
        next_state = 22
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state49(c):
    if c in col5:
        state_type = 'shift'
        next_state = 66
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col29:
        state_type = 'shift'
        next_state = 58
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col32:
        state_type = 'shift'
        next_state = 59
    elif c in col34:
        state_type = 'shift'
        next_state = 56
    elif c in col35:
        state_type = 'shift'
        next_state = 55
    elif c in col37:
        state_type = 'shift'
        next_state = 57
    elif c in col57:
        state_type = 'goto'
        next_state = 53
    elif c in col60:
        state_type = 'goto'
        next_state = 54
    elif c in col63:
        state_type = 'goto'
        next_state = 52
    elif c in col64:
        state_type = 'goto'
        next_state = 67
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state50(c):
    if c in col5:
        state_type = 'shift'
        next_state = 68
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col29:
        state_type = 'shift'
        next_state = 58
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col32:
        state_type = 'shift'
        next_state = 59
    elif c in col34:
        state_type = 'shift'
        next_state = 56
    elif c in col35:
        state_type = 'shift'
        next_state = 55
    elif c in col37:
        state_type = 'shift'
        next_state = 57
    elif c in col57:
        state_type = 'goto'
        next_state = 53
    elif c in col60:
        state_type = 'goto'
        next_state = 54
    elif c in col63:
        state_type = 'goto'
        next_state = 69
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state51(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 26
    elif c in col16:
        state_type = 'reduce'
        next_state = 26
    elif c in col29:
        state_type = 'reduce'
        next_state = 26
    elif c in col30:
        state_type = 'reduce'
        next_state = 26
    elif c in col32:
        state_type = 'reduce'
        next_state = 26
    elif c in col34:
        state_type = 'reduce'
        next_state = 26
    elif c in col35:
        state_type = 'reduce'
        next_state = 26
    elif c in col37:
        state_type = 'reduce'
        next_state = 26
    elif c in col43:
        state_type = 'shift'
        next_state = 13
    elif c in col44:
        state_type = 'shift'
        next_state = 12
    elif c in col53:
        state_type = 'shift'
        next_state = 16
    elif c in col66:
        state_type = 'goto'
        next_state = 60
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state52(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 28
    elif c in col16:
        state_type = 'reduce'
        next_state = 28
    elif c in col29:
        state_type = 'reduce'
        next_state = 28
    elif c in col30:
        state_type = 'reduce'
        next_state = 28
    elif c in col32:
        state_type = 'reduce'
        next_state = 28
    elif c in col34:
        state_type = 'reduce'
        next_state = 28
    elif c in col35:
        state_type = 'reduce'
        next_state = 28
    elif c in col37:
        state_type = 'reduce'
        next_state = 28
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state53(c):
    if c in col3:
        state_type = 'shift'
        next_state = 71
    elif c in col20:
        state_type = 'shift'
        next_state = 73
    elif c in col28:
        state_type = 'shift'
        next_state = 72
    elif c in col45:
        state_type = 'goto'
        next_state = 70
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state54(c):
    if c in col39:
        state_type = 'shift'
        next_state = 74
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state55(c):
    if c in col26:
        state_type = 'shift'
        next_state = 75
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state56(c):
    if c in col16:
        state_type = 'shift'
        next_state = 76
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state57(c):
    if c in col4:
        state_type = 'shift'
        next_state = 84
    elif c in col9:
        state_type = 'shift'
        next_state = 87
    elif c in col12:
        state_type = 'shift'
        next_state = 86
    elif c in col15:
        state_type = 'shift'
        next_state = 88
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col19:
        state_type = 'shift'
        next_state = 82
    elif c in col23:
        state_type = 'shift'
        next_state = 83
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col39:
        state_type = 'shift'
        next_state = 77
    elif c in col42:
        state_type = 'shift'
        next_state = 85
    elif c in col51:
        state_type = 'goto'
        next_state = 78
    elif c in col56:
        state_type = 'goto'
        next_state = 81
    elif c in col57:
        state_type = 'goto'
        next_state = 79
    elif c in col60:
        state_type = 'goto'
        next_state = 80
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state58(c):
    if c in col39:
        state_type = 'shift'
        next_state = 89
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state59(c):
    if c in col39:
        state_type = 'shift'
        next_state = 90
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state60(c):
    if c in col16:
        state_type = 'shift'
        next_state = 91
    elif c in col55:
        state_type = 'goto'
        next_state = 21
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state61(c):
    if c in col2:
        state_type = 'reduce'
        next_state = 38
    elif c in col3:
        state_type = 'reduce'
        next_state = 38
    elif c in col4:
        state_type = 'reduce'
        next_state = 38
    elif c in col5:
        state_type = 'reduce'
        next_state = 38
    elif c in col6:
        state_type = 'shift'
        next_state = 92
    elif c in col7:
        state_type = 'reduce'
        next_state = 38
    elif c in col8:
        state_type = 'reduce'
        next_state = 38
    elif c in col10:
        state_type = 'reduce'
        next_state = 38
    elif c in col11:
        state_type = 'reduce'
        next_state = 38
    elif c in col13:
        state_type = 'reduce'
        next_state = 38
    elif c in col14:
        state_type = 'reduce'
        next_state = 38
    elif c in col17:
        state_type = 'reduce'
        next_state = 38
    elif c in col18:
        state_type = 'reduce'
        next_state = 38
    elif c in col19:
        state_type = 'reduce'
        next_state = 38
    elif c in col20:
        state_type = 'reduce'
        next_state = 38
    elif c in col21:
        state_type = 'reduce'
        next_state = 38
    elif c in col22:
        state_type = 'reduce'
        next_state = 38
    elif c in col24:
        state_type = 'reduce'
        next_state = 38
    elif c in col25:
        state_type = 'reduce'
        next_state = 38
    elif c in col26:
        state_type = 'shift'
        next_state = 93
    elif c in col27:
        state_type = 'reduce'
        next_state = 38
    elif c in col28:
        state_type = 'reduce'
        next_state = 38
    elif c in col39:
        state_type = 'reduce'
        next_state = 38
    elif c in col41:
        state_type = 'reduce'
        next_state = 38
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state62(c):
    if c in col26:
        state_type = 'shift'
        next_state = 94
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state63(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 15
    elif c in col38:
        state_type = 'reduce'
        next_state = 15
    elif c in col43:
        state_type = 'reduce'
        next_state = 15
    elif c in col44:
        state_type = 'reduce'
        next_state = 15
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state64(c):
    if c in col8:
        state_type = 'reduce'
        next_state = 19
    elif c in col27:
        state_type = 'reduce'
        next_state = 19
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state65(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 17
    elif c in col38:
        state_type = 'reduce'
        next_state = 17
    elif c in col43:
        state_type = 'reduce'
        next_state = 17
    elif c in col44:
        state_type = 'reduce'
        next_state = 17
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state66(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 23
    elif c in col16:
        state_type = 'reduce'
        next_state = 23
    elif c in col29:
        state_type = 'reduce'
        next_state = 23
    elif c in col30:
        state_type = 'reduce'
        next_state = 23
    elif c in col32:
        state_type = 'reduce'
        next_state = 23
    elif c in col33:
        state_type = 'reduce'
        next_state = 23
    elif c in col34:
        state_type = 'reduce'
        next_state = 23
    elif c in col35:
        state_type = 'reduce'
        next_state = 23
    elif c in col37:
        state_type = 'reduce'
        next_state = 23
    elif c in col38:
        state_type = 'reduce'
        next_state = 23
    elif c in col43:
        state_type = 'reduce'
        next_state = 23
    elif c in col44:
        state_type = 'reduce'
        next_state = 23
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state67(c):
    if c in col5:
        state_type = 'shift'
        next_state = 95
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col29:
        state_type = 'shift'
        next_state = 58
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col32:
        state_type = 'shift'
        next_state = 59
    elif c in col34:
        state_type = 'shift'
        next_state = 56
    elif c in col35:
        state_type = 'shift'
        next_state = 55
    elif c in col37:
        state_type = 'shift'
        next_state = 57
    elif c in col57:
        state_type = 'goto'
        next_state = 53
    elif c in col60:
        state_type = 'goto'
        next_state = 54
    elif c in col63:
        state_type = 'goto'
        next_state = 69
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state68(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 24
    elif c in col16:
        state_type = 'reduce'
        next_state = 24
    elif c in col29:
        state_type = 'reduce'
        next_state = 24
    elif c in col30:
        state_type = 'reduce'
        next_state = 24
    elif c in col32:
        state_type = 'reduce'
        next_state = 24
    elif c in col33:
        state_type = 'reduce'
        next_state = 24
    elif c in col34:
        state_type = 'reduce'
        next_state = 24
    elif c in col35:
        state_type = 'reduce'
        next_state = 24
    elif c in col37:
        state_type = 'reduce'
        next_state = 24
    elif c in col38:
        state_type = 'reduce'
        next_state = 24
    elif c in col43:
        state_type = 'reduce'
        next_state = 24
    elif c in col44:
        state_type = 'reduce'
        next_state = 24
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state69(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 27
    elif c in col16:
        state_type = 'reduce'
        next_state = 27
    elif c in col29:
        state_type = 'reduce'
        next_state = 27
    elif c in col30:
        state_type = 'reduce'
        next_state = 27
    elif c in col32:
        state_type = 'reduce'
        next_state = 27
    elif c in col34:
        state_type = 'reduce'
        next_state = 27
    elif c in col35:
        state_type = 'reduce'
        next_state = 27
    elif c in col37:
        state_type = 'reduce'
        next_state = 27
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state70(c):
    if c in col4:
        state_type = 'shift'
        next_state = 84
    elif c in col9:
        state_type = 'shift'
        next_state = 87
    elif c in col12:
        state_type = 'shift'
        next_state = 86
    elif c in col15:
        state_type = 'shift'
        next_state = 88
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col19:
        state_type = 'shift'
        next_state = 82
    elif c in col23:
        state_type = 'shift'
        next_state = 83
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col42:
        state_type = 'shift'
        next_state = 85
    elif c in col51:
        state_type = 'goto'
        next_state = 96
    elif c in col56:
        state_type = 'goto'
        next_state = 81
    elif c in col57:
        state_type = 'goto'
        next_state = 79
    elif c in col60:
        state_type = 'goto'
        next_state = 80
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state71(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 40
    elif c in col9:
        state_type = 'reduce'
        next_state = 40
    elif c in col12:
        state_type = 'reduce'
        next_state = 40
    elif c in col15:
        state_type = 'reduce'
        next_state = 40
    elif c in col16:
        state_type = 'reduce'
        next_state = 40
    elif c in col19:
        state_type = 'reduce'
        next_state = 40
    elif c in col23:
        state_type = 'reduce'
        next_state = 40
    elif c in col30:
        state_type = 'reduce'
        next_state = 40
    elif c in col42:
        state_type = 'reduce'
        next_state = 40
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state72(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 41
    elif c in col9:
        state_type = 'reduce'
        next_state = 41
    elif c in col12:
        state_type = 'reduce'
        next_state = 41
    elif c in col15:
        state_type = 'reduce'
        next_state = 41
    elif c in col16:
        state_type = 'reduce'
        next_state = 41
    elif c in col19:
        state_type = 'reduce'
        next_state = 41
    elif c in col23:
        state_type = 'reduce'
        next_state = 41
    elif c in col30:
        state_type = 'reduce'
        next_state = 41
    elif c in col42:
        state_type = 'reduce'
        next_state = 41
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state73(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 42
    elif c in col9:
        state_type = 'reduce'
        next_state = 42
    elif c in col12:
        state_type = 'reduce'
        next_state = 42
    elif c in col15:
        state_type = 'reduce'
        next_state = 42
    elif c in col16:
        state_type = 'reduce'
        next_state = 42
    elif c in col19:
        state_type = 'reduce'
        next_state = 42
    elif c in col23:
        state_type = 'reduce'
        next_state = 42
    elif c in col30:
        state_type = 'reduce'
        next_state = 42
    elif c in col42:
        state_type = 'reduce'
        next_state = 42
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state74(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 30
    elif c in col16:
        state_type = 'reduce'
        next_state = 30
    elif c in col29:
        state_type = 'reduce'
        next_state = 30
    elif c in col30:
        state_type = 'reduce'
        next_state = 30
    elif c in col32:
        state_type = 'reduce'
        next_state = 30
    elif c in col34:
        state_type = 'reduce'
        next_state = 30
    elif c in col35:
        state_type = 'reduce'
        next_state = 30
    elif c in col37:
        state_type = 'reduce'
        next_state = 30
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state75(c):
    if c in col4:
        state_type = 'shift'
        next_state = 84
    elif c in col9:
        state_type = 'shift'
        next_state = 87
    elif c in col12:
        state_type = 'shift'
        next_state = 86
    elif c in col15:
        state_type = 'shift'
        next_state = 88
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col19:
        state_type = 'shift'
        next_state = 82
    elif c in col23:
        state_type = 'shift'
        next_state = 83
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col42:
        state_type = 'shift'
        next_state = 85
    elif c in col51:
        state_type = 'goto'
        next_state = 97
    elif c in col56:
        state_type = 'goto'
        next_state = 81
    elif c in col57:
        state_type = 'goto'
        next_state = 79
    elif c in col60:
        state_type = 'goto'
        next_state = 80
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state76(c):
    if c in col3:
        state_type = 'shift'
        next_state = 98
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state77(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 34
    elif c in col16:
        state_type = 'reduce'
        next_state = 34
    elif c in col29:
        state_type = 'reduce'
        next_state = 34
    elif c in col30:
        state_type = 'reduce'
        next_state = 34
    elif c in col32:
        state_type = 'reduce'
        next_state = 34
    elif c in col34:
        state_type = 'reduce'
        next_state = 34
    elif c in col35:
        state_type = 'reduce'
        next_state = 34
    elif c in col37:
        state_type = 'reduce'
        next_state = 34
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state78(c):
    if c in col2:
        state_type = 'shift'
        next_state = 112
    elif c in col10:
        state_type = 'shift'
        next_state = 102
    elif c in col11:
        state_type = 'shift'
        next_state = 110
    elif c in col13:
        state_type = 'shift'
        next_state = 108
    elif c in col14:
        state_type = 'shift'
        next_state = 106
    elif c in col17:
        state_type = 'shift'
        next_state = 109
    elif c in col18:
        state_type = 'shift'
        next_state = 107
    elif c in col19:
        state_type = 'shift'
        next_state = 104
    elif c in col21:
        state_type = 'shift'
        next_state = 101
    elif c in col22:
        state_type = 'shift'
        next_state = 103
    elif c in col24:
        state_type = 'shift'
        next_state = 111
    elif c in col25:
        state_type = 'shift'
        next_state = 113
    elif c in col39:
        state_type = 'shift'
        next_state = 99
    elif c in col41:
        state_type = 'shift'
        next_state = 105
    elif c in col46:
        state_type = 'goto'
        next_state = 100
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state79(c):
    if c in col2:
        state_type = 'reduce'
        next_state = 43
    elif c in col4:
        state_type = 'reduce'
        next_state = 43
    elif c in col5:
        state_type = 'reduce'
        next_state = 43
    elif c in col7:
        state_type = 'reduce'
        next_state = 43
    elif c in col8:
        state_type = 'reduce'
        next_state = 43
    elif c in col10:
        state_type = 'reduce'
        next_state = 43
    elif c in col11:
        state_type = 'reduce'
        next_state = 43
    elif c in col13:
        state_type = 'reduce'
        next_state = 43
    elif c in col14:
        state_type = 'reduce'
        next_state = 43
    elif c in col17:
        state_type = 'reduce'
        next_state = 43
    elif c in col18:
        state_type = 'reduce'
        next_state = 43
    elif c in col19:
        state_type = 'reduce'
        next_state = 43
    elif c in col21:
        state_type = 'reduce'
        next_state = 43
    elif c in col22:
        state_type = 'reduce'
        next_state = 43
    elif c in col24:
        state_type = 'reduce'
        next_state = 43
    elif c in col25:
        state_type = 'reduce'
        next_state = 43
    elif c in col27:
        state_type = 'reduce'
        next_state = 43
    elif c in col39:
        state_type = 'reduce'
        next_state = 43
    elif c in col41:
        state_type = 'reduce'
        next_state = 43
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state80(c):
    if c in col2:
        state_type = 'reduce'
        next_state = 44
    elif c in col4:
        state_type = 'reduce'
        next_state = 44
    elif c in col5:
        state_type = 'reduce'
        next_state = 44
    elif c in col7:
        state_type = 'reduce'
        next_state = 44
    elif c in col8:
        state_type = 'reduce'
        next_state = 44
    elif c in col10:
        state_type = 'reduce'
        next_state = 44
    elif c in col11:
        state_type = 'reduce'
        next_state = 44
    elif c in col13:
        state_type = 'reduce'
        next_state = 44
    elif c in col14:
        state_type = 'reduce'
        next_state = 44
    elif c in col17:
        state_type = 'reduce'
        next_state = 44
    elif c in col18:
        state_type = 'reduce'
        next_state = 44
    elif c in col19:
        state_type = 'reduce'
        next_state = 44
    elif c in col21:
        state_type = 'reduce'
        next_state = 44
    elif c in col22:
        state_type = 'reduce'
        next_state = 44
    elif c in col24:
        state_type = 'reduce'
        next_state = 44
    elif c in col25:
        state_type = 'reduce'
        next_state = 44
    elif c in col27:
        state_type = 'reduce'
        next_state = 44
    elif c in col39:
        state_type = 'reduce'
        next_state = 44
    elif c in col41:
        state_type = 'reduce'
        next_state = 44
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state81(c):
    if c in col2:
        state_type = 'reduce'
        next_state = 45
    elif c in col4:
        state_type = 'reduce'
        next_state = 45
    elif c in col5:
        state_type = 'reduce'
        next_state = 45
    elif c in col7:
        state_type = 'reduce'
        next_state = 45
    elif c in col8:
        state_type = 'reduce'
        next_state = 45
    elif c in col10:
        state_type = 'reduce'
        next_state = 45
    elif c in col11:
        state_type = 'reduce'
        next_state = 45
    elif c in col13:
        state_type = 'reduce'
        next_state = 45
    elif c in col14:
        state_type = 'reduce'
        next_state = 45
    elif c in col17:
        state_type = 'reduce'
        next_state = 45
    elif c in col18:
        state_type = 'reduce'
        next_state = 45
    elif c in col19:
        state_type = 'reduce'
        next_state = 45
    elif c in col21:
        state_type = 'reduce'
        next_state = 45
    elif c in col22:
        state_type = 'reduce'
        next_state = 45
    elif c in col24:
        state_type = 'reduce'
        next_state = 45
    elif c in col25:
        state_type = 'reduce'
        next_state = 45
    elif c in col27:
        state_type = 'reduce'
        next_state = 45
    elif c in col39:
        state_type = 'reduce'
        next_state = 45
    elif c in col41:
        state_type = 'reduce'
        next_state = 45
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state82(c):
    if c in col4:
        state_type = 'shift'
        next_state = 84
    elif c in col9:
        state_type = 'shift'
        next_state = 87
    elif c in col12:
        state_type = 'shift'
        next_state = 86
    elif c in col15:
        state_type = 'shift'
        next_state = 88
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col19:
        state_type = 'shift'
        next_state = 82
    elif c in col23:
        state_type = 'shift'
        next_state = 83
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col42:
        state_type = 'shift'
        next_state = 85
    elif c in col51:
        state_type = 'goto'
        next_state = 114
    elif c in col56:
        state_type = 'goto'
        next_state = 81
    elif c in col57:
        state_type = 'goto'
        next_state = 79
    elif c in col60:
        state_type = 'goto'
        next_state = 80
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state83(c):
    if c in col4:
        state_type = 'shift'
        next_state = 84
    elif c in col9:
        state_type = 'shift'
        next_state = 87
    elif c in col12:
        state_type = 'shift'
        next_state = 86
    elif c in col15:
        state_type = 'shift'
        next_state = 88
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col19:
        state_type = 'shift'
        next_state = 82
    elif c in col23:
        state_type = 'shift'
        next_state = 83
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col42:
        state_type = 'shift'
        next_state = 85
    elif c in col51:
        state_type = 'goto'
        next_state = 115
    elif c in col56:
        state_type = 'goto'
        next_state = 81
    elif c in col57:
        state_type = 'goto'
        next_state = 79
    elif c in col60:
        state_type = 'goto'
        next_state = 80
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state84(c):
    if c in col4:
        state_type = 'shift'
        next_state = 84
    elif c in col9:
        state_type = 'shift'
        next_state = 87
    elif c in col12:
        state_type = 'shift'
        next_state = 86
    elif c in col15:
        state_type = 'shift'
        next_state = 88
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col19:
        state_type = 'shift'
        next_state = 82
    elif c in col23:
        state_type = 'shift'
        next_state = 83
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col42:
        state_type = 'shift'
        next_state = 85
    elif c in col51:
        state_type = 'goto'
        next_state = 116
    elif c in col56:
        state_type = 'goto'
        next_state = 81
    elif c in col57:
        state_type = 'goto'
        next_state = 79
    elif c in col60:
        state_type = 'goto'
        next_state = 80
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state85(c):
    if c in col2:
        state_type = 'reduce'
        next_state = 57
    elif c in col4:
        state_type = 'reduce'
        next_state = 57
    elif c in col5:
        state_type = 'reduce'
        next_state = 57
    elif c in col7:
        state_type = 'reduce'
        next_state = 57
    elif c in col8:
        state_type = 'reduce'
        next_state = 57
    elif c in col10:
        state_type = 'reduce'
        next_state = 57
    elif c in col11:
        state_type = 'reduce'
        next_state = 57
    elif c in col13:
        state_type = 'reduce'
        next_state = 57
    elif c in col14:
        state_type = 'reduce'
        next_state = 57
    elif c in col17:
        state_type = 'reduce'
        next_state = 57
    elif c in col18:
        state_type = 'reduce'
        next_state = 57
    elif c in col19:
        state_type = 'reduce'
        next_state = 57
    elif c in col21:
        state_type = 'reduce'
        next_state = 57
    elif c in col22:
        state_type = 'reduce'
        next_state = 57
    elif c in col24:
        state_type = 'reduce'
        next_state = 57
    elif c in col25:
        state_type = 'reduce'
        next_state = 57
    elif c in col27:
        state_type = 'reduce'
        next_state = 57
    elif c in col39:
        state_type = 'reduce'
        next_state = 57
    elif c in col41:
        state_type = 'reduce'
        next_state = 57
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state86(c):
    if c in col2:
        state_type = 'reduce'
        next_state = 58
    elif c in col4:
        state_type = 'reduce'
        next_state = 58
    elif c in col5:
        state_type = 'reduce'
        next_state = 58
    elif c in col7:
        state_type = 'reduce'
        next_state = 58
    elif c in col8:
        state_type = 'reduce'
        next_state = 58
    elif c in col10:
        state_type = 'reduce'
        next_state = 58
    elif c in col11:
        state_type = 'reduce'
        next_state = 58
    elif c in col13:
        state_type = 'reduce'
        next_state = 58
    elif c in col14:
        state_type = 'reduce'
        next_state = 58
    elif c in col17:
        state_type = 'reduce'
        next_state = 58
    elif c in col18:
        state_type = 'reduce'
        next_state = 58
    elif c in col19:
        state_type = 'reduce'
        next_state = 58
    elif c in col21:
        state_type = 'reduce'
        next_state = 58
    elif c in col22:
        state_type = 'reduce'
        next_state = 58
    elif c in col24:
        state_type = 'reduce'
        next_state = 58
    elif c in col25:
        state_type = 'reduce'
        next_state = 58
    elif c in col27:
        state_type = 'reduce'
        next_state = 58
    elif c in col39:
        state_type = 'reduce'
        next_state = 58
    elif c in col41:
        state_type = 'reduce'
        next_state = 58
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state87(c):
    if c in col2:
        state_type = 'reduce'
        next_state = 59
    elif c in col4:
        state_type = 'reduce'
        next_state = 59
    elif c in col5:
        state_type = 'reduce'
        next_state = 59
    elif c in col7:
        state_type = 'reduce'
        next_state = 59
    elif c in col8:
        state_type = 'reduce'
        next_state = 59
    elif c in col10:
        state_type = 'reduce'
        next_state = 59
    elif c in col11:
        state_type = 'reduce'
        next_state = 59
    elif c in col13:
        state_type = 'reduce'
        next_state = 59
    elif c in col14:
        state_type = 'reduce'
        next_state = 59
    elif c in col17:
        state_type = 'reduce'
        next_state = 59
    elif c in col18:
        state_type = 'reduce'
        next_state = 59
    elif c in col19:
        state_type = 'reduce'
        next_state = 59
    elif c in col21:
        state_type = 'reduce'
        next_state = 59
    elif c in col22:
        state_type = 'reduce'
        next_state = 59
    elif c in col24:
        state_type = 'reduce'
        next_state = 59
    elif c in col25:
        state_type = 'reduce'
        next_state = 59
    elif c in col27:
        state_type = 'reduce'
        next_state = 59
    elif c in col39:
        state_type = 'reduce'
        next_state = 59
    elif c in col41:
        state_type = 'reduce'
        next_state = 59
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state88(c):
    if c in col2:
        state_type = 'reduce'
        next_state = 60
    elif c in col4:
        state_type = 'reduce'
        next_state = 60
    elif c in col5:
        state_type = 'reduce'
        next_state = 60
    elif c in col7:
        state_type = 'reduce'
        next_state = 60
    elif c in col8:
        state_type = 'reduce'
        next_state = 60
    elif c in col10:
        state_type = 'reduce'
        next_state = 60
    elif c in col11:
        state_type = 'reduce'
        next_state = 60
    elif c in col13:
        state_type = 'reduce'
        next_state = 60
    elif c in col14:
        state_type = 'reduce'
        next_state = 60
    elif c in col17:
        state_type = 'reduce'
        next_state = 60
    elif c in col18:
        state_type = 'reduce'
        next_state = 60
    elif c in col19:
        state_type = 'reduce'
        next_state = 60
    elif c in col21:
        state_type = 'reduce'
        next_state = 60
    elif c in col22:
        state_type = 'reduce'
        next_state = 60
    elif c in col24:
        state_type = 'reduce'
        next_state = 60
    elif c in col25:
        state_type = 'reduce'
        next_state = 60
    elif c in col27:
        state_type = 'reduce'
        next_state = 60
    elif c in col39:
        state_type = 'reduce'
        next_state = 60
    elif c in col41:
        state_type = 'reduce'
        next_state = 60
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state89(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 36
    elif c in col16:
        state_type = 'reduce'
        next_state = 36
    elif c in col29:
        state_type = 'reduce'
        next_state = 36
    elif c in col30:
        state_type = 'reduce'
        next_state = 36
    elif c in col32:
        state_type = 'reduce'
        next_state = 36
    elif c in col34:
        state_type = 'reduce'
        next_state = 36
    elif c in col35:
        state_type = 'reduce'
        next_state = 36
    elif c in col37:
        state_type = 'reduce'
        next_state = 36
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state90(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 37
    elif c in col16:
        state_type = 'reduce'
        next_state = 37
    elif c in col29:
        state_type = 'reduce'
        next_state = 37
    elif c in col30:
        state_type = 'reduce'
        next_state = 37
    elif c in col32:
        state_type = 'reduce'
        next_state = 37
    elif c in col34:
        state_type = 'reduce'
        next_state = 37
    elif c in col35:
        state_type = 'reduce'
        next_state = 37
    elif c in col37:
        state_type = 'reduce'
        next_state = 37
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state91(c):
    if c in col8:
        state_type = 'shift'
        next_state = 28
    elif c in col39:
        state_type = 'shift'
        next_state = 26
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state92(c):
    if c in col4:
        state_type = 'shift'
        next_state = 84
    elif c in col9:
        state_type = 'shift'
        next_state = 87
    elif c in col12:
        state_type = 'shift'
        next_state = 86
    elif c in col15:
        state_type = 'shift'
        next_state = 88
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col19:
        state_type = 'shift'
        next_state = 82
    elif c in col23:
        state_type = 'shift'
        next_state = 83
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col42:
        state_type = 'shift'
        next_state = 85
    elif c in col51:
        state_type = 'goto'
        next_state = 117
    elif c in col56:
        state_type = 'goto'
        next_state = 81
    elif c in col57:
        state_type = 'goto'
        next_state = 79
    elif c in col60:
        state_type = 'goto'
        next_state = 80
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state93(c):
    if c in col4:
        state_type = 'shift'
        next_state = 84
    elif c in col9:
        state_type = 'shift'
        next_state = 87
    elif c in col12:
        state_type = 'shift'
        next_state = 86
    elif c in col15:
        state_type = 'shift'
        next_state = 88
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col19:
        state_type = 'shift'
        next_state = 82
    elif c in col23:
        state_type = 'shift'
        next_state = 83
    elif c in col27:
        state_type = 'shift'
        next_state = 119
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col42:
        state_type = 'shift'
        next_state = 85
    elif c in col51:
        state_type = 'goto'
        next_state = 120
    elif c in col52:
        state_type = 'goto'
        next_state = 118
    elif c in col56:
        state_type = 'goto'
        next_state = 81
    elif c in col57:
        state_type = 'goto'
        next_state = 79
    elif c in col60:
        state_type = 'goto'
        next_state = 80
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state94(c):
    if c in col27:
        state_type = 'shift'
        next_state = 121
    elif c in col40:
        state_type = 'shift'
        next_state = 122
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state95(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 25
    elif c in col16:
        state_type = 'reduce'
        next_state = 25
    elif c in col29:
        state_type = 'reduce'
        next_state = 25
    elif c in col30:
        state_type = 'reduce'
        next_state = 25
    elif c in col32:
        state_type = 'reduce'
        next_state = 25
    elif c in col33:
        state_type = 'reduce'
        next_state = 25
    elif c in col34:
        state_type = 'reduce'
        next_state = 25
    elif c in col35:
        state_type = 'reduce'
        next_state = 25
    elif c in col37:
        state_type = 'reduce'
        next_state = 25
    elif c in col38:
        state_type = 'reduce'
        next_state = 25
    elif c in col43:
        state_type = 'reduce'
        next_state = 25
    elif c in col44:
        state_type = 'reduce'
        next_state = 25
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state96(c):
    if c in col2:
        state_type = 'shift'
        next_state = 112
    elif c in col10:
        state_type = 'shift'
        next_state = 102
    elif c in col11:
        state_type = 'shift'
        next_state = 110
    elif c in col13:
        state_type = 'shift'
        next_state = 108
    elif c in col14:
        state_type = 'shift'
        next_state = 106
    elif c in col17:
        state_type = 'shift'
        next_state = 109
    elif c in col18:
        state_type = 'shift'
        next_state = 107
    elif c in col19:
        state_type = 'shift'
        next_state = 104
    elif c in col21:
        state_type = 'shift'
        next_state = 101
    elif c in col22:
        state_type = 'shift'
        next_state = 103
    elif c in col24:
        state_type = 'shift'
        next_state = 111
    elif c in col25:
        state_type = 'shift'
        next_state = 113
    elif c in col39:
        state_type = 'shift'
        next_state = 123
    elif c in col41:
        state_type = 'shift'
        next_state = 105
    elif c in col46:
        state_type = 'goto'
        next_state = 100
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state97(c):
    if c in col2:
        state_type = 'shift'
        next_state = 112
    elif c in col10:
        state_type = 'shift'
        next_state = 102
    elif c in col11:
        state_type = 'shift'
        next_state = 110
    elif c in col13:
        state_type = 'shift'
        next_state = 108
    elif c in col14:
        state_type = 'shift'
        next_state = 106
    elif c in col17:
        state_type = 'shift'
        next_state = 109
    elif c in col18:
        state_type = 'shift'
        next_state = 107
    elif c in col19:
        state_type = 'shift'
        next_state = 104
    elif c in col21:
        state_type = 'shift'
        next_state = 101
    elif c in col22:
        state_type = 'shift'
        next_state = 103
    elif c in col24:
        state_type = 'shift'
        next_state = 111
    elif c in col25:
        state_type = 'shift'
        next_state = 113
    elif c in col27:
        state_type = 'shift'
        next_state = 124
    elif c in col41:
        state_type = 'shift'
        next_state = 105
    elif c in col46:
        state_type = 'goto'
        next_state = 100
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state98(c):
    if c in col4:
        state_type = 'shift'
        next_state = 84
    elif c in col9:
        state_type = 'shift'
        next_state = 87
    elif c in col12:
        state_type = 'shift'
        next_state = 86
    elif c in col15:
        state_type = 'shift'
        next_state = 88
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col19:
        state_type = 'shift'
        next_state = 82
    elif c in col23:
        state_type = 'shift'
        next_state = 83
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col42:
        state_type = 'shift'
        next_state = 85
    elif c in col51:
        state_type = 'goto'
        next_state = 125
    elif c in col56:
        state_type = 'goto'
        next_state = 81
    elif c in col57:
        state_type = 'goto'
        next_state = 79
    elif c in col60:
        state_type = 'goto'
        next_state = 80
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state99(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 35
    elif c in col16:
        state_type = 'reduce'
        next_state = 35
    elif c in col29:
        state_type = 'reduce'
        next_state = 35
    elif c in col30:
        state_type = 'reduce'
        next_state = 35
    elif c in col32:
        state_type = 'reduce'
        next_state = 35
    elif c in col34:
        state_type = 'reduce'
        next_state = 35
    elif c in col35:
        state_type = 'reduce'
        next_state = 35
    elif c in col37:
        state_type = 'reduce'
        next_state = 35
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state100(c):
    if c in col4:
        state_type = 'shift'
        next_state = 84
    elif c in col9:
        state_type = 'shift'
        next_state = 87
    elif c in col12:
        state_type = 'shift'
        next_state = 86
    elif c in col15:
        state_type = 'shift'
        next_state = 88
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col19:
        state_type = 'shift'
        next_state = 82
    elif c in col23:
        state_type = 'shift'
        next_state = 83
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col42:
        state_type = 'shift'
        next_state = 85
    elif c in col51:
        state_type = 'goto'
        next_state = 126
    elif c in col56:
        state_type = 'goto'
        next_state = 81
    elif c in col57:
        state_type = 'goto'
        next_state = 79
    elif c in col60:
        state_type = 'goto'
        next_state = 80
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state101(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 61
    elif c in col9:
        state_type = 'reduce'
        next_state = 61
    elif c in col12:
        state_type = 'reduce'
        next_state = 61
    elif c in col15:
        state_type = 'reduce'
        next_state = 61
    elif c in col16:
        state_type = 'reduce'
        next_state = 61
    elif c in col19:
        state_type = 'reduce'
        next_state = 61
    elif c in col23:
        state_type = 'reduce'
        next_state = 61
    elif c in col30:
        state_type = 'reduce'
        next_state = 61
    elif c in col42:
        state_type = 'reduce'
        next_state = 61
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state102(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 62
    elif c in col9:
        state_type = 'reduce'
        next_state = 62
    elif c in col12:
        state_type = 'reduce'
        next_state = 62
    elif c in col15:
        state_type = 'reduce'
        next_state = 62
    elif c in col16:
        state_type = 'reduce'
        next_state = 62
    elif c in col19:
        state_type = 'reduce'
        next_state = 62
    elif c in col23:
        state_type = 'reduce'
        next_state = 62
    elif c in col30:
        state_type = 'reduce'
        next_state = 62
    elif c in col42:
        state_type = 'reduce'
        next_state = 62
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state103(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 63
    elif c in col9:
        state_type = 'reduce'
        next_state = 63
    elif c in col12:
        state_type = 'reduce'
        next_state = 63
    elif c in col15:
        state_type = 'reduce'
        next_state = 63
    elif c in col16:
        state_type = 'reduce'
        next_state = 63
    elif c in col19:
        state_type = 'reduce'
        next_state = 63
    elif c in col23:
        state_type = 'reduce'
        next_state = 63
    elif c in col30:
        state_type = 'reduce'
        next_state = 63
    elif c in col42:
        state_type = 'reduce'
        next_state = 63
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state104(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 64
    elif c in col9:
        state_type = 'reduce'
        next_state = 64
    elif c in col12:
        state_type = 'reduce'
        next_state = 64
    elif c in col15:
        state_type = 'reduce'
        next_state = 64
    elif c in col16:
        state_type = 'reduce'
        next_state = 64
    elif c in col19:
        state_type = 'reduce'
        next_state = 64
    elif c in col23:
        state_type = 'reduce'
        next_state = 64
    elif c in col30:
        state_type = 'reduce'
        next_state = 64
    elif c in col42:
        state_type = 'reduce'
        next_state = 64
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state105(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 65
    elif c in col9:
        state_type = 'reduce'
        next_state = 65
    elif c in col12:
        state_type = 'reduce'
        next_state = 65
    elif c in col15:
        state_type = 'reduce'
        next_state = 65
    elif c in col16:
        state_type = 'reduce'
        next_state = 65
    elif c in col19:
        state_type = 'reduce'
        next_state = 65
    elif c in col23:
        state_type = 'reduce'
        next_state = 65
    elif c in col30:
        state_type = 'reduce'
        next_state = 65
    elif c in col42:
        state_type = 'reduce'
        next_state = 65
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state106(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 66
    elif c in col9:
        state_type = 'reduce'
        next_state = 66
    elif c in col12:
        state_type = 'reduce'
        next_state = 66
    elif c in col15:
        state_type = 'reduce'
        next_state = 66
    elif c in col16:
        state_type = 'reduce'
        next_state = 66
    elif c in col19:
        state_type = 'reduce'
        next_state = 66
    elif c in col23:
        state_type = 'reduce'
        next_state = 66
    elif c in col30:
        state_type = 'reduce'
        next_state = 66
    elif c in col42:
        state_type = 'reduce'
        next_state = 66
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state107(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 67
    elif c in col9:
        state_type = 'reduce'
        next_state = 67
    elif c in col12:
        state_type = 'reduce'
        next_state = 67
    elif c in col15:
        state_type = 'reduce'
        next_state = 67
    elif c in col16:
        state_type = 'reduce'
        next_state = 67
    elif c in col19:
        state_type = 'reduce'
        next_state = 67
    elif c in col23:
        state_type = 'reduce'
        next_state = 67
    elif c in col30:
        state_type = 'reduce'
        next_state = 67
    elif c in col42:
        state_type = 'reduce'
        next_state = 67
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state108(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 68
    elif c in col9:
        state_type = 'reduce'
        next_state = 68
    elif c in col12:
        state_type = 'reduce'
        next_state = 68
    elif c in col15:
        state_type = 'reduce'
        next_state = 68
    elif c in col16:
        state_type = 'reduce'
        next_state = 68
    elif c in col19:
        state_type = 'reduce'
        next_state = 68
    elif c in col23:
        state_type = 'reduce'
        next_state = 68
    elif c in col30:
        state_type = 'reduce'
        next_state = 68
    elif c in col42:
        state_type = 'reduce'
        next_state = 68
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state109(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 69
    elif c in col9:
        state_type = 'reduce'
        next_state = 69
    elif c in col12:
        state_type = 'reduce'
        next_state = 69
    elif c in col15:
        state_type = 'reduce'
        next_state = 69
    elif c in col16:
        state_type = 'reduce'
        next_state = 69
    elif c in col19:
        state_type = 'reduce'
        next_state = 69
    elif c in col23:
        state_type = 'reduce'
        next_state = 69
    elif c in col30:
        state_type = 'reduce'
        next_state = 69
    elif c in col42:
        state_type = 'reduce'
        next_state = 69
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state110(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 70
    elif c in col9:
        state_type = 'reduce'
        next_state = 70
    elif c in col12:
        state_type = 'reduce'
        next_state = 70
    elif c in col15:
        state_type = 'reduce'
        next_state = 70
    elif c in col16:
        state_type = 'reduce'
        next_state = 70
    elif c in col19:
        state_type = 'reduce'
        next_state = 70
    elif c in col23:
        state_type = 'reduce'
        next_state = 70
    elif c in col30:
        state_type = 'reduce'
        next_state = 70
    elif c in col42:
        state_type = 'reduce'
        next_state = 70
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state111(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 71
    elif c in col9:
        state_type = 'reduce'
        next_state = 71
    elif c in col12:
        state_type = 'reduce'
        next_state = 71
    elif c in col15:
        state_type = 'reduce'
        next_state = 71
    elif c in col16:
        state_type = 'reduce'
        next_state = 71
    elif c in col19:
        state_type = 'reduce'
        next_state = 71
    elif c in col23:
        state_type = 'reduce'
        next_state = 71
    elif c in col30:
        state_type = 'reduce'
        next_state = 71
    elif c in col42:
        state_type = 'reduce'
        next_state = 71
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state112(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 72
    elif c in col9:
        state_type = 'reduce'
        next_state = 72
    elif c in col12:
        state_type = 'reduce'
        next_state = 72
    elif c in col15:
        state_type = 'reduce'
        next_state = 72
    elif c in col16:
        state_type = 'reduce'
        next_state = 72
    elif c in col19:
        state_type = 'reduce'
        next_state = 72
    elif c in col23:
        state_type = 'reduce'
        next_state = 72
    elif c in col30:
        state_type = 'reduce'
        next_state = 72
    elif c in col42:
        state_type = 'reduce'
        next_state = 72
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state113(c):
    if c in col4:
        state_type = 'reduce'
        next_state = 73
    elif c in col9:
        state_type = 'reduce'
        next_state = 73
    elif c in col12:
        state_type = 'reduce'
        next_state = 73
    elif c in col15:
        state_type = 'reduce'
        next_state = 73
    elif c in col16:
        state_type = 'reduce'
        next_state = 73
    elif c in col19:
        state_type = 'reduce'
        next_state = 73
    elif c in col23:
        state_type = 'reduce'
        next_state = 73
    elif c in col30:
        state_type = 'reduce'
        next_state = 73
    elif c in col42:
        state_type = 'reduce'
        next_state = 73
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state114(c):
    if c in col2:
        state_type = 'shift'
        next_state = 112
    elif c in col4:
        state_type = 'reduce'
        next_state = 47
    elif c in col5:
        state_type = 'reduce'
        next_state = 47
    elif c in col7:
        state_type = 'reduce'
        next_state = 47
    elif c in col8:
        state_type = 'reduce'
        next_state = 47
    elif c in col10:
        state_type = 'shift'
        next_state = 102
    elif c in col11:
        state_type = 'shift'
        next_state = 110
    elif c in col13:
        state_type = 'shift'
        next_state = 108
    elif c in col14:
        state_type = 'shift'
        next_state = 106
    elif c in col17:
        state_type = 'shift'
        next_state = 109
    elif c in col18:
        state_type = 'shift'
        next_state = 107
    elif c in col19:
        state_type = 'shift'
        next_state = 104
    elif c in col21:
        state_type = 'shift'
        next_state = 101
    elif c in col22:
        state_type = 'shift'
        next_state = 103
    elif c in col24:
        state_type = 'shift'
        next_state = 111
    elif c in col25:
        state_type = 'shift'
        next_state = 113
    elif c in col27:
        state_type = 'reduce'
        next_state = 47
    elif c in col39:
        state_type = 'reduce'
        next_state = 47
    elif c in col41:
        state_type = 'shift'
        next_state = 105
    elif c in col46:
        state_type = 'goto'
        next_state = 100
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state115(c):
    if c in col2:
        state_type = 'shift'
        next_state = 112
    elif c in col4:
        state_type = 'reduce'
        next_state = 48
    elif c in col5:
        state_type = 'reduce'
        next_state = 48
    elif c in col7:
        state_type = 'reduce'
        next_state = 48
    elif c in col8:
        state_type = 'reduce'
        next_state = 48
    elif c in col10:
        state_type = 'shift'
        next_state = 102
    elif c in col11:
        state_type = 'shift'
        next_state = 110
    elif c in col13:
        state_type = 'shift'
        next_state = 108
    elif c in col14:
        state_type = 'shift'
        next_state = 106
    elif c in col17:
        state_type = 'shift'
        next_state = 109
    elif c in col18:
        state_type = 'shift'
        next_state = 107
    elif c in col19:
        state_type = 'shift'
        next_state = 104
    elif c in col21:
        state_type = 'shift'
        next_state = 101
    elif c in col22:
        state_type = 'shift'
        next_state = 103
    elif c in col24:
        state_type = 'shift'
        next_state = 111
    elif c in col25:
        state_type = 'shift'
        next_state = 113
    elif c in col27:
        state_type = 'reduce'
        next_state = 48
    elif c in col39:
        state_type = 'reduce'
        next_state = 48
    elif c in col41:
        state_type = 'shift'
        next_state = 105
    elif c in col46:
        state_type = 'goto'
        next_state = 100
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state116(c):
    if c in col2:
        state_type = 'shift'
        next_state = 112
    elif c in col5:
        state_type = 'shift'
        next_state = 127
    elif c in col10:
        state_type = 'shift'
        next_state = 102
    elif c in col11:
        state_type = 'shift'
        next_state = 110
    elif c in col13:
        state_type = 'shift'
        next_state = 108
    elif c in col14:
        state_type = 'shift'
        next_state = 106
    elif c in col17:
        state_type = 'shift'
        next_state = 109
    elif c in col18:
        state_type = 'shift'
        next_state = 107
    elif c in col19:
        state_type = 'shift'
        next_state = 104
    elif c in col21:
        state_type = 'shift'
        next_state = 101
    elif c in col22:
        state_type = 'shift'
        next_state = 103
    elif c in col24:
        state_type = 'shift'
        next_state = 111
    elif c in col25:
        state_type = 'shift'
        next_state = 113
    elif c in col41:
        state_type = 'shift'
        next_state = 105
    elif c in col46:
        state_type = 'goto'
        next_state = 100
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state117(c):
    if c in col2:
        state_type = 'shift'
        next_state = 112
    elif c in col7:
        state_type = 'shift'
        next_state = 128
    elif c in col10:
        state_type = 'shift'
        next_state = 102
    elif c in col11:
        state_type = 'shift'
        next_state = 110
    elif c in col13:
        state_type = 'shift'
        next_state = 108
    elif c in col14:
        state_type = 'shift'
        next_state = 106
    elif c in col17:
        state_type = 'shift'
        next_state = 109
    elif c in col18:
        state_type = 'shift'
        next_state = 107
    elif c in col19:
        state_type = 'shift'
        next_state = 104
    elif c in col21:
        state_type = 'shift'
        next_state = 101
    elif c in col22:
        state_type = 'shift'
        next_state = 103
    elif c in col24:
        state_type = 'shift'
        next_state = 111
    elif c in col25:
        state_type = 'shift'
        next_state = 113
    elif c in col41:
        state_type = 'shift'
        next_state = 105
    elif c in col46:
        state_type = 'goto'
        next_state = 100
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state118(c):
    if c in col8:
        state_type = 'shift'
        next_state = 130
    elif c in col27:
        state_type = 'shift'
        next_state = 129
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state119(c):
    if c in col2:
        state_type = 'reduce'
        next_state = 51
    elif c in col4:
        state_type = 'reduce'
        next_state = 51
    elif c in col5:
        state_type = 'reduce'
        next_state = 51
    elif c in col7:
        state_type = 'reduce'
        next_state = 51
    elif c in col8:
        state_type = 'reduce'
        next_state = 51
    elif c in col10:
        state_type = 'reduce'
        next_state = 51
    elif c in col11:
        state_type = 'reduce'
        next_state = 51
    elif c in col13:
        state_type = 'reduce'
        next_state = 51
    elif c in col14:
        state_type = 'reduce'
        next_state = 51
    elif c in col17:
        state_type = 'reduce'
        next_state = 51
    elif c in col18:
        state_type = 'reduce'
        next_state = 51
    elif c in col19:
        state_type = 'reduce'
        next_state = 51
    elif c in col21:
        state_type = 'reduce'
        next_state = 51
    elif c in col22:
        state_type = 'reduce'
        next_state = 51
    elif c in col24:
        state_type = 'reduce'
        next_state = 51
    elif c in col25:
        state_type = 'reduce'
        next_state = 51
    elif c in col27:
        state_type = 'reduce'
        next_state = 51
    elif c in col39:
        state_type = 'reduce'
        next_state = 51
    elif c in col41:
        state_type = 'reduce'
        next_state = 51
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state120(c):
    if c in col2:
        state_type = 'shift'
        next_state = 112
    elif c in col8:
        state_type = 'reduce'
        next_state = 56
    elif c in col10:
        state_type = 'shift'
        next_state = 102
    elif c in col11:
        state_type = 'shift'
        next_state = 110
    elif c in col13:
        state_type = 'shift'
        next_state = 108
    elif c in col14:
        state_type = 'shift'
        next_state = 106
    elif c in col17:
        state_type = 'shift'
        next_state = 109
    elif c in col18:
        state_type = 'shift'
        next_state = 107
    elif c in col19:
        state_type = 'shift'
        next_state = 104
    elif c in col21:
        state_type = 'shift'
        next_state = 101
    elif c in col22:
        state_type = 'shift'
        next_state = 103
    elif c in col24:
        state_type = 'shift'
        next_state = 111
    elif c in col25:
        state_type = 'shift'
        next_state = 113
    elif c in col27:
        state_type = 'reduce'
        next_state = 56
    elif c in col41:
        state_type = 'shift'
        next_state = 105
    elif c in col46:
        state_type = 'goto'
        next_state = 100
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state121(c):
    if c in col2:
        state_type = 'reduce'
        next_state = 52
    elif c in col4:
        state_type = 'reduce'
        next_state = 52
    elif c in col5:
        state_type = 'reduce'
        next_state = 52
    elif c in col7:
        state_type = 'reduce'
        next_state = 52
    elif c in col8:
        state_type = 'reduce'
        next_state = 52
    elif c in col10:
        state_type = 'reduce'
        next_state = 52
    elif c in col11:
        state_type = 'reduce'
        next_state = 52
    elif c in col13:
        state_type = 'reduce'
        next_state = 52
    elif c in col14:
        state_type = 'reduce'
        next_state = 52
    elif c in col17:
        state_type = 'reduce'
        next_state = 52
    elif c in col18:
        state_type = 'reduce'
        next_state = 52
    elif c in col19:
        state_type = 'reduce'
        next_state = 52
    elif c in col21:
        state_type = 'reduce'
        next_state = 52
    elif c in col22:
        state_type = 'reduce'
        next_state = 52
    elif c in col24:
        state_type = 'reduce'
        next_state = 52
    elif c in col25:
        state_type = 'reduce'
        next_state = 52
    elif c in col27:
        state_type = 'reduce'
        next_state = 52
    elif c in col39:
        state_type = 'reduce'
        next_state = 52
    elif c in col41:
        state_type = 'reduce'
        next_state = 52
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state122(c):
    if c in col8:
        state_type = 'shift'
        next_state = 132
    elif c in col27:
        state_type = 'shift'
        next_state = 131
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state123(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 29
    elif c in col16:
        state_type = 'reduce'
        next_state = 29
    elif c in col29:
        state_type = 'reduce'
        next_state = 29
    elif c in col30:
        state_type = 'reduce'
        next_state = 29
    elif c in col32:
        state_type = 'reduce'
        next_state = 29
    elif c in col34:
        state_type = 'reduce'
        next_state = 29
    elif c in col35:
        state_type = 'reduce'
        next_state = 29
    elif c in col37:
        state_type = 'reduce'
        next_state = 29
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state124(c):
    if c in col4:
        state_type = 'shift'
        next_state = 41
    elif c in col47:
        state_type = 'goto'
        next_state = 133
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state125(c):
    if c in col2:
        state_type = 'shift'
        next_state = 112
    elif c in col8:
        state_type = 'shift'
        next_state = 134
    elif c in col10:
        state_type = 'shift'
        next_state = 102
    elif c in col11:
        state_type = 'shift'
        next_state = 110
    elif c in col13:
        state_type = 'shift'
        next_state = 108
    elif c in col14:
        state_type = 'shift'
        next_state = 106
    elif c in col17:
        state_type = 'shift'
        next_state = 109
    elif c in col18:
        state_type = 'shift'
        next_state = 107
    elif c in col19:
        state_type = 'shift'
        next_state = 104
    elif c in col21:
        state_type = 'shift'
        next_state = 101
    elif c in col22:
        state_type = 'shift'
        next_state = 103
    elif c in col24:
        state_type = 'shift'
        next_state = 111
    elif c in col25:
        state_type = 'shift'
        next_state = 113
    elif c in col41:
        state_type = 'shift'
        next_state = 105
    elif c in col46:
        state_type = 'goto'
        next_state = 100
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state126(c):
    if c in col2:
        state_type = 'shift'
        next_state = 112
    elif c in col4:
        state_type = 'reduce'
        next_state = 46
    elif c in col5:
        state_type = 'reduce'
        next_state = 46
    elif c in col7:
        state_type = 'reduce'
        next_state = 46
    elif c in col8:
        state_type = 'reduce'
        next_state = 46
    elif c in col10:
        state_type = 'shift'
        next_state = 102
    elif c in col11:
        state_type = 'shift'
        next_state = 110
    elif c in col13:
        state_type = 'shift'
        next_state = 108
    elif c in col14:
        state_type = 'shift'
        next_state = 106
    elif c in col17:
        state_type = 'shift'
        next_state = 109
    elif c in col18:
        state_type = 'shift'
        next_state = 107
    elif c in col19:
        state_type = 'shift'
        next_state = 104
    elif c in col21:
        state_type = 'shift'
        next_state = 101
    elif c in col22:
        state_type = 'shift'
        next_state = 103
    elif c in col24:
        state_type = 'shift'
        next_state = 111
    elif c in col25:
        state_type = 'shift'
        next_state = 113
    elif c in col27:
        state_type = 'reduce'
        next_state = 46
    elif c in col39:
        state_type = 'reduce'
        next_state = 46
    elif c in col41:
        state_type = 'shift'
        next_state = 105
    elif c in col46:
        state_type = 'goto'
        next_state = 100
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state127(c):
    if c in col2:
        state_type = 'reduce'
        next_state = 49
    elif c in col4:
        state_type = 'reduce'
        next_state = 49
    elif c in col5:
        state_type = 'reduce'
        next_state = 49
    elif c in col7:
        state_type = 'reduce'
        next_state = 49
    elif c in col8:
        state_type = 'reduce'
        next_state = 49
    elif c in col10:
        state_type = 'reduce'
        next_state = 49
    elif c in col11:
        state_type = 'reduce'
        next_state = 49
    elif c in col13:
        state_type = 'reduce'
        next_state = 49
    elif c in col14:
        state_type = 'reduce'
        next_state = 49
    elif c in col17:
        state_type = 'reduce'
        next_state = 49
    elif c in col18:
        state_type = 'reduce'
        next_state = 49
    elif c in col19:
        state_type = 'reduce'
        next_state = 49
    elif c in col21:
        state_type = 'reduce'
        next_state = 49
    elif c in col22:
        state_type = 'reduce'
        next_state = 49
    elif c in col24:
        state_type = 'reduce'
        next_state = 49
    elif c in col25:
        state_type = 'reduce'
        next_state = 49
    elif c in col27:
        state_type = 'reduce'
        next_state = 49
    elif c in col39:
        state_type = 'reduce'
        next_state = 49
    elif c in col41:
        state_type = 'reduce'
        next_state = 49
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state128(c):
    if c in col2:
        state_type = 'reduce'
        next_state = 39
    elif c in col3:
        state_type = 'reduce'
        next_state = 39
    elif c in col4:
        state_type = 'reduce'
        next_state = 39
    elif c in col5:
        state_type = 'reduce'
        next_state = 39
    elif c in col7:
        state_type = 'reduce'
        next_state = 39
    elif c in col8:
        state_type = 'reduce'
        next_state = 39
    elif c in col10:
        state_type = 'reduce'
        next_state = 39
    elif c in col11:
        state_type = 'reduce'
        next_state = 39
    elif c in col13:
        state_type = 'reduce'
        next_state = 39
    elif c in col14:
        state_type = 'reduce'
        next_state = 39
    elif c in col17:
        state_type = 'reduce'
        next_state = 39
    elif c in col18:
        state_type = 'reduce'
        next_state = 39
    elif c in col19:
        state_type = 'reduce'
        next_state = 39
    elif c in col20:
        state_type = 'reduce'
        next_state = 39
    elif c in col21:
        state_type = 'reduce'
        next_state = 39
    elif c in col22:
        state_type = 'reduce'
        next_state = 39
    elif c in col24:
        state_type = 'reduce'
        next_state = 39
    elif c in col25:
        state_type = 'reduce'
        next_state = 39
    elif c in col27:
        state_type = 'reduce'
        next_state = 39
    elif c in col28:
        state_type = 'reduce'
        next_state = 39
    elif c in col39:
        state_type = 'reduce'
        next_state = 39
    elif c in col41:
        state_type = 'reduce'
        next_state = 39
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state129(c):
    if c in col2:
        state_type = 'reduce'
        next_state = 50
    elif c in col4:
        state_type = 'reduce'
        next_state = 50
    elif c in col5:
        state_type = 'reduce'
        next_state = 50
    elif c in col7:
        state_type = 'reduce'
        next_state = 50
    elif c in col8:
        state_type = 'reduce'
        next_state = 50
    elif c in col10:
        state_type = 'reduce'
        next_state = 50
    elif c in col11:
        state_type = 'reduce'
        next_state = 50
    elif c in col13:
        state_type = 'reduce'
        next_state = 50
    elif c in col14:
        state_type = 'reduce'
        next_state = 50
    elif c in col17:
        state_type = 'reduce'
        next_state = 50
    elif c in col18:
        state_type = 'reduce'
        next_state = 50
    elif c in col19:
        state_type = 'reduce'
        next_state = 50
    elif c in col21:
        state_type = 'reduce'
        next_state = 50
    elif c in col22:
        state_type = 'reduce'
        next_state = 50
    elif c in col24:
        state_type = 'reduce'
        next_state = 50
    elif c in col25:
        state_type = 'reduce'
        next_state = 50
    elif c in col27:
        state_type = 'reduce'
        next_state = 50
    elif c in col39:
        state_type = 'reduce'
        next_state = 50
    elif c in col41:
        state_type = 'reduce'
        next_state = 50
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state130(c):
    if c in col4:
        state_type = 'shift'
        next_state = 84
    elif c in col9:
        state_type = 'shift'
        next_state = 87
    elif c in col12:
        state_type = 'shift'
        next_state = 86
    elif c in col15:
        state_type = 'shift'
        next_state = 88
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col19:
        state_type = 'shift'
        next_state = 82
    elif c in col23:
        state_type = 'shift'
        next_state = 83
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col42:
        state_type = 'shift'
        next_state = 85
    elif c in col51:
        state_type = 'goto'
        next_state = 135
    elif c in col56:
        state_type = 'goto'
        next_state = 81
    elif c in col57:
        state_type = 'goto'
        next_state = 79
    elif c in col60:
        state_type = 'goto'
        next_state = 80
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state131(c):
    if c in col2:
        state_type = 'reduce'
        next_state = 53
    elif c in col4:
        state_type = 'reduce'
        next_state = 53
    elif c in col5:
        state_type = 'reduce'
        next_state = 53
    elif c in col7:
        state_type = 'reduce'
        next_state = 53
    elif c in col8:
        state_type = 'reduce'
        next_state = 53
    elif c in col10:
        state_type = 'reduce'
        next_state = 53
    elif c in col11:
        state_type = 'reduce'
        next_state = 53
    elif c in col13:
        state_type = 'reduce'
        next_state = 53
    elif c in col14:
        state_type = 'reduce'
        next_state = 53
    elif c in col17:
        state_type = 'reduce'
        next_state = 53
    elif c in col18:
        state_type = 'reduce'
        next_state = 53
    elif c in col19:
        state_type = 'reduce'
        next_state = 53
    elif c in col21:
        state_type = 'reduce'
        next_state = 53
    elif c in col22:
        state_type = 'reduce'
        next_state = 53
    elif c in col24:
        state_type = 'reduce'
        next_state = 53
    elif c in col25:
        state_type = 'reduce'
        next_state = 53
    elif c in col27:
        state_type = 'reduce'
        next_state = 53
    elif c in col39:
        state_type = 'reduce'
        next_state = 53
    elif c in col41:
        state_type = 'reduce'
        next_state = 53
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state132(c):
    if c in col4:
        state_type = 'shift'
        next_state = 84
    elif c in col9:
        state_type = 'shift'
        next_state = 87
    elif c in col12:
        state_type = 'shift'
        next_state = 86
    elif c in col15:
        state_type = 'shift'
        next_state = 88
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col19:
        state_type = 'shift'
        next_state = 82
    elif c in col23:
        state_type = 'shift'
        next_state = 83
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col40:
        state_type = 'shift'
        next_state = 138
    elif c in col42:
        state_type = 'shift'
        next_state = 85
    elif c in col48:
        state_type = 'goto'
        next_state = 137
    elif c in col49:
        state_type = 'goto'
        next_state = 136
    elif c in col51:
        state_type = 'goto'
        next_state = 139
    elif c in col56:
        state_type = 'goto'
        next_state = 81
    elif c in col57:
        state_type = 'goto'
        next_state = 79
    elif c in col60:
        state_type = 'goto'
        next_state = 80
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state133(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 31
    elif c in col16:
        state_type = 'reduce'
        next_state = 31
    elif c in col29:
        state_type = 'reduce'
        next_state = 31
    elif c in col30:
        state_type = 'reduce'
        next_state = 31
    elif c in col32:
        state_type = 'reduce'
        next_state = 31
    elif c in col33:
        state_type = 'shift'
        next_state = 140
    elif c in col34:
        state_type = 'reduce'
        next_state = 31
    elif c in col35:
        state_type = 'reduce'
        next_state = 31
    elif c in col37:
        state_type = 'reduce'
        next_state = 31
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state134(c):
    if c in col4:
        state_type = 'shift'
        next_state = 84
    elif c in col9:
        state_type = 'shift'
        next_state = 87
    elif c in col12:
        state_type = 'shift'
        next_state = 86
    elif c in col15:
        state_type = 'shift'
        next_state = 88
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col19:
        state_type = 'shift'
        next_state = 82
    elif c in col23:
        state_type = 'shift'
        next_state = 83
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col42:
        state_type = 'shift'
        next_state = 85
    elif c in col51:
        state_type = 'goto'
        next_state = 141
    elif c in col56:
        state_type = 'goto'
        next_state = 81
    elif c in col57:
        state_type = 'goto'
        next_state = 79
    elif c in col60:
        state_type = 'goto'
        next_state = 80
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state135(c):
    if c in col2:
        state_type = 'shift'
        next_state = 112
    elif c in col8:
        state_type = 'reduce'
        next_state = 55
    elif c in col10:
        state_type = 'shift'
        next_state = 102
    elif c in col11:
        state_type = 'shift'
        next_state = 110
    elif c in col13:
        state_type = 'shift'
        next_state = 108
    elif c in col14:
        state_type = 'shift'
        next_state = 106
    elif c in col17:
        state_type = 'shift'
        next_state = 109
    elif c in col18:
        state_type = 'shift'
        next_state = 107
    elif c in col19:
        state_type = 'shift'
        next_state = 104
    elif c in col21:
        state_type = 'shift'
        next_state = 101
    elif c in col22:
        state_type = 'shift'
        next_state = 103
    elif c in col24:
        state_type = 'shift'
        next_state = 111
    elif c in col25:
        state_type = 'shift'
        next_state = 113
    elif c in col27:
        state_type = 'reduce'
        next_state = 55
    elif c in col41:
        state_type = 'shift'
        next_state = 105
    elif c in col46:
        state_type = 'goto'
        next_state = 100
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state136(c):
    if c in col8:
        state_type = 'shift'
        next_state = 143
    elif c in col27:
        state_type = 'shift'
        next_state = 142
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state137(c):
    if c in col8:
        state_type = 'reduce'
        next_state = 75
    elif c in col27:
        state_type = 'reduce'
        next_state = 75
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state138(c):
    if c in col8:
        state_type = 'reduce'
        next_state = 76
    elif c in col27:
        state_type = 'reduce'
        next_state = 76
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state139(c):
    if c in col2:
        state_type = 'shift'
        next_state = 112
    elif c in col8:
        state_type = 'reduce'
        next_state = 77
    elif c in col10:
        state_type = 'shift'
        next_state = 102
    elif c in col11:
        state_type = 'shift'
        next_state = 110
    elif c in col13:
        state_type = 'shift'
        next_state = 108
    elif c in col14:
        state_type = 'shift'
        next_state = 106
    elif c in col17:
        state_type = 'shift'
        next_state = 109
    elif c in col18:
        state_type = 'shift'
        next_state = 107
    elif c in col19:
        state_type = 'shift'
        next_state = 104
    elif c in col21:
        state_type = 'shift'
        next_state = 101
    elif c in col22:
        state_type = 'shift'
        next_state = 103
    elif c in col24:
        state_type = 'shift'
        next_state = 111
    elif c in col25:
        state_type = 'shift'
        next_state = 113
    elif c in col27:
        state_type = 'reduce'
        next_state = 77
    elif c in col41:
        state_type = 'shift'
        next_state = 105
    elif c in col46:
        state_type = 'goto'
        next_state = 100
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state140(c):
    if c in col4:
        state_type = 'shift'
        next_state = 41
    elif c in col47:
        state_type = 'goto'
        next_state = 144
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state141(c):
    if c in col2:
        state_type = 'shift'
        next_state = 112
    elif c in col4:
        state_type = 'shift'
        next_state = 41
    elif c in col10:
        state_type = 'shift'
        next_state = 102
    elif c in col11:
        state_type = 'shift'
        next_state = 110
    elif c in col13:
        state_type = 'shift'
        next_state = 108
    elif c in col14:
        state_type = 'shift'
        next_state = 106
    elif c in col17:
        state_type = 'shift'
        next_state = 109
    elif c in col18:
        state_type = 'shift'
        next_state = 107
    elif c in col19:
        state_type = 'shift'
        next_state = 104
    elif c in col21:
        state_type = 'shift'
        next_state = 101
    elif c in col22:
        state_type = 'shift'
        next_state = 103
    elif c in col24:
        state_type = 'shift'
        next_state = 111
    elif c in col25:
        state_type = 'shift'
        next_state = 113
    elif c in col41:
        state_type = 'shift'
        next_state = 105
    elif c in col46:
        state_type = 'goto'
        next_state = 100
    elif c in col47:
        state_type = 'goto'
        next_state = 145
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state142(c):
    if c in col2:
        state_type = 'reduce'
        next_state = 54
    elif c in col4:
        state_type = 'reduce'
        next_state = 54
    elif c in col5:
        state_type = 'reduce'
        next_state = 54
    elif c in col7:
        state_type = 'reduce'
        next_state = 54
    elif c in col8:
        state_type = 'reduce'
        next_state = 54
    elif c in col10:
        state_type = 'reduce'
        next_state = 54
    elif c in col11:
        state_type = 'reduce'
        next_state = 54
    elif c in col13:
        state_type = 'reduce'
        next_state = 54
    elif c in col14:
        state_type = 'reduce'
        next_state = 54
    elif c in col17:
        state_type = 'reduce'
        next_state = 54
    elif c in col18:
        state_type = 'reduce'
        next_state = 54
    elif c in col19:
        state_type = 'reduce'
        next_state = 54
    elif c in col21:
        state_type = 'reduce'
        next_state = 54
    elif c in col22:
        state_type = 'reduce'
        next_state = 54
    elif c in col24:
        state_type = 'reduce'
        next_state = 54
    elif c in col25:
        state_type = 'reduce'
        next_state = 54
    elif c in col27:
        state_type = 'reduce'
        next_state = 54
    elif c in col39:
        state_type = 'reduce'
        next_state = 54
    elif c in col41:
        state_type = 'reduce'
        next_state = 54
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state143(c):
    if c in col4:
        state_type = 'shift'
        next_state = 84
    elif c in col9:
        state_type = 'shift'
        next_state = 87
    elif c in col12:
        state_type = 'shift'
        next_state = 86
    elif c in col15:
        state_type = 'shift'
        next_state = 88
    elif c in col16:
        state_type = 'shift'
        next_state = 61
    elif c in col19:
        state_type = 'shift'
        next_state = 82
    elif c in col23:
        state_type = 'shift'
        next_state = 83
    elif c in col30:
        state_type = 'shift'
        next_state = 62
    elif c in col40:
        state_type = 'shift'
        next_state = 138
    elif c in col42:
        state_type = 'shift'
        next_state = 85
    elif c in col48:
        state_type = 'goto'
        next_state = 146
    elif c in col51:
        state_type = 'goto'
        next_state = 139
    elif c in col56:
        state_type = 'goto'
        next_state = 81
    elif c in col57:
        state_type = 'goto'
        next_state = 79
    elif c in col60:
        state_type = 'goto'
        next_state = 80
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state144(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 32
    elif c in col16:
        state_type = 'reduce'
        next_state = 32
    elif c in col29:
        state_type = 'reduce'
        next_state = 32
    elif c in col30:
        state_type = 'reduce'
        next_state = 32
    elif c in col32:
        state_type = 'reduce'
        next_state = 32
    elif c in col34:
        state_type = 'reduce'
        next_state = 32
    elif c in col35:
        state_type = 'reduce'
        next_state = 32
    elif c in col37:
        state_type = 'reduce'
        next_state = 32
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state145(c):
    if c in col5:
        state_type = 'reduce'
        next_state = 33
    elif c in col16:
        state_type = 'reduce'
        next_state = 33
    elif c in col29:
        state_type = 'reduce'
        next_state = 33
    elif c in col30:
        state_type = 'reduce'
        next_state = 33
    elif c in col32:
        state_type = 'reduce'
        next_state = 33
    elif c in col34:
        state_type = 'reduce'
        next_state = 33
    elif c in col35:
        state_type = 'reduce'
        next_state = 33
    elif c in col37:
        state_type = 'reduce'
        next_state = 33
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state


def state146(c):
    if c in col8:
        state_type = 'reduce'
        next_state = 74
    elif c in col27:
        state_type = 'reduce'
        next_state = 74
    else:
        state_type = 'error'
        next_state = 0
    return state_type, next_state
