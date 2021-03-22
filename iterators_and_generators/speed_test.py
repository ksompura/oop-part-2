import time

gen_start_time = time.time()
print(sum(n for n in range(100000000))) # generator expression ()
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(100000000)])) # list comprehension []
list_time = time.time() - list_start_time

print(f"sum(n for n in range(10000000)) took: {gen_time}")
print(f"sum([n for n in range(10000000)]) took: {list_time}")

# generator expressions are faster than list comprehensions because list has to first create the list and then sum