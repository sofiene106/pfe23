#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv

df = pd.read_csv(r'C:\Users\sofi\Downloads\wetransfer-3ab4ca\2018.csv',sep=';', encoding = 'ISO-8859-1',
                     names=['ID_ORDER', 'DATE-ADD','TIME-ADD','LOCATION','ID_CUSTOMER','LAST_NAME','FIRST_NAME','YX_LIBELLE','BIRTH_YEAR','TELEX','EMAIL','ADRESS','POSTAL_CODE','CITY','ITEM_CODE','CC_LIBELLE','CC_LIBELLE_1','DESIGNATION','PVTTC','QTEFACT','PUTTCNET','MLR_REMISE','GTR_LIBELLE'],
                     dtype={'ID_ORDER':int,'DATE-ADD':object,'TIME-ADD':object,'LOCATION':int,'ID_CUSTOMER':object,'LAST_NAME':object,'FIRST_NAME':object,'YX_LIBELLE':object,'BIRTH_YEAR':object,'TELEX':object,'EMAIL':object,'ADRESS':object,'POSTAL_CODE':object,'CITY':object,'ITEM_CODE':object,'CC_LIBELLE':object,'CC_LIBELLE_1':object})

df
 


# In[2]:


df.info()


# In[3]:


#convert DataFrame column to date-time:'GP_DATEPIECE'
df['DATE-ADD'] = pd.to_datetime(df['DATE-ADD'], format = '%Y-%m-%d')
df['DATE-ADD']= pd.to_datetime(df['DATE-ADD'], errors='ignore')
df.head()


# In[4]:



df['TIME-ADD'] = pd.to_datetime(df['TIME-ADD'])

df


# In[ ]:





# In[5]:


df.info()


# In[6]:


# Create the dictionary for  ETABLISSEMENT
etab = {28:'Sasio Geant',31:'Blue Island Carrefour',62:'Central Park',16:'Sousse',8:'Lafayette',130:'Blue Island Palmarium',50:'Sasio Carrefour',24:'Bizerte',40:'Ennasr',56:'Sasio Manzah VI',14:'Blue Island Zephyr',61:'La Soukra',63:'Sasio Menzah V',54:'Nabeul',37:'Sasio Zephyr',134:'Sasio Palmarium',64:'Nabeul',65:'Blue Island Manar',36:'Sasio Manar',25:'Blue Island Djerba',52:'Blue Island Menzah VI',66:'Mehdia',42:'Lac 2',67:'Sfax',68:'Monastir',51:'Blue Island Menzah V',69:'El Kef',35:'Kairouan',15:'Sasio Mseken',27:'Sasio Mseken',60:'Sasio Djerba',18:'Kelibia',41:'Ksar Hellal',74:'Hammamet'}
df['LOCATION'] = df['LOCATION'].map(etab)
#display the first 5 lines
df


# In[7]:


df['LOCATION'].value_counts()


# In[8]:


df['DATE-ADD'] = pd.to_datetime(df['DATE-ADD'])

df['SEASON'] = (df['DATE-ADD'].dt.month - 1) // 3
df['SEASON'] += (df['DATE-ADD'].dt.month == 3)&(df['DATE-ADD'].dt.day>=20)
df['SEASON'] += (df['DATE-ADD'].dt.month == 6)&(df['DATE-ADD'].dt.day>=21)
df['SEASON'] += (df['DATE-ADD'].dt.month == 9)&(df['DATE-ADD'].dt.day>=23)
df['SEASON'] -= 3*((df['DATE-ADD'].dt.month == 12)&(df['DATE-ADD'].dt.day>=21)).astype(int)


# In[9]:


df.iloc[130766,:]


# In[ ]:





# In[10]:


season={0:'Winter',1:'Spring',2:'Summer',3:'Autumn'}

df['SEASON'] = df['SEASON'].map(season)
df


# In[11]:


df = df[['ID_ORDER', 'DATE-ADD','TIME-ADD','SEASON','LOCATION','ID_CUSTOMER','LAST_NAME','FIRST_NAME','YX_LIBELLE','BIRTH_YEAR','TELEX','EMAIL','ADRESS','POSTAL_CODE','CITY','ITEM_CODE','CC_LIBELLE','CC_LIBELLE_1','DESIGNATION','PVTTC','QTEFACT','PUTTCNET','MLR_REMISE','GTR_LIBELLE']]
df


# In[12]:


df.iloc[130850,:]


# In[13]:


df['COVID']='Pre-Covid'
df = df[['ID_ORDER', 'DATE-ADD','TIME-ADD','SEASON','COVID','LOCATION','ID_CUSTOMER','LAST_NAME','FIRST_NAME','YX_LIBELLE','BIRTH_YEAR','TELEX','EMAIL','ADRESS','POSTAL_CODE','CITY','ITEM_CODE','CC_LIBELLE','CC_LIBELLE_1','DESIGNATION','PVTTC','QTEFACT','PUTTCNET','MLR_REMISE','GTR_LIBELLE']]
df


# In[14]:


import numpy as np 


# In[15]:


df['AGE'] = df['DATE-ADD'].dt.year- df['BIRTH_YEAR'].astype(np.float).astype("Int32")
df


# In[16]:


