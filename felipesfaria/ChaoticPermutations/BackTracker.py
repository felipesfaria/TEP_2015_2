__author__ = 'felipesfaria'

class BackTracker:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, n):
        print "Hello BackTracker"
        self.N = n    # instance variable unique to each instance__init__.pyt
        self._state = []
        self._finalStates = []
        self._possibleSteps = range(0,n)

    def Run(self):
        self.BackTrack()
        return self._finalStates

    def BackTrack(self):
        if self.LastPositionIsValid()==False:
            return
        if len(self._state) == self.N:
            self._finalStates.append(self._state[:])
            return
        for i in range(0,len(self._possibleSteps)):
            current = self._possibleSteps[i]
            self._state.append(current)
            self._possibleSteps.pop(i)
            self.BackTrack()
            self._possibleSteps.insert(i,current)
            self._state.pop()


    def LastPositionIsValid(self):
        #return _state.size()==0|| _state.get(_state.size()-1)!= _state.size()-1;
        if len(self._state) == 0:
            return True;
        if self._state[-1] == len(self._state)-1:
            return False
        return True
