#!/usr/bin/python3
# program which performs similar options like CAT command

choice = int(input("Enter you choice : \n1.Cat \t2. Cat -b\t3.Cat -s\t4.Cat -E\n"))

#open the file
file=open("shivi.txt","r")
#normal reading like cat function
if choice==1:
	print(file.read())

#with -b option
elif choice==2:
	i=1
	#to print non empty lines
	for lines in file:
		if lines.strip() !="":
			print(str(i)+". " +lines.strip())
			i+=1


#with -s option
elif choice==3:
	#to suppress empty lines
	for lines in file:
		if lines.strip() !="":
			print(lines.strip())

#with -E option
elif choice==4:
	#to put $ symbol in end of files
	for lines in file:
		print(lines.strip() +"$")

#if wrong choice
else:
	print("Enter your choice from given inputs")

file.close()
