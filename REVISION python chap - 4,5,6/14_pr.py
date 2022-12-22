sub1 = input("enter the number :")
sub2 = input("enter the number :")
sub3 = input("enter the number :")

sub1 = int(sub1)
sub2 = int(sub2)
sub3 = int(sub3)

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail due to less than 33 marks in the individual subject")

if((sub1+sub2+sub3)/3<40):
    print("you are fail due to less than 40% marks in total ")

else:
    print("Congratulaions, you have passed the exam")    
