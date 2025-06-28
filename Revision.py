# This is revision before the python exam

import os

print('###############################################################')
print(' I am starting my revision of all python modules on 14- June25')
print('###############################################################')
print('There are 4 types of Data Types in python')
print('INTEGER.STRING,BOOLEAN,FLOAT')
print('###############################################################')
print('Getting THE DATATYPE IS DONE USING TYPE()')
print('Data type of number-->24 is=')
print(type(24))
print('Data type of String-->"KUNJIKA" is=')
print(type("kunjika"))
print('Data type of boolean-->TRUE is=')
print(type(True))
print('Data type of decimal-->0.05 is=')
print(type(0.05))

print('###############################################################')
print('New Line Character')
print('###############################################################')
print("Kunjika devi is in Kunjaragiri.\n I have been to the place couple of times")
print('In the above, the second line is printed in the new Line :-) ###############################################################')

print('String can be read in to an array')
print('###############################################################')
lsvar="ShriRaghuveeraSamaratha"
lsi=len(lsvar)
print(lsvar)
print('Length of the field is =')
print(lsi)
print('Printing in forward direction of arrays')
print(lsvar[0])
print(lsvar[10])
print(lsvar[15])
print(lsvar[20])
print(lsvar[22])
print('###############################################################')
print('Printing in reverse direction of arrays')
print('###############################################################')
print(lsvar[0])
print(lsvar[-1])
print(lsvar[-10])
print(lsvar[-15])
print(lsvar[-20])
print(lsvar[-22])
print('###############################################################')
print('###############################################################')

print(lsvar)
print('Range of values [3:5]')
print(lsvar[3:5])
print('###############################################################')
print('Range of values with skip of 01 character as a time [3:5:1]')
print(lsvar[4:9:1])
print('###############################################################')
print('Range of values with skip of 2 chars at a time [3:5:2]')
print(lsvar[4:9:2])
print('###############################################################')

print('Methods for Strings')
lsvar="shri Gurucharana Saroja Raja."
lsvar1="nijamana mukura sudhari"

print('###############################################################')
print(lsvar)
print('String to upper case')
print(lsvar.upper())
print('###############################################################')
print('Prints with First character of the sentence as upper')
print(lsvar.capitalize())
print('###############################################################')
print('Prints all the characters in the string as lowercase')
print(lsvar)
print(lsvar.lower())
print('###############################################################')
print('Checks if the string is numeric or not ?')
print(lsvar)
print(lsvar.isnumeric())
print('###############################################################')
lsvar3=34
print('Checks if the below is numeric or not ?')
print(lsvar3)
print(lsvar3.is_integer())
print('###############################################################')
print('Checks for alpha numeric against a string')
lsvar4="Recite Hanuman chalisa 100 times to get  the mukhti"
print(lsvar4)
print(lsvar.isalnum())
print("In the above,The space in the string is considered as special character")
lsvar4="ReciteHanumanchalisa100timestogetthemukhti"
print(lsvar4)
print(lsvar4.isalnum())
print('###############################################################')

