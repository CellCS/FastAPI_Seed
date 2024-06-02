from pydantic import BaseModel

tags_metadata = [
    {
        "name": "user",
        "description": "Operations related to user management."
    },
    {
        "name": "Ollama",
        "description": "Operations related to Ollama management."
    }
]

class ConnectionTestResponse(BaseModel):
    Message: str