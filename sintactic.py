"""This module represents the behavior of a syntactic analyzer for EduLangVis.

Grammar:

<SCRIPT>        -> ARRAY <ARRAY_LITERAL> ALGORITHM <ALGORITHM_NAME> VISUALIZE
<ARRAY_LITERAL> -> LBRACKET <NUMBER_LIST> RBRACKET
<NUMBER_LIST>   -> NUMBER ( COMMA NUMBER )*
"""

from lexical import Token  # tu clase Token

class ParserError(Exception):
    pass

class SyntacticAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current = self.tokens[0] if self.tokens else Token('EOF', None)
        self.array = []
        self.algorithm = None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current = self.tokens[self.pos]
        else:
            self.current = Token('EOF', None)

    def eat(self, type_, value=None):
        if self.current.type_ != type_ or (value is not None and self.current.value != value):
            esperado = f"{type_}{' '+value if value else ''}"
            raise ParserError(f"Se esperaba {esperado!r}, pero vino {self.current}")
        tok = self.current
        self.advance()
        return tok

    def parse(self):
        self.script()
        if self.current.type_ != 'EOF':
            raise ParserError(f"Tokens extra después de VISUALIZE: {self.current}")
        return {'array': self.array, 'algorithm': self.algorithm}

    def script(self):
        # ARRAY
        self.eat('KEYWORD', 'ARRAY')
        # [ ... ]
        self.array = self.array_literal()
        # ALGORITHM
        self.eat('KEYWORD', 'ALGORITHM')
        # Aquí cambiamos: en vez de eat('ID'), comemos ALGORITHM_NAME
        alg_tok = self.eat('ALGORITHM_NAME')
        self.algorithm = alg_tok.value
        # VISUALIZE
        self.eat('KEYWORD', 'VISUALIZE')

    def array_literal(self):
        self.eat('LBRACKET')
        nums = self.number_list()
        self.eat('RBRACKET')
        return nums

    def number_list(self):
        nums = []
        num_tok = self.eat('NUMBER')
        nums.append(int(num_tok.value))
        while self.current.type_ == 'COMMA':
            self.eat('COMMA')
            num_tok = self.eat('NUMBER')
            nums.append(int(num_tok.value))
        return nums


if __name__ == "__main__":
    from lexical import LexicalAnalyzer

    code = """
    ARRAY [6, 2, 9, 3]
    ALGORITHM bubble_sort
    VISUALIZE
    """
    toks = LexicalAnalyzer.lex(code)
    print("Tokens:", toks)

    parser = SyntacticAnalyzer(toks)
    result = parser.parse()
    print("Parsed result:", result)