data = 'From the hesam.seif@uct.ac.za Sat Jan  09:14:16 2008'
search1 = data.find('@')
print(search1)

search2 = data.find(' ',search1)
print(search2)

search_kalame = data[8+1 : search2]
print(search_kalame)