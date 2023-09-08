#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install pandas')


# In[ ]:


import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


pd.options.mode.chained_assignment = None


# In[ ]:


players_raw = pd.read_csv('C:/Users/x_fernare1/Downloads/players_data.csv', usecols=["NAME", "BIRTH_DATE", "COUNTRY", "OVERALL_RATING", "POTENTIAL", "VALUE", "WAGE", "HEIGHT", "RELEASE_CLAUSE", "POSITION"], delimiter=',', header=0)


# In[ ]:


print(players_raw.columns)


# In[ ]:


current_year = datetime.now().year


# In[ ]:


players_raw['VALUE'] = pd.to_numeric(players_raw['VALUE'].str.replace('€', '').str.replace('M', ''), errors='coerce')
players_raw['BIRTH_DATE'] = pd.to_datetime(players_raw['BIRTH_DATE'], format='%d/%m/%Y')
players_raw['AGE'] = current_year - players_raw['BIRTH_DATE'].dt.year


# In[ ]:


players_raw.head()


# In[ ]:


age_value = players_raw[['AGE', 'VALUE']]


# In[ ]:


age_value.head()

sorted_players = players_raw.sort_values(by='VALUE', ascending=False)
columns_to_display = ["NAME", "AGE", "VALUE"]

print("Top players by market value:")
sorted_players[columns_to_display].head(10)
# In[ ]:


plt.figure(figsize=(8, 6))
sns.scatterplot(data=age_value, x='AGE', y='VALUE')
plt.title('Scatter Plot between Age and Value')
plt.xlabel('Age')
plt.ylabel('Value')
plt.show()

