from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    filename = Column(String, unique=True, nullable=False)
    sections = relationship("Section", back_populates="document")

class Section(Base):
    __tablename__ = "sections"
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    heading = Column(String)
    content = Column(Text)
    summary = Column(Text)
    document = relationship("Document", back_populates="sections")
