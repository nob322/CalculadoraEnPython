#Implementar una clase Calculadora que defina los métodos:
#Sumar, Restar, Multiplicar y Dividir
#En lo posible realice tratamiento de excepciones.
#Crear a continuación un programa que pruebe la clase Calculadora
class Calculadora:
    def sumar(self,num1,num2):
        return num1 + num2
    def restar(self,num1,num2):
        return num1,num2
    def multiplicar(self,num1,num2):
        return num1 * num2
    def dividir(self,num1,num2):
        try:
             return num1 // num2
        except ZeroDivisionError:
            print("Usted ha dividido por cero y eso no se puede hacer.")
calculadora = Calculadora()
print("Bienvenido a la calculadora...")
def menu():
    print("||||||||||||||||||||")
    print("Elija una opción:")
    print("1-Sumar")
    print("2-Restar")
    print("3-Multiplicar")
    print("4-Dividir")
    print("||||||||||||||||||||")
    decision = int(input("Ingrese la operación que desea realizar: "))
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    if decision == 1:
        print("El resultado de la operación es: ",calculadora.sumar(num1,num2))
    elif decision == 2:
        print("El resultado de la operación es: ",calculadora.restar(num1,num2))
    elif decision == 3:     
        print("El resultado de la operación es: ",calculadora.multiplicar(num1,num2))
    else:
         print("El resultado de la operación es: ",calculadora.dividir(num1,num2))
        
menu()         