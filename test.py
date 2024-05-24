import requests 

def get_data(primary_genre, *additional_genres):
    api_key = '568bb4e8f6e76a6eda4ee919cd1d6b6e'
    base_url = 'https://api.themoviedb.org/3/discover/movie'
    
    all_genres = [primary_genre] + list(additional_genres)
    genres_str = ','.join(map(str, all_genres))
    
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'sort_by': 'popularity,vote_average.desc',
        'page': 1,
        'with_genres': genres_str
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()  
    else:
        return response.status_code, response.text  

if __name__ == "__main__":
  print("This is a python module. Import it and use its functions")