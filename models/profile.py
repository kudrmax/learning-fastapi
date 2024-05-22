from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from .base import Base

if TYPE_CHECKING:
    from .post import Post


class Profile(Base):
    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))
    bio: Mapped[str | None]

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), unique=True)