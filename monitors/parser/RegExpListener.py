# Generated from RegExp.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RegExpParser import RegExpParser
else:
    from RegExpParser import RegExpParser

# This class defines a complete listener for a parse tree produced by RegExpParser.
class RegExpListener(ParseTreeListener):

    # Enter a parse tree produced by RegExpParser#namedExpr.
    def enterNamedExpr(self, ctx:RegExpParser.NamedExprContext):
        pass

    # Exit a parse tree produced by RegExpParser#namedExpr.
    def exitNamedExpr(self, ctx:RegExpParser.NamedExprContext):
        pass


    # Enter a parse tree produced by RegExpParser#Concat.
    def enterConcat(self, ctx:RegExpParser.ConcatContext):
        pass

    # Exit a parse tree produced by RegExpParser#Concat.
    def exitConcat(self, ctx:RegExpParser.ConcatContext):
        pass


    # Enter a parse tree produced by RegExpParser#Star.
    def enterStar(self, ctx:RegExpParser.StarContext):
        pass

    # Exit a parse tree produced by RegExpParser#Star.
    def exitStar(self, ctx:RegExpParser.StarContext):
        pass


    # Enter a parse tree produced by RegExpParser#True.
    def enterTrue(self, ctx:RegExpParser.TrueContext):
        pass

    # Exit a parse tree produced by RegExpParser#True.
    def exitTrue(self, ctx:RegExpParser.TrueContext):
        pass


    # Enter a parse tree produced by RegExpParser#Atomic.
    def enterAtomic(self, ctx:RegExpParser.AtomicContext):
        pass

    # Exit a parse tree produced by RegExpParser#Atomic.
    def exitAtomic(self, ctx:RegExpParser.AtomicContext):
        pass


    # Enter a parse tree produced by RegExpParser#Grouping.
    def enterGrouping(self, ctx:RegExpParser.GroupingContext):
        pass

    # Exit a parse tree produced by RegExpParser#Grouping.
    def exitGrouping(self, ctx:RegExpParser.GroupingContext):
        pass


    # Enter a parse tree produced by RegExpParser#Question.
    def enterQuestion(self, ctx:RegExpParser.QuestionContext):
        pass

    # Exit a parse tree produced by RegExpParser#Question.
    def exitQuestion(self, ctx:RegExpParser.QuestionContext):
        pass


    # Enter a parse tree produced by RegExpParser#Plus.
    def enterPlus(self, ctx:RegExpParser.PlusContext):
        pass

    # Exit a parse tree produced by RegExpParser#Plus.
    def exitPlus(self, ctx:RegExpParser.PlusContext):
        pass


    # Enter a parse tree produced by RegExpParser#Union.
    def enterUnion(self, ctx:RegExpParser.UnionContext):
        pass

    # Exit a parse tree produced by RegExpParser#Union.
    def exitUnion(self, ctx:RegExpParser.UnionContext):
        pass


    # Enter a parse tree produced by RegExpParser#NegAtomic.
    def enterNegAtomic(self, ctx:RegExpParser.NegAtomicContext):
        pass

    # Exit a parse tree produced by RegExpParser#NegAtomic.
    def exitNegAtomic(self, ctx:RegExpParser.NegAtomicContext):
        pass


    # Enter a parse tree produced by RegExpParser#Prop.
    def enterProp(self, ctx:RegExpParser.PropContext):
        pass

    # Exit a parse tree produced by RegExpParser#Prop.
    def exitProp(self, ctx:RegExpParser.PropContext):
        pass


    # Enter a parse tree produced by RegExpParser#Pred.
    def enterPred(self, ctx:RegExpParser.PredContext):
        pass

    # Exit a parse tree produced by RegExpParser#Pred.
    def exitPred(self, ctx:RegExpParser.PredContext):
        pass


    # Enter a parse tree produced by RegExpParser#idlist.
    def enterIdlist(self, ctx:RegExpParser.IdlistContext):
        pass

    # Exit a parse tree produced by RegExpParser#idlist.
    def exitIdlist(self, ctx:RegExpParser.IdlistContext):
        pass


