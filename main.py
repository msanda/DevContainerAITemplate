from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

app = FastAPI()

class Paragraph(BaseModel):
    text: str

@app.post("/analyze/")
async def analyze_readability(paragraph: Paragraph):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Choose your model here
            messages=[
                {"role": "user", "content": f"Analyze the following paragraph for readability:\n\n{paragraph.text}"}
            ]
        )
        analysis = response.choices[0].message.content
        return {"analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)