11       	 <--SHAPES
11       	 <--LINES
id1
2       	 <--TYPE
284       	 <--LEFT
60       	 <--TOP
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
689       	 <--LEFT
777       	 <--TOP
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
317       	 <--LEFT
117       	 <--TOP
156       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
INPUT
vize notu
vize

id5
0       	 <--TYPE
333       	 <--LEFT
295       	 <--TOP
188       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
PERCENT
vize
40
vize_ort
id6
0       	 <--TYPE
325       	 <--LEFT
376       	 <--TOP
204       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
PERCENT
final
60
final_ort
id7
0       	 <--TYPE
322       	 <--LEFT
453       	 <--TOP
244       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
ADD
vize_ort
final_ort
sonuc
id8
92       	 <--TYPE
422       	 <--LEFT
539       	 <--TOP
128       	 <--WIDTH
50       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
IF_GREATER_EQUAL
sonuc
45

id9
91       	 <--TYPE
386       	 <--LEFT
668       	 <--TOP
132       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
gecti
sonuc

id10
91       	 <--TYPE
663       	 <--LEFT
582       	 <--TOP
132       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
kaldi
sonuc

id11
3       	 <--TYPE
705       	 <--LEFT
687       	 <--TOP
10       	 <--WIDTH
10       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
INTERSECTION



id4
91       	 <--TYPE
334       	 <--LEFT
204       	 <--TOP
172       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
INPUT
final notu
final

  
---- LINES ---- from,to ----
id1,id3
reserved 1

id5,id6
reserved 1

id6,id7
reserved 1

id7,id8
reserved 1

id8,id9
reserved 1
EVET
id8,id10
reserved 1
HAYIR
id10,id11
reserved 1

id9,id11
reserved 1

id11,id2
reserved 1

id3,id4
reserved 1

id4,id5
reserved 1

