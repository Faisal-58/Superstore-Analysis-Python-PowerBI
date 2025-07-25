#!/usr/bin/env python
# coding: utf-8

# ## Superstore Sale Analysis

# In[6]:


# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# ### Loading Data

# In[7]:


df = pd.read_csv('superstore.csv')
df.head()


# In[8]:


print(df['Order Date'].head(10).tolist())


# ### Necessary EDA and Preprocessing

# In[9]:


df.info()


# In[10]:


df = df.dropna()


# In[11]:


df.shape


# In[12]:


df.duplicated().sum()


# In[13]:


df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')

# Check results
print("Order Date NaT count:", df['Order Date'].isna().sum())
print("Ship Date NaT count:", df['Ship Date'].isna().sum())

print(df[['Order Date', 'Ship Date']].head())


# In[14]:


df.info()


# In[15]:


df['State'].unique()


# In[16]:


df['City'].unique()


# In[17]:


df['City'] = df['City'].str.strip().str.title()
df['State'] = df['State'].str.strip().str.title()


# In[18]:


from fuzzywuzzy import fuzz
from fuzzywuzzy import process

cities = df['City'].unique()
for city in cities[:100]:  # limit to avoid long output
    matches = process.extract(city, cities, limit=3)
    for match in matches:
        if match[0] != city and match[1] > 90:
            print(f"{city} ↔ {match[0]} (score: {match[1]})")


# In[19]:


df['Country'].unique()


# In[20]:


df['Postal Code'] = df['Postal Code'].astype('Int64').astype(str)


# In[21]:


df['Segment'].unique()


# In[22]:


df['Category'].unique()


# In[23]:


df['Ship Mode'].unique()


# In[24]:


# Extract Year, Month, Day from Order Date
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Order Day'] = df['Order Date'].dt.day
df['Order Weekday'] = df['Order Date'].dt.day_name()

# Extract the same from Ship Date
df['Ship Year'] = df['Ship Date'].dt.year
df['Ship Month'] = df['Ship Date'].dt.month
df['Ship Day'] = df['Ship Date'].dt.day
df['Ship Weekday'] = df['Ship Date'].dt.day_name()


# In[25]:


df.head()


# In[26]:


df['Shipping Delay (Days)'] = (df['Ship Date'] - df['Order Date']).dt.days


# In[27]:


df.head()


# ### Analyzing Visualizations using Matplotlib, Seaborn and Plotly

# In[28]:


# Group sales by year and month
monthly_sales = df.groupby(['Order Year', 'Order Month'])['Sales'].sum().reset_index()

# Create a proper date column for plotting
monthly_sales['Year-Month'] = pd.to_datetime(monthly_sales['Order Year'].astype(str) + '-' + monthly_sales['Order Month'].astype(str))

# Sort by date
monthly_sales = monthly_sales.sort_values('Year-Month')

# Plot
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales['Year-Month'], monthly_sales['Sales'], marker='o')
plt.title('Monthly Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.show()


# ### Sales by Category

# In[29]:


plt.figure(figsize=(8,5))
sns.barplot(data=df, x='Category', y='Sales', estimator='sum')
plt.title('Sales by Category')
plt.ylabel('Total Sales')
plt.xlabel('Category')
plt.show()


# ### Sales by Region

# In[30]:


plt.figure(figsize=(8,5))
sns.barplot(data=df, x='Region', y='Sales', estimator='sum')
plt.title('Sales by Region')
plt.ylabel('Total Sales')
plt.xlabel('Region')
plt.show()



# ### Top 10 Cities by Sales

# In[31]:


top_cities = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()

plt.figure(figsize=(10,6))
sns.barplot(data=top_cities, x='Sales', y='City')
plt.title('Top 10 Cities by Sales')
plt.xlabel('Sales')
plt.ylabel('City')
plt.show()


# ### Distribution of Shipping Delay

# In[32]:


plt.figure(figsize=(8,5))
sns.histplot(df['Shipping Delay (Days)'], bins=30, kde=True)
plt.title('Distribution of Shipping Delay (Days)')
plt.xlabel('Shipping Delay')
plt.ylabel('Frequency')
plt.show()


# ### Sales Distribution by Ship Mode

# In[33]:


plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='Ship Mode', y='Sales')
plt.title('Sales Distribution by Ship Mode')
plt.ylabel('Sales')
plt.xlabel('Ship Mode')
plt.show()


# ### Order Count by Weekday

# In[34]:


plt.figure(figsize=(10,5))
sns.countplot(data=df, x='Order Weekday', order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
plt.title('Order Count by Weekday')
plt.show()


# ### Sales by Sub-Category

# In[35]:


fig = px.bar(df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).reset_index(),
             x='Sub-Category', y='Sales', color='Sales',
             title="Sales by Sub-Category")
fig.show()


# ### Sales Distribution By Region

# In[36]:


fig = px.pie(df.groupby("Region")["Sales"].sum().reset_index(),
             names='Region', values='Sales',
             title="Sales Distribution by Region")
fig.show()


# ### Saving cleaned dataset (Used in PowerBI Dashboard)

# In[37]:


df.to_csv("cleaned_superstore.csv", index=False)



# In[ ]:




