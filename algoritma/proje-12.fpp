20       	 <--SHAPES
21       	 <--LINES
id1
2       	 <--TYPE
282       	 <--LEFT
84       	 <--TOP
70       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
START



id2
2       	 <--TYPE
1274       	 <--LEFT
829       	 <--TOP
70       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
STOP



id3
0       	 <--TYPE
262       	 <--LEFT
148       	 <--TOP
124       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
DEFINITION
tektoplam
0

id4
0       	 <--TYPE
267       	 <--LEFT
211       	 <--TOP
124       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
DEFINITION
tekcarpim
1

id5
0       	 <--TYPE
260       	 <--LEFT
280       	 <--TOP
132       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
DEFINITION
cifttoplam
0

id6
0       	 <--TYPE
276       	 <--LEFT
351       	 <--TOP
108       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
DEFINITION
artsayi
1

id7
91       	 <--TYPE
225       	 <--LEFT
437       	 <--TOP
204       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
INPUT
bir sayi gir
grssayi

id8
92       	 <--TYPE
226       	 <--LEFT
517       	 <--TOP
176       	 <--WIDTH
50       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
IF_GREATER
artsayi
grssayi

id9
0       	 <--TYPE
599       	 <--LEFT
345       	 <--TOP
188       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
MODULE
artsayi
2
kalan
id10
92       	 <--TYPE
637       	 <--LEFT
444       	 <--TOP
112       	 <--WIDTH
50       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
IF_EQUAL
kalan
0

id11
0       	 <--TYPE
841       	 <--LEFT
455       	 <--TOP
268       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
ADD
tektoplam
artsayi
tektoplam
id12
0       	 <--TYPE
568       	 <--LEFT
571       	 <--TOP
228       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
ADD
artsayi
artsayi
karesi
id13
0       	 <--TYPE
839       	 <--LEFT
576       	 <--TOP
268       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
MULTIPLY
tekcarpim
artsayi
tekcarpim
id14
0       	 <--TYPE
535       	 <--LEFT
677       	 <--TOP
276       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
ADD
cifttoplam
karesi
cifttoplam
id15
0       	 <--TYPE
214       	 <--LEFT
814       	 <--TOP
188       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
ADD
artsayi
1
artsayi
id16
3       	 <--TYPE
958       	 <--LEFT
681       	 <--TOP
10       	 <--WIDTH
10       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
INTERSECTION



id17
3       	 <--TYPE
55       	 <--LEFT
717       	 <--TOP
10       	 <--WIDTH
10       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
INTERSECTION



id18
91       	 <--TYPE
460       	 <--LEFT
847       	 <--TOP
244       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
tek toplam sayi
tektoplam

id19
91       	 <--TYPE
747       	 <--LEFT
833       	 <--TOP
244       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
tek carpim sayi
tekcarpim

id20
91       	 <--TYPE
1076       	 <--LEFT
742       	 <--TOP
260       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
cift toplam sayi
cifttoplam

  
---- LINES ---- from,to ----
id1,id3
reserved 1

id3,id4
reserved 1

id4,id5
reserved 1

id5,id6
reserved 1

id6,id7
reserved 1

id7,id8
reserved 1

id9,id10
reserved 1

id10,id12
reserved 1
EVET
id10,id11
reserved 1
HAYIR
id11,id13
reserved 1

id12,id14
reserved 1

id13,id16
reserved 1

id14,id16
reserved 1

id16,id15
reserved 1

id15,id17
reserved 1

id17,id8
reserved 1

id8,id18
reserved 1
EVET
id18,id19
reserved 1

id19,id20
reserved 1

id20,id2
reserved 1

id8,id9
reserved 1
HAYIR
