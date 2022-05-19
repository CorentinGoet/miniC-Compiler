"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""


class Visitor:
    """
    Visitor abstract class
    """

    def visit(self, element):
        """
        Visit an element
        """
        self.visitProgram(element)

    def visitProgram(self, program):
        """
        Visit a program Node

        :param program: Program Node to visit
        """
        program.declarations.accept(self)
        program.statements.accept(self)

    def visitDeclarations(self, declarations):
        """
        Visit a Declarations Node

        :param declarations: declarations Node to visit
        """
        for declaration in declarations.get_declarations():
            declaration.accept(self)

    def visitDeclaration(self, declaration):
        """
        Visit a Declaration Node

        :param declaration: declaration Node to visit
        """
        raise NotImplementedError

    def visitStatements(self, statements):
        """
        Visit a Statements Node
        :param statements: Statements Node to visit
        """

        for statement in statements.get_statements():
            statement.accept(self)

    def visitStatement(self, statement):
        """
        Visit a Statement Node

        :param statement: Statement Node to visit
        """
        statement.son_node.accept(self)

    def visitBlock(self, block):
        """
        Visit a Block Node

        :param block: Block Node to visit
        """
        for statement in block.get_statements():
            statement.accept(self)

    def visitIfStatement(self, if_statement):
        """
        Visit an If Statement Node

        :param if_statement: if Statement Node to visit
        """
        if_statement.expression.accept(self)
        if_statement.trueStatement.accept(self)
        if if_statement.falseStatement is not None:
            if_statement.falseStatement.accept(self)

    def visitWhileStatement(self, while_statement):
        """
        Visit a While Statement Node

        :param while_statement: While Statement Node to visit
        """
        while_statement.expression.accept(self)
        while_statement.statement.accept(self)

    def visitExpression(self, expression):
        """
        Visit an Expression Node
        :param expression: expression Node to visit
        """

        for conjunction in expression.get_conjunctions():
            conjunction.accept(self)

    def visitConjunction(self, conjunction):
        """
        Visit a Conjunction Node
        :param conjunction: Conjunction Node to visit
        """

        for equality in conjunction.get_equalities():
            equality.accept(self)

    def visitEquality(self, equality):
        """
        Visit an Equality Node

        :param equality: Equality Node to visit
        """

        equality.relation1.accept(self)
        equality.equOp.accept(self)
        equality.relation2.accept(self)

    def visitRelation(self, relation):
        """
        Visit a Relation Node

        :param relation: Relation Node to visit
        """
        relation.addition1.accept(self)
        relation.relOp.accept(self)
        relation.addition2.accept(self)

    def visitAddition(self, addition):
        """
        Visit an Addition Node

        :param addition: Addition Node to visit
        """
        terms = addition.get_terms()
        operators = addition.get_operators()

        terms[0].accept(self)
        for i in range(len(operators)):
            operators[i].accept(self)
            terms[i + 1].accept(self)

    def visitTerm(self, term):
        """
        Visit a Term Node

        :param term: Term Node to visit
        """
        factors = term.get_factors()
        operators = term.get_operators()

        factors[0].accept(self)
        for i in range(len(operators)):
            operators[i].accept(self)
            factors[i + 1].accept(self)

    def visitFactor(self, factor):
        """
        Visit a Factor Node

        :param factor: Factor Node to visit
        """
        factor.unaryOp.accept(self)
        factor.primary.accept(self)

    def visitPrimary(self, primary):
        """
        Visit a Primary Node

        :param primary: Primary Node to visit
        """
        primary.sonNode.accept(self)








