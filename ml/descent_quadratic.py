f = lambda x: (x + 5) ** 2
df = lambda x: 2 * (x + 5)

x0 = 3
learn_rate = 0.01
precision = 0.000001
prev_gap = 100
max_iter = 1000
iters = 0

while prev_gap > precision and iters < max_iter:
    prev_x = x0
    x0 = x0 - learn_rate * df(x0)
    prev_gap = abs(x0 - prev_x)
    iters  += 1
    print("Iter {}: x0={}\n".format(iters, x0))

print("The minimal value is [{},{}]".format(x0, f(x0))) 


# cur_x = 3 # The algorithm starts at x=3
# rate = 0.01 # Learning rate
# precision = 0.000001 #This tells us when to stop the algorithm
# previous_step_size = 1 #
# max_iters = 10000 # maximum number of iterations
# iters = 0 #iteration counter
# df = lambda x: 2*(x+5) #Gradient of our function 

# while previous_step_size > precision and iters < max_iters:
#     prev_x = cur_x #Store current x value in prev_x
#     cur_x = cur_x - rate * df(prev_x) #Grad descent
#     previous_step_size = abs(cur_x - prev_x) #Change in x
#     iters = iters+1 #iteration count
#     print("Iteration",iters,"\nX value is",cur_x) #Print iterations
    
# print("The local minimum occurs at", cur_x)