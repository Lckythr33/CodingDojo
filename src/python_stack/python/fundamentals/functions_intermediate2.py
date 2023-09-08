x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]["last_name"]="Bryant"
sports_directory['soccer'][0]="Andres"
z[0]['y']=30

print(x)
print(students)
print(sports_directory)
print(z)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(dic):
    for i in range(len(dic)):
       print ("first_name - "+ dic[i]['first_name'] + ", " + "last_name - " + dic[i]['last_name'])  
iterateDictionary(students)
    
def iterateDictionary2(key_name,some_list):
    for i in range(len(some_list)):
       print (some_list[i][key_name]) 
iterateDictionary2('first_name',students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dic):
    lcount=0;
    for i in range(len(dic['locations'])):
        lcount += 1
    print(lcount,"Locations")
    for i in range(len(dic['locations'])):
        print (dic['locations'][i])
    icount=0;

    print("\n")

    for i in range(len(dic['instructors'])):
        icount += 1
    print(icount,"Instructors")
    for i in range(len(dic['instructors'])):
        print (dic['instructors'][i])

printInfo(dojo)





