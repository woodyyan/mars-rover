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
        if command:
            demands = list(command)
            for demand in demands:
                self.__execute(demand)
        return '%s %s %s' % (self.__x, self.__y, self.__direction)

    def __execute(self, command):
        if command == 'M':
            self.__move()
        elif command == 'L':
            self.__turn_left()
        elif command == 'R':
            self.__turn_right()

    def __turn_right(self):
        if self.__direction == 'E':
            self.__direction = 'S'
        elif self.__direction == 'S':
            self.__direction = 'W'
        elif self.__direction == 'W':
            self.__direction = 'N'
        elif self.__direction == 'N':
            self.__direction = 'E'

    def __turn_left(self):
        if self.__direction == 'E':
            self.__direction = 'N'
        elif self.__direction == 'N':
            self.__direction = 'W'
        elif self.__direction == 'W':
            self.__direction = 'S'
        elif self.__direction == 'S':
            self.__direction = 'E'

    def __move(self):
        if self.__direction == 'E':
            self.__x += 1
        elif self.__direction == 'W':
            self.__x -= 1
        elif self.__direction == 'N':
            self.__y += 1
        elif self.__direction == 'S':
            self.__y -= 1
