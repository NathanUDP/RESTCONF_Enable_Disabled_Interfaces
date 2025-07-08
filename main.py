import requests
import json
from config import switch_info
from urllib.parse import quote
from input_validation import input_validation
from input_validation import input_validation_count
from input_validation import enabled_interface_list
from payload import build_payload
myheaders = {
    'Accept' : 'application/yang-data+json',
    'Content-type' : 'application/yang-data+json'
}
username = switch_info['username']
password = switch_info['password']

url = f"https://{switch_info['host']}/restconf/data/ietf-interfaces:interfaces"

response = requests.request("GET", url, headers=myheaders, auth=(username, password), verify=False).json()


interfaces = response['ietf-interfaces:interfaces']['interface']

disbaled_interface_list = []
interface_count = 0
disabled_interface_count = 0
for interface in interfaces:
    interface_count += 1
    interface_name = interface['name']
    if interface['enabled'] == False:
        disabled_interface_count += 1
        disbaled_interface_list.append(interface_name)
        print(f"{interface_name} is disabled")


print("-" * 25)
print(f"""
There are {interface_count} interfaces on this device.
{disabled_interface_count} are disbaled.  
""")
print("-" * 25)
print("Would you like to enable some interfaces?[y/n]")
usr_input = input(">")

q_response = input_validation(usr_input)
interface_list_count = len(disbaled_interface_list)

if q_response == 'n':
    exit()
else:
    print("-" * 25)
    print("Enter in the amount of interfaces that will be enabled")
    interface_en_count = input(">")

interface_en_count = input_validation_count(interface_en_count, interface_list_count)

to_enable_interface = enabled_interface_list(interface_en_count, disbaled_interface_list)

base_url = f"https://{switch_info['host']}/restconf/data/ietf-interfaces:interfaces"

for name in to_enable_interface:
    enc = quote(name, safe='')
    new_url = f"{base_url}/ietf-interfaces:interface={enc}"
    payload_data = build_payload(name)
    response = requests.request("PUT", new_url, headers=myheaders, auth=(username, password), data=json.dumps(payload_data), verify=False)
    print(f'Response: {response}')

print(response.text)
