from os import system


class Ext1:
    def __init__(self, supervisord, args):
        self.supervisord = supervisord
        self.args = args

    def add(self, num1: int, num2: int):
        return num1 + num2

    def ls(self):
        return system('ls')


def ext1(supervisord, **args):
    return Ext1(supervisord, args)
