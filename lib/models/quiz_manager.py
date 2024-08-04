from sqlalchemy.orm import Session
from models import Topic, Quiz
from database import SessionLocal

class QuizManager:
    def __init__(self):
        self.db = SessionLocal()

    def create_topic(self, name):
        topic = Topic(name=name)
        self.db.add(topic)
        self.db.commit()
        self.db.refresh(topic)
        return topic

    def delete_topic(self, topic_id):
        topic = self.db.query(Topic).filter(Topic.id == topic_id).first()
        self.db.delete(topic)
        self.db.commit()

    def get_all_topics(self):
        return self.db.query(Topic).all()

    def find_topic_by_id(self, topic_id):
        return self.db.query(Topic).filter(Topic.id == topic_id).first()

    def create_quiz(self, question, options, answer, topic_id):
        quiz = Quiz(question=question, options=options, answer=answer, topic_id=topic_id)
        self.db.add(quiz)
        self.db.commit()
        self.db.refresh(quiz)
        return quiz

    def delete_quiz(self, quiz_id):
        quiz = self.db.query(Quiz).filter(Quiz.id == quiz_id).first()
        self.db.delete(quiz)
        self.db.commit()

    def get_all_quizzes(self):
        return self.db.query(Quiz).all()

    def find_quiz_by_id(self, quiz_id):
        return self.db.query(Quiz).filter(Quiz.id == quiz_id).first()

    def get_quizzes_by_topic(self, topic_id):
        return self.db.query(Quiz).filter(Quiz.topic_id == topic_id).all()
