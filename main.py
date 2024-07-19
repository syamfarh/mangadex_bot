import requests

base_url = "https://api.mangadex.org"
manga_id = "22c844da-1122-4ab3-b726-e7d4b7114254"
languages = ["en"]
r = requests.get(
    f"{base_url}/manga/{manga_id}/feed",
    params={"translatedLanguage[]": languages},
    )
s = [[chapter["attributes"]["chapter"],chapter["id"]] for chapter in r.json()["data"]]
for i in s:
    try:
        i[0] = float(i[0])
    except:
        i[0] = 0
s.sort(key= lambda tup:tup[0])
print("https://mangadex.org/chapter/" +s[-1][1])