import pandas as pd

# Load the CSV file with the correct delimiter
df = pd.read_csv("environment-raw.csv", delimiter=";")

# Filter for the relevant indicator
indicator_filter = "Mortality rate attributed to unsafe water, unsafe sanitation and lack of hygiene (per 100,000 population)"
df_filtered = df[df["Indicator Name"] == indicator_filter]

# Drop irrelevant columns and keep countries with at least one non-null value
df_filtered = df_filtered.drop(columns=["Country Code", "Indicator Name", "Indicator Code"]).dropna(how="all", axis=0)

# Extract country names
countries_with_data = df_filtered["Country Name"].unique()
print(countries_with_data)
