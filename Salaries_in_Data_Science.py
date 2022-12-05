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
st.write("try out maps and ya done")
st.write("know your worth maybe skip")


st.map(df2)
def main():
    html_temp = """<div class='tableauPlaceholder' 
    id='viz1670124138937' style='position: relative'><noscript><a href='#'><img alt='HOW MUCH CAN YOU MAKE IN DATA SCIENCE?An analysis of jobs offered on Glassdoor ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sa&#47;SalariesinDataScience_16694182554330&#47;Story1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  
    style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='SalariesinDataScience_16694182554330&#47;Story1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' 
    /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Sa&#47;SalariesinDataScience_16694182554330&#47;Story1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' />
    <param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1670124138937');                 
       var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');              
             scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    components.html(html_temp)
if __name__ == "__main__":    
    main()





