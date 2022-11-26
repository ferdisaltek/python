import sys

liste=[i*2 for i in range(1000)]
print(sys.getsizeof(liste))

gen=(i**2 for i in range(1000))
print(sys.getsizeof(gen))

import time

list_start_time = time.time()
sum([i**2 for i in range(10000)])
list_stop = time.time() - list_start_time

gen_start_time = time.time()
sum((i**2 for i in range(10000)))
gen_stop = time.time() - gen_start_time

print(list_stop, gen_stop)
