from antlr4 import *

from monitors.parser.PastMTLLexer import PastMTLLexer
from monitors.parser.PastMTLParser import PastMTLParser
from monitors.parser.PastMTLVisitor import PastMTLVisitor

import intervals

class BaseMonitor:
    def update_timed_since_inf(self, now, state, left, right, lower):
        if left and right:
            return (state & intervals.closed(self.time, intervals.inf)) | intervals.closed(self.time + lower, intervals.inf)
        elif not left and right:
            return intervals.closed(self.time + lower, intervals.inf)
        elif left and not right:
            return (state & intervals.closed(self.time, intervals.inf))
        else:
            return intervals.empty()

    def update_timed_since(self, now, state, left, right, lower, upper):
        if left and right:
            return (state & intervals.closed(self.time, intervals.inf)) | intervals.closed(self.time + lower, self.time + upper)
        elif not left and right:
            return intervals.closed(self.time + lower, self.time + upper)
        elif left and not right:
            return (state & intervals.closed(self.time, intervals.inf))
        else:
            return intervals.empty()

    def output_timed(self, state):
        return self.time in state


def monitor(pattern, ext_objects=dict(), class_name=None, print_source_code=False):
        
    "Compile a past linear-time temporal logic formula"

    lexer = PastMTLLexer(InputStream(pattern))
    stream = CommonTokenStream(lexer)
    parser = PastMTLParser(stream)
    tree = parser.namedExpr()

    # lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)

    builder = PastMTLBuilder()
    init, update_stmt, output = builder.build(tree)

    if class_name != None:
        name = class_name
    else:
        name = builder.name

    statements = []
    statements += ["import intervals"]
    statements += ["from monitors.mtl import BaseMonitor"]
    statements += [""]
    statements += ["class {class_name}(BaseMonitor):".format(class_name=name)]
    statements += [""]
    statements += ["\ttime = -1"]
    statements += ["\tstates = [{}]".format(", ".join([str(init) for init in builder.initialization]))]
    # statements += ["\tprev_states = [{}]".format(", ".join([str(init) for init in builder.initialization]))]
    statements += [""]
    statements += ["\tdef update(self, **kwargs):"]
    statements += [""]
    statements += ["\t\tself.time = self.time + 1"]
    statements += ["\t\t{}".format(statement) for statement in update_stmt]
    statements += [""]
    statements += ["\t\treturn {}".format(builder.output)]

    source = '\n'.join(statements)

    if print_source_code:
        print(source)

    code = compile(source, "<string>", "exec")

    exec(code, ext_objects)

    return ext_objects[name]()

    # data = []
    # for letter in df.itertuples():
    #     exec(machine, globals(), {**local_dict, **locals()})
    #     prev_states = np.copy(states)
    #     data.append(output[0])
    #     # print(states[0] == db.const(False))

    # new_frame = pd.DataFrame(columns=[builder.name], data=data)




