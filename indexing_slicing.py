a=[ 5,7.8,'string,',5+6j]
b=( 3,' nishu', 8+7j, 8.6)
#indexing
print(a[3])
print(b[2]) #positive indexing
print(a[-2])
print(b[-3]) #negative indexing 
print(a[ 1:4:2]) # start : stop: step  positive slicing 
print(b[ -2: -5: -1])  #negative slicing  -1 is for revering 
print(b[ -1: :1]) # step is positive
print( b[ -4: -1: 1])
print(a[-1: : 1])
print(b[ -3: : 1]) 
c={
     " car" :  [ " mustang" , " thar" , "scorpio"] ,
     " color" : [ " yellow" , " black", " grey"]
     
 }
print(c[" car"] [1] )
print( c[" car"] [1], c[" color"] [1])