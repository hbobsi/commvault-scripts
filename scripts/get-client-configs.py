import os
import csv
from dotenv import load_dotenv # type: ignore
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()
COMMVAULT_SERVER = os.getenv("COMMVAULT_SERVER")
API_TOKEN = os.getenv("API_TOKEN")

payload={}
headers = {
    'Authtoken': API_TOKEN,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

url = f'{COMMVAULT_SERVER}/commandcenter/api/Client'

def get_clients():
    """Retrieves a list of client IDs from a remote server.
    
    This function sends a GET request to a specified URL to fetch client data. It filters the clients based on their type and returns a list of client IDs that do not have a type of 106. In case of a request error, it prints an error message and returns an empty list.
    
    Returns:
        list: A list of client IDs that meet the filtering criteria. If an error occurs during the request, an empty list is returned.
    
    Raises:
        requests.exceptions.RequestException: If there is an issue with the HTTP request.
    """
    try:
        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        response = response.json()
        filtered_clients = [
            client["client"]["clientEntity"]["clientId"]
            for client in response["clientProperties"]
            if client["client"]["clientEntity"]["_type_"] != 106
        ]
        return filtered_clients
    except requests.exceptions.RequestException as e:
        print(f"Error in searching clients: {e}")
        return []

def get_configs(filtered_clients):
    """Retrieves client configurations for a list of filtered clients and saves the information to a CSV file.
    
    Args:
        filtered_clients (list): A list of client IDs for which the configurations are to be retrieved.
    
    Returns:
        None
    
    Raises:
        requests.exceptions.RequestException: If there is an error during the HTTP request.
        KeyError: If the expected keys are not found in the response JSON.
    
    The function makes a GET request to retrieve details for each client ID, extracts the client name and install directory, 
    and writes this information to a CSV file named 'clients_info.csv'.
    """
    client_info_list = []
    for client_id in filtered_clients:
        response = requests.get(f"{url}/{client_id}", headers=headers, data=payload, verify=False)
        client_details = response.json()
        client_name = client_details["clientProperties"][0]["client"].get("displayName")
        install_directory = client_details["clientProperties"][0]["client"].get("installDirectory", "N/A")
        client_info_list.append([client_name, install_directory])
    with open("clients_info.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["ClientName", "InstallDirectory"])
        csv_writer.writerows(client_info_list)

if __name__ == "__main__":
    clients = get_clients()
    get_configs(clients)