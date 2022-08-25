import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff



st.write("Hello world!")

st.markdown("This is **bold** and this is _italics_")
st.title('My first title')
st.header("This is a header")


df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

st.dataframe(df)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)


df2 = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df2)

if st.button("This is a button"):
    st.write("You cliked on the button")

#st.download_button()

number = st.slider("my slider", 0, 100)
st.write(f"You selected {number}")

filter = st.selectbox("Please choose an option", [1, 2, 3])
my_text_input = st.text_input("Please inputttt")

st.checkbox("asas", "1")

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
st.write(uploaded_files)
#st.dataframe(uploaded_files.name)