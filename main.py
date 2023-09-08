from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Secrets(BaseModel):
    username: str
    message: str
    is_valid: Union[bool, None] = None

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/secrets/{secret_key}")
async def read_secrets(secret_key: int, valid: Union[str, None] = None):
    return {"secret_key": secret_key, "valid": valid}

@app.put("/secrets/{secret_key}")
def update_secrets(secret_key: int, secrets: Secrets):
    return {"secrets_username":secrets.username, "secret_key": secret_key}
