from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .tamu import Tamu
from .kamar import Kamar
from .reservasi import Reservasi