from antlr4 import *

from monitors.parser.RegExpLexer import RegExpLexer
from monitors.parser.RegExpParser import RegExpParser
from monitors.parser.RegExpVisitor import RegExpVisitor

import intervals

class BaseMonitor:
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
    "Compile a regular expression"

    lexer = RegExpLexer(InputStream(pattern))
    stream = CommonTokenStream(lexer)
    parser = RegExpParser(stream)
    tree = parser.namedExpr()

    # lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)

    # Annotate the syntax tree with positions, nullable values, and output positions 
    annotator = RegExpAnnotator()
    annotator.visit(tree)

    builder = RegExpBuilder()
    builder.build(tree)

    if class_name != None:
        name = class_name
    else:
        name = builder.name

    statements = []
    statements += ["class {class_name}: ".format(class_name=name)]
    statements += [""]
    statements += ["\tstates = [{}]".format(", ".join([str(init) for init in builder.initialization]))]
    statements += ["\tprev_states = [{}]".format(", ".join([str(init) for init in builder.initialization]))]
    statements += [""]
    statements += ["\tdef update(self, **kwargs):"]
    statements += [""]
    statements += ["\t\tself.prev_states = self.states.copy()"]
    statements += [""]
    statements += ["\t\t{}".format(statement) for statement in builder.statements]
    statements += [""]
    statements += ["\t\treturn {}".format(builder.output)]

    source = '\n'.join(statements)

    if print_source_code:
        print(source)

    code = compile(source, "<string>", "exec")

    exec(code, ext_objects)

    return ext_objects[name]()


class RegExpBuilder(RegExpVisitor):

    def __init__(self):
        super().__init__()
        self.name = "Monitor"
        self.statements = list()
        self.variables = set([])

    def build(self, tree, trigger_init=set([0])):

        # Start anywhere
        self.statements.append("self.states[0] = False")

        self.walk(tree, trigger_init)

        self.output = ' or '.join(['self.states[{}]'.format(i) for i in tree.output])

        # Zeroth state should be True initially
        self.initialization = [True]
        self.initialization.extend([False] * (len(self.statements) -1 ))

        return self.initialization, self.statements, self.output

    def walk(self, tree, trigger=set([0])):
        tree.trigger = trigger
        self.visit(tree)

    def visitNamedExpr(self, ctx:RegExpParser.NamedExprContext):
        try:
            self.name = ctx.name.text
        except AttributeError as e:
            self.name = "Monitor"

        self.walk(ctx.child, ctx.trigger)

    def visitTrue(self, ctx:RegExpParser.TrueContext):
        trig_cond = " or ".join(['self.prev_states[{}]'.format(i) for i in ctx.trigger])
        self.statements.append("self.states[{}] = {};".format(ctx.position, trig_cond))

    def visitAtomic(self, ctx:RegExpParser.AtomicContext):
        trig_cond = " or ".join(['self.prev_states[{}]'.format(i) for i in ctx.trigger])
        self.statements.append("self.states[{}] = {} and ({});".format(ctx.position, ctx.child.callname, trig_cond))

    def visitNegAtomic(self, ctx:RegExpParser.NegAtomicContext):
        trig_cond = " or ".join(['self.prev_states[{}]'.format(i) for i in ctx.trigger])
        self.statements.append("self.states[{}] = not {} and ({});".format(ctx.position, ctx.child.callname, trig_cond))

    def visitUnion(self, ctx:RegExpParser.UnionContext):
        self.walk(ctx.left, ctx.trigger)
        self.walk(ctx.right, ctx.trigger)

    # Visit a parse tree produced by RegExpParser#Concat.
    def visitConcat(self, ctx:RegExpParser.ConcatContext):

        self.walk(ctx.left, ctx.trigger)

        if ctx.left.nullable:
            self.walk(ctx.right, ctx.left.output | ctx.trigger)
        else:
            self.walk(ctx.right, ctx.left.output)

    # Visit a parse tree produced by RegExpParser#Star.
    def visitStar(self, ctx:RegExpParser.StarContext):
        self.walk(ctx.child, ctx.child.output | ctx.trigger)

    # Visit a parse tree produced by RegExpParser#Grouping.
    def visitGrouping(self, ctx:RegExpParser.GroupingContext):
        self.walk(ctx.child, ctx.trigger)

    # Visit a parse tree produced by RegExpParser#Question.
    def visitQuestion(self, ctx:RegExpParser.QuestionContext):
        self.walk(ctx.child, ctx.child.output | ctx.trigger)

    # Visit a parse tree produced by RegExpParser#Plus.
    def visitPlus(self, ctx:RegExpParser.PlusContext):
        self.walk(ctx.child, ctx.child.output | ctx.trigger)


