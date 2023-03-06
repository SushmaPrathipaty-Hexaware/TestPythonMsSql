from sqlalchemy import Boolean, Column, Float, Integer, String
from db.base import Base


class Pythonmssql(Base):
    __tablename__ = "pythonmssql"
    id = Column(Integer, primary_key=True)
    
    name = Column(String(50), nullable=False)