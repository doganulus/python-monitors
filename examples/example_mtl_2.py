from monitors import mtl

def p1(x):
	return x < 5
     
my_mtl_monitor = mtl.monitor("always[0,5](p1(x))", p1=p1)

for n in [9, 13, 4, 1, 2, 3,1,1,1,2]:
	output = my_mtl_monitor.update(x = n)
	print(my_mtl_monitor.time, p1(n), output, my_mtl_monitor.states)

