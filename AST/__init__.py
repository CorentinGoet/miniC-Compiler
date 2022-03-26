"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
This package is part of the mini-C Compiler project available on GitHub: https://github.com/CorentinGoet/miniC-Compiler.
It contains the classes for the Abstract Syntax Tree for the compiler.
"""

from AST.addition import Addition
from AST.assignment import Assignment
from AST.block import Block
from AST.conjunction import Conjunction
from AST.declaration import Declaration
from AST.declarations import Declarations
from AST.equality import Equality
from AST.expression import Expression
from AST.factor import Factor
from AST.identifier import Identifier
from AST.ifStatement import IfStatement
from AST.literal import Literal
from AST.operators import AddOp, MulOp, RelOp, UnaryOp, EquOp
from AST.primary import Primary
from AST.program import Program
from AST.relation import Relation
from AST.statement import Statement
from AST.statements import Statements
from AST.term import Term
from AST.type import Type
from AST.whileStatement import WhileStatement

