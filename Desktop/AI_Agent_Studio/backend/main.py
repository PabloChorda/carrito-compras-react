# main.py (FastAPI)
from fastapi import FastAPI, WebSocket
from agents.real_estate_agent import RealEstateAgent

app = FastAPI()
agent = RealEstateAgent()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        user_input = await websocket.receive_text()
        response = agent.process_message(user_input)
        await websocket.send_text(response)