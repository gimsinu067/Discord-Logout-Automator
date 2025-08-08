import requests

payload = {
    "provider": None,
    "voip_provider": None
}

headers = {
    "accept": "*/*",
    "accept-language": "ko",
    "authorization": "YOUR_DISCORD_TOKEN_HERE",
    "content-type": "application/json",
}

response = requests.post("https://discord.com/api/v9/auth/logout", headers=headers, json=payload)

if response.status_code == 204:
    print(response.json())
else: 
    print(f"Failed to fetch data: {response.status_code}")
