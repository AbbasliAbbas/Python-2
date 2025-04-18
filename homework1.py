#Tapsiriq 1
visited_cities = {'Bakı', 'Gəncə', 'Şəki'}
print(visited_cities)
visited_cities.add('Masalli')
print(visited_cities)

##################################################################

parents = ('Ana', 'Ata')
print(parents)
parents[0] = ('Baba')
print(parents)
#TypeError: 'tuple' object does not support item assignment yeni bu onu gosterir ki tuple deyisdirile bilmez (immutable-dir).

##################################################################

my_value = None
print(my_value)

#################################################################

if my_value is None:
    print("Deyer yoxdu")