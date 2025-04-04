import numpy as np
import pandas as pd

df = pd.read_csv("environment-raw.csv", delimiter=";")

indicator_namey = "Mortality rate attributed to unsafe water, " \
                 "unsafe sanitation and lack of hygiene (per 100,000 population)" #mortality rate will be the y axis
indicator_namex = "People with basic handwashing facilities including soap and water (% of population)" #sanitation rate will be the x axis

df_filtered = df[df["Indicator Name"] == indicator_namey]
df_filtered2 = df[df["Indicator Name"] == indicator_namex]

df_filtered = df_filtered.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
df_filtered2 = df_filtered2.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])



countries_with_data = df_filtered["Country Name"].unique()
# print(countries_with_data)
# print(len(countries_with_data))
# print("\n")

# for country in countries_with_data:
#     row = df.loc[df["Country Name"] == country].values[0]
#     print(row)

def safe_parse(value):
    if isinstance(value, str):
        if value.replace(',', '').replace('.', '').isdigit():
            return float(value.replace(',', '.'))
    return value


# for country in countries_with_data:
#     row = df.loc[df["Country Name"] == country].values[0]
#     clean_row = row[~pd.isna(row)]
#     converted = [safe_parse(x) for x in clean_row]
#
#     print(converted)

def total(row):
    data_only = row[4:]
    sum = 0
    for i in data_only:
        sum += i
    return sum

for country in countries_with_data:
    row = df.loc[df["Country Name"] == country].values[10]
    clean_row = row[~pd.isna(row)]
    converted = [safe_parse(x) for x in clean_row]
    value = total(converted)

    print(round(value,2))


