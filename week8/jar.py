class Jar:
    def __init__(self, capacity=12):
        if not (isinstance(capacity, int) and capacity >= 0):
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        cookies = ""
        for _ in range(int(self.size)):
            cookies += "🍪"

        return cookies

    def deposit(self, n):
        if (self._size + n > self._capacity):
            raise ValueError
        self._size += n


    def withdraw(self, n):
        if (self._size < n):
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
