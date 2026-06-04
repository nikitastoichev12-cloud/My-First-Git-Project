import requests



pdf_url = "https://github.com/progit/progit2/releases/download/2.1.449/progit.pdf"

response = requests.get(pdf_url)

with open("progit.pdf", "wb") as f:
    f.write(response.content)

print("PDF downloaded successfully")



json_url = "http://api.open-notify.org/astros.json"

response = requests.get(json_url)
data = response.json()

with open("astros.json", "w", encoding="utf-8") as f:
    import json
    json.dump(data, f, indent=4)

print("JSON saved successfully")