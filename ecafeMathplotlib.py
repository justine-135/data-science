import matplotlib.pyplot as plt
from numpy.lib.arraypad import pad
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
itemName = pd.read_sql_table("ordered_items", engine, columns=[
                         'item'])
date = pd.read_sql_table("ordered_items", engine, columns=['date_current',
                         'hourly_sales', 'quantity_sold'])

# Group data under 'item' column
# Sum data in 'quantity_sold' column
mergedItem = data.groupby('item')['quantity_sold'].sum()

arrItemName = np.array(itemName)

itemLabel = np.concatenate(arrItemName)
# print(mergedItem)
# print(np.unique(itemLabel))
# print(mergedItem.to_numpy())

newData = {
        'itemName': np.unique(itemLabel),
        'q_value' : mergedItem.to_numpy()
}

df = pd.DataFrame.from_dict(newData)
ascending = df.sort_values(by=['q_value'],ascending=False)

print(df)

#BAR GRAPH
fig1, ax = plt.subplots(figsize =(16, 9))

ax.set_title('Ordered items', fontsize='28', fontweight='bold', color ='grey', pad=20)
ax.set_ylabel('Items', fontsize='14', fontweight='bold', color ='grey', labelpad=10)
ax.set_xlabel('Quantity sold', fontsize='14', fontweight='bold', color ='grey', labelpad=10)

ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)

ax.invert_yaxis()

ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)

ax.set_xlim(0, df.q_value.max() * 1.25)

rects = ax.barh(ascending.itemName, ascending.q_value, color="coral")

for Y,X in enumerate(ascending.q_value):
        ax.annotate("{:.1f}%".format(X * 100/np.sum(ascending.q_value)), xy=(X,Y), color='grey', fontsize='10', va='center')

plt.show()

#PIE CHART
# labels = np.unique(itemLabel)
# sizes = mergedItem.to_numpy()

# ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
#         startangle=90)
# ax1.axis('equal')
# ax1.legend()

# plt.show()