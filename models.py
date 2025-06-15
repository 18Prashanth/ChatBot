from pydantic import BaseModel



class chatrequest(BaseModel):
    message:str

class chatresponse(BaseModel):
    reply:str