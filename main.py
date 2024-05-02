from fastapi import FastAPI
from db.dbInfo import get_tickets

app = FastAPI()


@app.get("/")
def read_root():
    tickets = get_tickets()
    return tickets


# , q: Union[str, None] = None
@app.get("/items/{ticket_id}")
def read_item(ticket_id: int):
    tickets = get_tickets()
    for ticket in tickets:
        if ticket.id == ticket_id:
            return ticket
    return {"message": "Ticket not found"}