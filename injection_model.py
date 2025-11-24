# run_and_tjunction.py
# Template: schedule pulses for A and B, run Smoldyn and log outlet counts
# Note: adapt API calls to the Smoldyn Python wrapper you have (names differ slightly across builds).

__author__ = "Emily Pike"
__email__ = "ekpike@Mmun.ca"

import math
import csv
import time
import smoldyn

# -------------- USER PARAMETERS --------------
t_total = 200.0      # ms total simulation time
dt = 0.01            # ms timestep (match the .cfg)
pulse_duration = 10.0   # ms for each pulse
pulse_interval = 50.0   # ms between pulses
A_count = 500        # molecules per A pulse
B_count = 500        # molecules per B pulse (if pulsed)
inlet_pos = (100, 20, 10)   # where to place A pulses
main_inlet_pos = (50, 50, 10) # where to place B background or B pulses
outlet_box = ((300,40,0), (400,60,20)) # detection box (two corners)

# -------------- PSEUDOCODE / API USAGE --------------
# The exact API calls depend on your Smoldyn Python binding.
# Replace the pseudo-calls below with your binding's methods.
#
# Example flow:
#   sim = SmoldynSimulation.from_cfg("and_tjunction_base.cfg")
#   sim.set_time_step(dt)
#   sim.register_output_logger(...)   # function that samples counts in outlet_box
#   for t in np.arange(0, t_total, dt):
#       # schedule pulses (A at times 20-30 ms, maybe B pulses too)
#       if 20.0 <= t < 20.0 + pulse_duration:
#           sim.add_molecules("A", A_count, inlet_pos)
#       if 20.0 <= t < 20.0 + pulse_duration and you_want_B_pulse:
#           sim.add_molecules("B", B_count, main_inlet_pos)
#       sim.step()   # run single dt
#       # optionally sample outlet region every few steps
#       if (int(t*100) % int(1.0*100)) == 0:   # sample every 1 ms
#           countA, countB, countC = sim.count_in_box(outlet_box)
#           log.append((t, countA, countB, countC))
#
#   sim.end()
#
# -------------- Example output writing --------------
# After the run, write log to CSV for plotting
# with open("and_outlet_log.csv","w",newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["time_ms","A","B","C"])
#     writer.writerows(log)
#
# -------------- End of template --------------
