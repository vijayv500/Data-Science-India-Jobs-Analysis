import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st 
st.set_option('deprecation.showPyplotGlobalUse', False)


df = pd.read_csv('jobs.csv') 
df1 = df.copy()
st.title("Check Out Data Science Jobs (Entry-Level) Trends In Your City: India")
st.markdown("""------------------------------------------------------------------------------------------------""")

st.markdown("""
* For the best user-experience, open this app link on your laptop/ipad/desktop.	
* Select the location & job title from the dropdown menus on top left.
* Total jobs analysed: 2424.
* Data was scraped from web. All the jobs have been posted during the past 30 days. 
* Entry-level jobs (usually 0-3 years experience sought).
* [Github Repo](https://github.com/vijayv500/Data-Science-India-Jobs-Analysis), [Twitter](https://twitter.com/vijayv500), [Medium Blog](https://vijayv500.medium.com), [Instagram](https://www.instagram.com/vijayv500/)
* Please scroll down till the end.
------------------------------------------------------------------------------------------------
""")

loc = dict(df1['location'].value_counts()[0:10])
loc_list = list(loc.keys())
location = st.sidebar.selectbox('Location',loc_list)
df1 = df1.loc[df1['location'] == location]
title_list = ['Data Engineer', 'Data Scientist', 'Data Analyst', 'Big Data Engineer', 'Machine Learning Engineer']
title = st.sidebar.selectbox('Job Title',title_list)
df1 = df1.loc[df1['title'] == title]
st.markdown("""


	""")
st.header('Hiring Trends For ' + title + ' role in ' + location + ':')

# **************************************************************************************************

companies = df1['company'].value_counts()
companies = dict(companies)
list1 = companies.keys()
list2 = companies.values()
companies_df = pd.DataFrame(list(zip(list1,list2)), columns=['company','count'])
fig = px.bar(companies_df[0:10],y='company', x='count', text='count',orientation='h',
            labels={'count':'Count'}, color='count', color_continuous_scale = 'Viridis') 
fig.update_traces(textposition='outside')
fig.update_layout(title_text="<b>Top Companies</b>",
                 title_font_size=25,
                 title_font_color='green',
                 title_font_family='Titillium Web',
                 title_x=0.65,
                 title_y=0.95,
                 title_xanchor='center',
                 title_yanchor='top',
                 yaxis={'categoryorder':'total ascending'}
                 )
fig.update_xaxes(
        color='teal',
        title_text='Jobs',
        title_font_family='Open Sans',
        title_font_size=20,
        title_font_color='maroon',
        title_standoff = 15,
        tickmode='auto',
        showgrid=False,
        linecolor='red',
        linewidth=3,
        mirror=True)
fig.update_yaxes(
        color='Teal',
        title_text='Company',
        title_font_family='Droid Sans',
        title_font_size=20,
        title_font_color='maroon',
        title_standoff = 15,
        showgrid=False,
        tickfont_family='Arial',
        linecolor='red',
        linewidth=3,
        mirror = True)
st.plotly_chart(fig)
# **************************************************************************************************

company_list = df1['company'].values.tolist()
count = Counter(company_list)
wordcloud = WordCloud(width = 1600, height = 800, background_color='lightblue')\
.generate_from_frequencies(count)
plt.figure(figsize=(40,30))
plt.imshow(wordcloud)
plt.axis("off")
plt.show() 
st.subheader('Companies Hiring For ' + title + ' role in ' + location)
st.pyplot()


# **************************************************************************************************
st.markdown("""------------------------------------------------------------------------------------------------""")

st.header('Trends For All India: All Data-Related Roles:')
st.markdown("""


	""")

companies = df['company'].value_counts()
companies = dict(companies)
list1 = companies.keys()
list2 = companies.values()
companies_df = pd.DataFrame(list(zip(list1,list2)), columns=['company','count'])

fig = px.bar(companies_df[0:20],y='company', x='count', text='count',orientation='h',
            labels={'count':'Count'}, color='count', color_continuous_scale = 'Viridis') 

