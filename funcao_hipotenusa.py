import math

def quadrado(n):
    return n**2

def soma(n1,n2):
    n = n1 + n2
    return n

def hipotenusa(x,y):
    hipo = math.sqrt(soma(quadrado(x), quadrado(y)))
    return hipo

def main():
	
    print("funcao chamada hipotenusa que retorna o comprimento da hipotenusa de um triangulo retangulo dados os comprimentos dos dois lados como parametros")		
    lado_1 = input('lado 1: ')
    lado_2 = input('lado 2: ')
    print 'Hipotenusa: ',hipotenusa(lado_1, lado_2)
    
if __name__ =='__main__':
    main()
