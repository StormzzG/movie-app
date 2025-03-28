import streamlit as st 
import joblib 
from test import get_data
from test import get_link

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
    path = get_data(37)

    new = []
    titles = []
    rating = []
    views = []
    counts = []
    ids = []

    for x in path:
        new.append(x['poster_path'])
        titles.append(x['title'])
        rating.append(round(x['vote_average'],1))
        views.append(x['overview'])
        counts.append(x['vote_count'])
        ids.append(x['id'])
    
    first = "https://image.tmdb.org/t/p/w500"

    col1,col2 = st.columns((2))
    with col1:
        st.image(first+new[0])
        st.write(titles[0])
        st.write(f"Rating: {rating[0]} by {counts[0]} reviews")
        st.write(f"Overview: {views[0]}")
        id = ids[0]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col2:
        st.image(first+new[1])
        st.write(titles[1])
        st.write(f"Rating: {rating[1]} by {counts[1]} reviews")
        st.write(f"Overview: {views[1]}")
        id = ids[1]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col3,col4 = st.columns((2))
    with col3:
        st.image(first+new[2])
        st.write(titles[2])
        st.write(f"Rating: {rating[2]} by {counts[2]} reviews")
        st.write(f"Overview: {views[2]}")
        id = ids[2]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col4:
        st.image(first+new[3])
        st.write(titles[3])
        st.write(f"Rating: {rating[3]} by {counts[3]} reviews")
        st.write(f"Overview: {views[3]}")
        id = ids[3]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col5,col6 = st.columns((2))
    with col5:
        st.image(first+new[4])
        st.write(titles[4])
        st.write(f"Rating: {rating[4]} by {counts[4]} reviews")
        st.write(f"Overview: {views[4]}")
        id = ids[4]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col6:
        st.image(first+new[5])
        st.write(titles[5])
        st.write(f"Rating: {rating[5]} by {counts[5]} reviews")
        st.write(f"Overview: {views[5]}")
        id = ids[5]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col7,col8 = st.columns((2))
    with col7:
        st.image(first+new[6])
        st.write(titles[6])
        st.write(f"Rating: {rating[6]} by {counts[6]} reviews")
        st.write(f"Overview: {views[6]}")
        id = ids[6]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col8:
        st.image(first+new[7])
        st.write(titles[7])
        st.write(f"Rating: {rating[7]} by {counts[7]} reviews")
        st.write(f"Overview: {views[7]}")
        id = ids[7]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col9,col10 = st.columns((2))
    with col9:
        st.image(first+new[8])
        st.write(titles[8])
        st.write(f"Rating: {rating[8]} by {counts[8]} reviews")
        st.write(f"Overview: {views[8]}")
        id = ids[8]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col10:
        st.image(first+new[9])
        st.write(titles[9])
        st.write(f"Rating: {rating[9]} by {counts[9]} reviews")
        st.write(f"Overview: {views[9]}")
        id = ids[9]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col11,col12 = st.columns((2))
    with col11:
        st.image(first+new[10])
        st.write(titles[10])
        st.write(f"Rating: {rating[10]} by {counts[10]} reviews")
        st.write(f"Overview: {views[10]}")
        id = ids[10]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col12:
        st.image(first+new[11])
        st.write(titles[11])
        st.write(f"Rating: {rating[11]} by {counts[11]} reviews")
        st.write(f"Overview: {views[11]}")
        id = ids[11]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col13,col14 = st.columns((2))
    with col13:
        st.image(first+new[12])
        st.write(titles[12])
        st.write(f"Rating: {rating[12]} by {counts[12]} reviews")
        st.write(f"Overview: {views[12]}")
        id = ids[12]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col14:
        st.image(first+new[13])
        st.write(titles[13])
        st.write(f"Rating: {rating[13]} by {counts[13]} reviews")
        st.write(f"Overview: {views[13]}")
        id = ids[13]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')
    st.write("<span style='color:#FFD700;'>Find all these movies [here](https://moviebox.ng/) and I hope you find them entertaining :)</span>",unsafe_allow_html=True)


