def evaluate(node):
    if node.type == 'Number':
        return node.value
    elif node.type == 'ADD':
        return evaluate(node.left) + evaluate(node.right)
    elif node.type == 'SUB':
        return evaluate(node.left) - evaluate(node.right)
    elif node.type == 'MUL':
        return evaluate(node.left) * evaluate(node.right)
    elif node.type == 'DIV':
        return evaluate(node.left) / evaluate(node.right)
    raise ValueError(f"Unknown node type: {node.type}")
