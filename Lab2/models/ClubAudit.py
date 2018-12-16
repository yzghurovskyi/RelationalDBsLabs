from sqlalchemy import Column, Integer, Table, CHAR, Sequence, TIMESTAMP, Text

from models.Base import Base

clubs_audit = Table('clubs_audit', Base.metadata,
                    Column('audit_id', Integer, Sequence('audit_id_seq'), primary_key=True),
                    Column('operation', CHAR(1), nullable=False),
                    Column('stamp', TIMESTAMP, nullable=False),
                    Column('userid', Text, nullable=False),
                    Column('clubid', Integer, nullable=False))
