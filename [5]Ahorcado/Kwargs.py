def suma(**kwargs):
    total=0
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total+=valor
    return total
print(suma(x=3,y=5,z=2))



def prueba(num1,num2,*args,**kwargs):
    print(f'el primer valor es: {num1}')
    print(f'el segundo valor es: {num2}')

    for arg in args:
        print(f'arg es: {arg}')

    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')


# prueba(15,20,30,40,1035,45250,'r',30,x='UNO', y='DOS', z='TRES')
args= [100,200,300]
kwargs={
    'x':'uno',
    'y':'dos',
    'z':'tres'
}
prueba(7,77, *args,**kwargs)