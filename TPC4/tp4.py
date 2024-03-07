import re
import ply.lex as lex

string = ("SeleCt (id,nome,salario) fROm empregados where \n"
          "salario>=820.5")


tokens = (
        "PR",  # select from where
        "NAME",  # nome id
        "OP",  # <= < > =>
        "PV",  # ;
        "ALL",  # *
        "COMMA",  # ,
        "INT",  # 820
        "FLOAT",  # 820.1
        "NL",  # \n
        'LPAREN',
        'RPAREN'
    )

t_PR = r"((?i)Select|(?i)from|(?i)where)"
t_NAME = r"(\w+)"
t_OP = r"<=|<|>|>=|="
t_PV = r";"
t_ALL = r"\*"
t_COMMA = r","
t_LPAREN = r'\('
t_RPAREN = r'\)'

# o float precisa de ser primeiro devido a
def t_FLOAT(t):
    r"""(\+|\-)?(\d+\.\d+)"""
    t.value = float(t.value)
    return t



def t_INT(t):
    r"""(\+|\-)?\d+"""
    t.value = int(t.value)
    return t


def t_nl(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

t_ignore = '\t '

lexer = lex.lex()

lexer.input(string)

for tok in lexer:
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
