import random

class Toad:
    def __init__(self, is_trustworthy):
        self.truthful: bool = bool(int(is_trustworthy))
    def is_trustworthy(self):
        return self.truthful
    def tell_about(self,toad):
        b_trustworthy= toad.is_trustworthy()
        if(self.is_trustworthy()):
            return b_trustworthy
        else:
            r = random.random()
            if(r<0.5):
                return True
            else:
                return False

def main():
    
    toad = Toad(True)
    print(toad.is_trustworthy())
    toadq = Toad(False)
    print(toadq.tell_about(toad))



if __name__ == "__main__":
    main()