def evaluate(node):
    if isinstance(node, float):
        return node

    if node[0] == "neg":
        return -evaluate(node[1])

    op, left, right = node

    l = evaluate(left)
    r = evaluate(right)

    if op == "+":
        return l + r
    if op == "-":
        return l - r
    if op == "*":
        return l * r
    if op == "/":
        if r == 0:
            return "ERROR"
        return l / r
