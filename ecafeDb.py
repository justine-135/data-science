import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine

# Access database
engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:@localhost:3306/tupc_ecafe')

# Get table
data = pd.read_sql_table("ordered_items", engine)

# Get specific columns from table
item = pd.read_sql_table("ordered_items", engine, columns=[
                         'item', 'quantity_sold'])
date = pd.read_sql_table("ordered_items", engine, columns=['date_current',
                         'hourly_sales', 'quantity_sold'])

print(data)
# Group data under 'item' column
# Sum data in 'quantity_sold' column
mergedItem = item.groupby('item')['quantity_sold'].sum()
# Group again
dateGroup = date.groupby(['date_current', 'hourly_sales'])[
    'quantity_sold'].sum()
# Sort values highest to lowest
ascending = mergedItem.sort_values(ascending=False)
# Sort values lowest to highest
descending = mergedItem.sort_values(ascending=True)


def topSelling():
    # display
    print('\n' 'Top selling items: ' '\n', ascending)


def leastSelling():
    print('\n' 'Low selling items: ' '\n', descending)


def dateAndTime():
    print('\n' 'Active selling time: ' '\n', dateGroup)
