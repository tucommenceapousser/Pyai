import requests

# Votre clé API Codestral
api_key = "CwrLyHiZC3KkU3G5FSNk1oBxAOMVBDju"

# Les URLs des points de terminaison de l'API Codestral
completion_url = "https://codestral.mistral.ai/v1/fim/completions"
chat_url = "https://codestral.mistral.ai/v1/chat/completions"

# Spécifiez le modèle à utiliser
model_name = "mistral-code-7b"  # Par exemple, utilisez un modèle valide tel que "mistral-code-7b"

def get_code_completion(prompt, max_tokens=100):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model_name,  # Ajoutez le nom du modèle ici
        "prompt": prompt,
        "max_tokens": max_tokens
    }

    response = requests.post(completion_url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json().get("choices")[0].get("text").strip()
    else:
        return f"Erreur : {response.status_code} - {response.text}"

def get_chat_response(message, max_tokens=150):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model_name,  # Ajoutez le nom du modèle ici
        "messages": [{"role": "user", "content": message}],
        "max_tokens": max_tokens
    }

    response = requests.post(chat_url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json().get("choices")[0].get("message").get("content").strip()
    else:
        return f"Erreur : {response.status_code} - {response.text}"

def main():
    print("Bienvenue dans l'interface interactive de Codestral !")

    while True:
        print("\nOptions :")
        print("1. Demander une complétion de code")
        print("2. Envoyer un message au chat")
        print("3. Quitter")

        choice = input("Choisissez une option (1/2/3) : ").strip()

        if choice == "1":
            prompt = input("Entrez votre prompt de code : ")
            completion = get_code_completion(prompt)
            print("\nComplétion de code :")
            print(completion)

        elif choice == "2":
            message = input("Entrez votre message pour le chat : ")
            response = get_chat_response(message)
            print("\nRéponse du chat :")
            print(response)

        elif choice == "3":
            print("Au revoir !")
            break

        else:
            print("Option non valide, veuillez réessayer.")

if __name__ == "__main__":
    main()