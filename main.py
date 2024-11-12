from helpers import FileParser, ProductionSimplifier


file_parser = FileParser()

def main():
    start_variable, variables, productions_rules = file_parser.read_file()

    productions_simplifier = ProductionSimplifier(start_variable, variables, productions_rules)

    print("1º",productions_simplifier.production_rules_map, "\n", productions_rules)
    
    productions_simplifier.remove_empty_productions()

    print("2º", productions_simplifier.productions, "\n", productions_simplifier.production_rules_map)

if __name__ == "__main__":
    main()