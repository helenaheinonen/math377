import matplotlib
import matplotlib.pyplot as plt
import math
import random
import sys
import logging
import numpy as np


def congruent(x, a, p):
    # returns true if x = a mod p, false otherwise
    x = x % p
    a = a % p
    if (x == a):
        return True
    else:
        return False




def rootModP(a, p):
    #returns a list of the roots of a mod p
    ls = legendreSymbol(a, p)
    roots = []
    if ls == -1 or ls == 0:
        return roots
    else:
        for i in range(0, p):
            if ((i*i - a)%p == 0):
                roots.append(i)

        return roots

    
def legendreSymbol(a, p):
    # returns the legendre symbol of a mod p 
    a = int(a)
    p = int(p)
    dummy = int((p-1)/2) 
    ls = pow(a, dummy) % p
    if ls == p - 1:
        return -1       
    else:
        return ls

def cauchySequence(a, p, d):
    # find the first d digits of square root of a in the p-adic expansion
    ls = legendreSymbol(a, p)
    
    if ls == -1 or ls == 0:
            print("no pAdic solution exists")
    else:
        rootsModP = rootModP(a, p)
        for x in rootsModP:
            
            digits = [x]
            a_n = x
            if (2*x % p) == 0:
                print("Fails Hensel's lemma")
            else:
                for n in range(1, d): 
                    k = 0
                    while (k <= p-1):
                        temp = a_n + k*(p**n)
                        
                        if congruent(temp**2, a, p**(n+1)):
                            a_n = temp
                            digits.append(k)
                            break
                        k += 1
            print(digits)
            



def main(a, p, d):
    #p is the prime p
    #a is the number we are taking square root of
    #d is the number of digits to obtain
    p = int(p)
    a = int(a)
    d = int(d)
    cauchySequence(a, p, d)



if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"""
usage: python3 {sys.argv[0]} <rational a> <prime p> <digits d>

arguments:
    rational    rational number a to take the square root of
    prime       which p-adic prime you want to consider
    digits      number of digits of the p-adic square root of a you want to produce
""")
        sys.exit(1) 
    p = int(sys.argv[2])
    d = int(sys.argv[3])
    if ((math.factorial(p-1)) % p != (-1 + p)):
        print(f"error '{sys.argv[2]}' is not prime")
        sys.exit(1)
    a = int(sys.argv[1])
    main(a, p, d)
    
    

