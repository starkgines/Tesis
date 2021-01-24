import uproot
import numpy as np


file = uproot.open("http://scikit-hep.org/uproot3/examples/nesteddirs.root")

print('..............useful functions................')
print("FILE : ", file)
print("FILE KEYS : ",file.keys())
keys = file.keys()
print('KEYS[0]:', keys[0])
print("FILE['one']",file[keys[0]].keys())
print("Value File['one']",file[keys[0]].values())


print('.................read events...................')

events = uproot.open("http://scikit-hep.org/uproot3/examples/Zmumu.root")["events"]
print("EVENTOS: ",events.keys())

events.show()


print('.................Reading arrays from a TTree...................')

a = events["E1"].array()
print("ARRAY E1 length:", np.array(a).shape)

print("Array E1 Values:",np.array(a))


print("................Finalizo....................")