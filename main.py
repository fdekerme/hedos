import os

import matplotlib.pyplot as plt

from blooddvh import CompartmentModel
from blooddvh import BloodDistribution
from blooddvh import tDVH
from blooddvh import bDVH

sample_size = 1000
time_per_step = 1.0  # Seconds
steps_per_min = 60  # Number of steps per min, e.g.,  step resolutions are 1 sec and 0.1 sec for 60 and 600, respectively
model = CompartmentModel(os.path.join('input', 'ICRP89_compartment_model.xlsx'), 'male volume_corrected_w2', vol=5.3, cardiac=6.5, resolution=steps_per_min)


blood = BloodDistribution()
nb_of_steps = 600
blood.generate_from_markov_weibull(model.markov_weibull, model.name, model.volume, time_per_step, sample_size, nb_of_steps)

blood.transition_time([])
blood.mtt

"""
dose = tDVH()
# First 60 sec, 2 Gy uniform
dose.add(55, lambda x: 2)

# To choose an organ where the dose is delivered, 0: brain, 19: liver
print(list(zip(range(len(model.name)), model.name)))
blood_dose = bDVH(blood.df, blood.dt)
# Add dose to Liver
blood_dose.add_dose(dose, 19, start_time=0)
blood_dose.add_dose(dose, 19, start_time=4)
# Add dose to Brain
blood_dose.add_dose(dose, 0, start_time=0)
# Draw your blood DVH (differential)
plt.figure(figsize=(10,6))
plt.hist(blood_dose.dose)
plt.xlabel('Dose (Gy)', fontsize=16)
plt.ylabel('# of Events', fontsize=16)

"""