class MarsRover:
    def __init__(self, info=None):
        if info:
            status = info.split(' ')
            self.__x = int(status[0])
            self.__y = int(status[1])
            self.__direction = status[2]
        else:
            self.__x = 0
            self.__y = 0
            self.__direction = 'E'

    def run(self, command=None):
        if command == 'M':
            if self.__direction == 'E':
                self.__x += 1
            elif self.__direction == 'W':
                self.__x -= 1
        return '%s %s %s' % (self.__x, self.__y, self.__direction)
