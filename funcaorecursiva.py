def fibonacci(i, b=0, c=1):

    if i != 0:                  
        print(b, end='->')
        b = b + c               
        c = b - c               
        fibonacci(i-1, b=b, c=c)   
        return 'FIM'


print(fibonacci(int(input('Quantos termos vc quer mostrar: '))))