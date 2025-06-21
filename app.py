


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

