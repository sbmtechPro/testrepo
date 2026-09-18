"""Small CodeQL test program.

This intentionally contains a direct eval() call so the custom query
.github/codeql/custom-queries/avoid-eval.ql can report it in a pull request.
"""


def run_user_expression(expression: str):
    # CodeQL should flag this line.
    return eval(expression)


if __name__ == "__main__":
    print(run_user_expression("1 + 1"))
