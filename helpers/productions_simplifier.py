from custom_types import ProductionsList


class ProductionSimplifier:
    def __init__(self, productions: ProductionsList) -> None:
        self.productions = productions

    def remove_useless_productions(self) -> ProductionsList:
        pass