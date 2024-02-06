import schedule
import time
import requests

def download_excel_file(url, destination):
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"Download successful. File saved to {destination}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

def job():
    url = "https://www.sebi.gov.in/sebiweb/other/IntmExportAction.do?intmId=13"
    destination_path = "Desktop2.xls"
    download_excel_file(url, destination_path)

# Schedule the job to run every day at 02:50 PM
schedule.every().day.at("14:50").do(job)

# Run the scheduler loop
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 seconds before checking the schedule again
