from blooddvh import CompartmentModel
from blooddvh import BloodDistribution
from blooddvh import tDVH
from blooddvh import bDVH
import matplotlib.pyplot as plt

sample_size  = 100 
time_per_step  = 1  # sec
steps_per_min  = 60 # number of steps per min, e.g.,  step resolutions are 1 sec and 0.1 sec for 60 and 600, respectively
model = CompartmentModel("input/ICRP89_compartment_model.xlsx", "male", vol=5.3, cardiac=6.5, resolution=60)


blood = BloodDistribution()
#blood.generate_from_markov(model.markov, model.name, model.volume, time_per_step, sample_size, steps_per_min)
blood.generate_from_markov(model.markov, model.name, model.volume, time_per_step, sample_size, 6000)


blood.save("Particle_Path.xlsx", "Sheet1")

blood_input = BloodDistribution()

blood_input.read_from_excel('Particle_Path.xlsx', 'Sheet1')

blood_input.df



"""
import numpy as np
L=[]
a=blood_input.df.to_numpy()
for x in a :
    k=1
    l=[]
    for i in range(len(x)):
        if i==len(x)-1:
            l.append((x[i-1],k))
        elif x[i] == x[i-1]:
            k+=1
        else:
            l.append((x[i-1],k))
            k=1
    L.append(l)

c=[]
for l in L:
    c.append(np.sum([x[1] for x in l]))



m=[]
for l in L:
    for k in l:
        if k[0]==0:
            m.append(k[1])
print(np.mean(m))
print(np.std(m))

"""
"""
dose = tDVH()
# First 10 sec, 2 Gy uniform
dose.add(10, lambda x: 2)
# Next 10 sec, no dose
dose.add(10, None)
# Next 10 sec, 5 Gy uniform
dose.add(10, lambda x: 5)
model.name
blood_dose = bDVH(blood.df, blood.dt)
# Add dose to Liver
blood_dose.add_dose(dose, 19, start_time=0)
blood_dose.add_dose(dose, 19, start_time=4)
# Add dose to Brain
blood_dose.add_dose(dose, 0, start_time=0)
# Draw your blood DVH (differential)
plt.hist(blood_dose.dose)
"""

"""
import matplotlib.patches as mpatches

plt.figure(figsize=(20,20))
im=plt.imshow(blood_input.df,aspect='auto',interpolation='none')
values = np.unique(blood_input.df.to_numpy().ravel())
colors = [ im.cmap(im.norm(value)) for value in values]

# create a patch (proxy artist) for every color 
patches = [ mpatches.Patch(color=colors[i], label="Level {l}".format(l=values[i]) ) for i in range(len(values)) ]
# put those patched as legend-handles into the legend
plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0. )

plt.grid(True)
plt.show()


"""

"""
a=blood_input.df.apply(pd.Series.value_counts, axis=1)
a[18].dropna().mean()
"""

"""
y, inverse = np.unique(a, return_inverse=True)
np.column_stack((y,np.bincount(inverse)))
"""