class RegExpAnnotator(RegExpVisitor):

    def __init__(self):
        super().__init__()
        self.num = 1
        self.variables = set()

        self.name = None
        self.statements = list()

    def visitNamedExpr(self, ctx:RegExpParser.NamedExprContext):
        
        self.visit(ctx.child)

        try:
            ctx.name = ctx.name.text
        except AttributeError as e:
            ctx.name = None
        finally:
            ctx.nullable = ctx.child.nullable
            ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

    def visitTrue(self, ctx:RegExpParser.TrueContext):

        ctx.nullable = False
        ctx.output = set([self.num])
        ctx.position = self.num
        ctx.callname = "True"
        self.num = self.num + 1 

        return self.num, ctx.nullable, ctx.output

    def visitProp(self, ctx:RegExpParser.PropContext):

        ctx.nullable = False
        ctx.output = set([self.num])
        ctx.position = self.num
        ctx.callname = "kwargs['{}']".format(ctx.name.text)
        self.num = self.num + 1 

        return self.num, ctx.nullable, ctx.output

    def visitPred(self, ctx:RegExpParser.PredContext):
        name = ctx.name.text
        nargs = ["kwargs['{}']".format(arg) for arg in ctx.args.getText().split(',')]

        ctx.callname = "{name}({params})".format(name=name, params=','.join(nargs))

        ctx.nullable = False
        ctx.output = set([self.num])
        ctx.position = self.num

        self.num = self.num + 1 

        return self.num, ctx.nullable, ctx.output

    def visitAtomic(self, ctx:RegExpParser.AtomicContext):

        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable
        ctx.output = ctx.child.output
        ctx.position = ctx.child.position

        return self.num, ctx.nullable, ctx.output

    def visitNegAtomic(self, ctx:RegExpParser.NegAtomicContext):

        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable
        ctx.output = ctx.child.output
        ctx.position = ctx.child.position

        return self.num, ctx.nullable, ctx.output

    def visitUnion(self, ctx:RegExpParser.UnionContext):
        self.visit(ctx.left)
        self.visit(ctx.right)

        ctx.nullable = ctx.left.nullable or ctx.right.nullable
        ctx.output = ctx.left.output | ctx.right.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by RegExpParser#Concat.
    def visitConcat(self, ctx:RegExpParser.ConcatContext):

        self.visit(ctx.left)
        self.visit(ctx.right)

        ctx.nullable = ctx.left.nullable and ctx.right.nullable
        ctx.output = ctx.left.output | ctx.right.output if ctx.right.nullable else ctx.right.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by RegExpParser#Star.
    def visitStar(self, ctx:RegExpParser.StarContext):

        self.visit(ctx.child)

        ctx.nullable = True
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by RegExpParser#Grouping.
    def visitGrouping(self, ctx:RegExpParser.GroupingContext):

        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by RegExpParser#Question.
    def visitQuestion(self, ctx:RegExpParser.QuestionContext):

        self.visit(ctx.child)

        ctx.nullable = True
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output

    # Visit a parse tree produced by RegExpParser#Plus.
    def visitPlus(self, ctx:RegExpParser.PlusContext):

        self.visit(ctx.child)

        ctx.nullable = ctx.child.nullable 
        ctx.output = ctx.child.output

        return self.num, ctx.nullable, ctx.output