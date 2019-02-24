# Generated from RegExp.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\5\2\r\n\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\64\n\3\f")
        buf.write("\3\16\3\67\13\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4?\n\4\3\5\3")
        buf.write("\5\3\5\7\5D\n\5\f\5\16\5G\13\5\3\5\2\3\4\6\2\4\6\b\2\2")
        buf.write("\2R\2\f\3\2\2\2\4\"\3\2\2\2\6>\3\2\2\2\b@\3\2\2\2\n\13")
        buf.write("\7\23\2\2\13\r\7\3\2\2\f\n\3\2\2\2\f\r\3\2\2\2\r\16\3")
        buf.write("\2\2\2\16\17\5\4\3\2\17\3\3\2\2\2\20\21\b\3\1\2\21#\7")
        buf.write("\4\2\2\22#\5\6\4\2\23\24\7\5\2\2\24#\5\6\4\2\25\26\7\23")
        buf.write("\2\2\26\27\7\6\2\2\27#\5\6\4\2\30\31\7\7\2\2\31\32\7\b")
        buf.write("\2\2\32\33\5\b\5\2\33\34\7\t\2\2\34\35\5\4\3\n\35#\3\2")
        buf.write("\2\2\36\37\7\20\2\2\37 \5\4\3\2 !\7\21\2\2!#\3\2\2\2\"")
        buf.write("\20\3\2\2\2\"\22\3\2\2\2\"\23\3\2\2\2\"\25\3\2\2\2\"\30")
        buf.write("\3\2\2\2\"\36\3\2\2\2#\65\3\2\2\2$%\f\6\2\2%&\7\r\2\2")
        buf.write("&\64\5\4\3\7\'(\f\5\2\2()\7\16\2\2)\64\5\4\3\6*+\f\4\2")
        buf.write("\2+,\7\17\2\2,\64\5\4\3\5-.\f\t\2\2.\64\7\n\2\2/\60\f")
        buf.write("\b\2\2\60\64\7\13\2\2\61\62\f\7\2\2\62\64\7\f\2\2\63$")
        buf.write("\3\2\2\2\63\'\3\2\2\2\63*\3\2\2\2\63-\3\2\2\2\63/\3\2")
        buf.write("\2\2\63\61\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66\3")
        buf.write("\2\2\2\66\5\3\2\2\2\67\65\3\2\2\28?\7\23\2\29:\7\23\2")
        buf.write("\2:;\7\20\2\2;<\5\b\5\2<=\7\21\2\2=?\3\2\2\2>8\3\2\2\2")
        buf.write(">9\3\2\2\2?\7\3\2\2\2@E\7\23\2\2AB\7\22\2\2BD\7\23\2\2")
        buf.write("CA\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\t\3\2\2\2GE")
        buf.write("\3\2\2\2\b\f\"\63\65>E")
        return buf.getvalue()


class RegExpParser ( Parser ):

    grammarFileName = "RegExp.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'True'", "'!'", "'<='", "'exists'", 
                     "'{'", "'}'", "'*'", "'+'", "'?'", "';'", "'&'", "'|'", 
                     "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IDENTIFIER", "NUMBER", "WS" ]

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
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    IDENTIFIER=17
    NUMBER=18
    WS=19

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


    class VarBindContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.var = None # Token
            self.child = None # AtomContext
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(RegExpParser.IDENTIFIER, 0)
        def atom(self):
            return self.getTypedRuleContext(RegExpParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarBind" ):
                listener.enterVarBind(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarBind" ):
                listener.exitVarBind(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarBind" ):
                return visitor.visitVarBind(self)
            else:
                return visitor.visitChildren(self)


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


    class IntersectionContext(ExprContext):

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
            if hasattr( listener, "enterIntersection" ):
                listener.enterIntersection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntersection" ):
                listener.exitIntersection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntersection" ):
                return visitor.visitIntersection(self)
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


    class ExistsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RegExpParser.ExprContext
            super().__init__(parser)
            self.args = None # IdlistContext
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def idlist(self):
            return self.getTypedRuleContext(RegExpParser.IdlistContext,0)

        def expr(self):
            return self.getTypedRuleContext(RegExpParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExists" ):
                listener.enterExists(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExists" ):
                listener.exitExists(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExists" ):
                return visitor.visitExists(self)
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
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = RegExpParser.TrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 15
                self.match(RegExpParser.T__1)
                pass

            elif la_ == 2:
                localctx = RegExpParser.AtomicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                localctx.child = self.atom()
                pass

            elif la_ == 3:
                localctx = RegExpParser.NegAtomicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(RegExpParser.T__2)
                self.state = 18
                localctx.child = self.atom()
                pass

            elif la_ == 4:
                localctx = RegExpParser.VarBindContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 19
                localctx.var = self.match(RegExpParser.IDENTIFIER)
                self.state = 20
                self.match(RegExpParser.T__3)
                self.state = 21
                localctx.child = self.atom()
                pass

            elif la_ == 5:
                localctx = RegExpParser.ExistsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(RegExpParser.T__4)
                self.state = 23
                self.match(RegExpParser.T__5)
                self.state = 24
                localctx.args = self.idlist()
                self.state = 25
                self.match(RegExpParser.T__6)
                self.state = 26
                localctx.child = self.expr(8)
                pass

            elif la_ == 6:
                localctx = RegExpParser.GroupingContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(RegExpParser.T__13)
                self.state = 29
                localctx.child = self.expr(0)
                self.state = 30
                self.match(RegExpParser.T__14)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 49
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = RegExpParser.ConcatContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 35
                        self.match(RegExpParser.T__10)
                        self.state = 36
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = RegExpParser.IntersectionContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 38
                        self.match(RegExpParser.T__11)
                        self.state = 39
                        localctx.right = self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = RegExpParser.UnionContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 41
                        self.match(RegExpParser.T__12)
                        self.state = 42
                        localctx.right = self.expr(3)
                        pass

                    elif la_ == 4:
                        localctx = RegExpParser.StarContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.child = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 44
                        self.match(RegExpParser.T__7)
                        pass

                    elif la_ == 5:
                        localctx = RegExpParser.PlusContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.child = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 46
                        self.match(RegExpParser.T__8)
                        pass

                    elif la_ == 6:
                        localctx = RegExpParser.QuestionContext(self, RegExpParser.ExprContext(self, _parentctx, _parentState))
                        localctx.child = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 48
                        self.match(RegExpParser.T__9)
                        pass

             
                self.state = 53
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
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = RegExpParser.PropContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                localctx.name = self.match(RegExpParser.IDENTIFIER)
                pass

            elif la_ == 2:
                localctx = RegExpParser.PredContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                localctx.name = self.match(RegExpParser.IDENTIFIER)
                self.state = 56
                self.match(RegExpParser.T__13)
                self.state = 57
                localctx.args = self.idlist()
                self.state = 58
                self.match(RegExpParser.T__14)
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
            self.state = 62
            localctx.param = self.match(RegExpParser.IDENTIFIER)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RegExpParser.T__15:
                self.state = 63
                self.match(RegExpParser.T__15)
                self.state = 64
                localctx.param = self.match(RegExpParser.IDENTIFIER)
                self.state = 69
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
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         




