import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}


	
def summeryCalc2(text):
    response = requests.post(API_URL, headers=headers, json=text)
	

    return response.json()
    