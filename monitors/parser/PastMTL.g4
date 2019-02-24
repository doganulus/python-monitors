grammar PastMTL;

namedExpr : (name=IDENTIFIER '=')? child=expr;

expr : child=atom                                                   # Atomic

     | ('!' | 'not') child=expr                                     # Negation
     | left=expr ('&&' | 'and') right=expr                          # Conjunction           
     | left=expr ('||' | 'or') right=expr                           # Disjunction
     | left=expr ('->' | 'implies') right=expr                      # Implies

     | 'pre' child=expr                                             # Previously

     | 'once' child=expr                                            # Once
     | 'once' '[' l=NUMBER ',' u=NUMBER ']' child=expr              # TimedOnce
     | 'once' '[' l=NUMBER ',' 'inf' ']' child=expr                 # TimedOnceInf

     | 'always' child=expr                                          # Always
     | 'always' '[' l=NUMBER ',' u=NUMBER ']' child=expr            # TimedAlways
     | 'always' '[' l=NUMBER ',' 'inf' ']' child=expr               # TimedAlwaysInf

     | left=expr 'since' right=expr                                 # Since
     | left=expr 'since' '[' l=NUMBER ',' u=NUMBER ']' right=expr   # TimedSince
     | left=expr 'since' '[' l=NUMBER ',' 'inf' ']' right=expr      # TimedSinceInf
     
     | '(' child=expr ')'                                           # Grouping
     ;

atom : name=IDENTIFIER                         # Prop
	| name=IDENTIFIER '(' args=idlist ')'     # Pred
	;

idlist : param=IDENTIFIER (',' param=IDENTIFIER)*;

IDENTIFIER : [_a-zA-Z][_a-zA-Z0-9]*;

NUMBER: DIGIT | (DIGIT_NOT_ZERO DIGIT+);

WS         : [ \r\n\t]+ -> channel (HIDDEN);

fragment DIGIT: ('0'..'9');
fragment DIGIT_NOT_ZERO: ('1'..'9');
