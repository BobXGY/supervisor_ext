from os import system


class Ext1:
    def __init__(self, supervisord):
        self.supervisord = supervisord

    def add(self, num1: int, num2: int):
        return num1 + num2

    def ls(self):
        return system('ls')

    def hello(self):
        return 'hello'


def myext(supervisord):
    return Ext1(supervisord)
