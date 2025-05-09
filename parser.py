class ASTNode:
    def __init__(self, type_, value=None, left=None, right=None):
        self.type = type_
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.value is not None:
            return f"{self.type}({self.value})"
        return f"{self.type}({self.left}, {self.right})"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, expected_type):
        token = self.current_token()
        if token and token[0] == expected_type:
            self.pos += 1
            return token
        return None

    def factor(self):
        token = self.current_token()
        if not token:
            raise SyntaxError("Unexpected end of expression")

        if token[0] == 'NUMBER':
            self.eat('NUMBER')
            return ASTNode('Number', token[1])
        elif token[0] == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()
            if not self.eat('RPAREN'):
                raise SyntaxError("Missing closing parenthesis")
            return node
        else:
            raise SyntaxError(f"Unexpected token: {token}")

    def term(self):
        node = self.factor()
        while True:
            token = self.current_token()
            if token and token[0] in ('MUL', 'DIV'):
                self.eat(token[0])
                right = self.factor()
                node = ASTNode(token[0], token[1], node, right)
            else:
                break
        return node

    def expr(self):
        node = self.term()
        while True:
            token = self.current_token()
            if token and token[0] in ('ADD', 'SUB'):
                self.eat(token[0])
                right = self.term()
                node = ASTNode(token[0], token[1], node, right)
            else:
                break
        return node

    def parse(self):
        node = self.expr()
        if self.pos < len(self.tokens):
            raise SyntaxError(f"Unexpected token at end: {self.tokens[self.pos]}")
        return node