df = df[['ID_ORDER', 'DATE-ADD','TIME-ADD','SEASON','COVID','LOCATION','ID_CUSTOMER','LAST_NAME','FIRST_NAME','YX_LIBELLE','BIRTH_YEAR','AGE','TELEX','EMAIL','ADRESS','POSTAL_CODE','CITY','ITEM_CODE','CC_LIBELLE','CC_LIBELLE_1','DESIGNATION','PVTTC','QTEFACT','PUTTCNET','MLR_REMISE','GTR_LIBELLE']]
df['AGE'] = df['AGE'].apply(lambda x: 0 if x == 2018 else x)


# In[17]:


df['AGE']=df['AGE'].astype("Int32")
df['AGE']


# In[18]:


df['AGE'].value_counts()


# In[19]:


df['CONFINEMENT']='NO'
df['CURFEW']='NO'
df = df[['ID_ORDER', 'DATE-ADD','TIME-ADD','SEASON','COVID','CONFINEMENT','CURFEW','LOCATION','ID_CUSTOMER','LAST_NAME','FIRST_NAME','YX_LIBELLE','BIRTH_YEAR','AGE','TELEX','EMAIL','ADRESS','POSTAL_CODE','CITY','ITEM_CODE','CC_LIBELLE','CC_LIBELLE_1','DESIGNATION','PVTTC','QTEFACT','PUTTCNET','MLR_REMISE','GTR_LIBELLE']]
df


# In[20]:


df['P_MONTH']=0
df['P_MONTH']+=(df['DATE-ADD'].dt.day>10)
df['P_MONTH']+=(df['DATE-ADD'].dt.day>20)
df['P_MONTH']=df['P_MONTH'].astype(int)


# In[21]:


month={0:'Start_of_Month',1:'Middle_of_Month',2:'End_of_Month'}
df['P_MONTH'] = df['P_MONTH'].map(month)



# In[22]:


df = df[['ID_ORDER', 'DATE-ADD','TIME-ADD','SEASON','P_MONTH','COVID','CONFINEMENT','CURFEW','LOCATION','ID_CUSTOMER','LAST_NAME','FIRST_NAME','YX_LIBELLE','BIRTH_YEAR','AGE','TELEX','EMAIL','ADRESS','POSTAL_CODE','CITY','ITEM_CODE','CC_LIBELLE','CC_LIBELLE_1','DESIGNATION','PVTTC','QTEFACT','PUTTCNET','MLR_REMISE','GTR_LIBELLE']]
df


# In[23]:


from datetime import date
import calendar


df['P_WEEK']=df['DATE-ADD'].dt.strftime('%A')
week={'Monday':'Start_of_Week','Tuesday':'Start_of_Week','Wednesday':'Mid_Week','Thursday':'Mid_Week','Friday':'Mid_Week','Saturday':'Week_End','Sunday':'Week_end'}
df['P_WEEK'] = df['P_WEEK'].map(week)



# In[24]:


df = df[['ID_ORDER', 'DATE-ADD','TIME-ADD','SEASON','P_MONTH','P_WEEK','COVID','CONFINEMENT','CURFEW','LOCATION','ID_CUSTOMER','LAST_NAME','FIRST_NAME','YX_LIBELLE','BIRTH_YEAR','AGE','TELEX','EMAIL','ADRESS','POSTAL_CODE','CITY','ITEM_CODE','CC_LIBELLE','CC_LIBELLE_1','DESIGNATION','PVTTC','QTEFACT','PUTTCNET','MLR_REMISE','GTR_LIBELLE']]
df.iloc[130850,:]


# In[25]:



df['TOTAL_QUANTITY'] = df.groupby(['ID_ORDER'])['DATE-ADD'].transform('count')
df


# In[26]:


df[df['ID_ORDER'] ==66032518]


# In[27]:


df2= pd.read_csv(r'C:\Users\sofi\Downloads\train_code_postal.csv')
df2 = df2.rename(columns={'code postal': 'POSTAL_CODE'})
df2.info()


# In[28]:


df['QTEFACT'].value_counts()


# In[29]:


df[df['QTEFACT'] ==89.9]

 



# In[40]:


hour=df['TIME-ADD'].dt.hour
hour


# In[44]:


# Create the dictionary for Hour 

H = {0:'Early_morning', 1:'Early_morning', 2:'Early_morning', 3:'Early_morning',4:'Early_morning',5:'Early_morning',6:'Early_morning',7:'Early_morning',8:'Early_morning',9:'Late_morning',10:'Late_morning',11:'Late_morning',12:'Early_afternoon',13:'Early_afternoon',14:'Early_afternoon',15:'Late_afternoon',16:'Late_afternoon',17:'Late_afternoon',18:'Evening',19:'Evening',20:'Evening',21:'Night',22:'Night',23:'Night'}
# Use the dictionary to map the 'Hour'
df['HOUR'] = hour.map(H)
#display the first 5 lines
df


# In[45]:


df = df[['ID_ORDER', 'DATE-ADD','TIME-ADD','HOUR','SEASON','P_MONTH','P_WEEK','COVID','CONFINEMENT','CURFEW','LOCATION','ID_CUSTOMER','LAST_NAME','FIRST_NAME','YX_LIBELLE','BIRTH_YEAR','AGE','TELEX','EMAIL','ADRESS','POSTAL_CODE','CITY','ITEM_CODE','CC_LIBELLE','CC_LIBELLE_1','DESIGNATION','PVTTC','QTEFACT','PUTTCNET','MLR_REMISE','GTR_LIBELLE','TOTAL_QUANTITY']]
df


# In[46]:


df['TIME-ADD'] = pd.Series([val.time() for val in df['TIME-ADD']])
df

