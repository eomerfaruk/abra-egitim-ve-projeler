



class BankaHesabi:

    def __init__(self  , hesabsahibi):

        self.hesabsahip = hesabsahibi
        self.bakiye = 0.0


    def parayatir(self , miktar):
        self.bakiye += miktar
        return self.bakiye

    def paracek(self , miktar):

        self.bakiye -= miktar 
        if self.bakiye < 0 :
            print(" bu miktarda para cekilemez")
            self.bakiye += miktar
            return 0

        else:
            return self.bakiye

            

if __name__ == '__main__':

    hesap = BankaHesabi("omer")
    hesap.parayatir(10000)
    print(hesap.bakiye)

    hesap.paracek(23000003)
    print(hesap.bakiye)
