from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import UserRelationMixin


class Post(UserRelationMixin, Base):

    _user_id_unique = False
    _user_id_nullable = False
    _user_back_populates = "posts"

    # @todo что такое Mapped и mapped_column
    title: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )

    # user_id: Mapped[int] = mapped_column(
    #     ForeignKey("users.id"),
    # )
    #
    # user: Mapped['User'] = relationship(back_populates='posts')
    # @todo зачем нужна эта связь? Почему недостаточно связи через user_id