fig.update_traces(textposition='outside')
fig.update_layout(title_text="<b>Top Companies </b>",
                 title_font_size=25,
                 title_font_color='green',
                 title_font_family='Titillium Web',
                 title_x=0.6,
                 title_y=0.95,
                 title_xanchor='center',
                 title_yanchor='top',
                 yaxis={'categoryorder':'total ascending'}
                 )

fig.update_xaxes(
        color='teal',
        title_text='Jobs',
        title_font_family='Open Sans',
        title_font_size=20,
        title_font_color='maroon',
        title_standoff = 15,
        showgrid=False,
        linecolor='red',
        linewidth=3,
        mirror=True)

fig.update_yaxes(
        color='Teal',
        title_text='Company',
        title_font_family='Droid Sans',
        title_font_size=20,
        title_font_color='maroon',
        title_standoff = 15,
        tickfont_family='Arial',
        nticks = 20,
        showgrid=False,
        linecolor='red',
        linewidth=3,
        mirror = True)
st.plotly_chart(fig)

# **************************************************************************************************


titles = df['title'].value_counts()
titles = dict(titles)
list1 = titles.keys()
list2 = titles.values()
titles_df = pd.DataFrame(list(zip(list1,list2)), columns=['title','count'])
fig = px.bar(titles_df[0:20],y='title', x='count', text='count',orientation='h',
            labels={'count':'Count'}, color='count', color_continuous_scale = 'Viridis') 
fig.update_traces(textposition='outside')
fig.update_layout(title_text="<b>Top Job Titles </b>",
                 title_font_size=25,
                 title_font_color='green',
                 title_font_family='Titillium Web',
                 title_x=0.6,
                 title_y=0.95,
                 title_xanchor='center',
                 title_yanchor='top',
                 yaxis={'categoryorder':'total ascending'}
                 )
fig.update_xaxes(
        color='teal',
        title_text='Jobs',
        title_font_family='Open Sans',
        title_font_size=20,
        title_font_color='maroon',
        title_standoff = 15,
        showgrid=False,
        tickmode='auto',
        linecolor='red',
        linewidth=3,
        mirror=True)
fig.update_yaxes(
        color='Teal',
        title_text='Title',
        title_font_family='Droid Sans',
        title_font_size=20,
        title_font_color='maroon',
        title_standoff = 15,
        tickfont_family='Arial',
        nticks = 20,
        showgrid=False,
        linecolor='red',
        linewidth=3,
        mirror = True)
st.plotly_chart(fig)

# **************************************************************************************************


locations = df['location'].value_counts()
locations = dict(locations)
list1 = locations.keys()
list2 = locations.values()
locations_df = pd.DataFrame(list(zip(list1,list2)), columns=['locality','count'])
fig = px.bar(locations_df[0:20],y='locality', x='count', text='count',orientation='h',
            labels={'count':'Count'}, color='count', color_continuous_scale = 'Viridis') 
fig.update_traces(textposition='outside')
fig.update_layout(title_text="<b>Top Locations </b>",
                 title_font_size=25,
                 title_font_color='green',
                 title_font_family='Titillium Web',
                 title_x=0.6,
                 title_y=0.95,
                 title_xanchor='center',
                 title_yanchor='top',
                 yaxis={'categoryorder':'total ascending'}
                 )
fig.update_xaxes(
        color='teal',
        title_text='Jobs',
        title_font_family='Open Sans',
        title_font_size=20,
        title_font_color='maroon',
        title_standoff = 15,
        showgrid=False,
        tickmode='auto',
        linecolor='red',
        linewidth=3,
        mirror=True)
fig.update_yaxes(
        color='Teal',
        title_text='Location',
        title_font_family='Droid Sans',
        title_font_size=20,
        title_font_color='maroon',
        title_standoff = 15,
        tickfont_family='Arial',
        nticks = 20,
        showgrid=False,
        linecolor='red',
        linewidth=3,
        mirror = True)
st.plotly_chart(fig)