lsString1="Trying the input prompts for the String. Name of the GOD is:{0}"
lsString1=lsString1.format('Hanuman')
print(lsString1)
print('###############################################################')
print('###############################################################')
print('###############################################################')
print('STRINGS ARE IMMUTABLE. i.e. THE CONTENT OF THE STRINGS CANNOT BE CHANGED')
print('###############################################################')
print('###############################################################')
print('###############################################################')
lsString2="{0}: WAS THE PARAMA BHAKTHA OF THE LORD SHREE {1}"
lsString2=lsString2.format('LORD Hanuman','Raghurama')
print(lsString2.capitalize())
print('###############################################################')
print('###############################################################')
print('###############################################################')
print('We are now working with Lists\n'.capitalize())
print('String is represented by " ". Where as Lists are represented by []\n'.upper())
print('Lists are mutuable i.e. The contents can be modified\n'.upper())
print('###############################################################')
print('###############################################################')
print('###############################################################')
ls_myList=[1,2,3,4,5,'a','b','c']
print('###############################################################')
print('List can contain alpha and numeric rt?')
print(ls_myList)
print('When I use list.pop(), the last item is eliminated')
print(ls_myList.pop())
print('By default, the index for pop would be the last item')
print('List now would be muted by eliminating  the last item from the LIST \n. The list now would like as follows')
print(ls_myList)
print('If i use the index and eliminate in the above. Index position=2.\n . Then it would appear as ')
print(ls_myList.pop(2))
print('The list would now appear as follows \n')
print(ls_myList)
print('###############################################################')
ls_myList=['Shree Rama Samartha']
ls_myList2=('Jaya Jaya Raghuveera Samartha')
print(ls_myList)
print(ls_myList2)
print('\n')
print('After appending the "List" & "Strings" , they get concatenated into one List')
ls_myList.append(ls_myList2)
print(ls_myList)
print('###############################################################')
print('Anything which is getting appended to LIST will get appended as ONE Array and not as individual arrays')
print('###############################################################')
ls_myList=['Shree Rama Samartha']
ls_myList2=['Jaya Jaya Raghuveera Samartha']
print(ls_myList)
print(ls_myList2)
ls_myList.append(ls_myList2)
print('concatenating 2 lists below. The appended list will be one complete array')
print(ls_myList)
li_myList=[99,98,56,0,-1,34]
print('\n')

print('List with integers, float can only be sorted')
print('\n')
print(li_myList)
print('List after sorting is as follows\n')
print('\n')
li_myList.sort()
print(li_myList)
print('\n')
print('List looks like as follows:')
ls_myList=['a','z','r','c','e']
print(ls_myList)
print('List with sort looks as below:\n')
ls_myList.sort()
print(ls_myList)
ls_myList.reverse()
print('List After (a)Sort and (b) after Reverse looks as below:\n')
print(ls_myList)
print('\n The length of the list array is as follows:')
print(len(ls_myList))

print('\n')
print('###############################################################')
print('###############################################################')
print('###############################################################')
print('WORKING WITH NESTED LISTS')
print('###############################################################')
print('###############################################################')
print('###############################################################')
print('\n')
ls_nested=['a','z','u','w','t',['Kunjika','Devi','Krishna','Jagadeeshwara','kateelu']]
print('Nested List appears as follows:')
print(ls_nested)
print('###############################################################')
ls_Extracted=ls_nested[5]
ls_nested1=ls_Extracted[0]
ls_nested2=ls_Extracted[1]
ls_nested3=ls_Extracted[2]
ls_nested4=ls_Extracted[3]
ls_nested5=ls_Extracted[4]
print('Extracted List is :')
print(ls_Extracted)

print('Array-1: Array-5 of Extracted List is as follows:')
print(ls_nested1)
print(ls_nested2)
print(ls_nested3)
print(ls_nested4)
print(ls_nested5)
print('###############################################################')
print('###############################################################')
print('###############################################################')
print('Querying with Nested Lists')
print('\n')
ls_Nested1=ls_nested[5][0]
print('[5][0]')
print(ls_Nested1)
print('\n [5][1]')
ls_Nested1=ls_nested[5][1]
print(ls_Nested1)
print('\n [5][2]')
ls_Nested1=ls_nested[5][2]
print(ls_Nested1)
print('\n [5][3]')
ls_Nested1=ls_nested[5][3]
print(ls_Nested1)
print('\n [5][4]')
ls_Nested1=ls_nested[5][4]
print(ls_Nested1)

ls_nested2=['a','b','c','d',['Green','Red','Blue',['I','am','Inside','Nested','Loop']],['Hanuman','Raghuvera','Samartha']]
print('###############################################################')
print('###############################################################')
print('###############################################################')
print('Printing using the nested lists')
print('\n Entire List looks like as follows')
print(ls_nested2)
print('To print the exact value=Loop, we will have to use [4][3][4]')
print(ls_nested2[4][3][4])
print('Changing the content of the List at place [4][3][4] from Loop to Shri Raghurama')
ls_nested2[4][3][4]="Shri Raghurama"
print('Printing the entire content of the List once again after change')
print(ls_nested2)
print('\n ###############################################################')
print('###############################################################')
print('###############################################################')
print('Finding the Index & Dupliates of the arrays in the Nested Lists')

