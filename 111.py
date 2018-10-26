from hyperparams import Hyperparams as hp
import numpy as np
list_of_refs = []
mname = open(hp.logdir + '/checkpoint', 'r').read().split('"') # model name
a = 'source: Das ist ein Baum'
ref = a.split()
print(ref)
list_of_refs.append([ref])
print(list_of_refs)