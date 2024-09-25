from sqlalchemy.orm import Session
from app.database import engine, Base, User, SessionLocal
import bcrypt

def hash_password(password: str):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def init():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if not db.query(User).filter(User.username == "user").first():
        user = User(
            username="user",
            role="user",
            password=hash_password("L0XuwPOdS5U")
        )
        db.add(user)

    if not db.query(User).filter(User.username == "admin").first():
        admin = User(
            username="admin",
            role="admin",
            password=hash_password("JKSipm0YH")
        )
        db.add(admin)

    db.commit()
    db.close()

if __name__ == "__main__":
    init()
