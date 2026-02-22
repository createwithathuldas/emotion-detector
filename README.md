# Emotion Detector

Emotion Detector is a web-based application that analyzes user-provided text and identifies associated emotions using IBM Watson Natural Language Processing (NLP).

## Overview

The application detects the following emotions:

- Anger  
- Disgust  
- Fear  
- Joy  
- Sadness  

It returns emotion scores in structured format and identifies the dominant emotion.

## Technologies Used

- Python  
- Flask  
- IBM Watson NLP  
- unittest  

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/emotion-detector.git
cd emotion-detector

# Install dependencies:

> pip install -r requirements.txt
> # Configuration

> # Set the following environment variables:

> *WATSON_API_KEY*

> *WATSON_URL*

> # Running the Application
> python server.py

> # Access the application at:

> http://localhost:5000
> # Testing
> python -m unittest


# Features
- Emotion detection using IBM Watson NLP

- Dominant emotion identification

- Structured JSON output

- Basic error handling

# License

This project is developed for educational purposes.
