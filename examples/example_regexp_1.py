from monitors import regexp

def p1(x):
    return x < 5

def p2(x):
	return x > 12

my_reg_monitor = regexp.monitor("True*; p1(x); p2(x)+; p1(x)+", ext_objects={'p1': p1, 'p2': p2})

for n in [1, 1, 1, 1, 13, 13, 14, 1, 1, 2]:
	output = my_reg_monitor.update(x = n)
	print(output, my_reg_monitor.states)

