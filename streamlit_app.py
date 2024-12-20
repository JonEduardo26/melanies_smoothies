# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

st.title(":cup_with_straw: Custom Smoothie Order Form!! :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom smoothie!!.
    """)
cnx = st.connection ("snowflake")
session = cnx.session()
#session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:'
    , my_dataframe
)

if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)

    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

    #st.write(my_insert_stmt)
    time_to_insert = st.button('Submit Order ')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")
    
    
#import streamlit as st

#option = st.selectbox(
 #   "What is your favorite fruit?",
  #  ("Banana", "Strawberries", "Peaches"),
#)

#st.write("Your favorite fruit is:", option)
