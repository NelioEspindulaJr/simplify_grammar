from helpers import FileParser

file_parser = FileParser()

def main():
    variables, rules = file_parser.read_file()
    print(variables)
    print(rules)

if __name__ == "__main__":
    main()