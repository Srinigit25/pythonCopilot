from os import lseek

print('Hello world')
print('this is the next statement')
lsvar="Kunjika Devi"
listr1 = " I weigh "
liweight = 230

lsPrint =listr1+ str(liweight)
print(lsPrint)
lsData_type =type(12)
lsData_decimal=type(0.444)
ls_boolean=type(True)

print( lsData_type)
print (lsData_decimal)
print (ls_boolean)
print(type(lsvar))
print (listr1[0:2])
print(listr1[-2])
print(lsvar.upper())
print(lsvar.capitalize())
print(lsvar.lower())
ls_Str1=" first number is {0}".format(1)
ls_Str2= " second number is {0}".format(2)
ls_str3= " and, the Result of addition is {0}".format(3)

print(ls_Str1 + ls_Str2 + ls_str3)

remainder = 15%4
print('Assignment #1 is\n')
print(remainder)

print("We have {0} small boxes {2} large boxes and {1} medium boxes ".format(40,12,45))

chars='<<>>'
lsword='hello'
lsfirst=chars[:2]
lslast=chars[2:]
lsfinal=lsfirst+lsword+lslast
print(lsfinal)

lsnewvar1=['b','d','a','z','x']
lsvar2=[1,2,3,4,5]

lsnewvar1.sort()
lsnewvar1.reverse()
lsvar3=lsvar2[0:3]
print(lsnewvar1)
print (lsvar3)

lsvar4=lsnewvar1[0:3]
lsvar3.reverse()
lsvar4.reverse()
print(lsvar4)
lsfinal=lsvar4+lsvar3
print(lsfinal)

#Nested Lists

ls_nested=[1,2,3,4,5,6,['parvathi','lakshmi','saraswathi'],'a',1,2]
print(ls_nested)

ls_extracted=ls_nested[6]
ls_dev1=ls_extracted[0]
ls_dev2=ls_extracted[1]
ls_dev3=ls_extracted[2]
print(ls_extracted)
print(ls_dev1.capitalize())
print(ls_dev2.capitalize())
print(ls_dev3.capitalize())

#Nested list
print(ls_nested[6][1].upper())

#nested List - 2nd level
ls_nested2=[1,2,3,4,5,6,['parvathi','lakshmi','saraswathi',['kavacha','arGala','keelaka'],'sapthaSATHI'],'a',11,22]
ls_ChandiParayana=ls_nested2[6][3][0]

print(ls_ChandiParayana.capitalize())

#change the content of the list
ls_nested2[6][3][0]='Devi Kavacham'
print(ls_nested2)
liIndex=ls_nested2.index(4)
print(liIndex)
liIndex2=ls_nested2.index(22)
print(liIndex2)
ls_count=['a','b','c','d','e','f','a','d','a','r','t','y','u','a']
liCount=ls_count.count('a')
print(liCount)

#tuple

my_Tuple=(1,2,3,'red',"green",[5,65,88,"Devi",'kunjika devi'],112,345)
ls_extracted=my_Tuple[3]
ls_extracted2=my_Tuple[5]
ls_changedList=ls_extracted2[2]="007"

print('Tuple Examples')
print(ls_extracted)
print(ls_extracted2)
print(ls_changedList)

print(type(my_Tuple))
print(type(ls_extracted2))

#Dictionary

ls_dict={'a1': 345,'k2':'Devi Chamundi',2:456}

print(ls_dict)

ls_dict['a1']="Kunjika Devi"

print(ls_dict)

ls_dict['k2']=" Raja Rajeshwari"

print(ls_dict)
ls_dict[2]='devi maHatMe'.capitalize()
#ls_dict[2].capitalize()

print(ls_dict)

#Modifying Dictionary
my_dict2={1:'Red',2:456,'name':"chamundi"}
print(my_dict2)

my_dict2[99]="Heaven".lower()

print(my_dict2)

#Example for Dictionary in a list which is in a dictionary

ls_MyDict={'john': 456,'mala':'chocolate',
           'custom_list':['ListVal1',{'minilist':'Great Value'} ]}

print('\n')
print(" This is the complete dictionary-->List--> dictionary")
print(ls_MyDict)
ls_List=ls_MyDict['custom_list']

print(' List contains \n' )
print (ls_List)



ls_nestedDict=ls_List[1]

print('nested Dictionary is ' )
print(ls_nestedDict)

ls_nestedKeyvalue=ls_nestedDict['minilist']

print('Nested Value within dictionary is ')
print( ls_nestedKeyvalue)

#Access key:value pair within nested Dictionary
print('\n')
print('The key:value pair within nested Dictionary is..')
print(ls_MyDict['custom_list'][1]['minilist'])


#Example for accessing values from Tuple within nested Dictionary

ls_My_Nested_dict2={
        'john': 456,'mala':'chocolate',
           'custom_list':['ListVal1',{'minilist':'Great Value'} ],
            'Tuple_list':(23,456,'Shumbha',45)
                    }
#Access key:value pair from Tuple within a dictionary

ls_Tuple=ls_My_Nested_dict2['Tuple_list'][2]
print('\n Tuple value within dictionary is .')
print(ls_Tuple)

#Refresher on Operators in Python
print('Negative operator')
print(not(5==5))

#Assignment 2
my_list=[{'Tom':20000,'Bill':12000},['car','laptop','TV']]

print("bill's salary is my_list[0]['Bill'] ")
print(my_list[0]['Bill'])
print('You can also use method my_list[0].get("Bill") ')
print(my_list[0].get('Bill'))

#Sorting tuple inside a list collection
ls_OriginalList=['cup','cereal','milk',[8,4,32,1]]
ls_extract_Tuple=ls_OriginalList[3]

