import requests,pprint,json
from bs4 import BeautifulSoup
url=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(url.text,"html.parser")
def scrape_top_list():
		tbody= soup.find("tbody",class_="lister-list")
		all_movies,dic=[],{}
		for tr in tbody.find_all("tr"):
			dic["ratting"]=float(tr.find("td",class_="ratingColumn imdbRating").text)
			for td in tr.find_all("td",class_="titleColumn"):
				nam,nyp="",[]
				dic["Url"]="https://www.imdb.com/"+td.find("a")["href"][:16]
				for letter in td.text:
					nam+=letter
					if letter=="\n":
						nyp.append(nam.strip())
						nam=""
				dic["position"]=int(nyp[1][:-1])
				dic["nam"] = str(nyp[2])
				dic["year"]=int(nyp[3][1:-1])
			all_movies.append(dic)
		with open("movies.json","w") as file:
			data=json.dumps(all_movies,indent=4)
			file.write(data)
		return all_movies
pprint.pprint(scrape_top_list())