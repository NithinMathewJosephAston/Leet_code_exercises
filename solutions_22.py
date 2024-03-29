# Singleton pattern
class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


if __name__ == '__main__':
    s = Singleton.getInstance()
    print(s)

    s2 = Singleton.getInstance()
    print(s2)
