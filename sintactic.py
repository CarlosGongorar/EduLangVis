"""This module represents the behavior of a syntactic analyzer for EduLangVis.

Grammar:

<SCRIPT>        -> ARRAY <ARRAY_LITERAL> ALGORITHM <ALGORITHM_NAME> VISUALIZE
<ARRAY_LITERAL> -> LBRACKET <NUMBER_LIST> RBRACKET
<NUMBER_LIST>   -> NUMBER ( COMMA NUMBER )*
"""

from lexical import Token

class ParserError(Exception):
    pass

class SyntacticAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens # Tokens list from LexicalAnalyzer
        self.pos = 0 # Array index
        self.current = self.tokens[0] if self.tokens else Token('EOF', None) # Current token that will be processed, if the array is empty we put a Token type EOF to indicate, end of data 
        # Fields for parsing result
        self.array = []
        self.algorithm = None

    # Increment self.pos.
    # If there are still tokens, update self.current to the next one.
    # If there are none left, assign Token('EOF', None), which acts as a sentinel to detect when we reach the end and prevent index errors.
    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current = self.tokens[self.pos]
        else:
            self.current = Token('EOF', None)

    # eat(type_, value) verifies that the current token matches the type (type_) and, optionally, an exact value (value, for example, "ARRAY").
    # If it doesn't match, it throws a ParserError, indicating where the syntax was not as expected.
    # If it matches, it saves the token, advances, and returns it.
    def eat(self, type_, value=None):
        if self.current.type_ != type_ or (value is not None and self.current.value != value):
            esperado = f"{type_}{' '+value if value else ''}"
            raise ParserError(f"Waiting for {esperado!r}, but {self.current} came")
        tok = self.current
        self.advance()
        return tok

    # It calls self.script(), which applies the main rule of the grammar.
    # It then checks that after processing VISUALIZE, there are no more tokens EOF left, always should EOF
    # It returns the parsed result (the array and the algorithm name).
    def parse(self):
        self.script()
        if self.current.type_ != 'EOF':
            raise ParserError(f"Tokens after VISUALIZE: {self.current}")
        return {'array': self.array, 'algorithm': self.algorithm}


    # Waits for the ARRAY keyword.
    # Reads the array literal (delegating to array_literal()).
    # Waits for ALGORITHM.
    # Reads the algorithm name (ALGORITHM_NAME).
    # Waits for VISUALIZE.
    def script(self):
        # ARRAY
        self.eat('KEYWORD', 'ARRAY')
        # [ ... ]
        self.array = self.array_literal()
        # ALGORITHM
        self.eat('KEYWORD', 'ALGORITHM')
        # ALGORITHM_NAME
        alg_tok = self.eat('ALGORITHM_NAME')
        self.algorithm = alg_tok.value
        # VISUALIZE
        self.eat('KEYWORD', 'VISUALIZE')

    # Consumes the left bracket ([).
    # Calls number_list() to read the sequence of numbers (and commas).
    # Consumes the right bracket (]).
    # Returns the list of integers.
    def array_literal(self):
        self.eat('LBRACKET')
        nums = self.number_list()
        self.eat('RBRACKET')
        return nums

    # It requires at least one NUMBER.
    # Then, as long as it sees commas, it consumes COMMA and another NUMBER.
    # It transforms each lexeme into an int and adds it to the list.
    def number_list(self):
        nums = []
        num_tok = self.eat('NUMBER')
        nums.append(int(num_tok.value))
        while self.current.type_ == 'COMMA':
            self.eat('COMMA')
            num_tok = self.eat('NUMBER')
            nums.append(int(num_tok.value))
        return nums