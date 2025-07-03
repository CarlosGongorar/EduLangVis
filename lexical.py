import re

# pylint: disable=too-few-public-methods
class Token:
    """This class represents the data structure of a token. It means: a type of token and its value (lexema)."""
    def __init__(self, type_: str, value: str):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type_!r}, {self.value!r})"


class LexicalAnalyzer:
    """LexicalAnalyzer EduLangVis."""

    @staticmethod
    def lex(code: str):
        """This method receives a code(str) and returns a list of tokens."""
        token_specification = [
            ("KEYWORDS", r"ARRAY|ALGORITHM|VISUALIZE"), # Keywords
            ("ALGORITHMS", r"bubble_sort|merge_sort|quick_sort"),
            ("LBRACKET",   r"\["),              # [
            ("RBRACKET",   r"\]"),              # ]
            ("COMMA",      r","),               # ,
            ("NUMBER",     r"\d+"),             # Numbers
            ("NEWLINE",    r"\n"),              # New lines
            ("SKIP",       r"[ \t]+"),          # Idens and space
            ("MISMATCH",   r"."),               # A wrong character
        ]

        tok_regex = "|".join(
            f"(?P<{name}>{pattern})" for name, pattern in token_specification
        )
        tokens = []
        for mo in re.finditer(tok_regex, code):
            kind = mo.lastgroup
            value = mo.group()

            if kind == "MISMATCH":
                raise RuntimeError(f"Caracter inesperado: {value!r}")
            elif kind in ("SKIP", "NEWLINE"):
                continue
            else:
                tokens.append(Token(kind, value))

        return tokens


if __name__ == "__main__":
    ejemplo = """
    ARRAY [6, 2, 9, 3]
    ALGORITHM merge_sort
    VISUALIZE
    """
    toks = LexicalAnalyzer.lex(ejemplo)
    print(toks)