import re

# Token types
TOKEN_SPECIFICATION = [
    ('NUMBER', r'\d+'),         # Integer
    ('ADD', r'\+'),             # Addition
    ('SUB', r'-'),              # Subtraction
    ('MUL', r'\*'),             # Multiplication
    ('DIV', r'/'),              # Division
    ('LPAREN', r'\('),          # Left Parenthesis
    ('RPAREN', r'\)'),          # Right Parenthesis
    ('SKIP', r'[ \t]+'),        # Skip spaces
    ('MISMATCH', r'.'),         # Any other character (error)
]

TOKEN_REGEX = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in TOKEN_SPECIFICATION)

def tokenize(expression):
    tokens = []
    for match in re.finditer(TOKEN_REGEX, expression):
        kind = match.lastgroup
        value = match.group()
        if kind == 'NUMBER':
            tokens.append(('NUMBER', int(value)))
        elif kind in ('ADD', 'SUB', 'MUL', 'DIV', 'LPAREN', 'RPAREN'):
            tokens.append((kind, value))
        elif kind == 'SKIP':
            continue
        else:
            raise SyntaxError(f'Unexpected token: {value}')
    return tokens
