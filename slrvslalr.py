from ply.lex import lex
from ply.yacc import yacc


tokens = ('ID', 'TIMES', 'EQUALS')

t_EQUALS = r'='
t_TIMES = r'\*'
t_ID = r'id'
t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex()


def p_stmt_L_EQ_R(p):
    """
    S : L EQUALS R
    """


def p_stmt_R(p):
    """
    S : R
    """


def p_L_TIMES_R(p):
    """
    L : TIMES R
    """


def p_L_ID(p):
    """
    L : ID
    """


def p_R_L(p):
    """
    R : L
    """


def p_error(p):
    print(p)


parser_slr = yacc(method='SLR', debugfile='parser_slr.out', tabmodule='parsetab_slr')
parser_lalr = yacc(method='LALR', debugfile='parser_lalr.out', tabmodule='parsetab_lalr')
