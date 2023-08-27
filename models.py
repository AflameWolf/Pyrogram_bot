from sqlalchemy import Column, Integer, String, Table, ForeignKey


from DB import Base


class clients(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    chat_id = Column(String)
    date = Column(String)

    def __repr__(self):
        return f"{self.id},id чата:{self.chat_id},дата создания {self.date}"