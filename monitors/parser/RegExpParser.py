# Generated from RegExp.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("=\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\5\2\r\n\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\32\n\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3(")
        buf.write("\n\3\f\3\16\3+\13\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\63\n\4")
        buf.write("\3\5\3\5\3\5\7\58\n\5\f\5\16\5;\13\5\3\5\2\3\4\6\2\4\6")
        buf.write("\b\2\2\2C\2\f\3\2\2\2\4\31\3\2\2\2\6\62\3\2\2\2\b\64\3")
        buf.write("\2\2\2\n\13\7\16\2\2\13\r\7\3\2\2\f\n\3\2\2\2\f\r\3\2")
        buf.write("\2\2\r\16\3\2\2\2\16\17\5\4\3\2\17\3\3\2\2\2\20\21\b\3")
        buf.write("\1\2\21\32\7\4\2\2\22\32\5\6\4\2\23\24\7\5\2\2\24\32\5")
        buf.write("\6\4\2\25\26\7\13\2\2\26\27\5\4\3\2\27\30\7\f\2\2\30\32")
        buf.write("\3\2\2\2\31\20\3\2\2\2\31\22\3\2\2\2\31\23\3\2\2\2\31")
        buf.write("\25\3\2\2\2\32)\3\2\2\2\33\34\f\5\2\2\34\35\7\t\2\2\35")
        buf.write("(\5\4\3\6\36\37\f\4\2\2\37 \7\n\2\2 (\5\4\3\5!\"\f\b\2")
        buf.write("\2\"(\7\6\2\2#$\f\7\2\2$(\7\7\2\2%&\f\6\2\2&(\7\b\2\2")
        buf.write("\'\33\3\2\2\2\'\36\3\2\2\2\'!\3\2\2\2\'#\3\2\2\2\'%\3")
        buf.write("\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\5\3\2\2\2+)\3\2")
        buf.write("\2\2,\63\7\16\2\2-.\7\16\2\2./\7\13\2\2/\60\5\b\5\2\60")
        buf.write("\61\7\f\2\2\61\63\3\2\2\2\62,\3\2\2\2\62-\3\2\2\2\63\7")
        buf.write("\3\2\2\2\649\7\16\2\2\65\66\7\r\2\2\668\7\16\2\2\67\65")
        buf.write("\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:\t\3\2\2\2;9")
        buf.write("\3\2\2\2\b\f\31\')\629")
        return buf.getvalue()


