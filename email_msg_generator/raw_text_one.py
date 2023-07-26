# import requests
# import json
# url = "https://paraphrase-genius.p.rapidapi.com/dev/paraphrase/"

# payload = {
#     "text": "\n\nEmail marketing is a great way for any business to increase its visibility, customer base, and profitability. It is an effective digital marketing tool to reach out to potential customers with tailored messages. Email marketing allows businesses to keep their customers informed, build relationships, and even increase sales.\n\nEmail marketing involves using email as a direct marketing tool to send out messages to current and potential customers. Companies can send out newsletters, special offers, or even simple reminders to engage their customers. This technique can be used to increase brand awareness, make direct sales, and even set up an affiliate-based business.\n\nTo ensure success with email marketing, careful target market selection is essential. Crafting messages that will capture the target audience\u2019s attention is also key. It is essential to have clear objectives before sending out emails. Knowing what impact the emails have made and ensuring that the message was received is also important. \n\nEmail marketing requires a lot of time and effort but it can be a very effective and efficient way for businesses to reach potential customers. It can lead to increased customer engagement and ultimately more sales. With the help of the right tools and strategies, email marketing can be an invaluable asset for any business.",
#     "result_type": "multiple"
# }
# headers = {
#     "content-type": "application/json",
#     "X-RapidAPI-Key": "1ed57a3380msh62d4ef476747f66p1efec7jsnbaacafbc4f35",
#     "X-RapidAPI-Host": "paraphrase-genius.p.rapidapi.com"
# }

# num_phrases = 1  # Number of paraphrased contents to generate
# paraphrased_contents = []  # Store the paraphrased contents

# for _ in range(num_phrases):
#     response = requests.post(url, json=payload, headers=headers)
#     paraphrased_contents.append(response.json())

# # Print all the paraphrased contents
# for i in paraphrased_contents:
#     with open("rephrased.json","a") as file:
#         data={'message_body':i}
#         json.dump(data,file)