class PastMTLBuilder(PastMTLVisitor):

    def __init__(self):
        super().__init__()
        self.num = 0
        self.name = "Monitor"
        self.initialization = list()
        self.statements = list()
        self.variables = set()
        self.output = set()

    def build(self, tree, length=20):
        self.output = self.visit(tree)
        label = "states[{}]".format(self.num)

        # self.statements.append('output[0] = True if states[-1] == db.bdd.true else False;')

        return self.initialization, self.statements, self.output

    def visitNamedExpr(self, ctx:PastMTLParser.NamedExprContext):
        try:
            self.name = ctx.name.text
        except AttributeError as e:
            self.name = "Monitor"

        return self.visit(ctx.child)

    def visitProp(self, ctx:PastMTLParser.PropContext):
        name = ctx.name.text
        return "kwargs['{}']".format(name)

    def visitPred(self, ctx:PastMTLParser.PredContext):
        name = ctx.name.text
        args = ctx.args.getText().split(',')
        nargs = ["kwargs['{}']".format(arg) for arg in args] 

        return "{name}({params})".format(name=name, params=', '.join(nargs))

    def visitNegation(self, ctx:PastMTLParser.NegationContext):
        child = self.visit(ctx.child)
        label = "self.states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{} = not({});".format(label, child))
        self.num = self.num + 1 

        return label

    def visitDisjunction(self, ctx:PastMTLParser.DisjunctionContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        label = "self.states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{} = {} or {};".format(label, left, right))
        self.num = self.num + 1 

        return label

    def visitConjunction(self, ctx:PastMTLParser.ConjunctionContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        label = "self.states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{} = {} and {};".format(label, left, right))
        self.num = self.num + 1 

        return label

    def visitImplies(self, ctx:PastMTLParser.ImpliesContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        label = "self.states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{} = not {} or {};".format(label, left, right))
        self.num = self.num + 1 

        return label

    def visitSince(self, ctx:PastMTLParser.SinceContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        label = "self.states[{}]".format(self.num)

        self.initialization.append(False)
        self.statements.append("{label} = {right} or ({left} and {label});".format(label=label, left=left, right=right))
        self.num = self.num + 1 

        return label

    def visitTimedSince(self, ctx:PastMTLParser.TimedSinceContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        min_val = ctx.l.text
        max_val = ctx.u.text

        label = "self.states[{}]".format(self.num)
        self.initialization.append("intervals.empty()")
        self.statements.append("{label} = self.update_timed_since(self.time, {label}, {left}, {right}, {min_val}, {max_val})".format(label=label, left=left, right=right, min_val=min_val, max_val=max_val)) 
        self.num = self.num + 1

        return "self.output_timed({})".format(label)

    def visitTimedSinceInf(self, ctx:PastMTLParser.TimedSinceInfContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)

        min_val = ctx.l.text

        label = "self.states[{}]".format(self.num)
        self.initialization.append("intervals.empty()")
        self.statements.append("{label} = self.update_timed_since_inf(self.time, {label}, {left}, {right}, {min_val})".format(label=label, left=left, right=right, min_val=min_valdInf)) 
        self.num = self.num + 1

        return "self.output_timed({})".format(label)

    def visitAlways(self, ctx:PastMTLParser.AlwaysContext):
        child = self.visit(ctx.child)
        label = "self.states[{}]".format(self.num)

        self.initialization.append(True)
        self.statements.append("{label} = {label} and {child};".format(label=label, child=child))
        self.num = self.num + 1 

        return label

    def visitTimedAlways(self, ctx:PastMTLParser.TimedAlwaysContext):
        child = self.visit(ctx.child)
        label = "self.states[{}]".format(self.num)

        min_val = ctx.l.text
        max_val = ctx.u.text

        self.initialization.append("intervals.empty()")
        self.statements.append("{label} = self.update_timed_since(self.time, {label}, True, not {right}, {min_val}, {max_val})".format(label=label, right=child, min_val=min_val, max_val=max_val)) 
        self.num = self.num + 1

        return "not(self.output_timed({}))".format(label)

    def visitTimedAlwaysInf(self, ctx:PastMTLParser.TimedAlwaysInfContext):
        child = self.visit(ctx.child)
        label = "self.states[{}]".format(self.num)

        min_val = ctx.l.text

        self.initialization.append("intervals.empty()")
        self.statements.append("{label} = self.update_timed_since_inf(self.time, {label}, True, not {right}, {min_val})".format(label=label, right=child, min_val=min_val)) 
        self.num = self.num + 1

        return "not(self.output_timed({}))".format(label)

    def visitOnce(self, ctx:PastMTLParser.OnceContext):
        child = self.visit(ctx.child)
        label = "self.states[{}]".format(self.num)

        self.initialization.append(list())
        self.statements.append("{label} = {label} or {child};".format(label=label, child=child))
        self.num = self.num + 1 

        return label

    def visitTimedOnce(self, ctx:PastMTLParser.TimedOnceContext):
        child = self.visit(ctx.child)
        label = "self.states[{}]".format(self.num)

        min_val = ctx.l.text
        max_val = ctx.u.text

        self.initialization.append("intervals.empty()")
        self.statements.append("{label} = self.update_timed_since(self.time, {label}, True, {right}, {min_val}, {max_val})".format(label=label, right=child, min_val=min_val, max_val=max_val)) 
        self.num = self.num + 1

        return "self.output_timed({})".format(label)

    def visitTimedOnceInf(self, ctx:PastMTLParser.TimedOnceInfContext):
        child = self.visit(ctx.child)
        label = "self.states[{}]".format(self.num)

        min_val = ctx.l.text

        self.initialization.append("intervals.empty()")
        self.statements.append("{label} = self.update_timed_since_inf(self.time, {label}, True, {right}, {min_val})".format(label=label, right=child, min_val=min_val)) 
        self.num = self.num + 1

        return "self.output_timed({})".format(label)

    # Visit a parse tree produced by PastMTLParser#Grouping.
    def visitGrouping(self, ctx:PastMTLParser.GroupingContext):
        return self.visit(ctx.child)

class BaseMTL:
    def update_timed_since(self, state, left, right, lower, upper):
        pass