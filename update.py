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

# Example usage:
url = "https://www.sebi.gov.in/sebiweb/other/IntmExportAction.do?intmId=13"
destination_path = "Desktop.xls"

download_excel_file(url, destination_path)