elif prediction == 'Action':
    st.subheader('Consider Watching...')
    path = get_data(28)

    new = []
    titles = []
    rating = []
    views = []
    counts = []
    ids = []

    for x in path:
        new.append(x['poster_path'])
        titles.append(x['title'])
        rating.append(round(x['vote_average'],1))
        views.append(x['overview'])
        counts.append(x['vote_count'])
        ids.append(x['id'])

    first = "https://image.tmdb.org/t/p/w500"

    col1,col2 = st.columns((2))
    with col1:
        st.image(first+new[0])
        st.write(titles[0])
        st.write(f"Rating: {rating[0]} by {counts[0]} reviews")
        st.write(f"Overview: {views[0]}")
        id = ids[0]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col2:
        st.image(first+new[1])
        st.write(titles[1])
        st.write(f"Rating: {rating[1]} by {counts[1]} reviews")
        st.write(f"Overview: {views[1]}")
        id = ids[1]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col3,col4 = st.columns((2))
    with col3:
        st.image(first+new[2])
        st.write(titles[2])
        st.write(f"Rating: {rating[2]} by {counts[2]} reviews")
        st.write(f"Overview: {views[2]}")
        id = ids[2]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col4:
        st.image(first+new[3])
        st.write(titles[3])
        st.write(f"Rating: {rating[3]} by {counts[3]} reviews")
        st.write(f"Overview: {views[3]}")
        id = ids[3]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col5,col6 = st.columns((2))
    with col5:
        st.image(first+new[4])
        st.write(titles[4])
        st.write(f"Rating: {rating[4]} by {counts[4]} reviews")
        st.write(f"Overview: {views[4]}")
        id = ids[4]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col6:
        st.image(first+new[5])
        st.write(titles[5])
        st.write(f"Rating: {rating[5]} by {counts[5]} reviews")
        st.write(f"Overview: {views[5]}")
        id = ids[5]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col7,col8 = st.columns((2))
    with col7:
        st.image(first+new[6])
        st.write(titles[6])
        st.write(f"Rating: {rating[6]} by {counts[6]} reviews")
        st.write(f"Overview: {views[6]}")
        id = ids[6]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col8:
        st.image(first+new[7])
        st.write(titles[7])
        st.write(f"Rating: {rating[7]} by {counts[7]} reviews")
        st.write(f"Overview: {views[7]}")
        id = ids[7]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col9,col10 = st.columns((2))
    with col9:
        st.image(first+new[8])
        st.write(titles[8])
        st.write(f"Rating: {rating[8]} by {counts[8]} reviews")
        st.write(f"Overview: {views[8]}")
        id = ids[8]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col10:
        st.image(first+new[9])
        st.write(titles[9])
        st.write(f"Rating: {rating[9]} by {counts[9]} reviews")
        st.write(f"Overview: {views[9]}")
        id = ids[9]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col11,col12 = st.columns((2))
    with col11:
        st.image(first+new[10])
        st.write(titles[10])
        st.write(f"Rating: {rating[10]} by {counts[10]} reviews")
        st.write(f"Overview: {views[10]}")
        id = ids[10]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col12:
        st.image(first+new[11])
        st.write(titles[11])
        st.write(f"Rating: {rating[11]} by {counts[11]} reviews")
        st.write(f"Overview: {views[11]}")
        id = ids[11]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col13,col14 = st.columns((2))
    with col13:
        st.image(first+new[12])
        st.write(titles[12])
        st.write(f"Rating: {rating[12]} by {counts[12]} reviews")
        st.write(f"Overview: {views[12]}")
        id = ids[12]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col14:
        st.image(first+new[13])
        st.write(titles[13])
        st.write(f"Rating: {rating[13]} by {counts[13]} reviews")
        st.write(f"Overview: {views[13]}")
        id = ids[13]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')
    st.write("<span style='color:#FFD700;'>Find all these movies [here](https://moviebox.ng/) and I hope you find them entertaining :)</span>",unsafe_allow_html=True)

