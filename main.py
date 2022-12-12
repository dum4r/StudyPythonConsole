# Dumar Ruiz Utadeo
import os

class Scenes:
  def __init__(self, index,label, desc, func):
    self.index=index; self.label=label; self.desc=desc; self.func=func

class Program:
  label ="===> FullStack Ejercicios Python <==="
  blnRun = True
  index=0
  scenes={}

  def __init__(self,*s):
    for x in s:
      self.scenes.update({x.index: x}) 
    self.run()

  def run(self):
    while self.blnRun:
      os.system('cls')
      print(self.label)
      self.ejercicio()
    print("Chauu :c")
  
  def end(self):
    self.blnRun=False 

  def ejercicio(self):
    print(self.scenes[self.index].label)
    self.scenes[self.index].func(self)
    
  def volver(self):
    n=input(f"99 -para volver al Menu. \nEnter para repetir...")
    if n=="99":
      self.index=0

def main():
  def funcS0(self):
    for i,s in self.scenes.items():
      print(f"{i} --{s.label}")
    self.index=int(input("Ingresa el numero del ejercicio: "))
  
  def funcS1(self):
    m=int(input("Ingresa el numero de la multiplicacion: "))
    for i in range(10):
      print(f"{m} x {i+1}= {int(m*(i+1))}")
    self.volver()
  
  def funcS2(self):
    def order(string):
      return "".join(list(string).sort())
    p1=input("Ingresa Palabra 1: ").lower()
    p2=input("Ingresa Palabra 2: ").lower()
    tmp_p1 = list(p1)
    tmp_p2 = list(p2)
    tmp_p1.sort()
    tmp_p2.sort()
    print(f"*** {(order(tmp_p1) == order(tmp_p2))} ***")
    self.volver()

  def funcS3(self):
    def mcd(x, y):
      if(y==0):
        return x
      else:
        return mcd(y,x%y)

    def mcm(x, y):
      return (x * y) / mcd(x, y)

    print("El máximo común divisor de dos números")
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    print(f"Máximo común divisor:{mcd(n1,n2)}")
    print("================================")
    print("El mínimo común múltiplo de dos números")
    m1=int(input("Ingrese el primer numero: "))
    m2=int(input("Ingrese el segundo numero: "))
    print(f"mínimo común múltiplo:{mcm(m1,m2)}")
    self.volver()

  def funcS4(self):
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    mn=min(n1,n2)
    mmn=max(n1,n2)
    for n in  range(mn,mmn):
      count = 0
      for i in range(2, (n//2 + 1)):
        if(n % i == 0):
          count = count + 1
          break
      if (count == 0 and n != 1):
        print(f" {n}")
    self.volver()

  def funcS5(self):
    def is_int(str) -> bool:
      try:
        float(str)
        return True
      except ValueError:
        return False
    phase=input("Ingresar oracion: ")
    tmp = phase.split(" ")
    arrTrue=[]
    for i in tmp:
      bln=False
      for j in i:
        if is_int(j):
          bln=True
          break
      if bln:
        arrTrue.append(i)
    print(arrTrue)
    self.volver()

  def funcEnd(self):
    self.end()
  
  Program(
    Scenes(0,"- Menu Principal","Escribe un numero porfa U.U", funcS0),
    Scenes(1,"- Tabla de Multiplicar","Crear un programa que devuelva la tabla de multiplicar dependiendo del numero que seleccione el usuario.", funcS1),
    Scenes(2,"- Anagramas", "Devuelve True/False: dos cadenas son anagramas.", funcS2),
    Scenes(3,"- Max como un divisor", "Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.", funcS3),
    Scenes(4,"- Numeros Primos","Escriba un programa que muestre los números primos entre 2 números.", funcS4),
    Scenes(5,"- Numeros entre palabras","Encuentre las palabras que tienen numero .", funcS5),
    Scenes(99," Salir","", funcEnd)
    )

if __name__ == '__main__':
  main()