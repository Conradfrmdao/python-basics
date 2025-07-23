#Dictionary have key-value pairs
empty_dict = {} # create an empty dictionary
my_dict={1:'john',2:'joe',3:'jane'}
print("Dictionary:", my_dict)

person_dict={'name':'wagaba','age':21,'city':'kampala','phone':256751929535}
print("Person Dictionary:", person_dict)

print("Name:", person_dict['name'])
print("Age:", person_dict['age'])   
print("City:", person_dict['city'])
print("Phone:", person_dict['phone'])

print("Using get",person_dict.get('name'))

#adding a new key-value pair
person_dict['email']='godlovesconrad@gmail.com'
print("Updated Person Dictionary:", person_dict)

##replacing a value
person_dict['age']=23
print("Updated Age:", person_dict['age'])

#removing a key-value pair
removed=person_dict.pop('phone')
print("Removed Phone:", removed)
print("Dictionary after removing phone:", person_dict)

#deleting a dictionary
#del my_dict

