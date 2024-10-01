import requests
from colorama import init, Fore, Style

init()

class Color:
    HEADER = Fore.RED
    OKBLUE = Fore.BLUE
    OKCYAN = Fore.CYAN
    OKGREEN = Fore.GREEN
    WARNING = Fore.YELLOW
    FAIL = Fore.RED
    ENDC = Style.RESET_ALL
    BOLD = Style.BRIGHT
    UNDERLINE = Style.BRIGHT + Fore.WHITE

ASCII_ART = r"""


 █    ██   ██████ ▓█████  ██▀███   ▄▄▄▄    ▄▄▄        ██████ ▓█████ 
 ██  ▓██▒▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▓█████▄ ▒████▄    ▒██    ▒ ▓█   ▀ 
▓██  ▒██░░ ▓██▄   ▒███   ▓██ ░▄█ ▒▒██▒ ▄██▒██  ▀█▄  ░ ▓██▄   ▒███   
▓▓█  ░██░  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  ▒██░█▀  ░██▄▄▄▄██   ▒   ██▒▒▓█  ▄ 
▒▒█████▓ ▒██████▒▒░▒████▒░██▓ ▒██▒░▓█  ▀█▓ ▓█   ▓██▒▒██████▒▒░▒████▒
░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░░▒▓███▀▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░░ ▒░ ░
░░▒░ ░ ░ ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░▒░▒   ░   ▒   ▒▒ ░░ ░▒  ░ ░ ░ ░  ░
 ░░░ ░ ░ ░  ░  ░     ░     ░░   ░  ░    ░   ░   ▒   ░  ░  ░     ░   
   ░           ░     ░  ░   ░      ░            ░  ░      ░     ░  ░

                                     ╔═══════════════════════════╗
                                     ║SnusBase Tool by user-osint║
                                     ║Version bêta               ║
                                     ║Discord : .osint.user.     ║
                                     ║GitHub : user-osint        ║
                                     ║Instagram : soon...        ║
                                     ║Web Site : soon...         ║
                                     ╚═══════════════════════════╝


      ════════════════════════════════════════════════════════════════════════════════════════════════  
         [1] -> Rechercher avec une Email         ║  [4] -> Rechercher avec un Mot De Passe
         [2] -> Rechercher avec un Pseudo         ║  [5] -> Rechercher avec un Mot De Passe Hasher
         [3] -> Rechercher avec un Nom & Prénom   ║  [6] -> Rechercher avec une Adresse IP
    ═════════════════════════════════════════════════════════════════════════════════════════════════════
                            ║          "Exit" = Fermer le tools          ║
                            ╚════════════════════════════════════════════╝ 
"""

SEARCH_TYPES = ["email", "username", "name", "password", "hash", "lastip"]

def search(search_input, search_type):
    if not search_input:
        print(f"{Color.FAIL}Please enter a search term.{Color.ENDC}")
        return

    apiKey = 'sbyjthkoft4yaimbwcjqpmxs8huovd'
    url = 'https://api-experimental.snusbase.com/data/search'
    headers = {
        'Auth': apiKey,
        'Content-Type': 'application/json'
    }
    payload = {
        'terms': [search_input],
        'types': [search_type],
        'wildcard': False
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        display_results(response.json().get('results', {}))
    else:
        print(f"{Color.FAIL}Error: {response.text}{Color.ENDC}")

def display_results(results):
    if not results:
        print(f"{Color.WARNING}No results found.{Color.ENDC}")
    else:
        for database, entries in results.items():
            for entry in entries:
                for key, value in entry.items():
                    if key == 'lastip':
                        print(f"{Color.OKGREEN}{key}: {value} (Get Location){Color.ENDC}")
                    else:
                        print(f"{Color.OKCYAN}{key}: {value}{Color.ENDC}")
                print('-' * 50)

def get_location(ip):
    try:
        response = requests.get("http://ip-api.com/json/" + ip)
        response.raise_for_status()
        get_location = response.json()
        print(f"{Color.OKGREEN}IP: {ip}{Color.ENDC}")
        print(f"{Color.OKCYAN}Country: {get_location['country']}{Color.ENDC}")
        print(f"{Color.OKCYAN}Region: {get_location['region']}{Color.ENDC}")
        print(f"{Color.OKCYAN}City: {get_location['city']}{Color.ENDC}")
        print(f"{Color.OKCYAN}Latitude: {get_location['lat']}{Color.ENDC}")
        print(f"{Color.OKCYAN}Longitude: {get_location['lon']}{Color.ENDC}")
        print("")
    except requests.exceptions.RequestException as e:
        print(f"{Color.FAIL}Error: {e}{Color.ENDC}")

def main():
    title = f"{Color.HEADER}{ASCII_ART}SnusBase Search Engine by user_osint{Color.ENDC}"
    print(title)
    
    search_type_choice = int(input("\nEnter the number corresponding to the search type: "))
    
    search_type = SEARCH_TYPES[search_type_choice - 1]
    search_input = input("Enter search term: ")

    search(search_input, search_type)

    while True:
        ip = input("Enter IP to get location (or 'exit' to quit): ")
        if ip.lower() == 'exit':
            break
        get_location(ip)

if __name__ == "__main__":
    main()
