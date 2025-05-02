from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    book_name: Mapped[str] = mapped_column(unique=True)
    author_name: Mapped[str] = mapped_column(unique=True)
    