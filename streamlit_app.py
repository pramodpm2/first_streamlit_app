import streamlit 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError



streamlit.title("hello world")




streamlit.header(' Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔  Hard-Boiled Free-Range Egg')
streamlit.text("🥑 🍞 Avacodo toast")

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)







fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)


try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  
  if not fruit_choice:
    streamlit.error("Please select the fruit.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlet.error()
    


streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values ('from streamlit');")
my_data_row = my_cur.fetchall()
streamlit.header("Fruit load list contains")
streamlit.dataframe(my_data_row)

add_my_fruit= streamlit.text_input('Whar fruit would you like to add?','jackfruit')
