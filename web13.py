from web12 import *
from web5 import *
from pprint import pprint

def scrape_movie_cast(cast_name,main):
    for i in range(len(main)):
        dic={}
        dic['cast']=cast_name[i]
        main[i].update(dic.copy())
    return main

scrape_movie_cast(movie_li(get_movie_list_details(scrape_top_list()),scrape_top_list()),get_movie_list_details(scrape_top_list()))