elif prediction == 'War':
    st.subheader('Consider Watching...')
    path = get_data(10752)

    new = []
    titles = []
    rating = []
    views = []
    counts = []
    ids = []

    for x in path:
        new.append(x['poster_path'])
        titles.append(x['title'])
        rating.append(round(x['vote_average'],1))
        views.append(x['overview'])
        counts.append(x['vote_count'])
        ids.append(x['id'])


    first = "https://image.tmdb.org/t/p/w500"

    col1,col2 = st.columns((2))
    with col1:
        st.image(first+new[0])
        st.write(titles[0])
        st.write(f"Rating: {rating[0]} by {counts[0]} reviews")
        st.write(f"Overview: {views[0]}")
        id = ids[0]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col2:
        st.image(first+new[1])
        st.write(titles[1])
        st.write(f"Rating: {rating[1]} by {counts[1]} reviews")
        st.write(f"Overview: {views[1]}")
        id = ids[1]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col3,col4 = st.columns((2))
    with col3:
        st.image(first+new[2])
        st.write(titles[2])
        st.write(f"Rating: {rating[2]} by {counts[2]} reviews")
        st.write(f"Overview: {views[2]}")
        id = ids[2]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col4:
        st.image(first+new[3])
        st.write(titles[3])
        st.write(f"Rating: {rating[3]} by {counts[3]} reviews")
        st.write(f"Overview: {views[3]}")
        id = ids[3]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col5,col6 = st.columns((2))
    with col5:
        st.image(first+new[4])
        st.write(titles[4])
        st.write(f"Rating: {rating[4]} by {counts[4]} reviews")
        st.write(f"Overview: {views[4]}")
        id = ids[4]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col6:
        st.image(first+new[5])
        st.write(titles[5])
        st.write(f"Rating: {rating[5]} by {counts[5]} reviews")
        st.write(f"Overview: {views[5]}")
        id = ids[5]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col7,col8 = st.columns((2))
    with col7:
        st.image(first+new[6])
        st.write(titles[6])
        st.write(f"Rating: {rating[6]} by {counts[6]} reviews")
        st.write(f"Overview: {views[6]}")
        id = ids[6]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col8:
        st.image(first+new[7])
        st.write(titles[7])
        st.write(f"Rating: {rating[7]} by {counts[7]} reviews")
        st.write(f"Overview: {views[7]}")
        id = ids[7]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col9,col10 = st.columns((2))
    with col9:
        st.image(first+new[8])
        st.write(titles[8])
        st.write(f"Rating: {rating[8]} by {counts[8]} reviews")
        st.write(f"Overview: {views[8]}")
        id = ids[8]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col10:
        st.image(first+new[9])
        st.write(titles[9])
        st.write(f"Rating: {rating[9]} by {counts[9]} reviews")
        st.write(f"Overview: {views[9]}")
        id = ids[9]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col11,col12 = st.columns((2))
    with col11:
        st.image(first+new[10])
        st.write(titles[10])
        st.write(f"Rating: {rating[10]} by {counts[10]} reviews")
        st.write(f"Overview: {views[10]}")
        id = ids[10]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col12:
        st.image(first+new[11])
        st.write(titles[11])
        st.write(f"Rating: {rating[11]} by {counts[11]} reviews")
        st.write(f"Overview: {views[11]}")
        id = ids[11]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col13,col14 = st.columns((2))
    with col13:
        st.image(first+new[12])
        st.write(titles[12])
        st.write(f"Rating: {rating[12]} by {counts[12]} reviews")
        st.write(f"Overview: {views[12]}")
        id = ids[12]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col14:
        st.image(first+new[13])
        st.write(titles[13])
        st.write(f"Rating: {rating[13]} by {counts[13]} reviews")
        st.write(f"Overview: {views[13]}")
        id = ids[13]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')
    st.write("<span style='color:#FFD700;'>Find all these movies [here](https://moviebox.ng/) and I hope you find them entertaining :)</span>",unsafe_allow_html=True)

