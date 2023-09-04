import streamlit as s
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


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

s.header('Fruityvice advice')
def get_fruit_from_frutyvice(fruit_choice):
    fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice}")
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
    

try:
    fruit_choice = s.text_input('What fruit would you like information about?')
    if not fruit_choice:
        s.error("Choose a fruit")
    else:        
        fruityvice_normalized = get_fruit_from_frutyvice(fruit_choice)
        s.dataframe(fruityvice_normalized)
except URLError as e:
    s.error()
    
s.text("The fruit load list:")
def get_fruit_list(cnx):
    with cnx.cursor() as my_cur:
        my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
        my_data_rows = my_cur.fetchall()
    return my_data_rows

if s.button("Get fruit list"):
    my_cnx = snowflake.connector.connect(**s.secrets["snowflake"])
    my_data_rows = get_fruit_list(my_cnx)
    s.dataframe(my_data_rows)

def insert_fruit_snowflake(fruit, cnx):
    with cnx.cursor() as my_cur:
        my_cur.execute(f"insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('{fruit}')")
    return f"Thanks for adding {fruit}"

fruit_add = s.text_input('What fruit would you like to add?','Jackfruit')
if s.button("Add fruit"):
    my_cnx = snowflake.connector.connect(**s.secrets["snowflake"])
    result = insert_fruit_snowflake(fruit_add, my_cnx)
    s.text(result)