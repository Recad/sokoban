class Puntos(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
    	return self.x

    def getY(self):
    	return self.y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Puntos(x, y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return str(self.x) + ', ' + str(self.y)

    def double(self):
        return Puntos(self.x * 2, self.y * 2)