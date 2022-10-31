import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

st.code(
'''
x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0, x_limit, 1)

# Create a random array of data that we will use for our y values
y_data = [random.random() for value in x_axis]

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})

st.write(df)''',language='python')

x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0, x_limit, 1)

# Create a random array of data that we will use for our y values
y_data = [random.random() for value in x_axis]

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})

st.write(df)


st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

st.code(
''' 
scatter = alt.Chart(df).mark_point().encode(
    x = 'x',
    y = 'y'
)

st.altair_chart(scatter, use_container_width=True)''',language='python')

scatter = alt.Chart(df).mark_point().encode(
    x = 'x',
    y = 'y'
)

st.altair_chart(scatter, use_container_width=True)


st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- Added title to the chart
- Added hover tooltip
- Added colored icons
- Added color legend
- Changed point icons
""")

df['color'] = np.where(df['y']> 0.5, 'blue', 'red')

def get_chart(data):
    hover = alt.selection_single(
        fields=["x"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    points = (
        alt.Chart(df, title="Random Data Scatterplot").mark_circle().encode(
            x = 'x',
            y = 'y',
            color=alt.Color('color', legend=alt.Legend(title="Point Color")))
       )

    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x="x",
            y="y",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("x", title="x"),
                alt.Tooltip("y", title="y"),
            ],
        )
        .add_selection(hover)
    )
    return (points + tooltips).interactive()

chart = get_chart(df)

st.altair_chart(chart, use_container_width=True)

st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

st.markdown("""
Simple Histogram (https://altair-viz.github.io/gallery/simple_histogram.html)
 
The 2 changes I made were:
- Added title
- Chagned color to gray
"""
)

from vega_datasets import data

source = pd.read_json('movies.json')
st.write(source)

histogram = alt.Chart(source, title='IMDB Rating Frequency').mark_bar().encode(
    alt.X("IMDB_Rating:Q", bin=True),
    y='count()',
    color=alt.value('gray')
)

st.altair_chart(histogram, use_container_width=True)
