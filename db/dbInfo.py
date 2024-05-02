from models.Ticket import Ticket


def get_tickets():
    tickets = []
    for i in range(1, 6):
        ticket = Ticket(id=i, title=f"Ticket {i}", description=f"Description {i}", status="Open")
        tickets.append(ticket)
    return tickets
