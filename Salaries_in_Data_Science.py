import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import streamlit.components.v1 as components


################################Data stuff##########################################
df = pd.read_csv("data/Cleaned_Salaries.csv")
job_title_option = df["Job Title"].unique()


############################SIDE BAR################################################
# st.sidebar.success("Select a demo above.")

#list of job titles to use in new df  ##should i keep this as a single value or multi
option1 = st.sidebar.multiselect(
    'Figure1: What job are you interested in?',
    job_title_option,["Data Scientist"])

#testing




###################################MAIN PAGE######################################

st.header("Salaries in Data Science")
# options = st.multiselect(
#     'What are your favorite colors',
#     ['Green', 'Yellow', 'Red', 'Blue'],
#     ['Yellow', 'Red'])
#st.write('You selected:', options)
st.write("This dataset was made by scrapping the job postings related to the position of 'Data Scientist' from www.glassdoor.com in USA, Selenium was used to scrap the data. After scrapping the raw data, duplicated rows from it which reduced the records from 1000 to 742. After this, several simplifications were performed to make the data user friendly for further data analysis and modelling.")

tab1, tab2, tab3 = st.tabs(["Average Salary", "Does Degree Matter?", "Senority"])

with tab1:
    #Figure 1 Salary vs title  Avg Salary(K)

    df2=df.loc[df["Job Title"].isin(option1)]
    #st.write(df2)
    st.write("FIGURE 1: Average Salary")


    #st.write(df2)
    c1=alt.Chart(df2).mark_bar().encode(
        alt.X("Avg Salary(K)",  bin=alt.Bin(maxbins=25)),
        y='count()',
    )

    st.altair_chart(c1, use_container_width=True)


with tab2:
    ## Figure 2

    st.write("FIGURE 2: What type of Degrees are used in the field?")


    #st.write(df2)
    c2=alt.Chart(df2).mark_bar().encode(
        x="Degree",
        y='count()',
    )

    st.altair_chart(c2, use_container_width=True)

    ## Figure 3



with tab3:
    st.write("FIGURE 3: Senority level")
    #st.write(df2)
    c3=alt.Chart(df2).mark_bar().encode(
        x="seniority_by_title",
        y='count()',
    )

    st.altair_chart(c3, use_container_width=True)





st.write("## The highest paying job in "+ str(option1).strip("[").strip("]"))
#st.write(df2.max())
st.write("#### Job Title: "+str(df2.max()["Job Title"]) )
st.write("#### Company: " + df2.max()["company_txt"] )
st.write("#### Salary: "+str(df2.max()["Avg Salary(K)"]) + " k")
st.write("#### Education: " + df2.max()["Degree"] )



