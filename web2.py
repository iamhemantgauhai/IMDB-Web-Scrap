import json,pprint
with open("movies0.json","r") as file:
	movies=json.load(file)
def group_by_year(movies):
	years,dic=[],{}
	for movie in movies:
		if movie["year"]  not in years:
			years.append(movie["year"] )
	for year in years:
		year_list=[]
		for movie in movies:
			if year==movie["year"]:
				year_list.append(movie)
		dic[year]=year_list
	return(dic)
dic=group_by_year(movies)
with open("movies1.json","w") as file:
		data=json.dumps(dic,indent=4)
		file.write(data)
pprint.pprint(group_by_year(movies))