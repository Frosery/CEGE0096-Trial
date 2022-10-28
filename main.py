# complete the code

class TrafficLight:
    def __init__(self):
        self.__red = False
        self.__orange = False
        self.__green = False
        self.tracker = True

    def next_state(self):
        result = ''
        if self.__green:
            self.__green = False
            self.__orange = True
            result = 'Orange is on!'
        elif self.__orange:
            self.__orange = False
            if not self.tracker:
                self.__red = True
                self.tracker = True
                result = 'Red is on!'
            else:
                self.__green = True
                self.tracker = False
                result = 'Green is on!'
        elif self.__red:
            self.__red = False
            self.__orange = True
            result = 'Orange is on!'
        else:
            self.__green = True
            result = 'Green is on!'
        return result

    def get_state(self):
        return 'Green light is {}. Orange light is {}. Red light is {}.'.format(self.__green, self.__orange, self.__red)


class ResettableTrafficLights(TrafficLight):
    def reset(self):
        self.__green = False
        self.__orange = False
        self.__red = False
        return 'Green light is {}. Orange light is {}. Red light is {}.'.format(self.__green, self.__orange, self.__red)


if __name__ == '__main__':
    lights = ResettableTrafficLights()
    print(lights.next_state())
    print(lights.next_state())
    print(lights.next_state())
    print(lights.next_state())
    print(lights.next_state())
    print(lights.next_state())
    print(lights.next_state())
    print(lights.next_state())
    print(lights.next_state())
    print(lights.get_state())
    print(lights.reset())





