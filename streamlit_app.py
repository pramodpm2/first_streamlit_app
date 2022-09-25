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





def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  



try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  
  if fruit_choice:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
  else:
    streamlit.error("Please select the fruit.")
    
except URLError as e:
  streamlet.error()
    
streamlit.header("Fruit load list contains")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
    

if streamlit.button("Get fruit load list"):
                    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
                    my_data_row = get_fruit_load_list()
                    streamlit.dataframe(my_data_row)






