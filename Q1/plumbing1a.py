### Python program for the simplified plumbing example....

# Artificial Intelligence: Foundations of Computational Agents
# http://artint.info
# Copyright David L Poole and Alan K Mackworth 2015.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en_US.

from logicProblem import Clause, Askable, KB

plumbing = KB([
    Clause('pressurized_p1'),
    Clause('pressurized_p2', ['on_t1', 'pressurized_p1']),
    Clause('flow_shower', ['on_t2', 'pressurized_p2']),
    Clause('wet_bath', ['flow_shower']),
    Clause('flow_d2', ['wet_bath', 'unplugged_bath']),
    Clause('flow_d1', ['flow_d2']),
    Clause('on_t1'),
    Clause('on_t2'),
    Clause('unplugged_bath'),

    Clause('unplugged_sink'),
    Clause('flow_faucet', ['on_t3', "pressurized_p3"]),
    Clause('flow_d1', ['flow_d3']),
    Clause('flow_d3', ['wet_sink', 'unplugged_sink']),
    Clause('wet_sink', ['flow_faucet']),
    Clause('on_t3'),
    Clause('pressurized_p3', ['on_t1', 'pressurized_p1'])
    ])

print(plumbing)
from logicBottomUp import fixed_point
fixed_point(plumbing)
from logicTopDown import prove
prove(plumbing, ['flow_d1'])
