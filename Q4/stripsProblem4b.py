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
     'mcc_mr', 'puc', 'dc', 'pum', 'dm', 'db', 'cib', 'mib', 'dcb', 'dmb', 'pub_cs', 'pub_off',
     'pub_lab', 'pub_mr', 'mc_cs_wbox', 'mc_off_wbox', 'mc_lab_wbox', 'mc_mr_wbox', 'mcc_cs_wbox', 'mcc_off_wbox',
     'mcc_lab_wbox', 'mcc_mr_wbox'},    #actions
    {'RLoc':{'cs', 'off', 'lab', 'mr'}, 'RHC':boolean, 'SWC':boolean,
     'MW':boolean, 'RHM':boolean, 'RHB':boolean, 'BLoc':{'cs', 'off', 'lab', 'mr',}, 'BHM':boolean, 'BHC':boolean},     #feaures:domains
    {'mc_cs': Strips({'RLoc':'cs', 'RHB':False}, {'RLoc':'off'}),
     'mc_off': Strips({'RLoc':'off', 'RHB':False}, {'RLoc':'lab'}),
     'mc_lab': Strips({'RLoc':'lab', 'RHB':False}, {'RLoc':'mr'}),
     'mc_mr': Strips({'RLoc':'mr', 'RHB':False}, {'RLoc':'cs'}),
     'mcc_cs': Strips({'RLoc':'cs', 'RHB':False}, {'RLoc':'mr'}),
     'mcc_off': Strips({'RLoc':'off', 'RHB':False}, {'RLoc':'cs'}),
     'mcc_lab': Strips({'RLoc':'lab', 'RHB':False}, {'RLoc':'off'}),
     'mcc_mr': Strips({'RLoc':'mr', 'RHB':False}, {'RLoc':'lab'}),
     'puc': Strips({'RLoc':'cs', 'RHC':False, 'RHM':False, 'RHB':False}, {'RHC':True}),
     'dc': Strips({'RLoc':'off', 'RHC':True}, {'RHC':False, 'SWC':False}),
     'pum': Strips({'RLoc':'mr','MW':True, 'RHC':False, 'RHB':False}, {'RHM':True,'MW':False}),
     'dm': Strips({'RLoc':'off', 'RHM':True}, {'RHM':False}),
    #moving with the box
     'mc_cs_wbox': Strips({'RLoc':'cs', 'RHB':True}, {'RLoc':'off', 'BLoc':'off'}),
     'mc_off_wbox': Strips({'RLoc':'off', 'RHB':True}, {'RLoc':'lab', 'BLoc':'lab'}),
     'mc_lab_wbox': Strips({'RLoc':'lab', 'RHB':True}, {'RLoc':'mr', 'BLoc':'mr'}),
     'mc_mr_wbox': Strips({'RLoc':'mr', 'RHB':True}, {'RLoc':'cs', 'BLoc':'cs'}),
     'mcc_cs_wbox': Strips({'RLoc':'cs', 'RHB':True}, {'RLoc':'mr', 'BLoc':'mr'}),
     'mcc_off_wbox': Strips({'RLoc':'off', 'RHB':True}, {'RLoc':'cs', 'BLoc':'cs'}),
     'mcc_lab_wbox': Strips({'RLoc':'lab', 'RHB':True}, {'RLoc':'off', 'BLoc':'off'}),
     'mcc_mr_wbox': Strips({'RLoc':'mr', 'RHB':True}, {'RLoc':'lab', 'BLoc':'lab'}),
    #picking up the box at each location
     'pub_cs': Strips({'RLoc':'cs','BLoc':'cs' , 'RHC':False, 'RHM':False, 'RHB':False}, {'RHB':True}),
     'pub_off': Strips({'RLoc':'off','BLoc':'off' , 'RHC':False, 'RHM':False, 'RHB':False}, {'RHB':True}),
     'pub_lab': Strips({'RLoc':'lab','BLoc':'lab' , 'RHC':False, 'RHM':False, 'RHB':False}, {'RHB':True}),
     'pub_mr': Strips({'RLoc':'mr','BLoc':'mr' , 'RHC':False, 'RHM':False, 'RHB':False}, {'RHB':True}),
     #drop box
      'db': Strips({'RHB':True},{'RHB':False}),
     #pick up/deliver coffee/mail while holding box
     'mib': Strips({'RLoc':'mr','MW':True, 'RHB':True}, {'BHM':True,'MW':False}),
     'cib': Strips({'RLoc':'cs', 'BHC':False, 'RHB':True}, {'BHC':True}),
     'dcb': Strips({'RLoc':'off', 'BHC':True, 'RHB':True}, {'BHC':False, 'SWC':False}),
     'dmb': Strips({'RLoc':'off', 'BHM':True, 'RHB':True}, {'BHM':False}),
    },
    incompatibles = [{'MW':True, 'RHM':True},
                     {'RHC':True, 'RHM':True},
                     {'RHC':True, 'RHB':True},
                     {'RHB':True, 'RHM':True}]   #currently ignored
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

#problem0 = Planning_problem(delivery_domain,
        #                    {'RLoc':'lab', 'MW':True, 'SWC':True, 'RHC':False,
              #               'RHM':False},
              #              {'RLoc':'off'})
#problem1 = Planning_problem(delivery_domain,
               #             {'RLoc':'lab', 'MW':True, 'SWC':True, 'RHC':False,
               #              'RHM':False},
                #            {'SWC':False})
problemX = Planning_problem(delivery_domain,
                            {'RLoc':'lab', 'MW':True, 'SWC':True, 'RHC':False, 
                             'RHM':False, 'RHB':False, 'BLoc':'lab', 'BHM':False, 'BHC':False},
                            {'SWC':False, 'MW':False, 'RHM':False, 'BHM':False})

