from tokenizer import tokenize
from parser import Parser
from evaluator_core import evaluate


def evaluate_file(input_path: str):
    results = []

    with open(input_path, "r") as f:
        lines = f.readlines()

    output_lines = []

    for line in lines:
        expr = line.strip()

        try:
            tokens = tokenize(expr)

            if tokens == "ERROR":
                raise Exception()

            parser = Parser(tokens)
            tree = parser.parse()
            result = evaluate(tree)

            output_lines.append(f"Input: {expr}")
            output_lines.append(f"Tree: {tree}")
            output_lines.append(f"Tokens: {tokens}")
            output_lines.append(f"Result: {result}")
            output_lines.append("")

            results.append({
                "input": expr,
                "tree": str(tree),
                "tokens": str(tokens),
                "result": result
            })

        except:
            output_lines.append(f"Input: {expr}")
            output_lines.append("Tree: ERROR")
            output_lines.append("Tokens: ERROR")
            output_lines.append("Result: ERROR")
            output_lines.append("")

            results.append({
                "input": expr,
                "tree": "ERROR",
                "tokens": "ERROR",
                "result": "ERROR"
            })

    with open("output.txt", "w") as f:
        f.write("\n".join(output_lines))

    return results
