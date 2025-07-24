print('Mathhelper Imported')



def give_fibo(n):
    fibo = [0,1]
    for i in range(n-2):
        last_num = fibo[-1]
        second_last_num = fibo[-2]
        next_num = last_num + second_last_num
        fibo.append(next_num)
    return fibo  



def check_prime(number):
    for i in range (2,number):
        if number%1 == 0:
            return 'not a prin no.'
            break
    else:
        return 'prime number'
        
        
        
def check_prime(number):
    for i in range (2,number):
        if number%1 == 0:
            return 'not a prin no.'
            break
    else:
        return 'prime number'
        
        