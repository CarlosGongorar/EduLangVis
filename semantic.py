class SemanticError(Exception):
    pass

class SemanticAnalyzer:
    """Verifica propiedades semánticas sobre el resultado del parser."""
    
    SUPPORTED_ALGORITHMS = {
        'bubble_sort',
        'insertion_sort',
        'selection_sort',
        'merge_sort',
        'quick_sort',
    }

    def __init__(self, parsed):
        # parsed = {'array': [...], 'algorithm': 'bubble_sort'}
        self.array = parsed['array']
        self.algorithm = parsed['algorithm']

    def analyze(self):
        self._check_array_not_empty()
        self._check_array_elements()
        self._check_algorithm_supported()
        self._check_algorithm_requirements()
        # Si llega hasta aquí, todo OK
        return True

    def _check_array_not_empty(self):
        if not self.array:
            raise SemanticError("Array semántico inválido: debe tener al menos 1 elemento.")

    def _check_array_elements(self):
        for x in self.array:
            if not isinstance(x, int):
                raise SemanticError(f"Elemento inválido en array: {x!r} no es un entero.")
            if x < 0:
                raise SemanticError(f"Valor inválido: {x} (solo enteros ≥ 0 permitidos).")

    def _check_algorithm_supported(self):
        if self.algorithm not in self.SUPPORTED_ALGORITHMS:
            raise SemanticError(f"Algoritmo '{self.algorithm}' no soportado.")

    def _check_algorithm_requirements(self):
        # Ejemplo: merge_sort y quick_sort necesitan al menos 2 elementos
        if self.algorithm in ('merge_sort', 'quick_sort') and len(self.array) < 2:
            raise SemanticError(
                f"{self.algorithm} requiere al menos 2 elementos (tienes {len(self.array)})."
            )

# Uso integrado después del parser:
if __name__ == "__main__":
    from lexical import LexicalAnalyzer
    from sintactic import SyntacticAnalyzer, ParserError

    code = """
    ARRAY[5] 
    ALGORITHM merge_sort 
    VISUALIZE"""
    try:
        tokens = LexicalAnalyzer.lex(code)
        parsed = SyntacticAnalyzer(tokens).parse()  # {'array':[5], 'algorithm':'merge_sort'}
        SemanticAnalyzer(parsed).analyze()
        print("¡Análisis semántico exitoso, listo para ejecutar/visualizar!")
    except (RuntimeError, ParserError, SemanticError) as e:
        print("Error en compilación:", e)