import pandas as pd
import schedule
import time

def find_added_rows(file1, file2):
    # Read the Excel files into DataFrames
    df1 = pd.read_excel(file1 , skiprows=2)
    df2 = pd.read_excel(file2 , skiprows=2)

    # Set the index for both DataFrames
    df1.set_index(['Name', 'Registration No.', 'Contact Person', 'Address', 'Email-Id',
       'Telephone', 'Fax', 'City', 'State', 'Pincode', 'Address.1',
       'Email-Id.1', 'Telephone.1', 'Fax.1', 'City.1', 'State.1', 'Pincode.1',
       'From', 'To', 'Country'], inplace=True)
    df2.set_index(['Name', 'Registration No.', 'Contact Person', 'Address', 'Email-Id',
       'Telephone', 'Fax', 'City', 'State', 'Pincode', 'Address.1',
       'Email-Id.1', 'Telephone.1', 'Fax.1', 'City.1', 'State.1', 'Pincode.1',
       'From', 'To', 'Country'], inplace=True)

    # Find added rows in the second DataFrame
    added_rows = df2[~df2.index.isin(df1.index)]

    return added_rows

def job():
    # Specify the file paths
    file1_path = 'Desktop.xls'
    file2_path = 'Desktop2.xls'

    # Find added rows
    added_rows_data = find_added_rows(file1_path, file2_path)
    
    # Save the added rows to a new Excel file
    compared_data_path = 'updated_report.xlsx'
    with pd.ExcelWriter(compared_data_path, engine='openpyxl') as writer:
        added_rows_data.to_excel(writer, sheet_name='Compared Data', index=True)
    
    print("Daily comparison and report generation completed.")

# Schedule the job to run every day at 02:55 PM
schedule.every().day.at("14:55").do(job)

# Run the scheduler loop
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 seconds before checking the schedule again
