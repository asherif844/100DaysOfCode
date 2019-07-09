prime = []
for number in range(-5,100):
    if number < 3:
        pass
    
    elif number>1:
        for i in range(2,number):
            if number % i ==0:
                break
        else:
            prime.append(number)
