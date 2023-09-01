import streamlit as s
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


s.title("Snowflake App")

s.header('Breakfast Menu')
s.text('🥣 Omega 3 & Blueberry Oatmeal')
s.text('🥗 Kale, Spinach & Rocket Smoothie')
s.text('🐔 Hard-Boiled Free-Range Egg')
s.text('🥑🍞 Avocado toast')

s.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_selected = s.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


s.dataframe(fruits_to_show)
