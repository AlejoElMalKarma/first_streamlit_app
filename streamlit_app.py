import streamlit
import pandas
import requests
from urllib.error import URLError


streamlit.title('My parents new healthy menu')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#Nw section to display fruityvice api response version anterior

#streamlit.header("Fruityvice Fruit Advice!")
#fruit_choice = streamlit.text_input('What fruit would you like information about?')
#streamlit.write('The user entered ', fruit_choice)
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)

#Nueva version

#Crea una funcion

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized


streamlit.header("Fruityvice Fruit Advice!")
try: 
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

# Allow the end user to add a fruit to the list

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values ('from streamlit')")
         return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit. button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)


streamlit.stop()

#import snowflake.connector

#streamlit.text(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains")
streamlit.dataframe(my_data_rows)
#my_fruit_list_2 = my_data_rows


# Let's put a pick list here so they can pick the fruit they want to include 
add_my_fruit = streamlit.text_input('What fruit would yo like to add?', 'jackfruit')
streamlit.write('Thanks for adding ',add_my_fruit)

#Que no va a funcionar dice... pos ok
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
