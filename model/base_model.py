from sqlalchemy import DateTime, Numeric

from config.db_exts import db
from utils.time_util import format_datetime


class BaseModel(db.Model):
    __abstract__ = True

    def model_to_dict(self, show=None):

        hidden = self._hidden_fields if hasattr(self, "_hidden_fields") else []

        columns = self.__table__.columns

        if show is None:
            show = self._default_fields if hasattr(self, "_default_fields") else columns.keys

        for col in columns:
            if col.name.startswith("_"):
                continue
            if col.name in hidden:
                continue
            if col.name in show:
                if isinstance(col.type, DateTime):
                    value = format_datetime(getattr(self, col.name))
                elif isinstance(col.type, Numeric):
                    value = float(getattr(self, col.name))
                else:
                    value = getattr(self, col.name)
                yield (col.name, value)
