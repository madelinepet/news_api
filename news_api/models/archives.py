from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
)
from .meta import Base


class Archives(Base):
    __tablename__ = 'archives'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    source = Column(Text)
    date_published = Column(Text)
    url = Column(Text)
    dom_tone = Column(Text)
    image = Column(Text)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    def __init__(self, title=None, description=None, url=None, dom_tone=None):
        self.title = title
        self.description = description
        self.url = url
        self.dom_tone = dom_tone

    @classmethod
    def get_all(cls, request):
        """Method to retrieve archive from database
        """
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).all()