# **************************************************************************************************

comploc = df['comp_loc'].value_counts()
comploc = dict(comploc)
list1 = comploc.keys()
list2 = comploc.values()
comploc_df = pd.DataFrame(list(zip(list1,list2)), columns=['comploc','count'])
fig = px.bar(comploc_df[0:20],y='comploc', x='count', text='count',orientation='h',
            labels={'count':'Count'}, color='count', color_continuous_scale = 'Turbo') 
fig.update_traces(textposition='outside')
fig.update_layout(title_text="<b>Top Companies + Locations </b>",
                 title_font_size=25,
                 title_font_color='green',
                 title_font_family='Titillium Web',
                 title_x=0.65,
                 title_y=0.95,
                 title_xanchor='center',
                 title_yanchor='top',
                 yaxis={'categoryorder':'total ascending'}
                 )

fig.update_xaxes(
        color='teal',
        title_text='Jobs',
        title_font_family='Open Sans',
        title_font_size=20,
        title_font_color='maroon',
        title_standoff = 15,
        showgrid=False,
        tickmode='auto',
        linecolor='red',
        linewidth=3,
        mirror=True)

fig.update_yaxes(
        color='Teal',
        title_text='Location',
        title_font_family='Droid Sans',
        title_font_size=20,
        title_font_color='maroon',
        title_standoff = 15,
        tickfont_family='Arial',
        nticks = 20,
        showgrid=False,
        linecolor='red',
        linewidth=3,
        mirror = True)
st.plotly_chart(fig)

# **************************************************************************************************

titlecomploc = df['title_comp_loc'].value_counts()
titlecomploc = dict(titlecomploc)
list1 = titlecomploc.keys()
list2 = titlecomploc.values()
titlecomploc_df = pd.DataFrame(list(zip(list1,list2)), columns=['titlecomploc','count'])
fig = px.bar(titlecomploc_df[0:20],y='titlecomploc', x='count', text='count',orientation='h',
            labels={'count':'Count'}, color='count', color_continuous_scale = 'Turbo') 
fig.update_traces(textposition='outside')
fig.update_layout(title_text="<b>Top Companies + Locations + Titles </b>",
                 title_font_size=25,
                 title_font_color='green',
                 title_font_family='Titillium Web',
                 title_x=0.7,
                 title_y=0.95,
                 title_xanchor='center',
                 title_yanchor='top',
                 yaxis={'categoryorder':'total ascending'}
                 )
fig.update_xaxes(
        color='teal',
        title_text='Jobs',
        title_font_family='Open Sans',
        title_font_size=20,
        title_font_color='maroon',
        title_standoff = 15,
        showgrid=False,
        tickmode='auto',
        linecolor='red',
        linewidth=3,
        mirror=True)
fig.update_yaxes(
        color='Teal',
        title_text='Location',
        title_font_family='Droid Sans',
        title_font_size=20,
        title_font_color='maroon',
        title_standoff = 15,
        tickfont_family='Arial',
        nticks = 20,
        showgrid=False,
        linecolor='red',
        linewidth=3,
        mirror = True)
st.plotly_chart(fig)

# **************************************************************************************************
st.subheader('Job Titles For All Data Science Related Roles')

title_list = df['title'].values.tolist()
count = Counter(title_list)
wordcloud = WordCloud(width = 1600, height = 800, background_color='white')\
.generate_from_frequencies(count)
plt.figure(figsize=(40,30))
plt.imshow(wordcloud)
plt.axis("off")
plt.show() 
st.pyplot()
st.markdown("""------------------------------------------------------------------------------------------------""")

# **************************************************************************************************
st.subheader('Companies Hiring For All Data Science Related Roles')
company_list = df['company'].values.tolist()
count = Counter(company_list)
wordcloud = WordCloud(width = 1600, height = 800, background_color='lightblue')\
.generate_from_frequencies(count)
plt.figure(figsize=(40,30))
plt.imshow(wordcloud)
plt.axis("off")
plt.show() 
st.pyplot()














