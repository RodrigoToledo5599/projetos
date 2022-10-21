class nubanco:
    

    def __init__(self):
        self.saldo = None
        self.deposito = None
        self.notas= {"q100":0,"q50":0,"q20":0,"q10":0,"q5":0,"q2":0,"q1":0} 
        self.historico = []
        self.saque =None
 

    def sacarDinheiro(self,*var):
        self.saque = int(input("valor do saque: "))
        if self.saque<0:
            self.dash.changelabel("proibido saque com valores negativos")
        else:
            self.saldo =nubanco._calcsaldo(self.saldo,self.historico)

            if self.saque>self.saldo:
                print("saldo insuficiente\n")
                
            else:
                self.historico.append(-self.saque)
                self.notas["q100"] = int(self.saque/100)
                self.saque = self.saque - self.notas["q100"]*100
                self.notas["q100"] = str(self.notas["q100"])    
                    
                self.notas["q50"] = int(self.saque/50)
                self.saque = self.saque - self.notas["q50"]*50
                self.notas["q50"] = str(self.notas["q50"])
                    
                self.notas["q20"] = int(self.saque/20)
                self.saque = self.saque - self.notas["q20"]*20
                self.notas["q20"] = str(self.notas["q20"])

                self.notas["q10"] = int(self.saque/10)
                self.saque = self.saque - self.notas["q10"]*10
                self.notas["q10"] = str(self.notas["q10"])

                self.notas["q5"] = int(self.saque/5)
                self.saque = self.saque - self.notas["q5"]*5
                self.notas["q5"] = str(self.notas["q5"])

                self.notas["q2"] = int(self.saque/2)
                self.saque = self.saque - self.notas["q2"]*2
                self.notas["q2"] = str(self.notas["q2"])

                self.notas["q1"] = int(self.saque/1)
                self.saque = self.saque - self.notas["q1"]*1
                self.notas["q1"] = str(self.notas["q1"])

                var = str(self.notas)
                
                print(var)
    
    
    def depositarDinheiro(self):
        
        self.deposito = int(input("valor do deposito: "))
        if self.deposito <0:
            print("impossivel depositar valores negativos")
        else:
            self.historico.append(self.deposito)
            
    def mostrar_historico(self):
        print(str(self.historico)) 
    

    def mostrar_saldo(self):
        print(nubanco._calcsaldo(self.saldo,self.historico))


    def _calcsaldo(var,iterable=[]): 
        var = 0
        for i in range(0,len(iterable)):
            var += iterable[i]
        return var








