a = int(input('Primeiro número'))
b = int(input('Segundo número'))
c = int(input('Terceiro número'))

d = b*b-4*a*c
x= (-b - (d) **(1/2)/(2*a))
x1 = (-b + (d)**(1/2)/(2*a))
print('x1 = {}, x2 = {}'.format(x1, x))

if (a == 0) and (b == 0) and (c != 1):
    print("Solução impossível")
    

    