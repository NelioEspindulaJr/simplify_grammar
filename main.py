from turtledemo.penrose import start

from helpers import FileParser, ProductionSimplifier

file_parser = FileParser()


def main():
    start_variable, variables, productions_rules_dict, entry_file_name = file_parser.read_file()

    productions_simplifier = ProductionSimplifier(start_variable, variables, productions_rules_dict)

    productions_simplifier.remove_empty_productions()

    productions_simplifier.remove_unit_productions()

    productions_simplifier.remove_useless_productions()

    print("Simplified productions dictionary: ", productions_simplifier.productions)

    file_parser.write_file(f"simplified_{entry_file_name}", start_variable, productions_simplifier.productions)

if __name__ == "__main__":
    main()
