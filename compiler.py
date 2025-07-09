"""This module contains the Compiler class for EduLangVis."""

from lexical import LexicalAnalyzer
from sintactic import SyntacticAnalyzer, ParserError
from semantic import SemanticAnalyzer, SemanticError
from sort_algorithms import bubble_sort_trace, merge_sort_trace, quick_sort_trace
from visualizer import SortVisualizer

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

            # 2: Sintax Analysis
            parser = SyntacticAnalyzer(self.tokens)
            self.parsed_result = parser.parse()

            # 3: Semantic Analysis
            semantic = SemanticAnalyzer(self.parsed_result)
            semantic.analyze()

            self.execute_visualization()
            self.success = True
            return True

        except (RuntimeError, ParserError, SemanticError) as e:
            print(f"[COMPILATION ERROR] {e}")
            self.success = False
            return False
        
    def execute_visualization(self):
        array = self.parsed_result["array"]
        algorithm = self.parsed_result["algorithm"]

        if algorithm == "bubble_sort":
            trace = bubble_sort_trace(array)
        elif algorithm == "merge_sort":
            trace = merge_sort_trace(array)
        elif algorithm == "quick_sort":
            trace = quick_sort_trace(array)
        else:
            print(f"No visualizer implemented for algorithm: {algorithm}")
            return

        visualizer = SortVisualizer(trace, array, algorithm)
        visualizer.run()
        
if __name__ == "__main__":
    code = """
    ARRAY [34, 17, 45, 3, 28, 11, 6, 50, 21, 38, 9, 41, 26, 7, 46, 31, 15, 44, 36, 5, 13, 40, 16, 2, 25, 23, 1, 10, 8, 27, 30, 49, 18, 4, 29, 43, 20, 12, 24, 35, 22, 48, 33, 39, 42, 47, 14, 32, 19, 37]
    ALGORITHM merge_sort
    VISUALIZE
    """
    
    compiler = Compiler()
    result = compiler.compile(code)

    if result:
        print("¡Compilación exitosa! Listo para ejecutar o visualizar.")
    else:
        print("Fallo la compilación.")