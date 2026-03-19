import json
from datetime import datetime, timedelta
from typing import Optional, Dict, List
from sqlalchemy import create_engine, Column, String, Text, DateTime, func
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import time
from sqlalchemy.exc import OperationalError
from app.config import DATABASE_URL

# DATABASE SETUP
connect_args = {"check_same_thread": False} if DATABASE_URL and DATABASE_URL.startswith("sqlite") else {"keepalives": 1, "keepalives_idle": 30}
engine = create_engine(DATABASE_URL or "sqlite:///honeypot.db", connect_args=connect_args, pool_pre_ping=True, pool_recycle=300)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class UserSession(Base):
    __tablename__ = "sessions"

    session_id = Column(String, primary_key=True, index=True)
    state_json = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class SessionManager:
    def __init__(self):
        self._init_db()

    def _init_db(self):
        try:
            Base.metadata.create_all(bind=engine)
            print(f"[OK] Database initialized")
        except Exception as e:
            print(f"[ERR] Database init failed: {e}")

    def save_session(self, session_id: str, state: Dict):
        state_json = json.dumps(state, default=str)
        db = SessionLocal()
        try:
            record = db.query(UserSession).filter(UserSession.session_id == session_id).first()
            if record:
                record.state_json = state_json
            else:
                record = UserSession(session_id=session_id, state_json=state_json)
                db.add(record)
            db.commit()
        except:
            db.rollback()
        finally:
            db.close()

    def get_session(self, session_id: str) -> Optional[Dict]:
        db = SessionLocal()
        try:
            record = db.query(UserSession).filter(UserSession.session_id == session_id).first()
            if record:
                return json.loads(record.state_json)
            return None
        finally:
            db.close()

    def get_all_sessions(self) -> List[Dict]:
        db = SessionLocal()
        try:
            records = db.query(UserSession).order_by(UserSession.updated_at.desc()).all()
            return [{"session_id": r.session_id, "updated_at": r.updated_at} for r in records]
        finally:
            db.close()
