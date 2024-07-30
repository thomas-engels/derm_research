import pandas as pd

# Read the dermatology providers data into data frame
df_derm_providers = pd.read_csv('/data/filtered_dermatology_data.csv')

# Create pivot table by group the zip, city, state and counting the providers per zip
df_derm_providers_by_zip = (df_derm_providers.groupby(['Rndrng_Prvdr_Zip5', 'Rndrng_Prvdr_City', 'Rndrng_Prvdr_State_Abrvtn'])
                            .agg({'Rndrng_NPI': pd.Series.count})).reset_index()

# Read the population data by zip code into data frame
df_population_by_zip = pd.read_csv('/data/2024_07_28_irs_population_estimates_by_zip.csv')

# Drop the empty columns
df_population_by_zip = df_population_by_zip.drop(columns=['Unnamed: 2', 'Unnamed: 3'])

# Perform a left join using the zip code, keeping filtered derm data on the left
df_merged = df_derm_providers_by_zip.merge(df_population_by_zip, left_on='Rndrng_Prvdr_Zip5',
                                                          right_on='zip', how='inner')
# Calculate dermatologist to population ratio
df_merged['derm_to_pop_ratio'] = df_merged['Rndrng_NPI'].div(df_merged['irs_estimated_population'])

# Convert dermatologist to population ratio to percentage
df_merged['derm_to_pop_percent'] = df_merged['derm_to_pop_ratio'] * 100

# Columns renaming for readability
df_merged.rename(columns={"Rndrng_NPI": 'derm_provider_count'}, inplace=True)

# Drop redundant zip code column
df_merged.drop(columns=['Rndrng_Prvdr_Zip5'], inplace=True)

# Reorder columns for readability
df_merged = df_merged[['Rndrng_Prvdr_City', 'Rndrng_Prvdr_State_Abrvtn', 'zip', 'derm_provider_count',
                       'irs_estimated_population','derm_to_pop_ratio', 'derm_to_pop_percent']]

# Convert from data frame to csv
df_merged.to_csv('/data/derm_providers_by_zip.csv', index=False, encoding='utf-8', header=True)
