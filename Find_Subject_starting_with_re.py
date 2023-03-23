data = {
    "MessageType": "Agent Inquiry",
    "Message": "Hi",
    "Sender": "test@test.com",
    "PropertyRef": "RENTAL IN SUNSET PARK",
    "PropertyURL": "https://test",
        "PropertyAddress": {
        "original": "111 50th Street #ID",
        "found": False,
        "normalized": "111 50th Street #ID",
        },
    "PropertyPrice": "$1,895",
    "PropertyDetails": "1 Bed 1.0 Bath Listing by Skyward (Park Avenue, New York, NY)",
    "Source": "StreetEasy",
    "Received": "2023-03-23T09:33:29.558975-04:00",
    "OriginalRecipient": "test.email@test.com",
    "Subject": "re: Agent Inquiry | 846 50th Street #ID",
    "Template": "StreetEasy v6 agent",
}

for value in data.values():
    if type(value) is not dict and value.lower().startswith("re:"):
        print("found it")

d = {k:v for (k,v) in data.items() if type(v) is not dict and v.lower().startswith("re:")}
if d["Subject"]:
    print("found it")

if data.get("Subject").lower().startswith("re:"):
    print("found it")
