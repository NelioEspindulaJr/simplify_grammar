from custom_types import ProductionsList


class ProductionSimplifier:
    def __init__(self, start_variable: str, productions: ProductionsList) -> None:
        self.productions = productions
        self.start_variable = start_variable

    def remove_useless_productions(self) -> ProductionsList:
        pass