elif prediction == 'Documentary':
    st.subheader('Consider Watching...')
    path = get_data(99)

    new = []
    titles = []
    rating = []
    views = []
    counts = []
    ids = []

    for x in path:
        new.append(x['poster_path'])
        titles.append(x['title'])
        rating.append(round(x['vote_average'],1))
        views.append(x['overview'])
        counts.append(x['vote_count'])
        ids.append(x['id'])

    first = "https://image.tmdb.org/t/p/w500"

    col1,col2 = st.columns((2))
    with col1:
        st.image(first+new[0])
        st.write(titles[0])
        st.write(f"Rating: {rating[0]} by {counts[0]} reviews")
        st.write(f"Overview: {views[0]}")
        id = ids[0]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col2:
        st.image(first+new[1])
        st.write(titles[1])
        st.write(f"Rating: {rating[1]} by {counts[1]} reviews")
        st.write(f"Overview: {views[1]}")
        id = ids[1]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col3,col4 = st.columns((2))
    with col3:
        st.image(first+new[2])
        st.write(titles[2])
        st.write(f"Rating: {rating[2]} by {counts[2]} reviews")
        st.write(f"Overview: {views[2]}")
        id = ids[2]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col4:
        st.image(first+new[3])
        st.write(titles[3])
        st.write(f"Rating: {rating[3]} by {counts[3]} reviews")
        st.write(f"Overview: {views[3]}")
        id = ids[3]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col5,col6 = st.columns((2))
    with col5:
        st.image(first+new[4])
        st.write(titles[4])
        st.write(f"Rating: {rating[4]} by {counts[4]} reviews")
        st.write(f"Overview: {views[4]}")
        id = ids[4]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col6:
        st.image(first+new[5])
        st.write(titles[5])
        st.write(f"Rating: {rating[5]} by {counts[5]} reviews")
        st.write(f"Overview: {views[5]}")
        id = ids[5]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col7,col8 = st.columns((2))
    with col7:
        st.image(first+new[6])
        st.write(titles[6])
        st.write(f"Rating: {rating[6]} by {counts[6]} reviews")
        st.write(f"Overview: {views[6]}")
        id = ids[6]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col8:
        st.image(first+new[7])
        st.write(titles[7])
        st.write(f"Rating: {rating[7]} by {counts[7]} reviews")
        st.write(f"Overview: {views[7]}")
        id = ids[7]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col9,col10 = st.columns((2))
    with col9:
        st.image(first+new[8])
        st.write(titles[8])
        st.write(f"Rating: {rating[8]} by {counts[8]} reviews")
        st.write(f"Overview: {views[8]}")
        id = ids[8]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col10:
        st.image(first+new[9])
        st.write(titles[9])
        st.write(f"Rating: {rating[9]} by {counts[9]} reviews")
        st.write(f"Overview: {views[9]}")
        id = ids[9]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col11,col12 = st.columns((2))
    with col11:
        st.image(first+new[10])
        st.write(titles[10])
        st.write(f"Rating: {rating[10]} by {counts[10]} reviews")
        st.write(f"Overview: {views[10]}")
        id = ids[10]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col12:
        st.image(first+new[11])
        st.write(titles[11])
        st.write(f"Rating: {rating[11]} by {counts[11]} reviews")
        st.write(f"Overview: {views[11]}")
        id = ids[11]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col13,col14 = st.columns((2))
    with col13:
        st.image(first+new[12])
        st.write(titles[12])
        st.write(f"Rating: {rating[12]} by {counts[12]} reviews")
        st.write(f"Overview: {views[12]}")
        id = ids[12]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col14:
        st.image(first+new[13])
        st.write(titles[13])
        st.write(f"Rating: {rating[13]} by {counts[13]} reviews")
        st.write(f"Overview: {views[13]}")
        id = ids[13]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')
    st.write("<span style='color:#FFD700;'>Find all these movies [here](https://moviebox.ng/) and I hope you find them entertaining :)</span>",unsafe_allow_html=True)


