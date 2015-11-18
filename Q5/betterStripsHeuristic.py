# stripsHeuristic.py - Planner with Heursitic Function
# Python 3 code. Full documentation at http://artint.info/code/python/code.pdf

# Artificial Intelligence: Foundations of Computational Agents
# http://artint.info
# Copyright David L Poole and Alan K Mackworth 2015.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en_US.

def heuristic_fun(state,goal):
    """An (under)estimate of the cost of solving goal from state.
    Both state and goal are variable:value dictionaries.
    This heuristic is the maximum of
    - the distance to the goal location, if there is one
    - the distance to the coffee shop if the goal has SWC=False, node has SWC=True and RHC=False
    """
    return max(h1(state,goal),
               h2(state,goal),
               h3(state,goal),
               h4(state,goal),
               h5(state,goal))

def h1(state,goal):
    """ returns the distance to the goal location, if there is one"""
    if 'RLoc' in goal:
        return dist(state['RLoc'], goal['RLoc'])
    else:
        return 0

def h2(state,goal):
    """ the distance to the coffee shop if the goal has SWC=False, node has SWC=True and RHC=False"""
    if 'SWC' in goal and goal['SWC']==False and state['SWC']==True and state['RHC']==False:
        return dist(state['RLoc'],'cs') + dist(state['RLoc'], 'off') + 2 
        """ add 1 because it takes 1 action to pick up the coffee """
    elif 'SWC' in goal and goal['SWC']==False and state['SWC']==True and state['RHC']==True:
        return dist(state['RLoc'], 'off') + 1 
        """ add 1 because it takes 1 action to pick up the coffee """
    else:
        return 0
        
def h3(state,goal):
    """ RHC """
    goalDist = 0
    if 'RHC' in goal and goal['RHC']==True and state['RHC']==False:
        if 'Rloc' in goal:
            goalDist = dist('cs', goal['RLoc']) 
        return dist(state['RLoc'],'cs') + goalDist + 1 
        """ add 1 because it takes 1 action to pick up the coffee """
    else:
        return 0

def h4(state,goal):
    """ MW """
    mailDelivery = 0
    if 'MW' in goal and goal['MW']==False and state['MW']==True:
        if 'RHM' in goal and goal['RHM']==False:
            mailDelivery = dist('mr','off') + 1 
            """ add 1 because it takes 1 action to deliver mail """
        return dist(state['RLoc'],'mr') + mailDelivery + 1 
        """ add 1 because it takes 1 action to pick up the mail """
    else:
        return 0

def h5(state,goal):
    """ RHM """
    goalDist = 0
    if 'RHM' in goal and goal['RHM']==False and state['RHM']==True:
        if 'Rloc' in goal:
            goalDist = dist('off', goal['RLoc']) 
        return dist(state['RLoc'],'off') + goalDist + 1 
        """ add 1 because it takes 1 action to deliver mail """
    elif 'RHM' in goal and goal['RHM']==False and state['RHM']==True:
        if 'Rloc' in goal:
            goalDist = dist('off', goal['RLoc']) 
        return dist(state['RLoc'],'off') + goalDist + 1 
        """ add 1 because it takes 1 action to pick up mail """
    else:
        return 0


def dist(loc1, loc2):
    """returns the distance from location loc1 to loc2
    """
    if loc1==loc2:
        return 0
    if {loc1,loc2} in [{'cs','lab'},{'mr','off'}]:
        return 2
    else:
        return 1

#####  Forward Planner #####
from searchAStar import Searcher
from stripsForwardPlanner import Forward_search_from_STRIPS
from stripsProblem import problem0, problem1, problem2
thisproblem = problem1

forward_search_problem = Forward_search_from_STRIPS(thisproblem)
searcherf = Searcher(forward_search_problem)
print("\n***** FORWARD NO HEURISTIC")
print(searcherf.search())  # forward no mpp

forward_search_problem_h = Forward_search_from_STRIPS(thisproblem,heuristic_fun)
searcherHeur = Searcher(forward_search_problem_h)
print("\n***** FORWARD WITH HEURISTIC")
print(searcherHeur.search()) 

#####  Regression Planner
from stripsRegressionPlanner import Regression_search_from_STRIPS

regression_search_problem = Regression_search_from_STRIPS(thisproblem)
rsearcher = Searcher(regression_search_problem)
print("\n***** REGRESSION NO HEURISTIC")
print(rsearcher.search())  # regression no mpp

regression_search_problem_h = Regression_search_from_STRIPS(thisproblem,heuristic_fun)
rsearcherHeur = Searcher(regression_search_problem_h)
print("\n***** REGRESSION WITH HEURISTIC")
print(rsearcherHeur.search()) 

