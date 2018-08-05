from timeit import default_timer as timer
import os

sum = 0
nr = 1000
for i in range(nr):
    start = timer()
    os.system('curl localhost:420/numbers/classification/predict -d \'{"input":[1]}\' -H "Content-Type: application/json"')
    end = timer()
    print (end - start)
    sum += (end - start)

print ('end:' + str(sum/nr))
