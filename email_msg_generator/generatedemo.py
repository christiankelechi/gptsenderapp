import os
import openai
import time
import csv
import json
import requests

class EmailGenerator:
    def __init__(self):
        self.init_api()
        self.translate_table = str.maketrans('aeiou', 'pzwbz')
    
    def init_api(self):
        with open(".env") as env:
            for line in env:
                key, value = line.strip().split("=")
                os.environ[key] = value
    
        openai.api_key = os.environ.get("API_KEY")
        openai.organization_id = os.environ.get("ORG_ID")
    
    def generate_email(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=1.5,
            max_tokens=300
        )
        return response.choices[0].text.strip()
    
    def paraphrase_text(self, text, limit):
        url = "https://paraphraser-genius.p.rapidapi.com/v1/paraphrase"
        headers = {
            "X-RapidAPI-Host": "paraphraser-genius.p.rapidapi.com",
            "X-RapidAPI-Key": "1ed57a3380msh62d4ef476747f66p1efec7jsnbaacafbc4f35",
            "Content-Type": "application/json"
        }
    
        payload = {
            "text": text,
            "limit": limit
        }
    
        response = requests.post(url, headers=headers, json=payload)
        if (response.status_code >= 200) and response.status_code < 220:
            paraphrases = response.json()["paraphrases"]
            return paraphrases
        else:
            print("Error:", response.status_code, response.text)
            return []
    
    def vowel_swapper(self, text):
        return text.translate(self.translate_table)

class EmailManager:
    def __init__(self, generator):
        self.generator = generator
    
    def generate_emails(self, number: int, prompt: str):
        messages = []
        for i in range(number):
            if i < 20:
                messages.append(self.generate_and_save_email(i+1, prompt))
            else:
                paraphrases = self.generator.paraphrase_text(prompt, 50)
                for j, paraphrase in enumerate(paraphrases, start=1):
                    paraphrase_prompt = f"{prompt}\n\nParaphrase {j}: {paraphrase}"
                    messages.append(self.generate_and_save_email(i+1, paraphrase_prompt))
        return messages
    
    def generate_and_save_email(self, index, prompt):
        email = self.generator.generate_email(prompt)
        self.save_to_csv(email, index, 'emails')
    
        msg = {}
        msg['message1'] = f'Generated {index} emails so far'
        
        swapped_email = self.generator.vowel_swapper(email)
        self.save_to_csv(swapped_email, index, 'swappedfolder')
        msg['message2'] = f'Swapped vowels in {index} emails so far'
    
        return msg
    
    def save_to_csv(self, email, index, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(f"{folder}/email_{index}.csv","w",encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow([email])

if __name__ == "__main__":
    generator = EmailGenerator()
    manager = EmailManager(generator)
    messages = manager.generate_emails(1000, "Assuming Codeblaze Academy is hiring for software developers write an awareness for general audience to apply.")
    print(messages)
