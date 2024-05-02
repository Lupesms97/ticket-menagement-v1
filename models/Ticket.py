from pydantic import BaseModel


class Ticket(BaseModel):
    id: int
    title: str
    description: str
    status: str

    class Config:
        orm_mode = True
