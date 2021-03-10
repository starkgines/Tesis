import uproot
import numpy as np
import matplotlib.pyplot as plt


file = uproot.open("../root_pandas/dose-rank000.root")

print("...............Primera lectura del root muon CCD1.........")
## KEYs Rama principal
print(file.keys())
keys_p = file.keys()
## Diferentes Hojas
print(file['muonCCD1'].keys())

keys_f = file['muonCCD1'].keys()

mounCCD1 = file['muonCCD1']

print(mounCCD1)
print('Tree in mounCCD1')
mounCCD1.show()

DiffX = np.array(mounCCD1["DiffX"].array())
DiffY = np.array(mounCCD1["DiffY"].array())

print("DiffX",np.array(DiffX).shape)
print("DiffY",np.array(DiffY).shape)

Diff = DiffX-DiffY

d = np.array([DiffX,DiffY])
print(d.shape)
track=np.array(mounCCD1["trackNumber"].array())


print("...............Primera lectura del root allCCD1.........")

print(file['allCCD1'].keys())





plt.plot(DiffY,DiffX,'ro')
#plt.plot(track)
plt.show()
