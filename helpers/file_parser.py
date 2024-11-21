import sys
from typing import Tuple, List, Dict
from custom_types import ProductionsDictionary


class FileParser:
    def __init__(self, file_name="") -> None:
        self.file_name = file_name
        self.start_variable = ""
        self.variables = []
        self.productions_dict: ProductionsDictionary = {}

    def read_file(self) -> Tuple[str, List[str], Dict[str, List[str]], str]:
        while True:
            if not self.file_name:
                self.file_name = input("Enter the file name inside this directory: ")

            try:
                with open(self.file_name, "rt") as search_file:
                    lines = search_file.readlines()

                    if len(lines) < 3:
                        print("File is not formatted correctly. Please try again.")
                        break

                    self.variables = lines[0].strip().split()
                    self.start_variable = lines[1].strip()

                    self.productions_dict = {var: [] for var in self.variables}

                    for index, line in enumerate(lines[2:], start=3):
                        rule_atoms = line.strip().split()

                        if len(rule_atoms) != 2:
                            print(
                                f"Grammar rule is not properly inserted on line number {index} (content: {' '.join(rule_atoms)}). Please correct it and try again."
                            )
                            sys.exit()

                        start_variable, production = rule_atoms

                        if start_variable not in self.variables:
                            print(
                                f"Invalid start variable '{start_variable}' on line {index}. Please fix the file and try again."
                            )
                            sys.exit()

                        if production == "h":
                            production = "λ"

                        self.productions_dict[start_variable].append(production)

            except FileNotFoundError:
                self.file_name = ""
                print("File not found. Please try again.")
            else:
                return self.start_variable, self.variables, self.productions_dict, self.file_name

    @staticmethod
    def write_file(output_file: str, start_variable: str, productions: Dict[str, List[str]]) -> None:
        try:
            with open(output_file, "w") as file:
                variables = " ".join(productions.keys())
                file.write(f"{variables}\n")
                file.write(f"{start_variable}\n")

                for var, rules in productions.items():
                    for rule in rules:
                        file.write(f"{var} {rule}\n")

            print(f"Simplified grammar successfully written to {output_file}.")
        except Exception as e:
            print(f"Error writing to file {output_file}: {e}")
