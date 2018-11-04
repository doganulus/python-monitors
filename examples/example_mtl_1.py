from monitors import mtl

my_mtl_monitor = mtl.monitor("always(q -> once[2,4](p))")

data = dict(
	p = [False, True,  False, False, False, False, False, True,  False, False, False, False, False, False, False], 
	q = [False, False, False, False, False, True,  False, False, False, False, False, False, False, False, True ]
)

for p, q in zip(data['p'], data['q']):

	output = my_mtl_monitor.update(p = p, q = q)

	print(my_mtl_monitor.time, output, my_mtl_monitor.states)


