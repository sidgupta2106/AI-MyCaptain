#Assigning elements to different lists
lst1 = [1, 2, 3, 4]
lst2 = ['apples', 'mangoes', 'bananas']
lst3 = ['Einstein', 'Newton', 'Tesla']

#accessing data in a tuple
tup = ('Python', 'Data', 'Computer Science')
cs = tup[2]
print(cs)

#Deleteing different ditionary elements
dict = {
    'Albert' : 'Einstein',
    'Issac' : 'Newton',
    'Nikola' : 'Tesla'
}
print(dict)
dict.pop('Issac')
print(dict)
dict.popitem()
print(dict)