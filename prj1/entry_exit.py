import sys
import time

for i in range(2):
    sys.stdout.write('{:03d} '.format(i))
    time.sleep(1)
#   sys.stdout.write('\r')

# return occupied free_space