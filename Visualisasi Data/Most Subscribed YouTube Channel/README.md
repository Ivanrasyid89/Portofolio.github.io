Data yang digunakan adalah data Most Subscribed YouTube Channel yang dapat diakses pada alamat laman: 
https://www.kaggle.com/datasets/sukhmandeepsinghbrar/most-subscribed-youtube-channel

Data terdiri dari 6 fitur, dengan rincian sebagai berikut:
1. Name
2. Brand Channel
3. Subscribers (millions)
4. Primary language
5. Category
6. Country

# Langkah-langkah #
## Exploratory Data Analysis ##
### Data Information
```
data.info()
```
### Identify Missing Value ###
```
print(data.isnull().sum())
```

## Data Preprocessing ##
### Cleaning Data ###
```
# Cleaning data on "Primary language" and "Country" column
# Removing numbers in square brackets and extra spaces
data['Primary language'] = data['Primary language'].apply(lambda x: re.sub(r'\[\d+\]', '', x).strip())
def clean_country(country):
    country = re.sub(r'\s*\(.*\)', '', country)  
    country = re.sub(r'[^\w\s-]', '', country)  
    country = country.strip()  
    country = country.replace('\xa0', ' ')
    country = country.split('-')[0].strip()  
    return country

data['Country'] = data['Country'].apply(clean_country)

print(data['Primary language'].unique())
print(data['Country'].unique())
```

## Save Data ##
```
# Save data format Excel
data.to_excel('Most Subscribed YouTube Channel.xlsx', index=False)

# Save data format CSV
data.to_csv('Most Subscribed YouTube Channel.csv', index=False)
```

# Dashboard with Power BI #
![Most Subscribed YouTube Channel_page-0001 (3)](https://github.com/Ivanrasyid89/Portofolio.github.io/assets/98071016/efbd1dc0-81dd-4760-8f29-ca1a8019c36d)


