# Simplify Grammar

## Description

Implementation of an algorithm to simplify (clean) a given grammar by removing all unwanted productions.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

Before you start, you must have Python installed in your environment, check [here](https://www.python.org/downloads/) for python's download documentation.

1. Clone the repository:
    ```sh
    git clone https://github.com/nelioespindulajr/simplify_grammar.git
    ```
2. Navigate to the project directory:
    ```sh
    cd simplify_grammar
    ```

## Usage

1. Make a `.txt` file with the grammar that you want to simplify, following the rules:
    ```txt
    # grammar.txt example
    S A B C D    # Variables line.
    S            # Start Variable Line.
    S a          # From the third line and beyond, the productions.
    S Aa
    A a
    A Aa
    A B
    B h
    ```
   (Remember to follow the rules or the code will throw an Exception, remove all comments if you do so.)
2. Run the main script:
    ```sh
    python main.py
    ```
3. Type the name of the file that you wrote your grammar with the `.txt` extension:
   ```
    Enter the file name inside this directory: grammar.txt
   ```