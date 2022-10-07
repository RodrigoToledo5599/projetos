def _calcsaldo(var,iterable=[]): 
            var = 0
            for i in range(0,len(iterable)):
                var += iterable[i]
            return var  

class banco:
    
    def __init__(self):
        
        self.saldo = 0
        self.deposito =0
        self.notas= {"q100":0,"q50":0,"q20":0,"q10":0,"q5":0,"q2":0,"q1":0} 
        self.historico = []
        self.saque =0

    def sacarDinheiro(self):
        self.saque = int(input("valor do saque: "))
        if self.saque<0:
            print("proibido saque com valores negativos")
        else:
            self.saldo =_calcsaldo(self.saldo,self.historico)

            if self.saque>self.saldo:
                print("saldo insuficiente\n")
                
            else:
                self.historico.append(-self.saque)

                self.notas["q100"] = int(self.saque/100)
                self.saque = self.saque - self.notas["q100"]*100
                    
                self.notas["q50"] = int(self.saque/50)
                self.saque = self.saque - self.notas["q50"]*50
                    
                self.notas["q20"] = int(self.saque/20)
                self.saque = self.saque - self.notas["q20"]*2

                self.notas["q10"] = int(self.saque/10)
                self.saque = self.saque - self.notas["q10"]*10

                self.notas["q5"] = int(self.saque/5)
                self.saque = self.saque - self.notas["q5"]*5

                self.notas["q2"] = int(self.saque/2)
                self.saque = self.saque - self.notas["q2"]*2

                self.notas["q1"] = int(self.saque/1)
                self.saque = self.saque - self.notas["q1"]*1

                print("notas de 100: ",self.notas["q100"])
                print("notas de 50: ",self.notas["q50"])
                print("notas de 20: ",self.notas["q20"])
                print("notas de 10: ",self.notas["q10"])
                print("notas de 5: ",self.notas["q5"])
                print("notas de 2: ",self.notas["q2"])
                print("notas de 1: ",self.notas["q1"])
                print("\n\n")

    def depositarDinheiro(self):
        
        self.deposito = int(input("valor do deposito: "))
        if self.deposito <0:
            print("impossivel depositar valores negativos")
        else:
            self.historico.append(self.deposito)
            
    def mostrar_historico(self):
        print(self.historico)

    def mostrar_saldo(self):
        print(_calcsaldo(self.saldo,self.historico))


    