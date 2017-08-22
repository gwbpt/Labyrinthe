#================================ EXEMPLE D'APPEL =================================
#                         UTILISE LA "BibliothequesGWB"
#set PYTHONPATH=D:\PYTHON\BibliothequesGWB
#c:\winpython\WinPython-64bit-2.7.6.4\python-2.7.6.amd64\python.exe labyrinthexx.py
#===================================================================================

from __future__ import print_function, division

import os,sys

"""
print("__file__                   : ", __file__)
print("os.pardir                  : ", os.pardir)
print("os.getcwd()                : ", os.getcwd())
print("os.getcwd()                : ", os.getcwd())
'''
print("exec : os.chdir('D:/Bridge')")
os.chdir("D:/Bridge")
'''
print("os.getcwd()                : ", os.getcwd())
print("sys.argv[0]                : ", sys.argv[0])
print("sys.path                   : ", sys.path)
print("dir(os.path)               : ", dir(os.path))
print("os.path.relpath(__file__)  : ", os.path.relpath(__file__))
print("os.path.realpath(__file__) : ", os.path.realpath(__file__))
print("os.path.abspath(__file__)  : ", os.path.abspath(__file__))
print("os.path.dirname(os.path.realpath(__file__))  : ", os.path.dirname(os.path.realpath(__file__)))
print("os.path.dirnameos.path.dirname(os.path.realpath(__file__)))  : ", os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
print("os.path.dirnameos.path.dirname(os.path.abspath(__file__)))  : ", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
"""

if 0 :
    #parentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(os.path.abspath(__file__))
    print("parentdir : ", parentdir)

    grandparentdir, dummy = os.path.split(parentdir)
    print("grandparentdir : ", grandparentdir)

    libraryGWB_path = os.path.join(grandparentdir, "libraryGWB")
    
else :
    libraryGWB_path = "d:\Docs\Python\BibliothequesGWB"
    
#print("libraryGWB_path : ", libraryGWB_path)

sys.path.insert(0,libraryGWB_path)
#print(sys.path)

#print(dir())

#from Tree_Finder.TreeFind import TreeFinder
from TreeFind import TreeFinder

#print(TreeFinder.__doc__)
print(dir(TreeFinder))
#print(help(TreeFinder))

#quit() #==============================
                
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

labyrinthe = [
[1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
[1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,],
[0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,],
[0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,],
[0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,],
[0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,],
[0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,],
[0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,],
[0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,],
[0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,],
[0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,],
[0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,],
[0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,],
[0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,],
[0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,],
[0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,],
[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,],
[1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,],
]

ny = len(labyrinthe)
nx = len(labyrinthe[0])

imgLabyrinthe = np.array(labyrinthe, dtype=np.float)
imgLabyrinthe = 0.8 + 0.2*np.array(labyrinthe)
# corners dark
imgLabyrinthe[ 0, 0] = 0
imgLabyrinthe[ 0,-1] = 0
imgLabyrinthe[-1,-1] = 0
imgLabyrinthe[-1, 0] = 0

#print(imgLabyrinthe[ 0, 0], imgLabyrinthe[ 1, 1], imgLabyrinthe[ 2, 2], imgLabyrinthe[ 3, 3])

if 0 :
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    plt.imshow(imgLabyrinthe, cmap='gray', interpolation='nearest')
    ax.text(0.40, 0.95, 'Labyrinthe', transform=ax.transAxes)

    ax.set_xlim(-2,nx+1)
    ax.set_ylim(ny+1,-2)

    plt.show()

#-------------------------------------------------------------------

EAST, NORTH, WEST, SOUTH = (1, 0), (0,-1), (-1, 0), (0, 1)  # dx, dy
ALL_DIRS = EAST, NORTH, WEST, SOUTH

class LabyrintheFinder(TreeFinder):
    
    def __init__(self, params, fctTargetReach=None, prev=None, maxNbOfInstances=200, maxNbOfPreviousStates=100):
        super(LabyrintheFinder, self).__init__(params, fctTargetReach=fctTargetReach, prev=prev, maxNbOfInstances=maxNbOfInstances, maxNbOfPreviousStates=maxNbOfPreviousStates)
        #TreeFinder.__init__(self            , params, fctTargetReach=fctTargetReach, prev=prev, maxNbOfInstances=maxNbOfInstances, maxNbOfPreviousStates=maxNbOfPreviousStates)
    
    def pathToTarget(self):
        positions = self.previousParams()
        positions.reverse()
        return positions  

    def findContigousParams(self):
        #print("LabyrintheFinder.findContigousParams")
        contigousParams = []
        x, y = self.params
        prevParams = self.previousParams()
        #print("prevParams : ", prevParams)
        for dx, dy in ALL_DIRS:
            if labyrinthe[y+dy][x+dx] != 0: # not in a wall
                next_pos = (x+2*dx, y+2*dy)
                if not next_pos in prevParams :
                    contigousParams.append(next_pos)
        #print("contigousParams : ", contigousParams)
        #if len(contigousParams) == 0 : print("End of branch reach")
        return contigousParams

#---------------------------------------------
targetPos = ( 9, 19)                    
def targetReach(state):
    #print("LabyrintheFinder.targetReach : ", LabyrintheFinder.targetPos)
    return state.params == targetPos
    
firstState = LabyrintheFinder(params=( 3, 1), fctTargetReach=targetReach, maxNbOfInstances=75, maxNbOfPreviousStates=45)

resultats = firstState.results()
if resultats != None :
    comment, solution, history = resultats
    print(comment)
    print("len(history) : ", len(history))
    XYs = solution.pathToTarget()   
    print("solution.pathToTarget() :\n", XYs)
    Xs, Ys = zip(*XYs)

#---------------------------------------------

fig = plt.figure()
ax = fig.add_subplot(111)

plt.imshow(imgLabyrinthe, cmap='gray', interpolation='nearest')

ax.set_xlim(-2,nx+1)
ax.set_ylim(ny+1,-2)

ax.text(0.20, 0.95, 'solution (green)', transform=ax.transAxes)

if resultats != None : ax.plot(Xs, Ys, 'go-', ms=12)

#plt.show() ; quit()
plt.pause(1.0)

#-------------------------------------------------------------
    
time_template = 'Time = %.1f s'    # prints running simulation time

def updateLineInfos(num, line, infos, history):
    infos.set_text("frame :%7d"%(num))
    state = history[num]
    XYs = state.pathToTarget()   
    #print(len(XYs)) 
    Xs, Ys = zip(*XYs)
    line.set_data(Xs, Ys)
    return line, infos

line, = ax.plot([], [], 'ro-', ms=8)
infos = ax.text(0.60, 0.95, '', transform=ax.transAxes)

ani = animation.FuncAnimation(fig, updateLineInfos, frames=len(LabyrintheFinder.history), fargs=(line, infos, LabyrintheFinder.history), blit=False, interval=200, repeat=False)

plt.show()

