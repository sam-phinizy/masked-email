import os
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from masked_email.core import generate_masked_email
import enum

app = FastAPI()

security = HTTPBasic()

USERNAME = os.environ["ME_SERVER_USERNAME"]
PASSWORD = os.environ["ME_SERVER_PASSWORD"]
JMAP_HOST = os.environ["JMAP_HOST"]
JMAP_API_KEY = os.environ["JMAP_API_KEY"]

class FormatTypes(str, enum.Enum):
    json = "json"
    text = "text"

@app.get("/masked-email")
def get_masked_email(credentials: Annotated[HTTPBasicCredentials, Depends(security)],format: FormatTypes = FormatTypes.json):
    if format == FormatTypes.text:
        return generate_masked_email(None, None, JMAP_API_KEY, JMAP_HOST, None)
    else:
        return {"masked-email": generate_masked_email(None, None, JMAP_API_KEY, JMAP_HOST, None)}
