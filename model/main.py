
import pickle
import pandas as pd


data = pickle.load(open('similarity.pkl','rb'))
tv_series = pd.read_csv('tv_series.csv')



def recommendrating(genre, lang, rating=6,num=10):
    try:
        
        result=[]
        mov = tv_series[(tv_series['vote_average'] >= rating) & (tv_series['genres'].str.contains(genre.casefold()).any()) & (tv_series['original_language'] == lang.casefold())]
        IND = list(mov.index[:num])
        
        for i in IND:
            resultname = mov.loc[i, 'name']
            resulturl = ("https://image.tmdb.org/t/p/w500" + mov.loc[i, 'poster_path'])
            resultoverview = mov.loc[i,'overview']
            result.append({
                "title":resultname,
                "image_url":resulturl,
                "movie_desc":resultoverview
            })
        return result
    except Exception as e:
        print(e)
        return []


def recommendcontent(series_name,n):
    
    try:
        print("0--------------")
        print(tv_series)
        index = tv_series[tv_series['name'] == series_name].index[0]
        print(index)
     
        print("1--------------")
        sim_scores = list(enumerate(data[index]))
        print("2--------------")
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        print("3--------------")
        sim_scores = sim_scores[1:n+1]
        print("4--------------")
      
        result=[]
        
        for i in sim_scores:
            try: 
                resultname = tv_series.loc[i[0],'name']                          
                resulturl = ("https://image.tmdb.org/t/p/w500" + tv_series.loc[i[0],'poster_path']) 
                simpercent = (int(i[1]*100)) 
                resultoverview = tv_series.loc[i[0],'overview']
                
                result.append({
                    "movie_title":resultname,
                    "image_url":resulturl,
                    "simi_percent":simpercent,
                    "movie_desc":resultoverview
                })
                  
            except Exception as e:
                print("in exce",e)
                result.append({
                    "movie_title":"",
                    "image_url":"",
                    "simi_percent":"",
                    "movie_desc":""
                })

        return result
    except Exception as e:
        print("in exception----",e)
        return []
    
   