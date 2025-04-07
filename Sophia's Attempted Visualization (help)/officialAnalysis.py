import pandas as pd

df = pd.read_csv("environment-raw.csv", delimiter=";")

indicator_namey = "Mortality rate attributed to unsafe water, " \
                 "unsafe sanitation and lack of hygiene (per 100,000 population)" #mortality rate will be the y axis
indicator_namex = "People with basic handwashing facilities including soap and water (% of population)" #sanitation rate will be the x axis

df_filtered = df[df["Indicator Name"] == indicator_namey]
df_filtered2 = df[df["Indicator Name"] == indicator_namex]

df_filtered = df_filtered.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])
df_filtered2 = df_filtered2.drop(columns=["Country Code", "Indicator Name", "Indicator Code"])

y_axis_data = []
x_axis_data = []

countries_with_data = df_filtered["Country Name"].unique()
#print(countries_with_data)
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


for country in countries_with_data:
    row = df.loc[df["Country Name"] == country].values[0] #getting row for df_filtered2 (indicator name for mortality rate attributed to unsafe hygeine )
    clean_row = row[~pd.isna(row)] # get rid of null or NaN cell values
    converted = [safe_parse(x) for x in clean_row] # convert from comma virgule to period decimal value

    y_axis_data.append(converted) #y axis data - Mortality rate attributed to unsafe water, unsafe sanitation and lack of hygiene (per 100,000 population)
#print(y_axis_data) #object array of relevant data for each country

for country in y_axis_data:
    if len(country) == 4:
        # print(country[0])
        y_axis_data.remove(country) #getting rid of countries that have no values for y axis
    else: country[4] = round(country[4], 2)

print(y_axis_data) #object array of relevant data for each country that has values for mortality rates
# print(len(y_axis_data))

def average(row):
    data_only = row[4:]
    sum = 0
    for i in data_only:
        sum += i
    if(len(data_only)) == 0:
        return 0
    return sum / len(data_only)

for country in y_axis_data:
    row = df.loc[df["Country Name"] == country[0]].values[10] #getting row for df_filtered2 (indicator name for handwashing facility)
    clean_row = row[~pd.isna(row)] # get rid of null or NaN cell values
    converted = [safe_parse(x) for x in clean_row] # convert from comma virgule to period decimal value
    value = average(converted) #average for people with basic handwashing facilities including soap and water (% of population)

    x_axis_data.append(round(value,2)) # x axis data - average of people with basic handwashing facilities including soap and water (% of population)


print(x_axis_data) #integer array of this is the average sanitation for each country

merged_array = [subarray + [element] for subarray, element in zip(y_axis_data, x_axis_data)]
cleaned_data = [sublist[:1] + sublist[4:] for sublist in merged_array]
print(cleaned_data)

for country in cleaned_data:
    if len(country) != 3:
        cleaned_data.remove(country) #remove all countries with missing data entries

for country in cleaned_data:
    if country[2] == 0:
        cleaned_data.remove(country)
    country[1] = round(country[1],2)





print("Final: ", cleaned_data) #all countries with values for mortality rate and sanitation rate
print(len(cleaned_data))

converted_data = []

for country in cleaned_data:
    converted_data.append({
        'Country': country[0],
        'Mortality Rate per 100,000 of Population': country[1],
        'Average Sanitation Rate by Percentage of Population': country[2]
    })

print(converted_data)



#non_zero_array = [value for value in x_axis_data if value != 0]
#
# print(non_zero_array)
#print(len(non_zero_array))

#narrowed down countries with mortality rates, then countries with sanitation data. went from 266 unique countries to 153, which makes a lot more sense since there are not 266 countries
# there were also country names in the dataset that weren't actually countries, such as 'Least developed countries: UN classification' 'Low income'