ls_nested2=['a','b','c','d',['a','Red','Blue',['a','am','Inside','Nested','Loop']],['Hanuman','Raghuvera','Samartha']]
print(ls_nested2)
print('Find the index of alphabet:a and how many times it has been repeated in the PARENT/ROOT ARRAY ONLY')
print(ls_nested2.index('a'))
print('\n')
ls_nested3=['a','b','c','d','a','t','r','w','a']
print(ls_nested3.count('a'))

print('\n ###############################################################')
print('###############################################################')
print('###############################################################')
print('TUPLES')
print('DATA CANNOT BE CHANGED IN TUPLE. ')
print('Note: Data can be changed in Lists')
print('VERY IMPORTANT:List as denoted using [1,2,3,"a","b"]. Tuple are denoted using (1,2,3,"a","b")')
print('###############################################################')
print('###############################################################')

ls_Tuple=('a','b',1,2,3,4,5,['Shri','Raghuvera','Samartha'])
print(ls_Tuple)
print('\n Shri can be fetched using [7][0] ')
print('List inside a Tuple can be modified')
print(ls_Tuple[7][0])
ls_Tuple[7][0]="Shri Rama"
print(ls_Tuple)

print('Printing the Datatype')
print(type(ls_Tuple))
ls_newList=ls_Tuple[7]
print('Printing the extract of the Data Type of extracted List ')
print(type(ls_newList))

print('\n ###############################################################')
print('###############################################################')
print('###############################################################')
print('DICTIONARIES IN PYTHON')
print('###############################################################')
print('###############################################################')
print('###############################################################')
print('Dictionaries are mutable i.e. content can be changed')
print('Dictionaries are represented by {} \n')
ls_dict={"Lord":"Raghuvera","Banta":"Hanuman","Brother":"Lakshmana"}
print('ORIGINAL DICTIONARY IS:')
print(ls_dict.items())
print('\n: Getting the values for the keys i.e. Lord & Brother from the above dictionary')
print(ls_dict["Lord"])
print(ls_dict["Brother"])
print('\n Changing the values of key i.e. Lord and inserting a new key:value pair i.e. Samartha \n')
ls_dict["Samartha"]="Shree Raghuveera Samartha"
ls_dict["Lord"]="Kodanda Rama"
print(ls_dict)

print('USING THE POP FUNCTION')
ls_dict2=ls_dict.pop("Lord")
print(type(ls_dict2))
print(ls_dict2)
print('Printing the original Dictrionary after applying the pope function on it')
print(ls_dict)
print('dictionary cleared using the method .clear()')
ls_dict.clear()
print(ls_dict)
ls_dict={"Lord":"Raghuvera","Banta":"Hanuman","Brother":"Lakshmana"}
print(ls_dict)
ls_dict["Brother"]="Bharatha"
print('After changing the content of the Key:value pair i.e. Brother')
print(ls_dict)

ls_dict3={"Lord":"Raghuvera","Friend":"Sugreeva","Samartha":["Hanuma","Bharatha",{"Khiskinda":"Kolar","Island":"Lanka"}]}

ls_string=ls_dict3['Samartha'][2]['Khiskinda']
print('Nested dictionary i.e. dictionary inside a list which is inside a dictionary')
print(ls_string)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(46))
print('###############################################################')
print('###############################################################')
print('###############################################################')



# Python
def call_Parvathi(lsname='Beloved Disciple....'):
    return '\n Devi Parvathi has blessed you:' + lsname

def my_Func_args(*args):
    return sum(args)


# Python
def add_numbers():
    # Accept two numbers from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Perform addition
    result = num1 + num2


    # Display the input numbers and the result
    print(f"First number is {num1} and the second number is {num2}. The output of {num1} + {num2} = {result}")


# Call the function
add_numbers()


