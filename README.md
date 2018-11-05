# About python-monitors
 python-monitors` is a pure Python package to monitor formal specifications over temporal sequences. It supports several specification languages such as regular expressions and variants of temporal logic. The usage is fairly easy thanks to Python and allows fast prototyping of applications that monitor temporal sequences using these specifications. For high-performance monitoring tasks, please see the project [Reelay](https://github.com/doganulus/reelay) that targets C++ applications.

# Install
The latest release of the package can be installed via `pip` such that

    pip install python-monitors

This command will also install dependencies `python-intervals` and `antlr4-python3-runtime`.

# Use

## MTL over propositions

First generate a monitor from past Metric Temporal Logic (MTL) formula:

    from monitors import mtl
     
	my_mtl_monitor = mtl.monitor("always(q -> once[2,4](p))")

Then process a data sequence (over propositions) by updating the monitor and collecting the output at each step:

	data = dict(
		p = [False, True,  False, False, False, False, False, True,  False, False, False, False, False, False, False], 
		q = [False, False, False, False, False, True,  False, False, False, False, False, False, False, False, True ]
	)
     
	for p, q in zip(data['p'], data['q']):
     
		output = my_mtl_monitor.update(p = p, q = q)
     
		print(my_mtl_monitor.time, output, my_mtl_monitor.states)


## MTL over predicates (also known as STL)

Any Boolean-valued Python function can be used as a predicate in MTL formulas. They are passed to monitor construction via a dictionary as follows:

	def p1(x):
	    return x < 5
     
    my_mtl_monitor = mtl.monitor("always[0,5](p1(x))", ext_objects={'p1': p1})
     
    for n in [9, 13, 4, 1, 2, 3,1,1,1,2]:
	    output = my_mtl_monitor.update(x = n)
	    print(my_mtl_monitor.time, p1(n), output, my_mtl_monitor.states)
	

## Regular expressions over propositions and predicates

Regular expressions over propositions and predicates are available in a similar fashion:

    from monitors import regexp
     
    def p1(x):
        return x < 5
     
    def p2(x):
	    return x > 12
     
    my_reg_monitor = regexp.monitor("True*; p1(x); p2(x)+; p1(x)+", ext_objects={'p1': p1, 'p2': p2}, print_source_code=True)
     
    for n in [1, 1, 1, 1, 13, 13, 14, 1, 1, 2]:
	    output = my_reg_monitor.update(x = n)
	    print(output, my_reg_monitor.states)