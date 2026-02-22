import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion(self):
        response = emotion_detector("I am very happy today")
        self.assertIn("dominant emotion", response.lower())

if __name__ == "__main__":
    unittest.main()