elif prediction == 'Drama':
    st.subheader('Consider Watching...')
    path = get_data(18,10749)

    new = []
    titles = []
    rating = []
    views = []
    counts = []
    ids = []

    for x in path:
        new.append(x['poster_path'])
        titles.append(x['title'])
        rating.append(round(x['vote_average'],1))
        views.append(x['overview'])
        counts.append(x['vote_count'])
        ids.append(x['id'])

    first = "https://image.tmdb.org/t/p/w500"

    col1,col2 = st.columns((2))
    with col1:
        st.image(first+new[0])
        st.write(titles[0])
        st.write(f"Rating: {rating[0]} by {counts[0]} reviews")
        st.write(f"Overview: {views[0]}")
        id = ids[0]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col2:
        st.image(first+new[1])
        st.write(titles[1])
        st.write(f"Rating: {rating[1]} by {counts[1]} reviews")
        st.write(f"Overview: {views[1]}")
        id = ids[1]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col3,col4 = st.columns((2))
    with col3:
        st.image(first+new[2])
        st.write(titles[2])
        st.write(f"Rating: {rating[2]} by {counts[2]} reviews")
        st.write(f"Overview: {views[2]}")
        id = ids[2]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col4:
        st.image(first+new[3])
        st.write(titles[3])
        st.write(f"Rating: {rating[3]} by {counts[3]} reviews")
        st.write(f"Overview: {views[3]}")
        id = ids[3]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col5,col6 = st.columns((2))
    with col5:
        st.image(first+new[4])
        st.write(titles[4])
        st.write(f"Rating: {rating[4]} by {counts[4]} reviews")
        st.write(f"Overview: {views[4]}")
        id = ids[4]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col6:
        st.image(first+new[5])
        st.write(titles[5])
        st.write(f"Rating: {rating[5]} by {counts[5]} reviews")
        st.write(f"Overview: {views[5]}")
        id = ids[5]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col7,col8 = st.columns((2))
    with col7:
        st.image(first+new[6])
        st.write(titles[6])
        st.write(f"Rating: {rating[6]} by {counts[6]} reviews")
        st.write(f"Overview: {views[6]}")
        id = ids[6]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col8:
        st.image(first+new[7])
        st.write(titles[7])
        st.write(f"Rating: {rating[7]} by {counts[7]} reviews")
        st.write(f"Overview: {views[7]}")
        id = ids[7]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col9,col10 = st.columns((2))
    with col9:
        st.image(first+new[8])
        st.write(titles[8])
        st.write(f"Rating: {rating[8]} by {counts[8]} reviews")
        st.write(f"Overview: {views[8]}")
        id = ids[8]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col10:
        st.image(first+new[9])
        st.write(titles[9])
        st.write(f"Rating: {rating[9]} by {counts[9]} reviews")
        st.write(f"Overview: {views[9]}")
        id = ids[9]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col11,col12 = st.columns((2))
    with col11:
        st.image(first+new[10])
        st.write(titles[10])
        st.write(f"Rating: {rating[10]} by {counts[10]} reviews")
        st.write(f"Overview: {views[10]}")
        id = ids[10]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col12:
        st.image(first+new[11])
        st.write(titles[11])
        st.write(f"Rating: {rating[11]} by {counts[11]} reviews")
        st.write(f"Overview: {views[11]}")
        id = ids[11]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col13,col14 = st.columns((2))
    with col13:
        st.image(first+new[12])
        st.write(titles[12])
        st.write(f"Rating: {rating[12]} by {counts[12]} reviews")
        st.write(f"Overview: {views[12]}")
        id = ids[12]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col14:
        st.image(first+new[13])
        st.write(titles[13])
        st.write(f"Rating: {rating[13]} by {counts[13]} reviews")
        st.write(f"Overview: {views[13]}")
        id = ids[13]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')
    st.write("<span style='color:#FFD700;'>Find all these movies [here](https://moviebox.ng/) and I hope you find them entertaining :)</span>",unsafe_allow_html=True)

