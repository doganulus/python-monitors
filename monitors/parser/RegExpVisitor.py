# Generated from RegExp.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RegExpParser import RegExpParser
else:
    from RegExpParser import RegExpParser

# This class defines a complete generic visitor for a parse tree produced by RegExpParser.

class RegExpVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RegExpParser#namedExpr.
    def visitNamedExpr(self, ctx:RegExpParser.NamedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Concat.
    def visitConcat(self, ctx:RegExpParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Star.
    def visitStar(self, ctx:RegExpParser.StarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#True.
    def visitTrue(self, ctx:RegExpParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Atomic.
    def visitAtomic(self, ctx:RegExpParser.AtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Grouping.
    def visitGrouping(self, ctx:RegExpParser.GroupingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Question.
    def visitQuestion(self, ctx:RegExpParser.QuestionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Plus.
    def visitPlus(self, ctx:RegExpParser.PlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Union.
    def visitUnion(self, ctx:RegExpParser.UnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#NegAtomic.
    def visitNegAtomic(self, ctx:RegExpParser.NegAtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Prop.
    def visitProp(self, ctx:RegExpParser.PropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#Pred.
    def visitPred(self, ctx:RegExpParser.PredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RegExpParser#idlist.
    def visitIdlist(self, ctx:RegExpParser.IdlistContext):
        return self.visitChildren(ctx)



del RegExpParser