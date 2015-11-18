### Python program for the simplified plumbing example....

# Artificial Intelligence: Foundations of Computational Agents
# http://artint.info
# Copyright David L Poole and Alan K Mackworth 2015.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en_US.

from logicProblem import Clause, Askable, KB

plumbing = KB([
    Clause('on_t1'),
    Clause('on_t2'),
    Clause('on_t3'),
    Clause('flow_shower'),
    Clause('flow_faucet'),
    Clause('unplugged_bath'),
    Clause('unplugged_sink'),
    Clause('wet_sink'),
    Clause('wet_bath'),
    Clause('flow_d3', ['wet_sink', 'unplugged_sink']),
    Clause('flow_d2', ['wet_bath', 'unplugged_bath']),
    Clause('flow_d1', ['flow_d3']),
    Clause('flow_d1', ['flow_d2']),
    Clause('pressurized_p3', ['on_t3', 'flow_faucet']),
    Clause('pressurized_p2', ['on_t2', 'flow_shower']),
    Clause('pressurized_p1', ['on_t1', 'pressurized_p3']),
    Clause('pressurized_p1', ['on_t1', 'pressurized_p3'])
    ])

print(plumbing)
from logicBottomUp import fixed_point
fixed_point(plumbing)
from logicTopDown import prove
prove(plumbing, ['pressurized_p1'])
prove(plumbing, ['flow_d1'])
