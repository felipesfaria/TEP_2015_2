from random import randint


memo = set()
bestPath = []
orientation = 1
def backtrack(state, vehicles, L, n_boarded_vehicles, max_boarded_vehicles,path):
    global orientation
    global bestPath
    switchBack = False
    if state[0] > L:
        return  # invalid state

    if tuple(state) in memo:
        return  # already visited

    if n_boarded_vehicles > max_boarded_vehicles[0]:
        max_boarded_vehicles[0] = n_boarded_vehicles
        bestPath = path[:]

    length_next_vehicle = vehicles[n_boarded_vehicles]

    new_state = [state[0] + length_next_vehicle, state[1]]
    path.append(1*orientation)
    backtrack(new_state, vehicles, L, n_boarded_vehicles + 1, max_boarded_vehicles,path)
    path.pop()

    path.append(-1*orientation)
    new_state = [state[0], state[1] + length_next_vehicle]
    if(new_state[0]<new_state[1]):
        orientation*=-1
        switchBack=True
    new_state.sort(reverse=True)  # [more_loaded, less_loaded] by convention
    backtrack(new_state, vehicles, L, n_boarded_vehicles + 1, max_boarded_vehicles,path)
    if switchBack:
        orientation*=-1
    path.pop()
    memo.add(tuple(state))

def ferry(vehicles, L):
    max_boarded_vehicles = [0]
    state = [0,0]
    path = []
    loaded={}
    loaded["E"]=0
    loaded["D"]=0
    backtrack(state, vehicles, L, 0, max_boarded_vehicles,path)
    
    print("We can board up to %d vehicles" % max_boarded_vehicles[0])
    print "Best order is {}".format(bestPath)
    print "Cars loaded: {}".format(queue[:max_boarded_vehicles[0]])
    for i in range(max_boarded_vehicles[0]):
        if(bestPath[i]==-1):
            bestPath[i] = "E"
        elif (bestPath[i]==1):
            bestPath[i]="D"
        else:
            print "Error:Invalid value in bestPath"
        loaded[bestPath[i]]+=queue[i]
    print "Loaded on Each Side:{}".format(loaded)
    print "Next Car in queue:{}".format(queue[max_boarded_vehicles[0]])




queue = []
for i in range(2000):
    queue += [randint(100, 500)]

ferry(queue, 1000)







