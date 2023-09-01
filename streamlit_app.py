import streamlit as s
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


s.title("Snowflake App")

s.header('Breakfast Menu')
s.text('🥣 Omega 3 & Blueberry Oatmeal')
s.text('🥗 Kale, Spinach & Rocket Smoothie')
s.text('🐔 Hard-Boiled Free-Range Egg')
s.text('🥑🍞 Avocado toast')

s.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
s.dataframe(my_fruit_list)
