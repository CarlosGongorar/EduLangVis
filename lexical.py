import re

class Token:
    """This class represents the data structure of a token."""
    def __init__(self, type_: str, value: str):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type_!r}, {self.value!r})"


class LexicalAnalyzer:
    """LexicalAnalyzer EduLangVis."""

    @staticmethod
    def lex(code: str):
        """This method receives a code and returns a list of tokens."""
        token_specification = [
            ("ALGORITHM_NAME", r"\b(?:bubble_sort|merge_sort|quick_sort)\b"), # Algorithms names
            ("KEYWORD",        r"\b(?:ARRAY|ALGORITHM|VISUALIZE)\b"), # Keywords
            # Separators and delimitations
            ("LBRACKET",       r"\["),
            ("RBRACKET",       r"\]"),
            ("COMMA",          r","),
            # Numbers
            ("NUMBER",         r"\d+"),
            # Skips and newlines
            ("NEWLINE",        r"\n"),
            ("SKIP",           r"[ \t]+"),
            # Errors
            ("MISMATCH",       r"."),
        ]


        # Compile a big regex that group all the posible classes of tokens
        # Travel source code with "finditer" extracting in each step token type and corresponding string
        # Finaly, filter the spaces and newlines, detect errors "MISMATCH" and colected all valid tokens in a array to return them to the SyntaxAnalyzer 

        tok_regex = "|".join(f"(?P<{name}>{pattern})"
            for name, pattern in token_specification)
        tokens = []
        for mo in re.finditer(tok_regex, code):
            kind = mo.lastgroup
            value = mo.group()

            if kind == "MISMATCH":
                raise RuntimeError(f"Unexpected character: {value!r}")
            elif kind in ("SKIP", "NEWLINE"):
                continue
            tokens.append(Token(kind, value))

        return tokens