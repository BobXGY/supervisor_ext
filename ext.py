from os import system


class Ext1:
    def __init__(self, supervisord, config):
        self.supervisord = supervisord
        self.args = config

    def add(self, num1: int, num2: int):
        return num1 + num2

    def ls(self):
        return system('ls')

    def hello(self):
        return 'hello'


def myext(supervisord, **config):
    retries = int(config.get('retries', 0))
    ext1 = Ext1(supervisord, retries)
    return ext1
