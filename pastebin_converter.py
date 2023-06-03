import re

def convert_pastebin_link(link):
    
    match = re.search(r'(?:https?://)?pastebin\.com/([a-zA-Z0-9]+)', link)
    if match:
        unique_id = match.group(1)
        raw_link = f'https://pastebin.com/raw/{unique_id}'
        return raw_link
    else:
        return None

pastebin_link = input("Enter the Pastebin link: ")

raw_link = convert_pastebin_link(pastebin_link)

if raw_link:
    print("Raw link:", raw_link)
else:
    print("Invalid Pastebin link.")
