def sumar (*args):
    total = 0
    for arg in args:
        total += arg
    return total
#   return sum(args)

print(sumar(5,20,6,10))
