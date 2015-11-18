# logicTopDown.py - Top-down Proof Procedure for Definite Clauses
# Python 3 code. Full documentation at http://artint.info/code/python/code.pdf

# Artificial Intelligence: Foundations of Computational Agents
# http://artint.info
# Copyright David L Poole and Alan K Mackworth 2015.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en_US.

import itertools

def min_conflicts(kb,ans_body):
    a = []
    prove(kb, ans_body,a)
    singular_conflict = []
    for conflict in kb.conflicts:			# any assumable that is present in all conflicts
        if len(conflict) == 1:				
            singular_conflict.append(list(conflict)[0])
    minimum_conflict = []
    if len(singular_conflict) > 0:			# we need to specially handle case where we have
        for s in singular_conflict:			# minimal conflict with only one atom involved.
            for conflict in kb.conflicts:     
                if s not in conflict:
                    minimum_conflict.append(conflict)
        minimum_conflict.append(s)
        print("Minimum Conflicts: ", minimum_conflict)
        print("Minimum Diagnoses: ", minimum_conflict)
        return
    print("Minimum Conflicts: ", kb.conflicts)
    print("Minimum Diagnoses: ", min_diagnoses(kb.conflicts))
    return

def min_diagnoses(min_conflicts):
    min_dg = []
    combos = list(itertools.product(*[min_conflicts[i] for i in range(0, len(min_conflicts))]))
    for combo in combos:
        min_dg.append(list(set(combo)))				# derive the combinations
    singles = []
    for min in min_dg:
        if len(min) == 1:
            singles.append(min[0])					# account for those with common conflicts
    result = []
    for min in min_dg:
        if not contains_any_single(min, singles):   # any combination not involving single case
            result.append(min)						# is a minimal diagnoses, as well as the single cases
    result.extend(singles)
    return result

def contains_any_single(lst, elems):
    for l in lst:
        for e in elems:
            if e in l:
                return True
    return False

def prove(kb,ans_body,conflicts,trace=True,indent=''):
    """returns True if kb |- ans_body
    """
    if trace: print(indent,'false <-',' & '.join(conflicts), " ", ' & '.join(ans_body))
    if ans_body:
        selected = ans_body[0]   					# select first atom from ans_body
        if selected in kb.assumables:
            if selected not in conflicts:
                conflicts.append(selected)
            return (prove(kb,ans_body[1:],conflicts.copy(),trace,indent+'    '))
        elif selected in kb.askables:
            return (input("Is "+selected+" true? ")=="yes"
                    and  prove(kb,ans_body[1:],conflicts.copy(),trace,indent+'    '))
        else:
            return any(prove(kb,cl.body+ans_body[1:],conflicts.copy(),trace,indent+'    ')
                       for cl in kb.clauses_for_atom(selected))
    else:
        kb.conflicts.append(conflicts.copy())		# have seen all conflicts in this chain
        conflicts.clear()
        return False								# empty body is true
   
        
# try
from logicProblem import q2
#min_conflicts(simple,['a','b'])
min_conflicts(q2,['a','z'])