class RegExpParser ( Parser ):

    grammarFileName = "RegExp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'True'", "'!'", "'*'", "'+'", 
                     "'?'", "';'", "'|'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "WS" ]

    RULE_namedExpr = 0
    RULE_expr = 1
    RULE_atom = 2
    RULE_idlist = 3

    ruleNames =  [ "namedExpr", "expr", "atom", "idlist" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    IDENTIFIER=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class NamedExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.child = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)


        def IDENTIFIER(self):
            return self.getToken(RegExpParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return RegExpParser.RULE_namedExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamedExpr" ):
                listener.enterNamedExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamedExpr" ):
                listener.exitNamedExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamedExpr" ):
                return visitor.visitNamedExpr(self)
            else:
                return visitor.visitChildren(self)




    def namedExpr(self):

        localctx = RegExpParser.NamedExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_namedExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 8
                localctx.name = self.match(RegExpParser.IDENTIFIER)
                self.state = 9
                self.match(RegExpParser.T__0)


            self.state = 12
            localctx.child = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegExpParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ConcatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegExpParser.ExprContext)
            else:
                return self.getTypedRuleContext(RegExpParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcat" ):
                listener.enterConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcat" ):
                listener.exitConcat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat" ):
                return visitor.visitConcat(self)
            else:
                return visitor.visitChildren(self)


    class StarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStar" ):
                listener.enterStar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStar" ):
                listener.exitStar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStar" ):
                return visitor.visitStar(self)
            else:
                return visitor.visitChildren(self)


    class TrueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrue" ):
                listener.enterTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrue" ):
                listener.exitTrue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrue" ):
                return visitor.visitTrue(self)
            else:
                return visitor.visitChildren(self)


    class AtomicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.child = None # AtomContext
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(RegExpParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomic" ):
                listener.enterAtomic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomic" ):
                listener.exitAtomic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic" ):
                return visitor.visitAtomic(self)
            else:
                return visitor.visitChildren(self)


    class GroupingContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrouping" ):
                listener.enterGrouping(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrouping" ):
                listener.exitGrouping(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrouping" ):
                return visitor.visitGrouping(self)
            else:
                return visitor.visitChildren(self)


    class QuestionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuestion" ):
                listener.enterQuestion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuestion" ):
                listener.exitQuestion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuestion" ):
                return visitor.visitQuestion(self)
            else:
                return visitor.visitChildren(self)


    class PlusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlus" ):
                listener.enterPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlus" ):
                listener.exitPlus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlus" ):
                return visitor.visitPlus(self)
            else:
                return visitor.visitChildren(self)


    class UnionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegExpParser.ExprContext)
            else:
                return self.getTypedRuleContext(RegExpParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnion" ):
                listener.enterUnion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnion" ):
                listener.exitUnion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnion" ):
                return visitor.visitUnion(self)
            else:
                return visitor.visitChildren(self)


    class NegAtomicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.child = None # AtomContext
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(RegExpParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegAtomic" ):
                listener.enterNegAtomic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegAtomic" ):
                listener.exitNegAtomic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegAtomic" ):
                return visitor.visitNegAtomic(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RegExpParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegExpParser.T__1]:
                localctx = RegExpParser.TrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 15
                self.match(RegExpParser.T__1)
                pass
            elif token in [RegExpParser.IDENTIFIER]:
                localctx = RegExpParser.AtomicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                localctx.child = self.atom()
                pass
            elif token in [RegExpParser.T__2]:
                localctx = RegExpParser.NegAtomicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(RegExpParser.T__2)
                self.state = 18
                localctx.child = self.atom()
                pass
            elif token in [RegExpParser.T__8]:
                localctx = RegExpParser.GroupingContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 19
                self.match(RegExpParser.T__8)
                self.state = 20
                localctx.child = self.expr(0)
                self.state = 21
                self.match(RegExpParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = RegExpParser.ConcatContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 25
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 26
                        self.match(RegExpParser.T__6)
                        self.state = 27
                        localctx.right = self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = RegExpParser.UnionContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 29
                        self.match(RegExpParser.T__7)
                        self.state = 30
                        localctx.right = self.expr(3)
                        pass

                    elif la_ == 3:
                        localctx = RegExpParser.StarContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.child = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 32
                        self.match(RegExpParser.T__3)
                        pass

                    elif la_ == 4:
                        localctx = RegExpParser.PlusContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.child = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 34
                        self.match(RegExpParser.T__4)
                        pass

                    elif la_ == 5:
                        localctx = RegExpParser.QuestionContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.child = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 36
                        self.match(RegExpParser.T__5)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegExpParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PropContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.AtomContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(RegExpParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProp" ):
                listener.enterProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProp" ):
                listener.exitProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProp" ):
                return visitor.visitProp(self)
            else:
                return visitor.visitChildren(self)


    class PredContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.AtomContext
            super().__init__(parser)
            self.name = None # Token
            self.args = None # IdlistContext
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(RegExpParser.IDENTIFIER, 0)
        def idlist(self):
            return self.getTypedRuleContext(RegExpParser.IdlistContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPred" ):
                listener.enterPred(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPred" ):
                listener.exitPred(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPred" ):
                return visitor.visitPred(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = RegExpParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = RegExpParser.PropContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                localctx.name = self.match(RegExpParser.IDENTIFIER)
                pass

            elif la_ == 2:
                localctx = RegExpParser.PredContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                localctx.name = self.match(RegExpParser.IDENTIFIER)
                self.state = 44
                self.match(RegExpParser.T__8)
                self.state = 45
                localctx.args = self.idlist()
                self.state = 46
                self.match(RegExpParser.T__9)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.param = None # Token

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(RegExpParser.IDENTIFIER)
            else:
                return self.getToken(RegExpParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return RegExpParser.RULE_idlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdlist" ):
                listener.enterIdlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdlist" ):
                listener.exitIdlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = RegExpParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            localctx.param = self.match(RegExpParser.IDENTIFIER)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RegExpParser.T__10:
                self.state = 51
                self.match(RegExpParser.T__10)
                self.state = 52
                localctx.param = self.match(RegExpParser.IDENTIFIER)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         




