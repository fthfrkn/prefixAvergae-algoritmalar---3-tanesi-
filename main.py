import time
import random

MAX_NUMBER = 2500

def prefix_average(S):

    A = [0 for x in range(len(S))]    

    for j in range (0, len(S)):      		
        total = 0                     

        for i in range (0, j+1):	    
            total = total + S[i]   

        A[j] = total/(j+1)          
        if j%1000 == 0:
            print (".", end="")
        if j%10000 == 0:
            print (f"\nIteration: {j} \n")
    
    print("")
    return A                            


def prefix_average2(S):

    A = [0 for x in range(len(S))]    	

    for j in range (0, len(S)):      		 
        A[j] = sum(S[0:j+1])/(j+1)     
        if j%1000 == 0:
            print (".", end="")
        if j%10000 == 0:
            print (f"\nIteration: {j} \n")
    
    print("")
    return A   


def prefix_average3(S):

    A = [0 for x in range(len(S))]    	
    total = 0   

    for j in range (0, len(S)):  
        total = total + S[j]    		 
        A[j] = total/(j+1)
        if j%1000 == 0:
            print (".", end="")   
        if j%10000 == 0:
            print (f"\nIteration: {j} \n")
    
    print("")
    return A   

if __name__ == "__main__":
    experiment_list = [1, 10, 100, 1000, 10000, 100000, 1000000]     
    elapsed_times = list()

    for experiment in experiment_list:
        l = [random.randint(0, MAX_NUMBER) for x in range (0, experiment)]
        times = list()

        start = time.time()
        ll = prefix_average(l)
        end = time.time()
        elapsed = end - start
        times.append (elapsed)

        start = time.time()
        ll = prefix_average2(l)
        end = time.time()
        elapsed = end - start
        times.append (elapsed)

        start = time.time()
        ll = prefix_average3(l)
        end = time.time()
        elapsed = end - start
        times.append (elapsed)

        elapsed_times.append(times)
    
    print (elapsed_times)

