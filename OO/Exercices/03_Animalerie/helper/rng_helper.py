import random

class RngHelper():

    @staticmethod
    def proba(chance):

        if chance >= 100:
            return True

        return (random.random() * 100) < chance
    

if __name__ == '__main__':

    # print("10%")
    # for i in range(10):
    #     print(RngHelper.proba(10))
    # print()

    # print("80%")
    # for i in range(10):
    #     print(RngHelper.proba(80))
    # print()

    value = 0.5
    print(f"{value}%")
    count = 0
    nb_try = 100000
    for i in range(nb_try):
        if(RngHelper.proba(value)):
            count += 1
    print(f"Résultat = {count}/{nb_try}")