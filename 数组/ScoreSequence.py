class GameEntry:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def getName(self):
        return self._name

    def getScore(self):
        return self._score

    def __str__(self):
        return "({0},{1})".format(self._name, self._score)


class ScoreBoard:
    def __init__(self, capacity=10):
        self._board = [None] * capacity
        self._n = capacity

    def __getitem__(self, j):
        return self._board[j]

    def __str__(self):
        return "\n".join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        score = entry.getScore()

        good = self._n < len(self._board) or score > self._board[-1].getScore()
        if good:
            if self._n < len(self._board):
                self._n += 1
            j = self._n - 1
            while j > 0 and self._board[j - 1] < score:
                self._board[j] = self._boar[j - 1]
                j -= 1
            self._board[j] = entry

