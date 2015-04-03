class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        self.x += v.x
        self.y += v.y

    def sub(self, v):
        self.x -= v.x
        self.y -= v.y

    def mult(self, v):
        self.x *= v.x
        self.y *= v.y

    def div(self, v):
        self.x /= v.x
        self.y /= v.y
