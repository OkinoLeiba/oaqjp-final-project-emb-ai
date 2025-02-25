import requests, json

# URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyse } }

def emotion_detector(text_to_analyse):
    while True:
        try:
            url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

            myobj = { "raw_document": { "text": text_to_analyse } }

            header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

            response = requests.post(url, json=myobj, headers=header, timeout=5)
            
            e_response = json.loads(response.text)

            stop_condition = False

            if response.status_code == 200:
                if e_response is not None:
                    e_score_raw = {
                        'anger': e_response['emotionPredictions'][0]['emotion']['anger'],
                        'disgust': e_response['emotionPredictions'][0]['emotion']['disgust'],
                        'fear': e_response['emotionPredictions'][0]['emotion']['fear'],
                        'joy': e_response['emotionPredictions'][0]['emotion']['joy'],
                        'sadness': e_response['emotionPredictions'][0]['emotion']['sadness'],
                    }

                    e_max = max(e_score_raw, key=e_score_raw.get)

                    e_score = {
                        'anger': e_response['emotionPredictions'][0]['emotion']['anger'],
                        'disgust': e_response['emotionPredictions'][0]['emotion']['disgust'],
                        'fear': e_response['emotionPredictions'][0]['emotion']['fear'],
                        'joy': e_response['emotionPredictions'][0]['emotion']['joy'],
                        'sadness': e_response['emotionPredictions'][0]['emotion']['sadness'],
                        'dominant_emotion': e_max
                    }
                else:
                    e_score = {
                        'anger': None,
                        'disgust': None,
                        'fear': None,
                        'joy': None,
                        'sadness': None,
                        'dominant_emotion': None
                    }
                return e_score
            elif response.status_code == 400 or response.status_code == 500:
                e_score = {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
                }
            else:
                print("Response Object is Empty")
        # response.raise_for_status()
        except requests.exceptions.ConnectionError as cerr:
            print("Connection Error: \n")
            print(cerr)
        except requests.exceptions.Timeout as terr:
            print("Timeout Error: \n")
            print(terr)
        except requests.exceptions.TooManyRedirects as tmerr:
            print("Too Many Redirect Error: \n")
            print(tmerr)
        except requests.exceptions.HTTPError as herr:
            print("HTTP Error: \n")
            print(herr)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        if not text_to_analyse.strip():
            break
               
    return e_score

# if __name__ == '__main__'
#     emotion_detector('I love spam.')