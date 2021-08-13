import json,pprint
from web2 import group_by_year
with open("movies.json0","r") as file:
	movies=json.load(file)
movies_by_year = group_by_year(movies)
def group_by_decade(movies):
	years,dic=[],{}
	for movie in movies:
		if movie["year"]  not in years:
			years.append(movie["year"] )
	min1=min(years)
	max1=max(years)
	while True:
		if min1%10!=0:
			min1-=1
		elif max1%10!=0:
			max1+=1
		else:
			break
	years=[]
	while True:
		years.append(min1)
		if min1==max1-10:
			break
		min1+=10
	for i in years:
		list1=[]
		for year in movies_by_year:
			if i<year and i+10>year:
				list1.append(movies_by_year[year][0])
		dic[i]=list1
	return dic
dic=group_by_decade(movies)
json=json.dumps(dic,indent=4)
with open('data_of_task3.json','w') as file:
    file.write(json)
pprint.pprint(group_by_decade(movies))