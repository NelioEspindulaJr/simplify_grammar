from helpers import FileParser

file_parser = FileParser()

def main():
    start_variable, variables, productions_rules = file_parser.read_file()
if __name__ == "__main__":
    main()