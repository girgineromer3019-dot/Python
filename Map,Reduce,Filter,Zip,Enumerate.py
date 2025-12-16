#Map fonksiyonu, bir fonksiyonu bir iterable'ın (örneğin liste, demet) her bir öğesine uygulamak için kullanılır ve sonuçları içeren yeni bir iterable döner.
def double(x):
    return x * 2

list(map(double, [1, 2, 3, 4]))  
print(list(map(double, [1, 2, 3, 4])))
# [2, 4, 6, 8]

number = [1, 2, 3, 4]
out = list(map(lambda x: x * 2, number))
print(out)
# [2, 4, 6, 8]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Reduce fonksiyonu, bir iterable'ın öğelerini tek bir değere indirgemek için kullanılır. Bu, genellikle toplama, çarpma gibi işlemler için kullanılır.
from functools import reduce
def add(x, y):
    return x + y    
result = reduce(add, [1, 2, 3, 4])  
print(result)
# 10

def multiply(x, y):
    return x * y
result = reduce(multiply, [1, 2, 3, 4])  
print(result)
# 24

def maksimum(x, y):
    if x > y:
        return x
    else:
        return y
result = reduce(maksimum, [1, 5, 3, 19, 9, 2])  
print(result)
# 19

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Filter fonksiyonu, bir iterable'ın öğelerini belirli bir koşula göre filtrelemek için kullanılır ve koşulu sağlayan öğeleri içeren yeni bir iterable döner.
def is_even(x):
    return x % 2 == 0   
result = filter(is_even, [1, 2, 3, 4, 5, 6])
print(list(result))
# [2, 4, 6]

result = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
print(list(result))
# [2, 4, 6]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Zip fonksiyonu, birden fazla iterable'ı birleştirerek her bir iterable'ın aynı indeksindeki öğeleri bir araya getirir ve bunları demetler halinde döner.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))
# [(1, 'a'), (2, 'b'), (3, 'c')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Enumerate fonksiyonu, bir iterable'ın öğelerini indeksleriyle birlikte döner. Bu, özellikle döngülerde öğelere erişirken indeks bilgisine ihtiyaç duyulduğunda kullanışlıdır.
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit) 
# 0 apple
# 1 banana
# 2 cherry

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------#

#All ve Any fonksiyonları, iterable'ların öğeleri hakkında mantıksal değerlendirmeler yapmak için kullanılır.
# All fonksiyonu, iterable'ın tüm öğelerinin True olup olmadığını kontrol eder.

print(all([True, True, True]))
# True
print(all([True, False, True]))
# False