import ast
import operator

operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}

def eval_expr(expr):
    try:
        tree = ast.parse(expr, mode='eval')
        return eval_node(tree.body)
    except Exception as e:
        return f"Ошибка: недопустимое выражение ({e})"

def eval_node(node):
    if isinstance(node, ast.BinOp):
        left = eval_node(node.left)
        right = eval_node(node.right)
        op_type = type(node.op)
        if op_type in operators:
            return operators[op_type](left, right)
        else:
            raise ValueError("Недопустимая операция.")
    elif isinstance(node, ast.UnaryOp):
        operand = eval_node(node.operand)
        op_type = type(node.op)
        if op_type in operators:
            return operators[op_type](operand)
        else:
            raise ValueError("Недопустимая унарная операция.")
    elif isinstance(node, ast.Constant):  
        return node.value
    else:
        raise ValueError("Недопустимое выражение.")

def main():
    print("Интерактивный калькулятор (введите 'выход' для завершения)")
    while True:
        expr = input("Введите выражение: ")
        if expr.lower() == 'выход':
            print("До свидания!")
            break
        result = eval_expr(expr)
        print(f"Результат: {result}")

if __name__ == "__main__":
    main()
