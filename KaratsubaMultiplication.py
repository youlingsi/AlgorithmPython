# Karasuba Algorythm to compute muitiplication between 2 numbers with the same n of digits
# during recursive call, the digits of the factors are always the same (ac has the same number of digits)

x = 12345
y = 12423

def kara(x, y):
    n = len(str(x))
    if n == 1:
       return x * y
    else:
        if n % 2 == 0:
            a = int(x / 10**(n / 2)) 
            c = int(y / 10**(n / 2))
            b = x - a * 10 **(n / 2)
            d = y - c * 10 **(n / 2)
            print a, b, c, d
            return 10**n*(kara(a, c)) + 10**(n/2)*(kara((a + b), (c + d)) - kara(a, c) - kara(b, d)) + kara(b, d)
        else:
            a = int(x / 10 ** ((n + 1) / 2)) 
            c = int(y / 10 ** ((n + 1) / 2))
            b = x - a * 10 ** ((n + 1) / 2)
            d = y - c * 10 ** ((n + 1) / 2)
            return 10**(n+1)*(kara(a, c)) + 10**((n+1)/2)*(kara((a + b), (c + d)) - kara(a, c) - kara(b, d)) + kara(b, d)            

print kara(x, y)