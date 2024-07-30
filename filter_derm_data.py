import pandas as pd
import zipfile

df_practitioner_data = pd.read_csv('MUP_PHY_R23_P05_V10_D21_Prov_Svc.csv')
# CSV not stored in Github repo due to massive size
# You can download the CSV here: https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service
# Select Download -> Agree to T&C -> All Datasets and/or Resources -> Dates 2021 to 2022 -> Datasets
# -> Medicare Physician & Other Practitioners - by Provider and Service 2022

df_derm_only = df_practitioner_data[df_practitioner_data['Rndrng_Prvdr_Type'] == 'Dermatology']
df_derm_only.drop_duplicates(subset='Rndrng_NPI', inplace=True)

df_derm_only.to_csv('filtered_dermatology_data.csv', index=False)

with zipfile.ZipFile('filtered_dermatology_data.zip', 'w') as zipf:
    zipf.write('filtered_dermatology_data.csv', compress_type=zipfile.ZIP_DEFLATED)