print('\n Original List')
print(ls_OriginalList)

print('\n tuple values are')
print(ls_extract_Tuple)

print('\n Sorted Tuple is')
ls_extract_Tuple.sort()

print(ls_extract_Tuple)


ls_Tuple_pop=ls_OriginalList.pop(3)
ls_Tuple_pop.sort()
print('\nThe alternate way of sorting Tuple is using pop() & sort of extracted Tuple ')
print(ls_Tuple_pop)

print('\nOriginal List now is ')
ls_OriginalList.append(ls_Tuple_pop)
print(ls_OriginalList)

# Assignment 3
#Replace 'm' with 'X'
#Replace 'TV' with 'Satellite Television'
ls_MynewList3=[
    (1,2),(3,4),
    (['c','d','a','m'],
        [3,9,4,12],
     4),
    'TV',42]

print('\n original List')
print(ls_MynewList3)

ls_MynewList3[2][0][3]='X'
ls_MynewList3[3]="Satellite Television"
print('\n Updated list')
print(ls_MynewList3)

#FUNCTIONS

print('\n')
print('############################################')
def call_Parvathi(lsname ='Beloved Disciple....'):
    '''
    this is the first function which i have created using
    Phython compiler - PyCharm Complier .link : https://www.jetbrains.com/pycharm/
    Python is installed using the link : https://www.python.org/downloads/
    '''

    lsDevotee=lsname
    return '\n Devi Parvathi has blessed you:' + lsDevotee

lsblessings =call_Parvathi()
print('Shaktha Sampradaya')
print(lsblessings)
lsblessings=call_Parvathi('Mala')
print(lsblessings)
print('############################################')

'''
Function using [*args]
this is used to accept unlimited number of arguments  
'''
def my_Func_args(*args):
    #li_inputValues()=*args
    print('\n We received all these numbers as arguments')
    print(args)
    liResult=sum(args)
    return liResult

liCall=my_Func_args(1,2,3,4,5,6,7,8,9)
print('\n the result of the function is:')
print(liCall)

'''
Function using [**kwargs]
this is used to accept key value pairs as arguments  
'''

def my_MyFunc_KeyValue(**kwargs):
    ls_dictNew=kwargs
    print(ls_dictNew)
    print(ls_dictNew.keys())
    print(ls_dictNew.values())
    print(ls_dictNew['Dev1'])
    return ls_dictNew['Devi3']
'''
Calling the key value arguments
'''
ls_outputFunc=my_MyFunc_KeyValue(Dev1='Parvathi',Dev2='Lakshmi',Devi3='Saraswathi')
print('\n The output of the key Value function is '+ ls_outputFunc)

'''
Create a function that accepts 2 Lists .
The function is supposed to merge both of the Lists together
and return the result 
'''

def Func_TwoList(Lsstr1, Lsstr2):
    lsStr1=str(Lsstr1)
    lsStr2=str(Lsstr2)
    lsFinal=lsStr1 + lsStr2
    return lsFinal

'''Calling the multiple argument function
'''
lsoutput=Func_TwoList([2,3,4,5],['Devi','Parvathi','Lakshmi'])

print('\n the output of Function_TwoList is : ')
print(lsoutput)

'''
Create a function called separate() that accepts a string as argument and
returns a list containing each of the characters of 
the string separated as individual items in the List.
'''

def func_Separate(lsinput):
    ls_localList=list(lsinput)
    #print(lsinput)
    return ls_localList



'''Calling the multiple argument function
    '''
ls_Getlist=func_Separate('Sapthasathi has 13 Chapters')
print(ls_Getlist)

'''
Create a function MultiMerge_lists that accepts 2 Lists
The function is supposed to merge both of those lists together 
and return the result 
'''

def MultiMerge_Lists(List1, List2):
    ls_Str1=List1
    ls_Str2=List2
    #return List2
    #lsMergeList= ls_Str1 + ls_Str2.split() + list(ls_Str2)
    return List2
'''
Call the function MultiMergeLists 
'''
lsoutputMergeList=MultiMerge_Lists([1,2,3,4,'f','r',23],["Devi Parayanam has 700 shlokas"])
print('\n')
print(lsoutputMergeList)


'''
Create function to accept unlimited List and then print the last list only
'''

def func_UnLimitedList(*args):
    return args[-1]

'''
Call unlimited list function and print last list
'''
lsOutput_UnlimitedList=func_UnLimitedList([1,2,3,4,5,6],['d','e','ty','Devi'],4,5,6,7,8,['Parvathi','Lakshmi','Saraswati'])
print('\n The output of extracting the last list from the unlimited input list is ')
print (lsOutput_UnlimitedList)


'''
Functions and Nested functions
def Main_func():
'''
age=49
def Main_func():
    age=69
    print('\n the age inside the main function is ' + str(age))

    def Sub_func1(age):

        age=14
        age=age+1
        print('\n the new age inside the Nested Function1 is :' + str(age))


    Sub_func1(1)


'''
Call Main function
'''
Main_func()
print('\n Scope of Global Variable is :' + str(age))

'''
Define a function called key_list_items that can accept an unlimited number
of lists along with another arguement. the function should return
the second to last item in the specific list specified by the user of the function

Example  output needed -->'Sakthi'
'''

#key_list_names=('people', things=['book','tv','shoes'],people=['Devi','Sakthi','Chamundi'])
def key_list_names(key, **kwargs):
    li_list=kwargs[key]
    return li_list[-2]

lsresult= key_list_names('people', things=['book','tv','shoes'],people=['Devi','Sakthi','Chamundi'])

print(lsresult)

'''
CONTROL FLOWS
'''



