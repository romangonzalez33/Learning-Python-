print("gestor de numeros")
n1=int(input("ingrese un numero: "))
n2=int(input("ingrese otro numero: ")) 
n3=int(input("ingrese otro numero: "))
def mayor(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        print(f"el numero mayor es {n1}")
    elif n2>=n1 and n2>=n3:
        print(f"el numero mayor es {n2}")
    else:
        print(f"el numero mayor es {n3}")
def menor(n1,n2,n3):
    if n1<=n2 and n1<=n3:
        print(f"el numero menor es {n1}")
    elif n2<=n1 and n2<=n3:
        print(f"el numero menor es {n2}")
    else:
        print(f"el numero menor es {n3}")

def promedio(n1,n2,n3):
    prom=(n1+n2+n3)/3
    print(f"el promedio es {prom}")

def suma(n1,n2,n3):
    suma=n1+n2+n3
    print(f"la suma es {suma}")

while True: 
    print("opcion: ")
    print("1. numero mayor")
    print("2. numero menor")
    print("3. promedio")
    print("4. suma")
    print("5. salir")
    opcion=int(input("ingrese una opcion: "))
    if opcion==1:
        mayor(n1,n2,n3)
    elif opcion==2:
        menor(n1,n2,n3)
    elif opcion==3:
        promedio(n1,n2,n3)
    elif opcion==4:
        suma(n1,n2,n3)
    elif opcion==5:
        print("gracias por usar el programa")
        break       
        