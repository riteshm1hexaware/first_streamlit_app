import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omeage 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Step 1 - list the fruits
#streamlit.dataframe(my_fruit_list)

#Step 3 - Allow fruit selection on the basis of name
my_fruit_list=my_fruit_list.set_index('Fruit')

#Step 2 - allow fruit selection
#streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))

#Step 4 - Allow pre-populated items
#streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index), ['Avocado', 'Strawberries'])
#streamlit.dataframe(my_fruit_list)

#Step 5 - Use variable names
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.dataframe(my_fruit_list)
