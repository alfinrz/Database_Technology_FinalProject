from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select


engine = create_engine("sqlite:///Something.sqlite", echo=True, future=True)

Base = declarative_base()

class User(Base):
    __tablename__ = "Customer"
    id = Column(Integer, primary_key=True)
    order = Column(Integer)
    fullname = Column(String)

    addresses = relationship(
    "Address", back_populates="user", cascade="all, delete-orphan"
    )  


class Orders(Base):
    __tablename__ = "Ticket_order"

    Ticketid = Column(Integer, primary_key = True)
    Order_id = Column(Integer, ForeignKey("Customer.order"), nullable = False)
    EventName = Column(String, nullable=False)
    EventStart = Column(DateTime)
    EventEnd = Column (DateTime)
    VenueLocation = Column(String)
    TicketPrice = Column (Integer)
    TicketsOrdered = Column(Integer)
    OrderDate = Column (DateTime)
    TotalPrice = Column(Integer)

    user = relationship("User", back_populates="addresses")


class Event(Base):
    __tablename__ = "Events"

    EventId = Column (Integer, primary_key = True)
    EventName = Column (String, ForeignKey("Ticket_order.EventName"), nullable = False)
    OrganizerId = Column (Integer)
    EventStart = Column (DateTime)
    EventEnd = Column (DateTime)
    Venues = Column (String)
    TotalCapacity = Column (Integer)
    TotalSales =Column (Integer)

class Organize(Base):
    __tablename__ = 'Organizer'

    id = Column(Integer, ForeignKey("Events.OrganizerId"), primary_key = True, nullable = False)
    Name = Column(String)

class Venues(Base):
    __tablename__ = 'Venue'

    VenueId = Column(Integer, ForeignKey("Events.Venues"), primary_key = True, nullable = False)
    Location = Column(String)
    MaxCapacity = Column(Integer)

Base.metadata.create_all(engine)

# with Session(engine) as session:

#     spongebob = User(
#         name="spongebob",
#         fullname="Spongebob Squarepants",
#         addresses=[Address(email_address="spongebob@sqlalchemy.org")],
#         )
#     sandy = User(
#         name="sandy",
#         fullname="Sandy Cheeks",
#         addresses=[
#             Address(email_address="sandy@sqlalchemy.org"),
#             Address(email_address="sandy@squirrelpower.org"),
#          ],
#     )
#     patrick = User(name="patrick", fullname="Patrick Star")

#     session.add_all([spongebob, sandy, patrick])

#     session.commit()

# session = Session(engine) 

# stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

# for user in session.scalars(stmt):
#     print(user)

# stmt = (
#     select(Address)
#     .join(Address.user)
#     .where(User.name == "sandy")
#     .where(Address.email_address == "sandy@sqlalchemy.org") 
#     )
# sandy_address = session.scalars(stmt).one()

# sandy_address

# stmt = select(User).where(User.name == "patrick")
# patrick = session.scalars(stmt).one()
# patrick.addresses.append(Address(email_address="patrickstar@sqlalchemy.org"))

# sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"
# session.commit()

# sandy = session.get(User, 2)
# sandy.addresses.remove(sandy_address)

# session.flush()

# session.delete(patrick)

# session.commit()