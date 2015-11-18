# logicProblem.py - Representations Logics
# Python 3 code. Full documentation at http://artint.info/code/python/code.pdf

# Artificial Intelligence: Foundations of Computational Agents
# http://artint.info
# Copyright David L Poole and Alan K Mackworth 2015.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en_US.

class Clause(object):
    """A definite clause"""

    def __init__(self,head,body=[]):
        """clause with atom head and lost of atoms body"""
        self.head=head
        self.body = body

    def __str__(self):
        """returns the string representation of a clause.
        """
        if self.body:
            return self.head + " <- " + " & ".join(self.body) + "."
        else:
            return self.head + "."

class Askable(object):
    """An askable atom"""

    def __init__(self,atom):
        """clause with atom head and lost of atoms body"""
        self.atom=atom

    def __str__(self):
        """returns the string representation of a clause.
        """
        return "askable " + atom + "."

class Assumable(object):
    """An assumable atom"""

    def __init__(self,atom):
        self.atom=atom

    def __str__(self):
        return "assumable " + atom + "."

class KB(object):
    """A knowledge base consists of a set of clauses.
    We also create a dictionary to give fast access to the clauses with an atom in head.
    """
    def __init__(self, statements=[]):
        self.statements = statements
        self.clauses = [c for c in statements if isinstance(c, Clause)]
        self.askables = [c.atom for c in statements if isinstance(c, Askable)]
        self.assumables = [c.atom for c in statements if isinstance(c, Assumable)]
        self.atom_to_clauses = {}  # dictionary giving clauses with atom as head
        self.conflicts = []
        for c in self.clauses:
            if c.head in self.atom_to_clauses:
                self.atom_to_clauses[c.head].add(c)
            else:
                self.atom_to_clauses[c.head] = {c}

    def clauses_for_atom(self,a):
        """returns set of clauses with atom a as the head"""
        if a in self.atom_to_clauses:
            return  self.atom_to_clauses[a]
        else:
            return set()

    def __str__(self):
        """returns a string representation of this knowledge base.
        """
        return '\n'.join([str(c) for c in self.statements])

elect = KB([
    Clause('light_l1'),
    Clause('light_l2'),
    Clause('ok_l1'),
    Clause('ok_l2'),
    Clause('ok_cb1'),
    Clause('ok_cb2'),
    Clause('live_outside'),
    Clause('live_l1', ['live_w0']),
    Clause('live_w0', ['up_s2','live_w1']),
    Clause('live_w0', ['down_s2','live_w2']),
    Clause('live_w1', ['up_s1', 'live_w3']),
    Clause('live_w2', ['down_s1','live_w3' ]),
    Clause('live_l2', ['live_w4']),
    Clause('live_w4', ['up_s3','live_w3' ]),
    Clause('live_p_1', ['live_w3']),
    Clause('live_w3', ['live_w5', 'ok_cb1']),
    Clause('live_p_2', ['live_w6']),
    Clause('live_w6', ['live_w5', 'ok_cb2']),
    Clause('live_w5', ['live_outside']),
    Clause('lit_l1', ['light_l1', 'live_l1', 'ok_l1']),
    Clause('lit_l2', ['light_l2', 'live_l2', 'ok_l2']),
    Askable('up_s1'),
    Askable('down_s1'),
    Askable('up_s2'),
    Askable('down_s2'),
    Askable('up_s3'),
    Askable('down_s2')
    ])

simple = KB([
    Clause('a',['c']),
    Clause('a',['e']),
    Clause('b',['d']),
    Clause('b',['e']),
    Assumable('c'),
    Assumable('d'),
    Assumable('e')
    ])


q2 = KB([
    Clause('k'),
    Clause('c'),
    Clause('a',['h','s1']),
    Clause('d',['c','s1']),
    Clause('e',['d','s2']),
    Clause('f',['k','s2']),
    Clause('z',['g','s2']),
    Clause('h',['d','s3']),
    Clause('a',['b','e','s4']),
    Clause('b',['c','s4']),
    Clause('g',['f','j','s5']),
    Clause('j',['s2']),
    Assumable('s1'),
    Assumable('s2'),
    Assumable('s3'),
    Assumable('s4'),
    Assumable('s5')
    ])
