from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Allow CORS for all origins (for demonstration purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to your frontend's origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Message model
class Message(BaseModel):
    username: str
    content: str

# Store connected clients and messages
connected_clients: List[WebSocket] = []
messages: List[Message] = []

@app.post("/send-message/")
async def send_message(message: Message):
    # Store the message
    messages.append(message)
    # Notify all connected clients
    for client in connected_clients:
        await client.send_text(f"{message.username}: {message.content}")
    return {"status": "Message sent"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()  # Receive message from client
            # Broadcast the message to all clients
            for client in connected_clients:
                if client != websocket:
                    await client.send_text(data)
    except WebSocketDisconnect:
        connected_clients.remove(websocket)  # Remove the client on disconnect

@app.get("/messages/", response_model=List[Message])
async def get_messages():
    return messages  # Return the list of messages

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
