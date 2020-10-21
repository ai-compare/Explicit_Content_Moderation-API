# Explicit_Content_Moderation - AI-Compare API
## Description
This repositery provides code to implement [AI-Compare Explicit Content Moderation API](https://www.ai-compare.com/vision_apis/explicit_content_detection). [AI-Compare Explicit Content Moderation API](https://www.ai-compare.com/vision_apis/explicit_content_detection) allows to call Explicit Content Moderation APIs from Google Cloud Platform Cloud Vision, AWS Rekognition, Microsoft Azure Computer Vision, and IBM Watson Visual Recognition. It permits to get results from these providers and compare the results.

## What is AI-Compare ?
[AI-Compare](https://www.ai-compare.com/) is a SaaS providing APIs connected to big (AWS, GCP, etc.) and small AI providers: [object detection](https://www.ai-compare.com/vision_apis/object_detection), [OCR](https://www.ai-compare.com/vision_apis/ocr), [NLP](https://www.ai-compare.com/text_apis/sentiment_analysis/), [speech-to-text](https://www.ai-compare.com/audio_apis/speech_recognition), custom vision, etc. Our solution allows users to compare the performance of these providers APIs according to their data and use them directly via our API thus offering great flexibility and making it very easy to change supplier. In particular, we offer better performance with the "Genius" feature that cleverly combines results from multiple providers.

AI-Compare offers 2$ free credits when you [create your account for free](https://www.ai-compare.com/accounts/login/?next=/my_apis). You can then use [APIs](https://www.ai-compare.com/v1/redoc/), use the [interface](https://www.ai-compare.com/my_apis), manage your account and have access to all the APIs.

You can find APIs documentation here : https://www.ai-compare.com/v1/redoc/

## Usage
### Initialization
Enter your access token and select your API endpoint. You can get your token on your account manager [here](https://www.ai-compare.com/accounts/login/?next=/my_apis/my_account).
```python
import requests
headers = {  'Authorization': 'Bearer your API Key'}
url = 'https://www.ai-compare.com/v1/pretrained/vision/explicit_content_detection'
```
### Select parameters 
Set your file (.jpg, .png, .jpeg, .tiff), the attempted objects, and providers APIs you want to run :
```python
payload = {'providers': '[\'google_cloud\', \'cognitives_service\', \'aws\', \'ibm\']'}
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

## FAQ
Here you can access to AI-Compare [FAQ](https://www.ai-compare.com/faq/).

## Use cases
We provides on our website some [use cases examples for Vision APIs](https://www.ai-compare.com/use_cases_vision/)

## Contact
If you have any question or request, you can contact us at contact@ai-compare.com

## Terms of use
You can access to our terms [here](https://www.ai-compare.com/terms/) on our website.

#
![Screenshot](Ai-compare_new.png)
