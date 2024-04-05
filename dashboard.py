import streamlit as st 
import joblib 
import requests

st.set_page_config(page_icon=':popcorn:',page_title='Movie Recommender')
st.title(':popcorn: Movie Recommender')

with open('movie-recommender2.joblib','rb') as f:
    model = joblib.load(f)

st.sidebar.header('Welcome')
age_1 =  st.sidebar.multiselect('Choose Age', list(range(21,37)))
if age_1:
    for x in age_1:
        age = x
if not age_1:
    st.warning('Please input age')


gender_1 = st.sidebar.multiselect('Choose Gender', ['Male','Female'])

if gender_1:
    for d in gender_1:
        if d == 'Male':
            gender = 1
        else:
            gender = 0
if not gender_1:
    st.warning('Please input gender')

if not age_1 and not gender_1:
    age = 0
    gender = 3
if age_1 and not gender_1:
    age = 0
    gender = 3
if gender_1 and not age_1:
    age = 0
    gender = 3


prediction = model.predict([[age,gender]])

if prediction == 'All':
    st.subheader('Generally watched Shows...')
    url = "https://api.themoviedb.org/3/discover/movie?api_key=568bb4e8f6e76a6eda4ee919cd1d6b6e&language=en-US&sort_by=popularity.desc&page=1&with_genres=37"

    response = requests.get(url)
    r = response.json()

    path = r['results']

    new = []
    titles = []
    rating = []
    views = []

    for x in path:
        new.append(x['poster_path'])
        titles.append(x['title'])
        rating.append(round(x['vote_average'],1))
        views.append(x['overview'])
    
    first = "https://image.tmdb.org/t/p/w500"

    col1,col2 = st.columns((2))
    with col1:
        st.image(first+new[0])
        st.write(titles[0])
        st.write(f"Rating: {rating[0]}")
        st.write(f"Overview: {views[0]}")
    with col2:
        st.image(first+new[1])
        st.write(titles[1])
        st.write(f"Rating: {rating[1]}")
        st.write(f"Overview: {views[1]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col3,col4 = st.columns((2))
    with col3:
        st.image(first+new[2])
        st.write(titles[2])
        st.write(f"Rating: {rating[2]}")
        st.write(f"Overview: {views[2]}")
    with col4:
        st.image(first+new[3])
        st.write(titles[3])
        st.write(f"Rating: {rating[3]}")
        st.write(f"Overview: {views[3]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col5,col6 = st.columns((2))
    with col5:
        st.image(first+new[4])
        st.write(titles[4])
        st.write(f"Rating: {rating[4]}")
        st.write(f"Overview: {views[4]}")
    with col6:
        st.image(first+new[5])
        st.write(titles[5])
        st.write(f"Rating: {rating[5]}")
        st.write(f"Overview: {views[5]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col7,col8 = st.columns((2))
    with col7:
        st.image(first+new[6])
        st.write(titles[6])
        st.write(f"Rating: {rating[6]}")
        st.write(f"Overview: {views[6]}")
    with col8:
        st.image(first+new[7])
        st.write(titles[7])
        st.write(f"Rating: {rating[7]}")
        st.write(f"Overview: {views[7]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col9,col10 = st.columns((2))
    with col9:
        st.image(first+new[8])
        st.write(titles[8])
        st.write(f"Rating: {rating[8]}")
        st.write(f"Overview: {views[8]}")
    with col10:
        st.image(first+new[9])
        st.write(titles[9])
        st.write(f"Rating: {rating[9]}")
        st.write(f"Overview: {views[9]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col11,col12 = st.columns((2))
    with col11:
        st.image(first+new[10])
        st.write(titles[10])
        st.write(f"Rating: {rating[10]}")
        st.write(f"Overview: {views[10]}")
    with col12:
        st.image(first+new[11])
        st.write(titles[11])
        st.write(f"Rating: {rating[11]}")
        st.write(f"Overview: {views[11]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col13,col14 = st.columns((2))
    with col13:
        st.image(first+new[12])
        st.write(titles[12])
        st.write(f"Rating: {rating[12]}")
        st.write(f"Overview: {views[12]}")
    with col14:
        st.image(first+new[13])
        st.write(titles[13])
        st.write(f"Rating: {rating[13]}")
        st.write(f"Overview: {views[13]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')
    st.write("<span style='color:#FFD700;'>Find all these movies [here](https://fbox.to/home) and I hope you find them entertaining :)</span>",unsafe_allow_html=True)



elif prediction == 'Action':
    st.subheader('Consider Watching...')
    url = "https://api.themoviedb.org/3/discover/movie?api_key=568bb4e8f6e76a6eda4ee919cd1d6b6e&language=en-US&sort_by=popularity,vote_average.desc&page=1&with_genres=28"


    response = requests.get(url)
    r = response.json()

    path = r['results']

    new = []
    titles = []
    rating = []
    views = []

    for x in path:
        new.append(x['poster_path'])
        titles.append(x['title'])
        rating.append(round(x['vote_average'],1))
        views.append(x['overview'])

    first = "https://image.tmdb.org/t/p/w500"

    col1,col2 = st.columns((2))
    with col1:
        st.image(first+new[0])
        st.write(titles[0])
        st.write(f"Rating: {rating[0]}")
        st.write(f"Overview: {views[0]}")
    with col2:
        st.image(first+new[1])
        st.write(titles[1])
        st.write(f"Rating: {rating[1]}")
        st.write(f"Overview: {views[1]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col3,col4 = st.columns((2))
    with col3:
        st.image(first+new[2])
        st.write(titles[2])
        st.write(f"Rating: {rating[2]}")
        st.write(f"Overview: {views[2]}")
    with col4:
        st.image(first+new[3])
        st.write(titles[3])
        st.write(f"Rating: {rating[3]}")
        st.write(f"Overview: {views[3]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col5,col6 = st.columns((2))
    with col5:
        st.image(first+new[4])
        st.write(titles[4])
        st.write(f"Rating: {rating[4]}")
        st.write(f"Overview: {views[4]}")
    with col6:
        st.image(first+new[5])
        st.write(titles[5])
        st.write(f"Rating: {rating[5]}")
        st.write(f"Overview: {views[5]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col7,col8 = st.columns((2))
    with col7:
        st.image(first+new[6])
        st.write(titles[6])
        st.write(f"Rating: {rating[6]}")
        st.write(f"Overview: {views[6]}")
    with col8:
        st.image(first+new[7])
        st.write(titles[7])
        st.write(f"Rating: {rating[7]}")
        st.write(f"Overview: {views[7]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col9,col10 = st.columns((2))
    with col9:
        st.image(first+new[8])
        st.write(titles[8])
        st.write(f"Rating: {rating[8]}")
        st.write(f"Overview: {views[8]}")
    with col10:
        st.image(first+new[9])
        st.write(titles[9])
        st.write(f"Rating: {rating[9]}")
        st.write(f"Overview: {views[9]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col11,col12 = st.columns((2))
    with col11:
        st.image(first+new[10])
        st.write(titles[10])
        st.write(f"Rating: {rating[10]}")
        st.write(f"Overview: {views[10]}")
    with col12:
        st.image(first+new[11])
        st.write(titles[11])
        st.write(f"Rating: {rating[11]}")
        st.write(f"Overview: {views[11]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col13,col14 = st.columns((2))
    with col13:
        st.image(first+new[12])
        st.write(titles[12])
        st.write(f"Rating: {rating[12]}")
        st.write(f"Overview: {views[12]}")
    with col14:
        st.image(first+new[13])
        st.write(titles[13])
        st.write(f"Rating: {rating[13]}")
        st.write(f"Overview: {views[13]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')
    st.write("<span style='color:#FFD700;'>Find all these movies [here](https://fbox.to/home) and I hope you find them entertaining :)</span>",unsafe_allow_html=True)

elif prediction == 'War':
    st.subheader('Consider Watching...')
    url = "https://api.themoviedb.org/3/discover/movie?api_key=568bb4e8f6e76a6eda4ee919cd1d6b6e&language=en-US&sort_by=popularity,vote_average.desc&page=1&with_genres=10752"


    response = requests.get(url)
    r = response.json()

    path = r['results']

    new = []
    titles = []
    rating = []
    views = []

    for x in path:
        new.append(x['poster_path'])
        titles.append(x['title'])
        rating.append(round(x['vote_average'],1))
        views.append(x['overview'])

    first = "https://image.tmdb.org/t/p/w500"

    col1,col2 = st.columns((2))
    with col1:
        st.image(first+new[0])
        st.write(titles[0])
        st.write(f"Rating: {rating[0]}")
        st.write(f"Overview: {views[0]}")
    with col2:
        st.image(first+new[1])
        st.write(titles[1])
        st.write(f"Rating: {rating[1]}")
        st.write(f"Overview: {views[1]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col3,col4 = st.columns((2))
    with col3:
        st.image(first+new[2])
        st.write(titles[2])
        st.write(f"Rating: {rating[2]}")
        st.write(f"Overview: {views[2]}")
    with col4:
        st.image(first+new[3])
        st.write(titles[3])
        st.write(f"Rating: {rating[3]}")
        st.write(f"Overview: {views[3]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col5,col6 = st.columns((2))
    with col5:
        st.image(first+new[4])
        st.write(titles[4])
        st.write(f"Rating: {rating[4]}")
        st.write(f"Overview: {views[4]}")
    with col6:
        st.image(first+new[5])
        st.write(titles[5])
        st.write(f"Rating: {rating[5]}")
        st.write(f"Overview: {views[5]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col7,col8 = st.columns((2))
    with col7:
        st.image(first+new[6])
        st.write(titles[6])
        st.write(f"Rating: {rating[6]}")
        st.write(f"Overview: {views[6]}")
    with col8:
        st.image(first+new[7])
        st.write(titles[7])
        st.write(f"Rating: {rating[7]}")
        st.write(f"Overview: {views[7]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col9,col10 = st.columns((2))
    with col9:
        st.image(first+new[8])
        st.write(titles[8])
        st.write(f"Rating: {rating[8]}")
        st.write(f"Overview: {views[8]}")
    with col10:
        st.image(first+new[9])
        st.write(titles[9])
        st.write(f"Rating: {rating[9]}")
        st.write(f"Overview: {views[9]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col11,col12 = st.columns((2))
    with col11:
        st.image(first+new[10])
        st.write(titles[10])
        st.write(f"Rating: {rating[10]}")
        st.write(f"Overview: {views[10]}")
    with col12:
        st.image(first+new[11])
        st.write(titles[11])
        st.write(f"Rating: {rating[11]}")
        st.write(f"Overview: {views[11]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col13,col14 = st.columns((2))
    with col13:
        st.image(first+new[12])
        st.write(titles[12])
        st.write(f"Rating: {rating[12]}")
        st.write(f"Overview: {views[12]}")
    with col14:
        st.image(first+new[13])
        st.write(titles[13])
        st.write(f"Rating: {rating[13]}")
        st.write(f"Overview: {views[13]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')
    st.write("<span style='color:#FFD700;'>Find all these movies [here](https://fbox.to/home) and I hope you find them entertaining :)</span>",unsafe_allow_html=True)

elif prediction == 'Documentary':
    st.subheader('Consider Watching...')
    url = "https://api.themoviedb.org/3/discover/movie?api_key=568bb4e8f6e76a6eda4ee919cd1d6b6e&language=en-US&sort_by=popularity,vote_average.desc&page=1&with_genres=99"


    response = requests.get(url)
    r = response.json()

    path = r['results']

    new = []
    titles = []
    rating = []
    views = []

    for x in path:
        new.append(x['poster_path'])
        titles.append(x['title'])
        rating.append(round(x['vote_average'],1))
        views.append(x['overview'])

    first = "https://image.tmdb.org/t/p/w500"

    col1,col2 = st.columns((2))
    with col1:
        st.image(first+new[0])
        st.write(titles[0])
        st.write(f"Rating: {rating[0]}")
        st.write(f"Overview: {views[0]}")
    with col2:
        st.image(first+new[1])
        st.write(titles[1])
        st.write(f"Rating: {rating[1]}")
        st.write(f"Overview: {views[1]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col3,col4 = st.columns((2))
    with col3:
        st.image(first+new[2])
        st.write(titles[2])
        st.write(f"Rating: {rating[2]}")
        st.write(f"Overview: {views[2]}")
    with col4:
        st.image(first+new[3])
        st.write(titles[3])
        st.write(f"Rating: {rating[3]}")
        st.write(f"Overview: {views[3]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col5,col6 = st.columns((2))
    with col5:
        st.image(first+new[4])
        st.write(titles[4])
        st.write(f"Rating: {rating[4]}")
        st.write(f"Overview: {views[4]}")
    with col6:
        st.image(first+new[5])
        st.write(titles[5])
        st.write(f"Rating: {rating[5]}")
        st.write(f"Overview: {views[5]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col7,col8 = st.columns((2))
    with col7:
        st.image(first+new[6])
        st.write(titles[6])
        st.write(f"Rating: {rating[6]}")
        st.write(f"Overview: {views[6]}")
    with col8:
        st.image(first+new[7])
        st.write(titles[7])
        st.write(f"Rating: {rating[7]}")
        st.write(f"Overview: {views[7]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col9,col10 = st.columns((2))
    with col9:
        st.image(first+new[8])
        st.write(titles[8])
        st.write(f"Rating: {rating[8]}")
        st.write(f"Overview: {views[8]}")
    with col10:
        st.image(first+new[9])
        st.write(titles[9])
        st.write(f"Rating: {rating[9]}")
        st.write(f"Overview: {views[9]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col11,col12 = st.columns((2))
    with col11:
        st.image(first+new[10])
        st.write(titles[10])
        st.write(f"Rating: {rating[10]}")
        st.write(f"Overview: {views[10]}")
    with col12:
        st.image(first+new[11])
        st.write(titles[11])
        st.write(f"Rating: {rating[11]}")
        st.write(f"Overview: {views[11]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col13,col14 = st.columns((2))
    with col13:
        st.image(first+new[12])
        st.write(titles[12])
        st.write(f"Rating: {rating[12]}")
        st.write(f"Overview: {views[12]}")
    with col14:
        st.image(first+new[13])
        st.write(titles[13])
        st.write(f"Rating: {rating[13]}")
        st.write(f"Overview: {views[13]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')
    st.write("<span style='color:#FFD700;'>Find all these movies [here](https://fbox.to/home) and I hope you find them entertaining :)</span>",unsafe_allow_html=True)


elif prediction == 'Drama':
    st.subheader('Consider Watching...')
    url = "https://api.themoviedb.org/3/discover/movie?api_key=568bb4e8f6e76a6eda4ee919cd1d6b6e&language=en-US&sort_by=popularity,vote_average.desc&page=1&with_genres=18,10749"


    response = requests.get(url)
    r = response.json()

    path = r['results']

    new = []
    titles = []
    rating = []
    views = []

    for x in path:
        new.append(x['poster_path'])
        titles.append(x['title'])
        rating.append(round(x['vote_average'],1))
        views.append(x['overview'])

    first = "https://image.tmdb.org/t/p/w500"

    col1,col2 = st.columns((2))
    with col1:
        st.image(first+new[0])
        st.write(titles[0])
        st.write(f"Rating: {rating[0]}")
        st.write(f"Overview: {views[0]}")
    with col2:
        st.image(first+new[1])
        st.write(titles[1])
        st.write(f"Rating: {rating[1]}")
        st.write(f"Overview: {views[1]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col3,col4 = st.columns((2))
    with col3:
        st.image(first+new[2])
        st.write(titles[2])
        st.write(f"Rating: {rating[2]}")
        st.write(f"Overview: {views[2]}")
    with col4:
        st.image(first+new[3])
        st.write(titles[3])
        st.write(f"Rating: {rating[3]}")
        st.write(f"Overview: {views[3]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col5,col6 = st.columns((2))
    with col5:
        st.image(first+new[4])
        st.write(titles[4])
        st.write(f"Rating: {rating[4]}")
        st.write(f"Overview: {views[4]}")
    with col6:
        st.image(first+new[5])
        st.write(titles[5])
        st.write(f"Rating: {rating[5]}")
        st.write(f"Overview: {views[5]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col7,col8 = st.columns((2))
    with col7:
        st.image(first+new[6])
        st.write(titles[6])
        st.write(f"Rating: {rating[6]}")
        st.write(f"Overview: {views[6]}")
    with col8:
        st.image(first+new[7])
        st.write(titles[7])
        st.write(f"Rating: {rating[7]}")
        st.write(f"Overview: {views[7]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col9,col10 = st.columns((2))
    with col9:
        st.image(first+new[8])
        st.write(titles[8])
        st.write(f"Rating: {rating[8]}")
        st.write(f"Overview: {views[8]}")
    with col10:
        st.image(first+new[9])
        st.write(titles[9])
        st.write(f"Rating: {rating[9]}")
        st.write(f"Overview: {views[9]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col11,col12 = st.columns((2))
    with col11:
        st.image(first+new[10])
        st.write(titles[10])
        st.write(f"Rating: {rating[10]}")
        st.write(f"Overview: {views[10]}")
    with col12:
        st.image(first+new[11])
        st.write(titles[11])
        st.write(f"Rating: {rating[11]}")
        st.write(f"Overview: {views[11]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col13,col14 = st.columns((2))
    with col13:
        st.image(first+new[12])
        st.write(titles[12])
        st.write(f"Rating: {rating[12]}")
        st.write(f"Overview: {views[12]}")
    with col14:
        st.image(first+new[13])
        st.write(titles[13])
        st.write(f"Rating: {rating[13]}")
        st.write(f"Overview: {views[13]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')
    st.write("<span style='color:#FFD700;'>Find all these movies [here](https://fbox.to/home) and I hope you find them entertaining :)</span>",unsafe_allow_html=True)

elif prediction == 'Thriller':
    st.subheader('Consider Watching...')
    key = "568bb4e8f6e76a6eda4ee919cd1d6b6e"
    url = "https://api.themoviedb.org/3/discover/movie?api_key=568bb4e8f6e76a6eda4ee919cd1d6b6e&language=en-US&sort_by=popularity,vote_average.desc&page=1&with_genres=53,9648"


    response = requests.get(url)
    r = response.json()

    path = r['results']

    new = []
    titles = []
    rating = []
    views = []

    for x in path:
        new.append(x['poster_path'])
        titles.append(x['title'])
        rating.append(round(x['vote_average'],1))
        views.append(x['overview'])

    #st.write(r)

    first = "https://image.tmdb.org/t/p/w500"

    # for m in new[:15]:
    #     st.image(first+m)


    col1,col2 = st.columns((2))
    with col1:
        st.image(first+new[0])
        st.write(titles[0])
        st.write(f"Rating: {rating[0]}")
        st.write(f"Overview: {views[0]}")
    with col2:
        st.image(first+new[1])
        st.write(titles[1])
        st.write(f"Rating: {rating[1]}")
        st.write(f"Overview: {views[1]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col3,col4 = st.columns((2))
    with col3:
        st.image(first+new[2])
        st.write(titles[2])
        st.write(f"Rating: {rating[2]}")
        st.write(f"Overview: {views[2]}")
    with col4:
        st.image(first+new[3])
        st.write(titles[3])
        st.write(f"Rating: {rating[3]}")
        st.write(f"Overview: {views[3]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col5,col6 = st.columns((2))
    with col5:
        st.image(first+new[4])
        st.write(titles[4])
        st.write(f"Rating: {rating[4]}")
        st.write(f"Overview: {views[4]}")
    with col6:
        st.image(first+new[5])
        st.write(titles[5])
        st.write(f"Rating: {rating[5]}")
        st.write(f"Overview: {views[5]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col7,col8 = st.columns((2))
    with col7:
        st.image(first+new[6])
        st.write(titles[6])
        st.write(f"Rating: {rating[6]}")
        st.write(f"Overview: {views[6]}")
    with col8:
        st.image(first+new[7])
        st.write(titles[7])
        st.write(f"Rating: {rating[7]}")
        st.write(f"Overview: {views[7]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col9,col10 = st.columns((2))
    with col9:
        st.image(first+new[8])
        st.write(titles[8])
        st.write(f"Rating: {rating[8]}")
        st.write(f"Overview: {views[8]}")
    with col10:
        st.image(first+new[9])
        st.write(titles[9])
        st.write(f"Rating: {rating[9]}")
        st.write(f"Overview: {views[9]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col11,col12 = st.columns((2))
    with col11:
        st.image(first+new[10])
        st.write(titles[10])
        st.write(f"Rating: {rating[10]}")
        st.write(f"Overview: {views[10]}")
    with col12:
        st.image(first+new[11])
        st.write(titles[11])
        st.write(f"Rating: {rating[11]}")
        st.write(f"Overview: {views[11]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col13,col14 = st.columns((2))
    with col13:
        st.image(first+new[12])
        st.write(titles[12])
        st.write(f"Rating: {rating[12]}")
        st.write(f"Overview: {views[12]}")
    with col14:
        st.image(first+new[13])
        st.write(titles[13])
        st.write(f"Rating: {rating[13]}")
        st.write(f"Overview: {views[13]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')
    st.write("<span style='color:#FFD700;'>Find all these movies [here](https://fbox.to/home) and I hope you find them entertaining :)</span>",unsafe_allow_html=True)


elif prediction == 'Romance':
    st.subheader('Consider Watching...')
    url = "https://api.themoviedb.org/3/discover/movie?api_key=568bb4e8f6e76a6eda4ee919cd1d6b6e&language=en-US&sort_by=popularity,vote_average.desc&page=1&with_genres=10749,9648"


    response = requests.get(url)
    r = response.json()

    path = r['results']

    new = []
    titles = []
    rating = []
    views = []

    for x in path:
        new.append(x['poster_path'])
        titles.append(x['title'])
        rating.append(round(x['vote_average'],1))
        views.append(x['overview'])

    first = "https://image.tmdb.org/t/p/w500"

    col1,col2 = st.columns((2))
    with col1:
        st.image(first+new[0])
        st.write(titles[0])
        st.write(f"Rating: {rating[0]}")
        st.write(f"Overview: {views[0]}")
    with col2:
        st.image(first+new[1])
        st.write(titles[1])
        st.write(f"Rating: {rating[1]}")
        st.write(f"Overview: {views[1]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col3,col4 = st.columns((2))
    with col3:
        st.image(first+new[2])
        st.write(titles[2])
        st.write(f"Rating: {rating[2]}")
        st.write(f"Overview: {views[2]}")
    with col4:
        st.image(first+new[3])
        st.write(titles[3])
        st.write(f"Rating: {rating[3]}")
        st.write(f"Overview: {views[3]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col5,col6 = st.columns((2))
    with col5:
        st.image(first+new[4])
        st.write(titles[4])
        st.write(f"Rating: {rating[4]}")
        st.write(f"Overview: {views[4]}")
    with col6:
        st.image(first+new[5])
        st.write(titles[5])
        st.write(f"Rating: {rating[5]}")
        st.write(f"Overview: {views[5]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col7,col8 = st.columns((2))
    with col7:
        st.image(first+new[6])
        st.write(titles[6])
        st.write(f"Rating: {rating[6]}")
        st.write(f"Overview: {views[6]}")
    with col8:
        st.image(first+new[7])
        st.write(titles[7])
        st.write(f"Rating: {rating[7]}")
        st.write(f"Overview: {views[7]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col9,col10 = st.columns((2))
    with col9:
        st.image(first+new[8])
        st.write(titles[8])
        st.write(f"Rating: {rating[8]}")
        st.write(f"Overview: {views[8]}")
    with col10:
        st.image(first+new[9])
        st.write(titles[9])
        st.write(f"Rating: {rating[9]}")
        st.write(f"Overview: {views[9]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col11,col12 = st.columns((2))
    with col11:
        st.image(first+new[10])
        st.write(titles[10])
        st.write(f"Rating: {rating[10]}")
        st.write(f"Overview: {views[10]}")
    with col12:
        st.image(first+new[11])
        st.write(titles[11])
        st.write(f"Rating: {rating[11]}")
        st.write(f"Overview: {views[11]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col13,col14 = st.columns((2))
    with col13:
        st.image(first+new[12])
        st.write(titles[12])
        st.write(f"Rating: {rating[12]}")
        st.write(f"Overview: {views[12]}")
    with col14:
        st.image(first+new[13])
        st.write(titles[13])
        st.write(f"Rating: {rating[13]}")
        st.write(f"Overview: {views[13]}")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')
    st.write("<span style='color:#FFD700;'>Find all these movies [here](https://fbox.to/home) and I hope you find them entertaining :)</span>",unsafe_allow_html=True)
