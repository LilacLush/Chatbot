import requests
import json

def get_prediction(data={"sentence":"I am so sad to see you go. "}):
  url = 'https://askai.aiclub.world/2992066b-a20f-4d2d-b841-bef4c25bc7c5'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  #print(response)
  return response

ask_your_ai = {"sentence": "I am not happy"}

prediction = get_prediction(ask_your_ai)
#print(prediction)
#print(type(prediction))
prediction_dict = json.loads(prediction)
#print(type(prediction_dict))
prediction_body = prediction_dict['body']
#print(prediction_body)
#print(type(prediction_body))
prediction_body_dict = json.loads(prediction_body)
#print(type(prediction_body_dict))
predicted_label = prediction_body_dict['predicted_label']
print(predicted_label)