from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    framework = Column(String(50), default="react-fastapi")
    frontend_code = Column(Text, default="")
    backend_code = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", backref="projects")
