from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True)

    email = Column(String(255), unique=True, nullable=False)

    username = Column(String(100), unique=True, nullable=False)

    password_hash = Column(Text, nullable=False)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True
    )

    user_id = Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False
    )

    bio = Column(Text)

    phone = Column(String(50))
