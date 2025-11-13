sub1= int(input( " enter marks of Physics:") )
sub2= int(input(" enter marks of Chemistry:") )
sub3=int(input(" enter marks of Mathematics:") )
sub4= int ( input(" enter marks of English") )
sub5= int (input(" enter marks of  hindi :") )
total_marks=sub1+sub2+sub3+sub4+sub5
average =total_marks / 5
if average >=90 :
    print( " A Grade")
elif average >= 80-89 :
    print(" B Grade")
elif average >= 70-79:
    print(" C Grade")
elif average < 70:
    print(" FAIL!!")
      
    
