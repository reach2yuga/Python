from array import *
vals = array('i',[5,9,-8,4,2])

newarr = array(vals.typecode,(a for a in vals))

for i in newarr:
    print(i)