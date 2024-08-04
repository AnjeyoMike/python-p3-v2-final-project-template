from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, engine

class Topic(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    quizzes = relationship('Quiz', back_populates='topic', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Topic(name={self.name})>"

class Quiz(Base):
    __tablename__ = 'quizzes'
    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    options = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    topic_id = Column(Integer, ForeignKey('topics.id'), nullable=False)
    topic = relationship('Topic', back_populates='quizzes')

    def __repr__(self):
        return f"<Quiz(question={self.question}, topic={self.topic.name})>"

Base.metadata.create_all(engine)
