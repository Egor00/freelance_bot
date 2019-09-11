from sqlalchemy import Column, Boolean, Integer, DateTime, String, Text, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

base = declarative_base()


user_par_table = Table('user_par', base.metadata,
                       Column('user_id', Integer, ForeignKey('users.id')),
                       Column('par_id', Integer, ForeignKey('parameters.id'))
                       )


offer_par_table = Table('offer_par', base.metadata,
                        Column('offer_id', Integer, ForeignKey('offers.id')),
                        Column('par_id', Integer, ForeignKey('parameters.id'))
                        )


class User(base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    subscribed = Column(Boolean, default=True, nullable=False)
    last_post_date = Column(DateTime)
    sub_pars = relationship('Parameter', secondary=user_par_table, backref='users', collection_class=set)

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(id)

    def __repr__(self):
        return '<%s(id=%s, subscribed=%s, last_post_date=%s, sub_pars=%s)>' % (self.__class__.__name__, self.id,
                                                                               self.subscribed, self.last_post_date,
                                                                               self.sub_pars)


class Offer(base):
    __tablename__ = 'offers'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    link = Column(String, unique=True, nullable=False)
    datetime = Column(DateTime, nullable=False)
    pars = relationship('Parameter', secondary=offer_par_table, backref='offers', collection_class=set)


class Parameter(base):
    __tablename__ = 'parameters'

    id = Column(Integer, primary_key=True)
    par = Column(String, nullable=False)

    def __eq__(self, other):
        return self.par == other.par

    def __hash__(self):
        return hash(self.par)

    def __repr__(self):
        return '<%s(id=%s, par=%s)>' % (self.__class__.__name__, self.id, self.par)

