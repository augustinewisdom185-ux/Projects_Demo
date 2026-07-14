import pandas as pd

#Loading the csv file to file_name
file_name = pd.read_csv("marketing_campaign_data_messy.csv", encoding='utf-8')
#Removes any space in column names
file_name.columns = file_name.columns.str.strip()
#Separating date and time to get just date
file_name['Date'] = file_name['Start_Date'].str.split(" ").str[0]
#Dropping the initial date which was start_date
file_name.drop(columns=['Start_Date'], inplace=True)
#Arranging the date so it looks like y-m-d
file_name['Dates'] = pd.to_datetime(file_name['Date']) #format = %d-%m-%Y
file_name.rename(columns={'Dates':'Start_Date'},inplace = True)
#Converting end_date to datetime
file_name['End_D'] = pd.to_datetime(file_name['End_Date'])
file_name.rename(columns={'End_D':'End_Dats'},inplace = True)
#Dropping end_start
file_name.drop(columns=['End_Date'], inplace=True)
#Dropping the Date table
file_name.drop(columns=['Date'], inplace=True)
#Ajusting the active column
try:
    def active_res(row):
        if row ['Active'] == 'Y' or row['Active'] == 1 or row ['Active'] == 'True':
            return "Yes"
        else:
            return "No"
    file_name['Actives'] = file_name.apply(active_res, axis=1)
    file_name.rename(columns={'Actives':'Active_Val'}, inplace = True)
    file_name.drop(columns=['Active'], inplace=True)

# Clean up duplicate columns (safeguards against the 2D DataFrame error)
    file_name = file_name.loc[:, ~file_name.columns.duplicated()]

    # 2. Rename the column to Num_Click
    file_name.rename(columns={'Clicks': 'Num_Click'}, inplace=True)

    # 3. Convert values to numeric (safely handles strings and sets invalid values to NaN)
    file_name['Num_Click'] = pd.to_numeric(file_name['Num_Click'], errors='coerce')

except KeyError as error:
    print(f"Error: The specified column was not found in the dataset. Details: {error}")
except Exception as error:
    print(f"An unexpected error occurred: {error}")
  
def campaign(row):
    if row['Campaign_Tag'] == 'FA':
        return 'Facebook'
    elif row['Campaign_Tag'] == 'IN':
        return 'Instagram'
    elif row['Campaign_Tag'] =='EM':
        return 'Email'
    elif row['Campaign_Tag'] == 'GO':
        return 'Google Ads'
    elif row['Campaign_Tag'] == " ": return "None"
    else:
        return 'TikTok'
    
file_name['Channel'] = file_name.apply(campaign, axis=1)
file_name.drop(columns=['Num_Click'], inplace = True)
file_name.drop(columns=['Campaign_Tag'], inplace=True)

#Adding $ to all the values lacking $
#astype(str) converts spend to string
file_name['Spend'] = file_name['Spend'].astype(str)
missing_doll = ~file_name['Spend'].str.startswith('$')
file_name.loc[missing_doll,'Spend'] = '$' + file_name.loc[missing_doll,'Spend']

#Removing minus signs in spend
file_name['Spend'] = file_name['Spend'].str.replace(r'[-()]',"", regex=True)

#Handling empty spaces in conversion column
file_name['Conversions'] = file_name['Conversions'].fillna('-')
#Converts numbers to float, keeps '-' as NaN
file_name['Conversions'] = pd.to_numeric(file_name['Conversions'], errors='coerce')
#Checking for duplicates in Campaign_ID and Campaign_Name if there is any it deletes the entire row
file_name.drop_duplicates(subset = ['Campaign_ID', 'Campaign_Name'], inplace=True)
file_name
file_name.shape
