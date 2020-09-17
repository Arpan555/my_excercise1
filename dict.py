student=[
    {'name':'arpan','age':23,'city':'indore','mobile_no':9977336574},
    {'name':'rohit','age':22,'city':'hyderabad','mobile_no':7699772237},
    {'name':'rani','age':23,'city':'pune','mobile_no':9977774444},
    {'name':'ashish','age':23,'city':'bangalore','mobile_no':9924757755},
    {'name':'yogesh','age':23,'city':'mumbai','mobile_no':9977870843},
    {'name':'vijay','age':23,'city':'delhi','mobile_no':9977657983},
    {'name':'kavya','age':23,'city':'noida','mobile_no':9473475735},
    {'name':'chetan','age':23,'city':'punjab','mobile_no':9477375323},
    {'name':'tulsiram','age':23,'city':'hariyana','mobile_no':9986784433}
]
Name=input('enter name: ')
for items in student:
    if items['name'] == Name:
        print(items['mobile_no'])