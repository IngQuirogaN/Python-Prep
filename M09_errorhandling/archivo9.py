class funciones_lista:
    def __init__(self,lista):
        if (type(lista)!=list):
            raise ValueError('El objeto ingresado no es una lista') 
        self.lista=lista


    def lista_primo(self):
        for i in self.lista:
            if (self.primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')

    def lista_grados(self, origen, destino):
        lista_respuesta=[]
        for i in self.lista:
            lista_respuesta.append(self.convert_grados(i,origen,destino))
        return lista_respuesta
    
    def lista_factorial(self):
        lista_respuesta=[]
        for i in self.lista:
            lista_respuesta.append(self.factorial(i))
        return lista_respuesta

    def primo(self,numero):
        lista_respuesta=[]
        self.numero=numero
        self.primoflag=0
        for i in range(2,self.numero):
            if numero%i==0:
                self.primoflag =1
        if self.primoflag==0:
            lista_respuesta.append(True)
        else:
            lista_respuesta.append(False)
        
        return lista_respuesta
        
    def contar_repetido(self):
        self.contador_max=0
        self.contador=0
        self.valor=0
        for elemento in self.lista:
            self.contador=self.lista.count(elemento)
            if self.contador>self.contador_max:
                self.contador_max=self.contador
                self.valor=elemento
        return self.valor,self.contador_max
    
    def convert_grados(self,valor,med_origen,med_destino):
        self.valor = valor
        self.med_origen = med_origen
        self.med_destino = med_destino
        if self.med_origen=='F':
            if self.med_destino == 'C':
                return ((self.valor-32)/(9/5))
            if self.med_destino == 'K':
                return ((self.valor-32)/(9/5)+273.15)
            if self.med_destino == 'F':
                return self.valor
    
        if self.med_origen=='C':
            if self.med_destino == 'F':
                return (self.valor*(9/5)+32)
            if self.med_destino == 'K':
                return (self.valor+273.15)
            if self.med_destino == 'C':
                return self.valor

        if self.med_origen=='K':
            if self.med_destino == 'C':
                return (self.valor-273.15)
            if self.med_destino == 'F':
                return (((self.valor-273.15)*(9/5))+32)
            if self.med_destino == 'K':
                return self.valor
            
    def factorial(self,numero):
        self.numero=numero
        self.resultado=1
        if type(self.numero)!=int:
            print('El numero debe ser entero')
            return
        elif self.numero<0:
            print('El numero debe ser positivo')
            return
        if  self.numero>1:
            self.resultado=self.numero*self.factorial(self.numero-1)
        else:
            return self.numero
        return self.resultado
    
    