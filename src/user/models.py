"""
User app related models.
"""
from custom_user.models import AbstractEmailUser

from utils.models import BaseCustomModel


class User(AbstractEmailUser, BaseCustomModel):
    """
    User auth model.
    """
    pass
