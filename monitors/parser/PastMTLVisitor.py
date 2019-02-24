# Generated from PastMTL.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PastMTLParser import PastMTLParser
else:
    from PastMTLParser import PastMTLParser

# This class defines a complete generic visitor for a parse tree produced by PastMTLParser.

class PastMTLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PastMTLParser#namedExpr.
    def visitNamedExpr(self, ctx:PastMTLParser.NamedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#TimedAlwaysInf.
    def visitTimedAlwaysInf(self, ctx:PastMTLParser.TimedAlwaysInfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#TimedAlways.
    def visitTimedAlways(self, ctx:PastMTLParser.TimedAlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#Negation.
    def visitNegation(self, ctx:PastMTLParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#Once.
    def visitOnce(self, ctx:PastMTLParser.OnceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#TimedSince.
    def visitTimedSince(self, ctx:PastMTLParser.TimedSinceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#Previously.
    def visitPreviously(self, ctx:PastMTLParser.PreviouslyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#TimedSinceInf.
    def visitTimedSinceInf(self, ctx:PastMTLParser.TimedSinceInfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#Atomic.
    def visitAtomic(self, ctx:PastMTLParser.AtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#Grouping.
    def visitGrouping(self, ctx:PastMTLParser.GroupingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#TimedOnce.
    def visitTimedOnce(self, ctx:PastMTLParser.TimedOnceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#Disjunction.
    def visitDisjunction(self, ctx:PastMTLParser.DisjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#Implies.
    def visitImplies(self, ctx:PastMTLParser.ImpliesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#Conjunction.
    def visitConjunction(self, ctx:PastMTLParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#Since.
    def visitSince(self, ctx:PastMTLParser.SinceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#Always.
    def visitAlways(self, ctx:PastMTLParser.AlwaysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#TimedOnceInf.
    def visitTimedOnceInf(self, ctx:PastMTLParser.TimedOnceInfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#Prop.
    def visitProp(self, ctx:PastMTLParser.PropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#Pred.
    def visitPred(self, ctx:PastMTLParser.PredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PastMTLParser#idlist.
    def visitIdlist(self, ctx:PastMTLParser.IdlistContext):
        return self.visitChildren(ctx)



del PastMTLParser