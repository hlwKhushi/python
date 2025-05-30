# Without using function(def):
'''
a = 5
b = 13
gmean = (a*b)/(a+b)
print(gmean)
'''
# using function(def):::
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
    a = 15
    b = 51
    calculateGmean(a,b)

