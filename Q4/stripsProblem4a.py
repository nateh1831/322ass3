# stripsProblem.py - STRIPS Representations of Actions
# Python 3 code. Full documentation at http://artint.info/code/python/code.pdf

# Artificial Intelligence: Foundations of Computational Agents
# http://artint.info
# Copyright David L Poole and Alan K Mackworth 2015.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en_US.

class Strips(object):
    def __init__(self,preconditions,effects):
        """
        defines the STRIPS represtation for an action:
        * preconditions is property:value dictionary that must hold
        for the action to be carried out
        * effects is a property:value map that this action makes
        true. The action changes the value of any property specified
        here, and leaves other properties unchanged.
        """
        self.preconditions = preconditions
        self.effects = effects

class STRIPS_domain(object):
    def __init__(self, actions, domains, strips_map, incompatibles=[]):
        self.actions = actions
        self.domains = domains
        self.strips_map = strips_map
        self.incompatibles = incompatibles

boolean = {True, False}
delivery_domain = STRIPS_domain(
    {'mc_cs', 'mc_off','mc_lab','mc_mr', 'mcc_cs', 'mcc_off','mcc_lab',
     'mcc_mr', 'puc', 'dc', 'pum', 'dm'},    #actions
    {'RLoc':{'cs', 'off', 'lab', 'mr'}, 'RHC':boolean, 'SWC':boolean,
     'MW':boolean, 'RHM':boolean},     #feaures:domains
    {'mc_cs': Strips({'RLoc':'cs'}, {'RLoc':'off'}),   
     'mc_off': Strips({'RLoc':'off'}, {'RLoc':'lab'}),
     'mc_lab': Strips({'RLoc':'lab'}, {'RLoc':'mr'}),
     'mc_mr': Strips({'RLoc':'mr'}, {'RLoc':'cs'}),
     'mcc_cs': Strips({'RLoc':'cs'}, {'RLoc':'mr'}),   
     'mcc_off': Strips({'RLoc':'off'}, {'RLoc':'cs'}),
     'mcc_lab': Strips({'RLoc':'lab'}, {'RLoc':'off'}),
     'mcc_mr': Strips({'RLoc':'mr'}, {'RLoc':'lab'}),
     'puc': Strips({'RLoc':'cs', 'RHC':False, 'RHM':False}, {'RHC':True}),
     'dc': Strips({'RLoc':'off', 'RHC':True}, {'RHC':False, 'SWC':False}),
     'pum': Strips({'RLoc':'mr','MW':True, 'RHC':False}, {'RHM':True,'MW':False}),
     'dm': Strips({'RLoc':'off', 'RHM':True}, {'RHM':False})
    },
    incompatibles = [{'MW':True, 'RHM':True},
                     {'RHC':True, 'RHM':True}]   #currently ignored
     )

class Planning_problem(object):
    def __init__(self, prob_domain, initial_state, goal):
        """
        a planning problem consists of
        * a planning domain
        * the initial state
        * a goal 
        """
        self.prob_domain = prob_domain
        self.initial_state = initial_state
        self.goal = goal

problem0 = Planning_problem(delivery_domain,
                            {'RLoc':'lab', 'MW':True, 'SWC':True, 'RHC':False, 
                             'RHM':False}, 
                            {'RLoc':'off'})
problem1 = Planning_problem(delivery_domain,
                            {'RLoc':'lab', 'MW':True, 'SWC':True, 'RHC':False, 
                             'RHM':False}, 
                            {'SWC':False})
problemX = Planning_problem(delivery_domain,
                            {'RLoc':'lab', 'MW':True, 'SWC':True, 'RHC':False, 
                             'RHM':False}, 
                            {'SWC':False, 'MW':False, 'RHM':False})

