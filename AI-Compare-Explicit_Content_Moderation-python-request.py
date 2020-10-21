import requests

# You can find the documentation here : https://www.ai-compare.com/v1/redoc/#operation/Explicit%20Content%20Detection

#Enter your API Token
headers = {  'Authorization': 'Bearer your API Key'} #You can get your free API token here https://www.ai-compare.com/accounts/login/?next=/my_apis

# Select API
url = 'https://www.ai-compare.com/v1/pretrained/vision/explicit_content_detection'

# Select providers
payload = {'providers': '[\'google_cloud\', \'cognitives_service\', \'aws\', \'ibm\']'}

# Select file to test
files = [  ('files', open('Picture/example.jpg','rb'))]

# Request to AI COMPARE
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))
