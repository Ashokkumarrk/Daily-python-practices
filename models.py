from sqlalchemy import column, Integer, String
from database import Base

class Note(Base):
    __tablename__ = "notes"

    id = column(Integer, Primary_key=True, index=True)
    title = column(String, index=True)
    content = column(String)
    
