


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RNNInput(BaseModel):
    text: str = ""

@app.post("/rnn")
async def rnn_predict(data: RNNInput):
    text_input = data.text
    prediction = text_input[::-1]
    return {"input": text_input, "prediction": prediction}


#from flask import Flask, jsonify, request

#app = Flask(__name__)

#@app.route('/')
#def home():
#    return "✅ Flask API is working!"


#@app.route('/rnn', methods=['POST'])
#def rnn_predict():
#    data = request.json
#    text_input = data.get('text', '')
    # Here you would call your RNN model to predict based on text_input
    # For demo, just echo the input reversed as “prediction”
#    prediction = text_input[::-1]  
#    return jsonify({'input': text_input, 'prediction': prediction})

#if __name__ == '__main__':
#    import os
#    port = int(os.environ.get("PORT", 10000))
#    app.run(host='0.0.0.0', port=port)
