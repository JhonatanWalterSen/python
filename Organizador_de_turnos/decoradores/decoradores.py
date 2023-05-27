def decorar_saludo(function):

    def otra_funcion(palabra):
        print('Hola')
        function(palabra)
        print('adios')
    return otra_funcion

def mayusculas(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

mayusculas_decorada =decorar_saludo(mayusculas)
mayusculas_decorada('PEDOOO')