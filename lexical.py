import re

# pylint: disable=too-few-public-methods
class Token:
    """Un token con su tipo y su valor (lexema)."""
    def __init__(self, type_: str, value: str):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type_!r}, {self.value!r})"


class LexicalAnalyzer:
    """LexicalAnalyzer EduLangVis."""

    @staticmethod
    def lex(code: str):
        """Recibe el código y devuelve la lista de tokens."""
        token_specification = [
            # 1) Algoritmos (patrón más largo, antes que KEYWORD)
            ("ALGORITHM_NAME", r"\b(?:bubble_sort|merge_sort|quick_sort)\b"),
            # 2) Palabras clave EDU
            ("KEYWORD",        r"\b(?:ARRAY|ALGORITHM|VISUALIZE)\b"),
            # 3) Delimitadores y separadores
            ("LBRACKET",       r"\["),
            ("RBRACKET",       r"\]"),
            ("COMMA",          r","),
            # 4) Número entero
            ("NUMBER",         r"\d+"),
            # 6) Saltos de línea y espacios (se ignoran)
            ("NEWLINE",        r"\n"),
            ("SKIP",           r"[ \t]+"),
            # 7) Cualquier otro carácter → error
            ("MISMATCH",       r"."),
        ]

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


if __name__ == "__main__":
    ejemplo = """
    ARRAY [6, 2, 9, 3]
    ALGORITHM merge_sort
    VISUALIZE
    """
    toks = LexicalAnalyzer.lex(ejemplo)
    print(toks)