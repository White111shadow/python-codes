rno=input("Enter Student Roll No")
name=input("Enter Student Name")
m1=int(input("Enter the marks of python:"))
m2=int(input("Enter the marks of linux:"))
m3=int(input("Enter the marks of DM:"))
m4=int(input("Enter the marks of FOSS:"))
m5=int(input("Enter the marks of SS:"))

tot=m1+m2+m3+m4+m5
per=tot/5

if per >70:
    grade="A"
elif per >=60 and per <70:
    grade="B"
elif per >=50 and per <60:
    grade="C"
elif per >=40 and per <50:
    grade="D"
else:
    grade="F"

print("------MARKSHEET-----")
print("Roll No:",rno)
print("Name of Student :",name)
print("-----MARKS-----")
print("python:",m1)
print("linux:",m2)
print("DM:",m3)
print("FOSS:",m4)
print("SS:",m5)
print("*****RESULT****")

print("TOTAL:",tot)
print("PERCENTAGE:",per)
print("GRADEl:",grade)
