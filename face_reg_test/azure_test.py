from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face import FaceClient
import os
import glob
from itertools import permutations, combinations
import pandas as pd
import tqdm
import time
dirname = os.path.dirname(__file__)


def get_face_client():
    """Create an authenticated FaceClient."""
    SUBSCRIPTION_KEY = '88e42e84c2fb40d3a2eb888c6736e1aa'
    ENDPOINT = 'https://fyp-face-recognition.cognitiveservices.azure.com/'
    credential = CognitiveServicesCredentials(SUBSCRIPTION_KEY)
    return FaceClient(ENDPOINT, credential)

def compare_image(client, fid1, fid2):
    try:
        time.sleep(4)
        test = client.face.verify_face_to_face(fid1, fid2)
        test = test.as_dict()

        return test["confidence"]
    except: 
        return -1 


if __name__=="__main__":
    face_client = get_face_client()

    pattern = os.path.join(dirname, "face_data/*.jpeg")
    test_images = [file for file in glob.glob(pattern)][:6]

    face_id_list = []

    for i in tqdm.tqdm(range(len(test_images))):
        attributes = [] 
        include_id = True
        include_landmarks = False

        img_obj = open(test_images[i], 'rb') 
        try: 
            result = face_client.face.detect_with_stream(img_obj, include_id, include_landmarks, attributes, raw=True)
            result = result.response.json()[0]['faceId']
            face_id_list.append(result)
            time.sleep(4)
        except: 
            face_id_list.append(None)

    all_combination = list(combinations(list(range(0, len(test_images))), 2))

    result_list = []

    for combination in tqdm.tqdm(all_combination): 
        identity1 = test_images[combination[0]].split('/')[-1]
        identity2 = test_images[combination[1]].split('/')[-1]

        if face_id_list[combination[0]] is None: 
            result = {"identity1": identity1, "identity2": identity2, "score": -1}


        elif face_id_list[combination[1]] is None: 
            result = {"identity1": identity1, "identity2": identity2, "score": -1}
        
        else: 
            conf = compare_image(face_client, face_id_list[combination[0]], face_id_list[combination[1]])

            result = {"identity1": identity1, "identity2": identity2, "score": conf}

        result_list.append(result)

    df = pd.DataFrame(result_list).to_csv("result.csv")


