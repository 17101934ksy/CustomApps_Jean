import shutil


class Variable:
    def __init__(self,name):
        self.name=name

    def name(self,name):
        self.name=name
    def pt(self):
        print(self.name)


if __name__ == '__main__':
    a= Variable()
    a.name("seyun")
    a.pt()

