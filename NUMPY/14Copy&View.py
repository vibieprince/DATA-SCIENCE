import numpy as np
var = np.array([29,3,1,5,74])
cop = var.copy() # changes affect internally only
vi = var.view() # changes here affects universally
print("Var : ",var)
print("Var copy : ",cop)
print("Var view : ",vi)

var[1] = 60
print("Var : ",var)
print("Var copy : ",cop)
print("Var view : ",vi)

vi[2] = 90
print("Var : ",var)
print("Var copy : ",cop)
print("Var view : ",vi)
