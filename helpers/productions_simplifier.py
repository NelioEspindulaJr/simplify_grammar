from typing import Dict, List
from custom_types import ProductionsList


class ProductionSimplifier:
    def __init__(self, start_variable: str, variables, productions: ProductionsList) -> None:
        self.productions = productions
        self.start_variable = start_variable
        self.variables = variables
        self.production_rules_map = self._build_production_rules_map()

    def _build_production_rules_map(self) -> Dict[str, List[str]]:
        production_rules_map = {}
        for start, prod in self.productions:
            if start not in production_rules_map:
                production_rules_map[start] = []
            production_rules_map[start].append(prod)
        return production_rules_map
    
    def remove_empty_productions(self) -> ProductionsList:
        for variable in list(self.production_rules_map.keys()):
            updated_rules = []
            for rule in self.production_rules_map[variable]:
                if rule != 'h' and rule != 'λ':
                    updated_rules.append(rule)
                else:
                    self.productions.remove((variable, rule))
            self.production_rules_map[variable] = updated_rules
