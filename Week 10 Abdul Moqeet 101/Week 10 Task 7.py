x=int(input("Enter total numbers: "))
y=int(input("Enter obtained marks: "))
per=y*100/x
print(per)
if per>=90:
    grade="A"
elif per>=85:
    grade="A-"
elif per>=80:
    grade="B+"
elif per>=75:
    grade="B"
elif per>=70:
    grade="B-"
elif per>=65:
    grade="C+"
elif per>=60:
    grade="C"
elif per>=55:
    grade="C-"
elif per>=50:
    grade="D+"
elif per>=45:
    grade="D"
elif per>=40:
    grade="D-"
else:
    grade="F"
print(grade)