class SemanticError(Exception):
    pass

class SemanticAnalyzer:
    """Verifi semantic proms about result from parser"""
    
    """Supported algotiths"""
    SUPPORTED_ALGORITHMS = {
        'bubble_sort'
    }

    
    def __init__(self, parsed):
        # parsed = {'array': [...], 'algorithm': 'algorithm_name'}
        self.array = parsed['array']
        self.algorithm = parsed['algorithm']

    # Do checks
    def analyze(self):
        self._check_array_not_empty()
        self._check_array_elements()
        self._check_algorithm_supported()
        self._check_algorithm_requirements()
        # If pass until here, everything is ok
        return True

    # Check that the array is not empty
    def _check_array_not_empty(self):
        if not self.array:
            raise SemanticError("ARRAY SEMANTIC ERROR: Must have at least 1 element.")

    # Check array elements
    def _check_array_elements(self):
        for x in self.array:
            if not isinstance(x, int):
                raise SemanticError(f"INVALID ELEMENT IN ARRAY: {x!r} aint int.")
            if x <= 0:
                raise SemanticError(f"INVALID VALUE: {x} (only integers greater than 0).")

    # Check that the algorithm is supported 
    def _check_algorithm_supported(self):
        if self.algorithm not in self.SUPPORTED_ALGORITHMS:
            raise SemanticError(f"ALGORITHM '{self.algorithm}' NOT SUPPORTED.")

    # Check algoruthm requirements
    def _check_algorithm_requirements(self):
        # Ejemplo: merge_sort y quick_sort necesitan al menos 2 elementos
        if self.algorithm in ('merge_sort', 'quick_sort') and len(self.array) < 2:
            raise SemanticError(
                f"{self.algorithm} Must have at least 2 elements (you have {len(self.array)})."
            )

# Using lexical and syntax analyzer
if __name__ == "__main__":
    from lexical import LexicalAnalyzer
    from sintactic import SyntacticAnalyzer, ParserError

    code = """
    ARRAY[5, 3, 4, 2, 1 ] 
    ALGORITHM bubble_sort 
    VISUALIZE"""
    try:
        tokens = LexicalAnalyzer.lex(code)
        parsed = SyntacticAnalyzer(tokens).parse()
        SemanticAnalyzer(parsed).analyze()
        print("¡Análisis semántico exitoso, listo para ejecutar/visualizar!")
    except (RuntimeError, ParserError, SemanticError) as e:
        print("Compilation error:", e)