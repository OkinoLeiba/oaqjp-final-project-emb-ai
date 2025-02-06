
from flask import Flask, render_template, request
from emotion.emotion_detection import emotion_detector


app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def sent_detector():
       
    text_to_analyze = request.args.get('textToAnalyze')
    
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] == None:
        print('Invalid text! Please try again!.')
    else:
        return response

  
    return response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
