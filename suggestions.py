import re

def suggest_correction(expression):
    suggestions = []

    # Rule 1: Three or more consecutive operators
    if re.search(r'([+\-*/]{3,})', expression):
        suggestions.append("Invalid operator repetition — please check your expression.")

    # Rule 2: Two consecutive operators
    operator_pairs = re.findall(r'([+\-*/])([+\-*/])', expression)
    for pair in operator_pairs:
        corrected_expr_1 = expression.replace(f'{pair[0]}{pair[1]}', pair[0])
        corrected_expr_2 = expression.replace(f'{pair[0]}{pair[1]}', pair[1])
        if corrected_expr_1 != expression:
            suggestions.append(f"Did you mean: {corrected_expr_1}?")
        if corrected_expr_2 != expression:
            suggestions.append(f"Did you mean: {corrected_expr_2}?")

    # Rule 3: Expression ends with an operator
    if expression and expression[-1] in "+-*/":
        suggestions.append("Expression ends with an operator — did you forget a number?")

    # Rule 4: Repetitive operators reduction
    # if re.search(r'[\+\-\*\/]{2,}', expression):
    #     corrected_expr = re.sub(r'[\+\-\*\/]{2,}', lambda m: m.group(0)[0], expression)
    #     if corrected_expr != expression:
    #         suggestions.append(f"Did you mean {corrected_expr}?")

    # Rule 5: Unbalanced parentheses
    if expression.count('(') > expression.count(')'):
        suggestions.append("Missing closing parenthesis.")
    elif expression.count(')') > expression.count('('):
        suggestions.append("Missing opening parenthesis.")

    # Rule 6: Empty parentheses
    if "()" in expression:
        suggestions.append("Empty parentheses detected — did you mean something else?")

    # Rule 7: Unclosed opening parenthesis (redundant but can remain for clarity)
    if '(' in expression and ')' not in expression:
        suggestions.append("Unclosed parentheses detected.")

    # Rule 8: Operator spacing issue
    if re.search(r'[+\-*/]\s+[+\-*/]', expression):
        suggestions.append("Unexpected operator placement — did you mean a different operation?")

    # Rule 9: Things like `3*+2`
    corrected_expr = re.sub(r'([*/+-])\+', r'\1', expression)
    if corrected_expr != expression:
        suggestions.append(f"Did you mean {corrected_expr}?")

    return list(set(suggestions))  # Remove duplicates
