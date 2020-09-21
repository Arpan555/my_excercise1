name=input("Enter Your Name: ")
roll_no=input("Enter Your Roll No: ")
no=int(input('Enter Number Of Subject: '))
subject_list=[]
number_list=[]
maximum_number=[]
for i in range(no):
    subject=input('Enter Your Subject Name: ')
	number=int(input('Enter Your Number: '))
	max_number=int(input('Enter Maximum Number: '))
	if number>max_number:
		print("Please Enter Valid Number: ")
	subject_list.append(subject)
	number_list.append(number)
	maximum_number.append(max_number)
total_max=0	
for i in maximum_number:
	total_max+=i
total=0
for i in number_list:
	total+=i
avg=(total*100)/total_max
zip_iterator=zip(subject_list,number_list)
dictionary=dict(zip_iterator)
print(dictionary)
print('M P BOARD MARKSHEET BHOPAL')
print("Your Name:-",name)
print('Your Rollno:-',roll_no)
print("-----------------------------------------------------------------")
for k,v in dictionary.items():
	print(k,'------------',str(v))

print("-----------------------------------------------------------------")
print("Your Percentages Is ",avg)