elif prediction == 'Thriller':
    st.subheader('Consider Watching...')
    path = get_data(53, 9648)

    new = []
    titles = []
    rating = []
    views = []
    counts = []
    ids = []

    for x in path:
        new.append(x['poster_path'])
        titles.append(x['title'])
        rating.append(round(x['vote_average'],1))
        views.append(x['overview'])
        counts.append(x['vote_count'])
        ids.append(x['id'])

    first = "https://image.tmdb.org/t/p/w500"

    col1,col2 = st.columns((2))
    with col1:
        st.image(first+new[0])
        st.write(titles[0])
        st.write(f"Rating: {rating[0]} by {counts[0]} reviews")
        st.write(f"Overview: {views[0]}")
        id = ids[0]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col2:
        st.image(first+new[1])
        st.write(titles[1])
        st.write(f"Rating: {rating[1]} by {counts[1]} reviews")
        st.write(f"Overview: {views[1]}")
        id = ids[1]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col3,col4 = st.columns((2))
    with col3:
        st.image(first+new[2])
        st.write(titles[2])
        st.write(f"Rating: {rating[2]} by {counts[2]} reviews")
        st.write(f"Overview: {views[2]}")
        id = ids[2]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col4:
        st.image(first+new[3])
        st.write(titles[3])
        st.write(f"Rating: {rating[3]} by {counts[3]} reviews")
        st.write(f"Overview: {views[3]}")
        id = ids[3]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col5,col6 = st.columns((2))
    with col5:
        st.image(first+new[4])
        st.write(titles[4])
        st.write(f"Rating: {rating[4]} by {counts[4]} reviews")
        st.write(f"Overview: {views[4]}")
        id = ids[4]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col6:
        st.image(first+new[5])
        st.write(titles[5])
        st.write(f"Rating: {rating[5]} by {counts[5]} reviews")
        st.write(f"Overview: {views[5]}")
        id = ids[5]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col7,col8 = st.columns((2))
    with col7:
        st.image(first+new[6])
        st.write(titles[6])
        st.write(f"Rating: {rating[6]} by {counts[6]} reviews")
        st.write(f"Overview: {views[6]}")
        id = ids[6]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col8:
        st.image(first+new[7])
        st.write(titles[7])
        st.write(f"Rating: {rating[7]} by {counts[7]} reviews")
        st.write(f"Overview: {views[7]}")
        id = ids[7]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col9,col10 = st.columns((2))
    with col9:
        st.image(first+new[8])
        st.write(titles[8])
        st.write(f"Rating: {rating[8]} by {counts[8]} reviews")
        st.write(f"Overview: {views[8]}")
        id = ids[8]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col10:
        st.image(first+new[9])
        st.write(titles[9])
        st.write(f"Rating: {rating[9]} by {counts[9]} reviews")
        st.write(f"Overview: {views[9]}")
        id = ids[9]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col11,col12 = st.columns((2))
    with col11:
        st.image(first+new[10])
        st.write(titles[10])
        st.write(f"Rating: {rating[10]} by {counts[10]} reviews")
        st.write(f"Overview: {views[10]}")
        id = ids[10]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col12:
        st.image(first+new[11])
        st.write(titles[11])
        st.write(f"Rating: {rating[11]} by {counts[11]} reviews")
        st.write(f"Overview: {views[11]}")
        id = ids[11]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col13,col14 = st.columns((2))
    with col13:
        st.image(first+new[12])
        st.write(titles[12])
        st.write(f"Rating: {rating[12]} by {counts[12]} reviews")
        st.write(f"Overview: {views[12]}")
        id = ids[12]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col14:
        st.image(first+new[13])
        st.write(titles[13])
        st.write(f"Rating: {rating[13]} by {counts[13]} reviews")
        st.write(f"Overview: {views[13]}")
        id = ids[13]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')
    st.write("<span style='color:#FFD700;'>Find all these movies [here](https://moviebox.ng/) and I hope you find them entertaining :)</span>",unsafe_allow_html=True)


