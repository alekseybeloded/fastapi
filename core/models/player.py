from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.base import Base
from core.models.mixins import BaseFieldsMixin

if TYPE_CHECKING:
    from core.models.injury import Injury
    from core.models.team import Team


class Player(BaseFieldsMixin, Base):

    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))

    team: Mapped["Team"] = relationship(back_populates="players")
    injury: Mapped["Injury"] = relationship(back_populates="player")
