"""This module contains the Compiler class for EduLangVis."""

from lexical import LexicalAnalyzer
from sintactic import SyntacticAnalyzer, ParserError
from semantic import SemanticAnalyzer, SemanticError

class Compiler:
    """This class represents the behavior of the EduLangVis compiler."""

    def __init__(self):
        self.tokens = []
        self.parsed_result = {}
        self.success = False

    def compile(self, code: str) -> bool:
        try:
            # 1: Lexical Analysis
            self.tokens = LexicalAnalyzer.lex(code)
            print("[LEXICAL ANALYSIS SUCCESSFUL] Tokens:")
            for token in self.tokens:
                print(f"  {token}")

            # 2: Sintax Analysis
            parser = SyntacticAnalyzer(self.tokens)
            self.parsed_result = parser.parse()
            print("[SYNTACTIC ANALYSIS SUCCESSFUL] Parsed structure:")
            print(f"  Array: {self.parsed_result['array']}")
            print(f"  Algorithm: {self.parsed_result['algorithm']}")

            # 3: Semantic Analysis
            semantic = SemanticAnalyzer(self.parsed_result)
            semantic.analyze()
            print("[SEMANTIC ANALYSIS SUCCESSFUL] Code is valid.")

            self.success = True
            return True

        except (RuntimeError, ParserError, SemanticError) as e:
            print(f"[COMPILATION ERROR] {e}")
            self.success = False
            return False
        
if __name__ == "__main__":
    code = """
    ARRAY[5, 2]
    ALGORITHM quick_sort
    VISUALIZE
    """
    
    compiler = Compiler()
    result = compiler.compile(code)

    if result:
        print("¡Compilación exitosa! Listo para ejecutar o visualizar.")
    else:
        print("Fallo la compilación.")