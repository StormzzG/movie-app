import requests 

#Get movie data
def get_data(primary_genre, *additional_genres):
    api_key = '568bb4e8f6e76a6eda4ee919cd1d6b6e'
    base_url = 'https://api.themoviedb.org/3/discover/movie'
    
    all_genres = [primary_genre] + list(additional_genres)
    genres_str = ','.join(map(str, all_genres))
    
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'sort_by': 'popularity.desc',
        'vote_average.gte': 6,
        'page': 1,
        'with_genres': genres_str
    }

    response = requests.get(base_url, params=params)
    
    x = response.json()  
    y = x['results']
    data = sorted(y, key=lambda x: x['vote_average'], reverse=True)

    new = []
    for x in data:
        try:
            get_link(x['id'])
            new.append(x)
        except Exception as e:
            pass
    
    return new


#Get movie trailer
def get_link(id):
  url = f"https://api.themoviedb.org/3/movie/{id}/videos"
  api_key = '568bb4e8f6e76a6eda4ee919cd1d6b6e'

  params = {
    'api_key':api_key,
    'language':'en-US'
  }

  response = requests.get(url, params=params)

  data = response.json()
  key = data['results'][0]['key']
  link = f'https://www.youtube.com/watch?v={key}'
  
  return link


if __name__ == "__main__":
  print("This is a python module built to get movie data from TMDB using TMDB API. Import it and use its functions")