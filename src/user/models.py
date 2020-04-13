from django.db import models
from custom_user.models import AbstractEmailUser

from utils.models import BaseCustomModel


class User(AbstractEmailUser, BaseCustomModel):
    pass
