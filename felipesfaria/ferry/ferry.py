from random import randint


memo = set()
bestPath = []
orientation = 1
def backtrack(state, vehicles, L, n_boarded_vehicles, max_boarded_vehicles,path):
    global bestPath
    if state[0] > L or state[1] > L:
        return  # invalid state

    loadState = state[:]
    loadState.sort()
    if tuple(loadState) in memo:
        return  # already visited

    if n_boarded_vehicles > max_boarded_vehicles[0]:
        max_boarded_vehicles[0] = n_boarded_vehicles
        bestPath = path[:]

    length_next_vehicle = vehicles[n_boarded_vehicles]

    new_state = [state[0] + length_next_vehicle, state[1]]
    path.append("L")
    backtrack(new_state, vehicles, L, n_boarded_vehicles + 1, max_boarded_vehicles,path)
    path.pop()

    path.append("R")
    new_state = [state[0], state[1] + length_next_vehicle]
    backtrack(new_state, vehicles, L, n_boarded_vehicles + 1, max_boarded_vehicles,path)
    path.pop()
    saveState = state[:]
    saveState.sort()
    memo.add(tuple(saveState))

def ferry(vehicles, L):
    max_boarded_vehicles = [0]
    state = [0,0]
    path = []
    loaded={}
    loaded["L"]=0
    loaded["R"]=0
    backtrack(state, vehicles, L, 0, max_boarded_vehicles,path)
    
    print("We can board up to %d vehicles" % max_boarded_vehicles[0])
    print "Best order is {}".format(bestPath)
    print "Cars loaded: {}".format(queue[:max_boarded_vehicles[0]])
    for i in range(max_boarded_vehicles[0]):
        loaded[bestPath[i]]+=queue[i]
    print "Loaded on Each Side:{}".format(loaded)
    print "Next Car in queue:{}".format(queue[max_boarded_vehicles[0]])




queue = []
for i in range(2000):
    queue += [randint(100, 500)]

ferry(queue, 1000)







