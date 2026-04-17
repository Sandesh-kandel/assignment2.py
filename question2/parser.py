class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def eat(self):
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def parse(self):
        return self.expr()

    def expr(self):
        node = self.term()

        while self.current()[1] in ["+", "-"]:
            op = self.eat()[1]
            right = self.term()
            node = (op, node, right)

        return node

    def term(self):
        node = self.factor()

        while self.current()[1] in ["*", "/"]:
            op = self.eat()[1]
            right = self.factor()
            node = (op, node, right)

        return node

    def factor(self):
        token = self.current()

        if token[0] == "NUM":
            return float(self.eat()[1])

        elif token[1] == "-":
            self.eat()
            return ("neg", self.factor())

        elif token[0] == "LPAREN":
            self.eat()
            node = self.expr()
            self.eat()
            return node
