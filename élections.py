import requests
import json

def telecharger_resultats():
    url = "https://api.electionresults.belgium.be/api/v1/results/view"
    payload = {
        "ElectionType": "CG",
        "ElectionDate": "2019-05-26",
        "Language": "fr",
        "Level": "be"
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://electionresults.belgium.be/fr/results/view?el=CG&date=2019-05-26",
        "Origin": "https://electionresults.belgium.be",
        "Content-Type": "application/json"
    }

    try:
        print(f"📡 Envoi de la requête vers {url} ...")
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"❌ Erreur lors de l'appel API : {e}")
        return

    with open("resultats_elections_belgique.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("✅ Résultats enregistrés dans resultats_elections_belgique.json")

if __name__ == "__main__":
    telecharger_resultats()