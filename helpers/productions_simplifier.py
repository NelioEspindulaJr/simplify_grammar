from typing import Dict, List
from custom_types import ProductionsDictionary


class ProductionSimplifier:
    def __init__(self, start_variable: str, variables, productions: ProductionsDictionary) -> None:
        self.productions = productions
        self.start_variable = start_variable
        self.variables = variables

    def remove_empty_productions(self) -> None:
        for variable in list(self.productions.keys()):
            updated_rules = [rule for rule in self.productions[variable] if rule not in ('h', 'λ')]

            if updated_rules:
                self.productions[variable] = updated_rules
            else:
                del self.productions[variable]

    def remove_useless_productions(self) -> None:
        generating = self._find_generating_symbols()
        self.productions = {
            var: [rule for rule in rules if all(symbol in generating or symbol.islower() for symbol in rule)]
            for var, rules in self.productions.items()
            if var in generating
        }

        reachable = self._find_reachable_symbols()
        self.productions = {
            var: rules for var, rules in self.productions.items() if var in reachable
        }

    def remove_unit_productions(self) -> None:
        unit_pairs = set()
        for var in self.productions:
            unit_pairs.add((var, var))
            for rule in self.productions[var]:
                if len(rule) == 1 and rule.isupper():
                    unit_pairs.add((var, rule))

        changed = True
        while changed:
            changed = False
            new_pairs = set()
            for (A, B) in unit_pairs:
                for (X, Y) in unit_pairs:
                    if B == X and (A, Y) not in unit_pairs:
                        new_pairs.add((A, Y))
                        changed = True
            unit_pairs.update(new_pairs)

        new_productions = {var: [] for var in self.productions}
        for A, rules in self.productions.items():
            new_productions[A].extend([rule for rule in rules if not (len(rule) == 1 and rule.isupper())])

        for A, B in unit_pairs:
            if A != B and B in self.productions:
                new_productions[A].extend(
                    rule for rule in self.productions[B] if not (len(rule) == 1 and rule.isupper())
                )

        self.productions = {var: list(set(rules)) for var, rules in new_productions.items()}

    def _find_generating_symbols(self) -> set:
        generating = set()
        changed = True

        while changed:
            changed = False
            for var, rules in self.productions.items():
                if var in generating:
                    continue
                for rule in rules:
                    if all(symbol.islower() or symbol in generating for symbol in rule):
                        generating.add(var)
                        changed = True
                        break
        return generating

    def _find_reachable_symbols(self) -> set:
        reachable = {self.start_variable}
        to_explore = [self.start_variable]

        while to_explore:
            current = to_explore.pop()
            for rule in self.productions.get(current, []):
                for symbol in rule:
                    if symbol.isupper() and symbol not in reachable:
                        reachable.add(symbol)
                        to_explore.append(symbol)
        return reachable