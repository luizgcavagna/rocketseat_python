# pip3 install requests==2.31.0

print("\nImportacao e uso de um modulo de terceiros")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitacao HTTP {url} retornou o status {response.status_code}")