# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


class Circle(object):
    pi = 3.14
    def __init__(self, radius = 1):
        self.radius = radius

    #method
    def get_circumf(self):
        return self.radius * self.pi * 2


if __name__ == '__main__':
    print_hi('PyCharm')
    my_circle = Circle(30)
    print(my_circle.pi)
    print(my_circle.get_circumf())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/