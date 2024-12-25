from sqlalchemy import Column, Integer, String, Text
from .database import Base

class MockData(Base):
    __tablename__ = "mock_data"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
