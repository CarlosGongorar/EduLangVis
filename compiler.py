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
        self.message_log = ""

    def log(self, message: str):
        self.message_log += message + "\n"

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

            self.log("[Success Compilation, Ready to visualize]")
            return True
        except (RuntimeError, ParserError, SemanticError) as e:
            self.log(f"[COMPILATION ERROR] {e}")
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