from LinkedBTree import LinkedBinaryTree
from StackAndQueue.stack import ArrayStack


class ExpressionTree(LinkedBinaryTree):
    def __init__(self, token, left=None, right=None):
        super().__init__()
        if not isinstance(token, str):
            raise ValueError("Token must be a string")
        self._add_root(token)
        if left is not None:
            if token not in "+-/*x":
                raise ValueError("Token must be a operator")
            self.attach(self.root(), left, right)

    def _parenthesize_recur(self, p, result):
        if self.is_leaf(p):
            result.append(p.element())
        else:
            result.append("(")
            self._parenthesize_recur(self.left(p), result)
            result.append(p.element())
            self._parenthesize_recur(self.right(p), result)
            result.append(")")

    def __str__(self):
        result = []
        self._parenthesize_recur(self.root(), result)
        return "".join(result)

    def _evaluate_recur(self, p):
        if self.is_leaf(p):
            return float(p.element())
        else:
            op = p.element()
            left = self._evaluate_recur(self.left(p))
            right = self._evaluate_recur(self.right(p))
            if op == "+":
                return left + right
            elif op == "-":
                return left - right
            elif op == "/":
                return left / right
            else:
                return left * right

    def evaluate(self):
        return self._evaluate_recur(self.root())

    @classmethod
    def build_expression_tree(self, tokens):
        S = ArrayStack()
        for t in tokens:
            if t in "+-*/x":
                S.push(t)
            elif t not in "()":
                S.push(ExpressionTree(t))
            elif t == ")":
                right = S.pop()
                op = S.pop()
                left = S.pop()
                S.push(ExpressionTree(op, left, right))
        return S.pop()


if __name__ == "__main__":
    tree1 = ExpressionTree.build_expression_tree("(((3+1)*4)/((9-5)+2))")
    print(tree1, " = ", tree1.evaluate())

