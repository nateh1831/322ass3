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
    Clause('on_t1'),
    Clause('on_t2'),
    Clause('on_t3'),
    Clause('plugged_sink'),
    Clause('plugged_bath'),
    Clause('flow_faucet', ['on_t3', "pressurized_p3"]),
    Clause('wet_sink', ['flow_faucet']),
    Clause('pressurized_p3', ['on_t1', 'pressurized_p1']),
    Clause('flooding_sink', ['plugged_sink', 'wet_sink']),
    Clause('flooding_bath', ['plugged_bath', 'wet_bath']),
    Clause('wet_floor', ['flooding_sink']),
    Clause('wet_floor', ['flooding_bath'])
    ])

print(plumbing)
from logicBottomUp import fixed_point
fixed_point(plumbing)
from logicTopDown import prove
prove(plumbing, ['wet_floor'])
