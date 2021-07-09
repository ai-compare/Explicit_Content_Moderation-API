# Explicit_Content_Detection - Eden AI API
## Description
This repositery provides code to implement Eden AI Explicit Content Detection  API. Eden AI Explicit Content Detection API allows to call Explicit Content Detection APIs from multpile explicit content detection providers. It permits to get results from these providers, compare the results, siwtch between providers or combine them.

## What is Eden AI ?
[Eden AI](https://www.edanai.co/) is a SaaS providing APIs connected to big (AWS, GCP, etc.) and small AI providers for vision, text, audio, OCR, prediction and translation AI engines. Our solution allows users to compare the performance of these providers APIs according to their data and use them directly via our API thus offering great flexibility and making it very easy to change supplier. In particular, we offer better performance with the "Genius" feature that cleverly combines results from multiple providers.

Eden AI offers community offer (free) when you [create your account for free](https://app.edenai.run/user/login). You can then use [APIs](https://api.edenai.run/v1/redoc/), use the [interface](https://app.edenai.run/bricks/default), manage your account, access to cost management.

You can find APIs documentation here : https://api.edenai.run/v1/redoc/

## Usage
### Initialization
Enter your access token and select your API endpoint. You can get your token on your account manager [here](https://www.ai-compare.com/accounts/login/?next=/my_apis/my_account).
```python
import requests
headers = {  'Authorization': 'Bearer your API Key'}
url = 'https://api.edenai.run/v1/pretrained/vision/explicit_content_detection'
```
### Select parameters 
Set your file (.jpg, .png, .jpeg, .tiff) and providers APIs you want to run :
```python
payload = {'providers': '[\'google_cloud\', \'microsoft\', \'aws\', \'ibm\']'}
files = [  ('files', open('Picture/example.jpg','rb'))]
```
### Get results
```python
response = requests.request("POST", url, headers=headers, data = payload, files = files)
print(response.text.encode('utf8'))
```

## Response example
<details>
</summary>

```json
[
  {
    "solution_name": "Google Cloud",
    "execution_time": "1.372380",
    "result": {
      "image_path": "media/data/files/94025962_235348981071578_8173325693455695872_n_BZ2ZYv4.jpg",
      "labels": [
        "Adult",
        "Spoof",
        "Medical",
        "Gore",
        "Racy"
      ],
      "likelihood": [
        1,
        1,
        2,
        1,
        2
      ]
    },
    "api_response": {
      "adult": "VERY_UNLIKELY",
      "spoof": "VERY_UNLIKELY",
      "medical": "UNLIKELY",
      "violence": "VERY_UNLIKELY",
      "racy": "UNLIKELY"
    },
    "status": "Success"
  },
  {
    "solution_name": "Microsoft Azure",
    "execution_time": "1.615618",
    "result": {
      "image_path": "media/data/files/94025962_235348981071578_8173325693455695872_n_BZ2ZYv4.jpg",
      "labels": [
        "Gore",
        "Adult",
        "Racy"
      ],
      "likelihood": [
        1,
        1,
        1
      ]
    },
    "api_response": {
      "adult": {
        "isAdultContent": false,
        "isRacyContent": false,
        "isGoryContent": false,
        "adultScore": 0.00341306091286242,
        "racyScore": 0.004433806985616684,
        "goreScore": 0.08777628093957901
      },
      "requestId": "6b8a21fe-c7e0-47e7-8c5e-f605d0da9b72",
      "metadata": {
        "width": 900,
        "height": 1900,
        "format": "Jpeg"
      }
    },
    "status": "Success"
  },
  {
    "solution_name": "Amazon Web Services",
    "execution_time": "2.842318",
    "result": {
      "image_path": "media/data/files/94025962_235348981071578_8173325693455695872_n_BZ2ZYv4.jpg",
      "labels": [],
      "likelihood": []
    },
    "api_response": [],
    "status": "Success"
  },
  {
    "solution_name": "Genius",
    "nb_Provider": 3,
    "status": "Success",
    "result": {
      "labels": [
        "Adult",
        "Spoof",
        "Medical",
        "Gore",
        "Racy"
      ],
      "likelihood": [
        1,
        1,
        2,
        1,
        2
      ]
    }
  }
]
```

</details>

## Blog articles
We provides on our website some [blog articles on AI engines](https://www.edenai.co/blog)

## Contact
If you have any question or request, you can contact us at contact@edenai.com

## Terms of use
You can access to our terms [here](https://www.edenai.co/terms) on our website.

#
![Screenshot](https://github.com/ai-compare/Speech_to_text-API/blob/ba9d4f1668d8758141f24240d1287640b4211c63/Logo%20complet%20Eden%20AI%20-%20format%20PNG.png)
