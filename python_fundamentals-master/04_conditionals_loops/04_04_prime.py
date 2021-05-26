'''
Print out every prime number between 1 and 100.

'''

for num in range(1,101):
    for i in range(2,num):
        if num % i == 0:
            break
        else: print(num)
        break

'''got the code by searching online, but do not fully understand the visualizer. if num % i == 0 should go over the range 2, num, so you check if num is divisible by the range 2, num.
in the visualizer it does not do that?'''