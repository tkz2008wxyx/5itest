class Human(object):
    def run(self):
        print('he is running')


if __name__ == '__main__':
    human = Human()
    myfunc = getattr(human,'run')
    myfunc()
