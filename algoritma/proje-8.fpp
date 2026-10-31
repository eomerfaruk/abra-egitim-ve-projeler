9       	 <--SHAPES
9       	 <--LINES
id1
2       	 <--TYPE
403       	 <--LEFT
102       	 <--TOP
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
402       	 <--LEFT
698       	 <--TOP
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
364       	 <--LEFT
183       	 <--TOP
156       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
INPUT
1.kenar
kenar1

id5
0       	 <--TYPE
298       	 <--LEFT
368       	 <--TOP
292       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
ADD
kenar1
kenar2
kenarlar_toplami
id6
92       	 <--TYPE
335       	 <--LEFT
461       	 <--TOP
224       	 <--WIDTH
50       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
IF_GREATER_EQUAL
kenarlar_toplami
180

id7
3       	 <--TYPE
90       	 <--LEFT
234       	 <--TOP
10       	 <--WIDTH
10       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
INTERSECTION



id8
0       	 <--TYPE
580       	 <--LEFT
581       	 <--TOP
268       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
SUBTRACT
180
kenarlar_toplami
kenar3
id9
91       	 <--TYPE
641       	 <--LEFT
665       	 <--TOP
156       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
3.kenar
kenar3

id4
91       	 <--TYPE
367       	 <--LEFT
262       	 <--TOP
156       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
INPUT
2.kenar
kenar2

  
---- LINES ---- from,to ----
id1,id3
reserved 1

id5,id6
reserved 1

id6,id7
reserved 1
EVET
id6,id8
reserved 1
HAYIR
id9,id2
reserved 1

id8,id9
reserved 1

id7,id1
reserved 1

id3,id4
reserved 1

id4,id5
reserved 1

