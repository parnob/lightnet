from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/rnn', methods=['GET', 'POST'])
def rnn_predict():
    data = request.json
    text_input = data.get('text', '')
    # Here you would call your RNN model to predict based on text_input
    # For demo, just echo the input reversed as “prediction”
    prediction = text_input[::-1]  
    return jsonify({'input': text_input, 'prediction': prediction})

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
