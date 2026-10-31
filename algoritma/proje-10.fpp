16       	 <--SHAPES
18       	 <--LINES
id1
2       	 <--TYPE
287       	 <--LEFT
73       	 <--TOP
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
1081       	 <--LEFT
780       	 <--TOP
70       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
STOP



id3
91       	 <--TYPE
249       	 <--LEFT
150       	 <--TOP
156       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
INPUT
isci maas
maas

id4
91       	 <--TYPE
206       	 <--LEFT
259       	 <--TOP
228       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
INPUT
cocuk sayisi
cocuk_aded

id5
92       	 <--TYPE
249       	 <--LEFT
354       	 <--TOP
152       	 <--WIDTH
50       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
IF_EQUAL
cocuk_aded
1

id6
0       	 <--TYPE
539       	 <--LEFT
359       	 <--TOP
148       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
PERCENT
maas
5
yuzde
id7
0       	 <--TYPE
752       	 <--LEFT
360       	 <--TOP
172       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
ADD
maas
yuzde
maas
id8
92       	 <--TYPE
243       	 <--LEFT
455       	 <--TOP
152       	 <--WIDTH
50       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
IF_EQUAL
cocuk_aded
2

id9
0       	 <--TYPE
533       	 <--LEFT
453       	 <--TOP
156       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
PERCENT
maas
10
yuzde
id10
0       	 <--TYPE
777       	 <--LEFT
453       	 <--TOP
172       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
ADD
maas
yuzde
maas
id11
0       	 <--TYPE
778       	 <--LEFT
535       	 <--TOP
172       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
ADD
maas
yuzde
maas
id12
0       	 <--TYPE
536       	 <--LEFT
543       	 <--TOP
156       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
PERCENT
maas
15
yuzde
id13
92       	 <--TYPE
255       	 <--LEFT
532       	 <--TOP
152       	 <--WIDTH
50       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
IF_EQUAL
cocuk_aded
3

id14
91       	 <--TYPE
260       	 <--LEFT
696       	 <--TOP
116       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
maas
maas

id15
91       	 <--TYPE
1060       	 <--LEFT
593       	 <--TOP
116       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
maas
maas

id16
3       	 <--TYPE
1106       	 <--LEFT
361       	 <--TOP
10       	 <--WIDTH
10       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
INTERSECTION



  
---- LINES ---- from,to ----
id1,id3
reserved 1

id3,id4
reserved 1

id4,id5
reserved 1

id5,id6
reserved 1
EVET
id6,id7
reserved 1

id5,id8
reserved 1
HAYIR
id8,id9
reserved 1
EVET
id9,id10
reserved 1

id12,id11
reserved 1

id13,id12
reserved 1
EVET
id8,id13
reserved 1
HAYIR
id13,id14
reserved 1
HAYIR
id14,id2
reserved 1

id7,id16
reserved 1

id10,id16
reserved 1

id11,id16
reserved 1

id16,id15
reserved 1

id15,id2
reserved 1

