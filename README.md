# Mini-C Compiler

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