elif prediction == 'Romance':
    st.subheader('Consider Watching...')
    path = get_data(10749, 9648)

    new = []
    titles = []
    rating = []
    views = []
    counts = []
    ids = []

    for x in path:
        new.append(x['poster_path'])
        titles.append(x['title'])
        rating.append(round(x['vote_average'],1))
        views.append(x['overview'])
        counts.append(x['vote_count'])
        ids.append(x['id'])

    first = "https://image.tmdb.org/t/p/w500"

    col1,col2 = st.columns((2))
    with col1:
        st.image(first+new[0])
        st.write(titles[0])
        st.write(f"Rating: {rating[0]} by {counts[0]} reviews")
        st.write(f"Overview: {views[0]}")
        id = ids[0]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col2:
        st.image(first+new[1])
        st.write(titles[1])
        st.write(f"Rating: {rating[1]} by {counts[1]} reviews")
        st.write(f"Overview: {views[1]}")
        id = ids[1]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col3,col4 = st.columns((2))
    with col3:
        st.image(first+new[2])
        st.write(titles[2])
        st.write(f"Rating: {rating[2]} by {counts[2]} reviews")
        st.write(f"Overview: {views[2]}")
        id = ids[2]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col4:
        st.image(first+new[3])
        st.write(titles[3])
        st.write(f"Rating: {rating[3]} by {counts[3]} reviews")
        st.write(f"Overview: {views[3]}")
        id = ids[3]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col5,col6 = st.columns((2))
    with col5:
        st.image(first+new[4])
        st.write(titles[4])
        st.write(f"Rating: {rating[4]} by {counts[4]} reviews")
        st.write(f"Overview: {views[4]}")
        id = ids[4]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col6:
        st.image(first+new[5])
        st.write(titles[5])
        st.write(f"Rating: {rating[5]} by {counts[5]} reviews")
        st.write(f"Overview: {views[5]}")
        id = ids[5]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col7,col8 = st.columns((2))
    with col7:
        st.image(first+new[6])
        st.write(titles[6])
        st.write(f"Rating: {rating[6]} by {counts[6]} reviews")
        st.write(f"Overview: {views[6]}")
        id = ids[6]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col8:
        st.image(first+new[7])
        st.write(titles[7])
        st.write(f"Rating: {rating[7]} by {counts[7]} reviews")
        st.write(f"Overview: {views[7]}")
        id = ids[7]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col9,col10 = st.columns((2))
    with col9:
        st.image(first+new[8])
        st.write(titles[8])
        st.write(f"Rating: {rating[8]} by {counts[8]} reviews")
        st.write(f"Overview: {views[8]}")
        id = ids[8]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col10:
        st.image(first+new[9])
        st.write(titles[9])
        st.write(f"Rating: {rating[9]} by {counts[9]} reviews")
        st.write(f"Overview: {views[9]}")
        id = ids[9]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col11,col12 = st.columns((2))
    with col11:
        st.image(first+new[10])
        st.write(titles[10])
        st.write(f"Rating: {rating[10]} by {counts[10]} reviews")
        st.write(f"Overview: {views[10]}")
        id = ids[10]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col12:
        st.image(first+new[11])
        st.write(titles[11])
        st.write(f"Rating: {rating[11]} by {counts[11]} reviews")
        st.write(f"Overview: {views[11]}")
        id = ids[11]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')

    col13,col14 = st.columns((2))
    with col13:
        st.image(first+new[12])
        st.write(titles[12])
        st.write(f"Rating: {rating[12]} by {counts[12]} reviews")
        st.write(f"Overview: {views[12]}")
        id = ids[12]
        key = get_link(id)
        st.write(f"[Trailer]({key})")
    with col14:
        st.image(first+new[13])
        st.write(titles[13])
        st.write(f"Rating: {rating[13]} by {counts[13]} reviews")
        st.write(f"Overview: {views[13]}")
        id = ids[13]
        key = get_link(id)
        st.write(f"[Trailer]({key})")

    st.markdown('<style>div.block-container{padding-top: 8rem}<style>', unsafe_allow_html=True)
    st.markdown('-----------------------------------')
    st.write("<span style='color:#FFD700;'>Find all these movies [here](https://moviebox.ng/) and I hope you find them entertaining :)</span>",unsafe_allow_html=True)

with st.expander('About App'):
    st.write("<span style='color:#FFD700;'>This recommender is built on a supervised Decision Tree Classifier machine learning algorithm. Classification is based on age and gender using this data to recommend the best movies for you. The use of TMDB API [documentation here](https://developer.themoviedb.org/reference/intro/getting-started) has been implemented to keep you up to date with the latest and the best.</span>", unsafe_allow_html=True)