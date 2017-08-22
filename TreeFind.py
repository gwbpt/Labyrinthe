"""
Like a Abstract Base Class (in Python3)

create recursively from the first (root) instance a tree of instances 
according the findContigousParams which should return a list of param to create branches

to stop search a targetReach function should be given as fctTargetReach param of the root instance

usage example :

#----------------------------------------------

class Test(TreeFinder):

    def __init__(self, params, fctTargetReach=None, prev=None, maxNbOfInstances=40, maxNbOfPreviousStates=8):
        super(Test, self).__init__(params, fctTargetReach=fctTargetReach, prev=prev, maxNbOfInstances=maxNbOfInstances, maxNbOfPreviousStates=maxNbOfPreviousStates) # 
        ...
    # overload    
    def findContigousParams(self):
        if len(self.params) < 40 :
            return [self.params+"/folderA",self.params+"/folderB"] # list of params
        #print("End of branch reach", self)
        return [] # list of params of possible instance

#----------------------------------------------

toBeSerarch = 'root/folderB/folderA/folderA/folderB'
def targetReach(state):
    if state.params == toBeSerarch:
        #print("<<<<<<<<<<<<< Found >>>>>>>>>>>>>")
        return True
    return False

print("toBeSerarch : ", toBeSerarch)
test = Test('root', fctTargetReach=targetReach, maxNbOfInstances=39, maxNbOfPreviousStates=6)

resultats = test.results()
if resultats != None :
    comment, solution, history = resultats
    print(comment)
    print("len(history) : ", len(history))
    for p in solution.pathToTarget():
        print(p)

"""

from __future__ import print_function, division

class TreeFinder(object): #  object mandatory for inheritance with super
        
    def __init__(self, params, fctTargetReach=None, prev=None, maxNbOfInstances=100, maxNbOfPreviousStates=10):
        if prev == None :
            print("first object")
            self.previousStatesLength = 0 # len of  previous states
            # init class attributes
            TreeFinder.found          = None
            TreeFinder.history        = []
            TreeFinder.instancesNb    = 1
            TreeFinder.fctTargetReach = fctTargetReach
            TreeFinder.maxInstances   = maxNbOfInstances
            TreeFinder.maxPrevStates  = maxNbOfPreviousStates
            if fctTargetReach == None :
                raise Exception("First instance of TreeFinder should have a fctTargetReach in parameters")
        else :
            self.previousStatesLength = prev.previousStatesLength + 1
            TreeFinder.instancesNb   += 1
            
        self.idx    = TreeFinder.instancesNb
        self.prev   = prev
        self.params = params
        self.nexts  = []
        TreeFinder.history.append(self)
        
        if self.idx > TreeFinder.maxInstances :
            s = "instances number max%6d reach"%TreeFinder.maxInstances
            TreeFinder.found = (s, self, TreeFinder.history) 
        elif TreeFinder.found == None :
            if TreeFinder.fctTargetReach(self) :# self.__class__.targetReach(self):
                s = "Found"
                TreeFinder.found = (s, self,TreeFinder.history) 
                print("<<<<<<< %s >>>>>>"%s)
            elif self.previousStatesLength >= TreeFinder.maxPrevStates :
                s = "search length reach%4d"%TreeFinder.maxPrevStates
                TreeFinder.found = (s, self,TreeFinder.history) 
                print("<<<<<<<<<<<<< %s >>>>>>>>>>>>>"%s)
            else :
                self.scanSolutions()
    
    def __str__(self):
        return "idx:%6d ; len:%6d : %s"%(self.idx, self.previousStatesLength, self.params)
    
    def results(self):
        return TreeFinder.found
    
    def previousStates(self):
        states = []
        state = self
        while state != None :
            #print(state)
            states.append(state)
            state = state.prev
        #print("len(previousStates) : ", len(states))
        return states
        
    def previousParams(self):
         return [s.params for s in self.previousStates()]   
        
    def findContigousParams(self):
        raise NotImplementedError("Abstract Class ! findContigousParams method should be Overrided\n" + 
            "           to return a list of params where to continue exploration")
        return [] # list of params
        
    def scanSolutions(self):
        #print("TreeFinder.scanSolutions")
        for params in self.findContigousParams():
            #print("params : ", params)
            if TreeFinder.found != None : break
            if not params in self.previousStates():
                #print("Creation d'un nouvel objet de la classe ", self.__class__)
                newObject = self.__class__(params, self.fctTargetReach, prev=self) 
                self.nexts.append(newObject)

#===============================================================================

if __name__ == '__main__' :
    
    class Test(TreeFinder):

        def __init__(self, params, fctTargetReach=None, prev=None, maxNbOfInstances=40, maxNbOfPreviousStates=8):
            super(Test, self).__init__(params, fctTargetReach=fctTargetReach, prev=prev, maxNbOfInstances=maxNbOfInstances, maxNbOfPreviousStates=maxNbOfPreviousStates) # 
            #TreeFinder.__init__(self, params, fctTargetReach=fctTargetReach, prev=prev)
            
        def findContigousParams(self):
            #print("Test.findContigousParams")
            if len(self.params) < 40 :
                return [self.params+"/folderA",self.params+"/folderB"] # list of params
            #print("End of branch reach", self)
            return []
            
        def pathToTarget(self):
            positions = self.previousParams()
            positions.reverse()
            return positions
        
    #----------------------------------------------
    
    toBeSerarch = 'root/folderB/folderA/folderA/folderB'
    def targetReach(state):
        if state.params == toBeSerarch:
            #print("<<<<<<<<<<<<< Found >>>>>>>>>>>>>")
            return True
        return False
    
    print("toBeSerarch : ", toBeSerarch)
    test = Test('root', fctTargetReach=targetReach, maxNbOfInstances=39, maxNbOfPreviousStates=6)

    resultats = test.results()
    if resultats != None :
        comment, solution, history = resultats
        print(comment)
        print("len(history) : ", len(history))
        for p in solution.pathToTarget():
            print(p)

