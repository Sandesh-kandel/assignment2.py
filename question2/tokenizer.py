def tokenize(expr):
    tokens = []
    i = 0

    # loop through the expression character by character
    while i < len(expr):

        # if it's a number, collect the full number (could be multiple digits)
        if expr[i].isdigit():
            num = ""

            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1

            tokens.append(("NUM", num))
            continue  # skip increment since we already moved forward

        # if it's one of the operators
        elif expr[i] in "+-*/":
            tokens.append(("OP", expr[i]))

        # opening bracket
        elif expr[i] == "(":
            tokens.append(("LPAREN", "("))

        # closing bracket
        elif expr[i] == ")":
            tokens.append(("RPAREN", ")"))

        # ignore spaces (just move ahead)
        elif expr[i].isspace():
            i += 1
            continue

        # if any unknown character appears → invalid expression
        else:
            return "ERROR"

        # move to next character
        i += 1

    # mark the end of input
    tokens.append(("END", ""))

    return tokens
