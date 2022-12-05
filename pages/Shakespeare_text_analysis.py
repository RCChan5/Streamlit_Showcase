from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# Importing the StringIO module.
from io import StringIO 
from collections import Counter
import re
import altair as alt
st.write("## Analyzing shakespeare texts")

st.sidebar.header("Word Cloud Settings")
max_word = st.sidebar.slider("Max Words",10,200,100,10)
max_font = st.sidebar.slider("Size of largest word",50,350,60)
image_size = st.sidebar.slider("Image width",100,800,400,10)
random = st.sidebar.slider("Random State",30,100,42)
stop_words_bool = st.sidebar.checkbox("Remove stop words?")
st.sidebar.header("Word Count Settings")
min_Count_Word=st.sidebar.slider("Minimum count of words",5,100,40,1) 



file=st.selectbox("slect your book:",("","A Mid Summers Night's Dream","The Merchant of Venice","Romeo and Juliet"))
if file == "A Mid Summers Night's Dream":
    file = "data/summer.txt"
elif file == "The Merchant of Venice":
    file = "data/merchant.txt"
elif file == "Romeo and Juliet":
    file = "data/romeo.txt"  
else:
    file=None

if file is not None:
    with open(file, 'r') as file:
        data = file.read()


uploaded_file=file


if uploaded_file is not None:
   

    # To convert to a string based IO:
    #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))  

    stringio = StringIO(data)
    
    dataset=stringio.read()

    stopwords = set(STOPWORDS)
    if stop_words_bool:
        stopwords.update(['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',
        'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
        'put', 'seem', 'asked', 'made', 'half', 'much',
        'certainly', 'might', 'came'])
tab1, tab2, tab3 = st.tabs(["Word Cloud","Bar Chart","View Text"])


with tab1:
     if uploaded_file is not None:
        cloud = WordCloud(background_color = "white", 
                            max_words = max_word, 
                            max_font_size=max_font, 
                            stopwords = stopwords, 
                            random_state=random)
        wc = cloud.generate(dataset)
        word_cloud = cloud.to_file('wordcloud.png')
        st.image(wc.to_array(),width=image_size)
display=[]
with tab2:
    if uploaded_file is not None:
        

        data2 = re.sub(r'[^\w\s]', '', data)
        #data2.replace("19901993","1990 1993")
        #insert the fix for copyright label here
        data2=data2.lower()

        stop_words = ['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',
        'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
        'put', 'seem', 'asked', 'made', 'half', 'much',
        'certainly', 'might', 'came']

        
#x axis is word count
#y is the word
#if stopwords is true if word in the list skip

        x = sorted(Counter(data2.split()).items())
        new = pd.DataFrame.from_dict(x)
        new.columns=["Word","Count"]
        new=new.sort_values(["Count"], ascending=False)
        display = new[new["Count"]>=min_Count_Word]

        if stop_words_bool:
            
            for i in stop_words:
                display.drop(display[display['Word'] == i].index, inplace = True)
               
                       

#sort df by max# sort by desc

        c = alt.Chart(display).mark_bar().encode(
            x='Count:Q',
            y=alt.Y('Word:N', sort='-x'),
            tooltip=["Count"]

        )
        # text = c.mark_text(
        # align='left',
        # baseline='middle',
        # dx=3  # Nudges text to right so it doesn't appear on top of the bar
        # ).encode(
        # text='Count:Q'
        # )

       
        st.altair_chart(c, use_container_width=True)


        #st.bar_chart(data=display, x="Count",y="Word")
                    





with tab3:
    if uploaded_file is not None:   
        st.write(dataset)