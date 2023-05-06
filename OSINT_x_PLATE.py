import argparse
import json
import requests

# Print Banner
print("")     
print("                                ╓▄▓▌▀▓▓▓▓@▄▄,                              ")
print("                             .▄█▓▓▓▀╜└└╙╙▀▀▓▓▄¿                            ")
print("                           `Å╙      ,▄▄▓▓▀▀▓█▀▀▄                           ")
print("                       ,         █▀▓▓▓▀▓▀Ñ▄▄▄▓▓▌   ,▓▓▓█▓▓▄,               ")
print("                  ,▄▓▓▀▀▀▓▓▓     █▀╫╫╫╫╫╫╫▓╩╨███   J█╫▓▓▓█▓╫▀▓▄            ")
print("                ╥▓▌Ñ██▓█▓▓╫╫▌   █▀▓▓▓▓▓▓▓▌  ▄█▀█    ▌╫▓█▓▓▓▓▓▓▓█▄¿         ")
print("              ╥▓█▓▓▓▓▓▓▓▓▓▒▓L  ▐▓▓▓█▓▓▓▌▓▌ ▄█▌█    ,▌╫▀█▓▓▀▓▓█▓█▓▀▄        ")
print("             ▓▌▀▓▓▀████▀╫█▀█   █▓▓▓▓█▓▓▌▓▓█▓▀█    ▄▓╫╫▌▓▓▀▀█▓▓█╫▓▓▓█▄      ")
print("           ▄█▓▓▓█▓█▓█▓█▓▓▓▓▓▓▄▓▓▓▓▓▓▓▓▓▓▓▀▓▓█▓▓▓▓▓▓▓█▀█▄▒██▓▓▌█╫█╫█▓▓▄     ")
print("          ╥███▓╫▓╫▓╫█▀▓▓▓▓▓▀█▓▓█▓▓▓▓▓▓▓█▄▌▓█▌▀▓▓▀▓▀▓▓▓▓▓▓▓█▓█▓▀▌▀▌▓▓▓▓▌    ")
print("         ,█▓╫█╫█▀▓▓▓▌▓▓▓▓╫▓▓▀▒█▓▓▓╫█▀▀█▀▌▓█╫▓▓▓█▓▓▓▓▓▓▓▀▓▓▓▓▓█╫█▓█▓▓█▓▓█   ")
print("         █▓▓█▓█▓██▓▌██▓█▓█▓▒█▀█▓▓▓╫▌╫█▌▓▓██╫█╫▓▓▌▓▓▓▓▒▓█▓█▀██▓████▓██▓██▄  ")
print("        ▄█▓╫█▀█▀█▓█╫█▓▓╫▓╫█▓█▓█▓▓█▓█▓▌╫▌█▓█╫▓▓▓▓█▓▓▓█▓▓▓▓▓▓╫█╫█▓█▓▓█▓▓▓▓█  ")
print("       ╒██╫▓▓▓▌╫▓╫▌▓▌▓╫█▓▓▓╫▓╫▓██▓▓▓▓▀▀▌█▓▓▀▓▀▓▀▓╫▓▓▌╫▓╫▓╫▓╫█▓▓▓█▓█╫█▓▓█▓▄ ")
print("       █▓▀╫▓╫█▀█▓▓▓▓▓▌╫▌╫█▓▓▓╫█▓█▓▓▓▓▀▓▓█╫▓╫▌╫▌╫▓╫█╫▌╫█▓▓╫▓╫█▓╫█▀█▓▓╫▓█▓▓█ ")
print("       █▓╫▓▀╫▌╫█╫▌╫▌▓▌╫▌╫█╫╫█╫▓▓▓█▓█▓▓▄▌██▓▓▓▓▓▓▓╫▌╫▌╫▌╫▌╫█▓▀▀▓▓▓▀██▓▀▓█▓█ ")
print("      ▄▓▒▓▓▓█╫▓▓▓▓▀▀`▀▀█▓▓▓╫█▓▓▀███▓▀█▀▓▓█▒╫▒▓▓█▀▀▀▀▓▓▓▀▀▀`   `▀█▓█▓▓▌▓▓▓█ ")
print("      █╫▓▓╫▓▀▓▌▓▀       `└`▀  ▄▌▀▓█▓▓▓▌█╫█▓█▓▓▓▓█▄               ▀▀▀▓╫▓▀▓█ ")
print("      █▓▓╫▓▌▓█▌`              █▓▓██▓▓▓▌▄▓█▓███▓▓▓█▓▄                  ▀▀▓╫▌")
print("      ▀▓╫▓█▓Ö                 ▀▓▓▒▓▓▓█▌█╫█▓▓▓▓▓▓█▓█▓▌        ▓█▓ ▄▄,    ▀▓▌")
print("       █▀╜       ▄µ            ╨▀▓▓▓▓██▌██▀█▓▓▓▓▓▓▌▀▓▓       ▀▓▓█▓▓█▌      ")
print("              ▀▀▄▄▄▀▓▓▄▄        ╥▄▀█▓▓█▓▓▌█▓▓██▓█▓██▓▀▓▓        ▓▓▓▓█      ")
print("            ╥,▄█▓▓▓▓▌ ╙▓▓▄,╥╥æ▓█▀▀└ ▄█▓▓╙▓▓█╫▓▓▀█▓█▓▓▓▓▓▌     ▄▄▓▓█▌ ▄▄▄   ")
print("           ╨█▓▓██▓▓▓▓▌▄▄▓▓▀▀▌╫▓█▄▄▓█▓▀▀   ╙ ╙╙└▀██▀▀╙▀▀└ ,  ,▄▓▓▓▓▓█▓▓▓█F  ")
print("              `  ╙▀▀█▓▓▓▓██▓▌▀█▓█▓▓█▓▌     ,▄▄▄▄▓█     ▄▓▓█▄▄▓▓▓▓▓▓█▓▓▀╙   ")
print("              ⁿ▄▄▓▓▓█▓▓▓▓▓▓█µ -█▓▓▓▓▓▓▓▄   ▓▓▓██▒▀█▓▓ ▄▓▓▓▓▌█▓▓▓▓▓▀        ")
print("              ▀▓▓▓▓▓▓▓▓▓▓▓▓▓█  Å█▓▓▓▓▓▓▓▌ ▄█▓▓▓▓█▓▓██ █▓▓▓█▄█▓██▀          ")
print("                ▀▀█▓█▓▌▀█▓▓▓█▄▄▄▓██▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█▄███▓▓▓▓▓▓▓▌          ")
print("                         ▄█▓▓▓▓▓▓▓▓▓▓█▓▓▓█▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓█▀          ")
print("                         █▓▓▓▓▓▓▓▓▓▓▓▀,. █▓▓▓▓▓▓▓▓█▀▀▀▓█▓▓▓▓█▌▀            ")
print("                          ▐▌▀█▀▓▀▀██▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓█▓Γ `                 ")
print("                                  ▀▓█▓▓█▓▀▓▓▓▓▀╙▀▀▓█▀▀                     ")
print("           =============================================================   ")                                       
print("                                   OSINT MX                                ")  
print("           =============================================================   ")
print("                               osint x car plate                           ")
print("                             ======================                        ")
print("                              Author: Edgar Medina                         ")
print("                             ======================                        ")  
print("")

# Define command line arguments
parser = argparse.ArgumentParser(description='Verifies a car license plate number registered in Mexico, using the Repuve/SCT API')
parser.add_argument('--plate', required=True, help='License plate number to verify')
args = parser.parse_args()

# Load API key from config file
with open('config.json', 'r') as f:
    config = json.load(f)
    api_key = config['api_key']

# Set up API request
url = "https://documentos-mex1.p.rapidapi.com/Repuve/VerificarPlaca"
querystring = {"placa": args.plate}
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "documentos-mex1.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers, params=querystring)

# Print API response
print(response.text)
