# Mini-C Compiler
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="78" height="20" role="img" aria-label="license: MIT"><title>license: MIT</title><linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="r"><rect width="78" height="20" rx="3" fill="#fff"/></clipPath><g clip-path="url(#r)"><rect width="47" height="20" fill="#555"/><rect x="47" width="31" height="20" fill="#97ca00"/><rect width="78" height="20" fill="url(#s)"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110"><text aria-hidden="true" x="245" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="370">license</text><text x="245" y="140" transform="scale(.1)" fill="#fff" textLength="370">license</text><text aria-hidden="true" x="615" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="210">MIT</text><text x="615" y="140" transform="scale(.1)" fill="#fff" textLength="210">MIT</text></g></svg>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="80" height="20" role="img" aria-label="tests: 100%"><title>tests: 100%</title><linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><clipPath id="r"><rect width="80" height="20" rx="3" fill="#fff"/></clipPath><g clip-path="url(#r)"><rect width="37" height="20" fill="#555"/><rect x="37" width="43" height="20" fill="#4c1"/><rect width="80" height="20" fill="url(#s)"/></g><g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110"><text aria-hidden="true" x="195" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="270">tests</text><text x="195" y="140" transform="scale(.1)" fill="#fff" textLength="270">tests</text><text aria-hidden="true" x="575" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="330">100%</text><text x="575" y="140" transform="scale(.1)" fill="#fff" textLength="330">100%</text></g></svg>

**This project is in development, the first version is not released yet.**

MiniC-Compiler is a compiler for the mini-C programming language, a simplified version of C (the grammar for it is
detailed in a further section). The compiled program is made to run on an instruction set simulator I designed in
another project called [SIMJI](https://github.com/CorentinGoet/SIMJI).

## Table of Contents
1. [Context](#context)
2. [Objective](#objective)
3. [Mini-C Language](#mini-c-language)

## Context
This project is made within a compilation course at [ENSTA Bretagne](https://www.ensta-bretagne.fr/fr) (Frenche graduate
engineering school). Because of this the main report detailing the project will be in French. However, most of the
documentation and this readme will be in English.

## Objective
The objective for this project is to design a compiler for the mini-C language containing the following elements:
- Lexer
- Parser
- AST (Abstract Syntax Tree / Arbre de Syntaxe Abstraite)
- Visitor Pattern
- Pretty-printer

### Mini-C language
Mini-C has a syntax a little different from C, it is detailed in the 
[EBNF](https://wikipedia.org/wiki/Extended_Backus-Naur_Form) code below:
```ebnf
Program         = int main(){Declarations Statements}
Declarations    = {Declaration}
Declaration     = Type Identifier [ [Integer] ] {, Identifier [ [Integer] ]}; 
// Be careful the first set of bracket is from ebnf and the second one is from mini-C
Type            = int | bool | float | char
Statements      = {Statement}
Statement       = ; | Block | Assignment | IfStatement | WhileStatement
Block           = {Statements}
Assignment      = Identifier [ [Expression] ] = Expression;
IfStatement     = if (Expression) Statement [else Statement]
WhileStatement  = while (Expression) Statement
Expression      = Conjunction {|| Conjunction}
Conjunction     = Equality {&& Equality}
Equality        = Relation [ EquOp Relation ]
EquOp           = == | !=
Relation        = Addition [ RelOp Addition]
RelOp           = < | > | <= | >=
Addition        = Term { AddOp Term }
AddOp           = + | -
Term            = Factor { MulOp Factor }
MulOp           = * | / | %
Factor          = [ UnaryOp ] Primary
UnaryOp         = - | !
Primary         = Identifier [ [Expression] ] | Literal | ( Expression ) | Type Expression
Identifier      = Letter{ Letter | Digit }
Letter          = a | b | c | ... | z | A | B | C | ... | Z
Digit           = 0 | 1 | ... | 9
Literal         = Integer | Boolean | Float | Char
Boolean         = true | false
Float           = Integer.Integer
Char            = ' ASCII char '    // Where ASCII char is the set of ASCII Characters
```

## Lexer
The lexer is the part of the compiler responsible for breaking the source code into lexems.
The class for the lexer is `Lexer`, found in the [lexer.py](/lexer.py) file, it has one main function `tokenize`, which
takes a string as input and returns a list of tokens, by matching the lexems with the regexes.

For example, the following mini-c source code:
```mini-c
int main(){
    int a;
}
```
would be tokenized as:
```python
Lexem(value: LexemTag.TYPE, type: int , position: [1, 0])
Lexem(value: LexemTag.MAIN, type: main, position: [1, 4])
Lexem(value: LexemTag.L_PARENTHESIS, type: (, position: [1, 8])
Lexem(value: LexemTag.R_PARENTHESIS, type: ), position: [1, 9])
Lexem(value: LexemTag.L_BRACE, type: {, position: [1, 10])
Lexem(value: LexemTag.TYPE, type: int , position: [2, 4])
Lexem(value: LexemTag.IDENTIFIER, type: a, position: [2, 8])
Lexem(value: LexemTag.TERMINATOR, type: ;, position: [2, 9])
Lexem(value: LexemTag.R_BRACE, type: }, position: [3, 0])
```

with the following instructions:
```python
from lexer import Lexer
lexer = Lexer()
lexer.tokenize("int main(){int a;}")
print(lexer)
```

### Tests
The lexer is tested in the [lexerTest.py](unit_tests/lexerTest.py) file. Each syntax possibility is tested with a 
separate method. This test file gives a test coverage of 100% for the Lexer and Lexem classes.

## Parser
The parser is the part of the compiler responsible for turning the lexems into an AST.
It takes the list of lexems given by the lexer and builds the AST from the classes found in the AST package.

