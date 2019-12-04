class MarsRover:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__direction = 'E'

    def run(self):
        return '%s %s %s' % (self.__x, self.__y, self.__direction)
