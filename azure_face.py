from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face import FaceClient


def get_face_client():
    """Create an authenticated FaceClient."""
    SUBSCRIPTION_KEY = '88e42e84c2fb40d3a2eb888c6736e1aa'
    ENDPOINT = 'https://fyp-face-recognition.cognitiveservices.azure.com/'
    credential = CognitiveServicesCredentials(SUBSCRIPTION_KEY)
    return FaceClient(ENDPOINT, credential)

if __name__=="__main__":
    face_client = get_face_client()
    
    url = "https://storage.googleapis.com/airport-patrol-robot.appspot.com/MDY4NjAzOTI0MDVGNDM2MTlGMkY4NjJFQTg3M0E1Q.jpg"
    url2 = "https://storage.googleapis.com/airport-patrol-robot.appspot.com/MjNFN0EwM0U4MjRCNEE1MUE1OTg3ODU1RUE4NUY2M.jpg"
    attributes = [] #we don't need them in this case
    include_id = True
    include_landmarks = False
    result1 = face_client.face.detect_with_url(url, include_id, include_landmarks, attributes, raw=True)
    result2 = face_client.face.detect_with_url(url2, include_id, include_landmarks, attributes, raw=True)
    result1 = result1.response.json()[0]
    result2 = result2.response.json()[0]
    test = face_client.face.verify_face_to_face(result1['faceId'], result2['faceId'])
    test.as_dict()

    print(test)
