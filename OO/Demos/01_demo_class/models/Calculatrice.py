class Calculatrice:
    
    def __init__(self):
        self.result = 0
        self.a = 2
        self.A = 3

    def sum(self, nb1, nb2):
        self.result = nb1 + nb2
        return self.result

def helloWorld():
    print('Hello World !')