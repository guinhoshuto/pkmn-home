import pandas as pd
import requests as re

# pegar dex da api
# adicionar hisui

pokeapi = re.get("https://pokeapi.co/api/v2/pokemon/?limit=2000").json()

def dex_entry(row): 
    number = row["url"].split("/")
    return number[6]

def variant(row):
    entry_name = row["name"].split("-")
    if len(entry_name) > 1:
        if entry_name[1] in ["alola", "hisui", "galar"]:
            return entry_name[1]
     
    return ""

def variant_entry_number(row):
    data = re.get(row["url"]).json()
    specie = data["species"]["url"].split("/")
    return specie[6]

pkmn = pd.DataFrame.from_dict(pokeapi["results"])

print(pkmn.tail())
pkmn["dex_entry"] = pkmn.apply(lambda row: dex_entry(row), axis=1)
pkmn["variant"] = pkmn.apply(lambda row: variant(row), axis=1) 

variants = pkmn[pkmn["variant"] == "alola"]
variants["dex_entry"] = variants.apply(lambda row: variant_entry_number(row), axis=1)

pkmn = pkmn.head(898)
print(variants["dex_entry"])

print(pkmn)
pkmn.to_csv("pkmn-home.csv")
