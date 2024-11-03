import sys
from typing import List, Tuple, Optional

Production = Tuple[str, str]
ProductionsList = List[Production]


class FileParser:
    def __init__(self, file_name="") -> None:
        self.file_name = file_name
        self.variables = []
        self.productions_rules = []

    def read_file(self) -> Optional[Tuple[List[str], ProductionsList]]:
        while True:
            if not self.file_name:
                self.file_name = input("Enter the file name inside this directory: ")

            try:
                with open(self.file_name, "rt") as search_file:
                    lines = search_file.readlines()

                    if len(lines) < 2:
                        print("File is not formatted correctly. Please try again.")
                        break
                    else:
                        self.variables = lines[0].strip().split()

                        for index, line in enumerate(lines[1:], start=1):
                            rule_atoms = line.strip().split()

                            if len(rule_atoms) != 2:
                                print(
                                    f"Transition is not properly inserted on line number {index + 1}. Please correct it and try again."
                                )
                                sys.exit()
                            else:
                                start_variable, production = rule_atoms
                                if production == "h":
                                    production = "λ"

                                self.productions_rules.append(
                                    (start_variable, production)
                                )
            except FileNotFoundError:
                self.file_name = ""
                print("File not found. Please try again.")
            else:
                return self.variables, self.productions_rules
