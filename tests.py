
##### * * * * * * * * * * * * * * * TESTS * * * * * * * * * * * * * * * #####

print()
print('Edit distance between \
kitten and sitting is ',dist('kitten','sitting'),'.',sep='')
from Ldistance import *

print('The alignment of that distance looks like:')
alignment('kitten','sitting')
print()

print('Edit distance between \
kitten and kitten is ',dist('kitten','kitten'),'.',sep='')
print('The alignment of that distance looks like:')
alignment('kitten','kitten')
print()

print('Edit distance between \
kitten and mitten is ',dist('kitten','mitten'),'.',sep='')
print('The alignment of that distance looks like:')
alignment('kitten','mitten')
print()

print('Edit distance between \
mittens and smitten is ',dist('mittens','smitten'),'.',sep='')
print('The alignment of that distance looks like:')
alignment('mittens','smitten')
print()

print('Edit distance between \
Sunday and Saturday is ',dist('Sunday','Saturday'),'.',sep='')
print('The alignment of that distance looks like:')
alignment('Sunday','Saturday')
print()
