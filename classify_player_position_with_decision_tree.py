#!/usr/bin/env python
# coding: utf-8

# In[530]:


# pip install -U scikit-learn scipy matplotlib


# In[531]:


import pandas as pd
import numpy as np
import math


# In[532]:


players_data = pd.read_csv("C:/Users/x_fernare1/Downloads/players_data.csv")


# In[533]:


attacking_columns = ['CROSSING', 'FINISHING', 'HEADING_ACCURACY', 'SHORT_PASSING', 'VOLLEYS']
players_data['ATTACKING'] = players_data[attacking_columns].mean(axis=1)


# In[534]:


skill_columns = ['DRIBBLING', 'CURVE', 'FK_ACCURACY', 'LONG_PASSING', 'BALL_CONTROL']
players_data['SKILL'] = players_data[skill_columns].mean(axis=1)

movement_columns = ['ACCELERATION', 'SPRINT_SPEED', 'AGILITY', 'REACTIONS', 'BALANCE']
players_data['MOVEMENT'] = players_data[movement_columns].mean(axis=1)

power_columns = ['SHOT_POWER', 'JUMPING', 'STAMINA', 'STRENGTH', 'LONG_SHOTS']
players_data['POWER'] = players_data[power_columns].mean(axis=1)

mentality_columns = ['AGGRESSION', 'INTERCEPTIONS', 'POSITIONING', 'VISION', 'PENALTIES', 'COMPOSURE']
players_data['MENTALITY'] = players_data[mentality_columns].mean(axis=1)

defending_columns = ['DEFENSIVE_AWARENESS', 'STANDING_TACKLE', 'SLIDING_TACKLE']
players_data['DEFENDING'] = players_data[defending_columns].mean(axis=1)

goalkeeping_columns = ['GK_DIVING', 'GK_HANDLING', 'GK_KICKING', 'GK_POSITIONING', 'GK_REFLEXES']
players_data['GOALKEEPING'] = players_data[goalkeeping_columns].mean(axis=1)


# In[535]:


attacking_ratings_to_drop = ['CROSSING', 'FINISHING', 'HEADING_ACCURACY', 'SHORT_PASSING', 'VOLLEYS']
players_data.drop(columns=attacking_ratings_to_drop, inplace=True)

movement_ratings_to_drop = ['ACCELERATION', 'SPRINT_SPEED', 'AGILITY', 'REACTIONS', 'BALANCE']
players_data.drop(columns=movement_ratings_to_drop, inplace=True)

skill_ratings_to_drop = ['DRIBBLING', 'CURVE', 'FK_ACCURACY', 'LONG_PASSING', 'BALL_CONTROL']
players_data.drop(columns=skill_ratings_to_drop, inplace=True)

power_ratings_to_drop = ['SHOT_POWER', 'JUMPING', 'STAMINA', 'STRENGTH', 'LONG_SHOTS']
players_data.drop(columns=power_ratings_to_drop, inplace=True)

mentality_ratings_to_drop = ['AGGRESSION', 'INTERCEPTIONS', 'POSITIONING', 'VISION', 'PENALTIES', 'COMPOSURE']
players_data.drop(columns=mentality_ratings_to_drop, inplace=True)

defending_ratings_to_drop = ['DEFENSIVE_AWARENESS', 'STANDING_TACKLE', 'SLIDING_TACKLE']
players_data.drop(columns=defending_ratings_to_drop, inplace=True)

goalkeeping_ratings_to_drop = ['GK_DIVING', 'GK_HANDLING', 'GK_KICKING', 'GK_POSITIONING', 'GK_REFLEXES']
players_data.drop(columns=goalkeeping_ratings_to_drop, inplace=True)


# In[536]:


players_data.drop(columns=['REAL_FACE', 'ID', 'INTERNATIONAL_REPUTATION', 'TEAM', 'COUNTRY', 'NAME'], inplace=True)


# In[537]:


from datetime import datetime

players_data['BIRTH_DATE'] = pd.to_datetime(players_data['BIRTH_DATE'], format='%d/%m/%Y')

current_year = datetime.now().year

players_data['AGE'] = current_year - players_data['BIRTH_DATE'].dt.year

players_data.drop(columns=['BIRTH_DATE'], inplace=True)


# In[538]:


def clean_and_convert(column):
    return pd.to_numeric(column.str.replace(r'[^0-9.]', '', regex=True).replace('', pd.NA), errors='coerce').astype('float64')

players_data['VALUE'] = clean_and_convert(players_data['VALUE'])
players_data['WAGE'] = clean_and_convert(players_data['WAGE'])
players_data['RELEASE_CLAUSE'] = clean_and_convert(players_data['RELEASE_CLAUSE'])

players_data['KIT_NUMBER'] = pd.to_numeric(players_data['KIT_NUMBER'].replace(r'[^0-9]', '', regex=True), errors='coerce')
players_data['KIT_NUMBER'] = players_data['KIT_NUMBER'].astype('Int64')


# In[539]:


players_data = pd.get_dummies(players_data, columns=['PREFERRED_FOOT'], prefix='PREFERRED_FOOT')


# In[540]:


def rounded_mean(row):
    return math.ceil(np.nanmean(row))

for column in ['ATTACKING', 'SKILL', 'MOVEMENT', 'POWER', 'MENTALITY', 'DEFENDING', 'GOALKEEPING']:
    players_data[column] = players_data[column].apply(rounded_mean)

players_data.to_csv('C:/Users/x_fernare1/git/Python-ML-Snippets/preprocessed_players_data.csv', index=False)

players_data.head()


# In[541]:


features = players_data.drop(columns='POSITION')
labels = players_data['POSITION']


# In[542]:


from sklearn.model_selection import train_test_split

features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2, random_state=0)


# In[543]:


from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(random_state=0)
tree.fit(features_train,labels_train)


# In[544]:


labels_pred_test = tree.predict(features_test)


# In[545]:


from sklearn.metrics import accuracy_score,f1_score

accuracy_score(labels_test,labels_pred_test)


# In[546]:


f1_score(labels_test,labels_pred_test, average='weighted')


# In[547]:


labels_pred_train = tree.predict(features_train)
f1_score(labels_train,labels_pred_train, average='weighted')

