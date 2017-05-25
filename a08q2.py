##
## *********************************
## Ayaan Mansoor Pal 
## *********************************
##

import check

## Important constants and statements:
not_prime="{0}={1}"
prime="{0} is prime"

## is_prime(num) consumes a number and return False if it is not prime
## and True if it is prime.
## is_prime: Nat -> Bool

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

## prime_list(n) consumes a number n and produces a list of prime numbers
## that n is divisible by.
## prime_list: Nat -> (listof Nat)

def prime_list(n):
    prime_list=[]
    for i in range(2,n):
        if n%i==0 and is_prime(i)==True:
            prime_list.append(i)
    return prime_list

## factorize_list(n,prime_list) consumes a number n and its list of primes,
## prime_list and produces a list which holds the prime factorization of n
## (including repetitions).
## factorize_list: Nat (listof Nat) -> (listof Str)
            
def factorize_list(n,prime_list):
    rem=n
    factorizing_list=[]
    while rem !=0 and rem !=1:
        for n in prime_list:
            if rem%n==0:
                factorizing_list.append(n)
                rem=rem//n
            else:
                rem=rem
    factorizing_list.sort()
    new_list=[]
    for i in factorizing_list:
        num=str(i)
        new_list.append(num)
    return new_list

## factorize(n) consumes a natural number n and produces a dictionary
## which represents its prime factorization where each key corresponds to
## the prime factor and the associated value is the number of times it
## appeared. Also the basic multiplication statement is printed using the
## primes.If n is prime then a statement saying it is prime is printed.
## Effects: the basic multiplication statement is printed using the primes
##          where the primes are in increasing order.
##          If it is prime then "# is prime" is printed where "#" is the prime
## factorize: Nat -> (dictof Nat Nat)
## requires: n>=2
## Examples:
## factorize(2) => {2:1} and "2 is prime" is printed.
## factorize(10) => {2:1,5:1} and "2*5=10" is printed.
## factorize(5) => {5:1} and "5 is prime" is printed.

def factorize(n):
    if is_prime(n)==True:
        factor_dict={n:1}
        print(prime.format(n))
        return factor_dict
    else:
       primes=prime_list(n)
       factors=factorize_list(n,primes)
       statement="*".join(factors)
       print(not_prime.format(statement,n))
       factor_dict={}
       for i in factors:
          counter=factors.count(i)
          factor_dict[int(i)]=counter
       return factor_dict

## Tests:
## Test 1:
n=2
check.set_screen(prime.format(n))
check.expect("Q2T01",factorize(n),{2:1})
## Test 2:
n=10
check.set_screen(not_prime.format("2*5",n))
check.expect("Q2T02",factorize(n),{5:1,2:1})
## Test 3:
n=100
check.set_screen("2*2*5*5=100")
check.expect("Q2T03",factorize(n),{5:2,2:2})
## Test 4:
n=3333
check.set_screen(not_prime.format("3*11*101",n))
check.expect("Q2T04",factorize(n),{3:1,11:1,101:1})
## Test 5:
n=101
check.set_screen(prime.format(n))
check.expect("Q2T05",factorize(n),{101:1})
## Test 6:
n=40157
check.set_screen(not_prime.format("13*3089",n))
check.expect("Q2T06",factorize(n),{13:1,3089:1})
## Test 7:
n=3089
check.set_screen(prime.format(n))
check.expect("Q2T07",factorize(n),{3089:1})
## Test 8:
n=204973
check.set_screen(prime.format(n))
check.expect("Q2T08",factorize(n),{204973:1})
## Test 9:
n=134567
check.set_screen(not_prime.format("53*2539",n))
check.expect("Q2T09",factorize(n),{53:1,2539:1})
## Test 10:
n=120
check.set_screen(not_prime.format("2*2*2*3*5",n))
check.expect("Q2T10",factorize(n),{2:3,3:1,5:1})
## Test 11:
n=4325265
check.set_screen(not_prime.format("3*3*3*5*7*23*199",n))
check.expect("Q2T11",factorize(n),{3:3,5:1,7:1,23:1,199:1})


        
    








