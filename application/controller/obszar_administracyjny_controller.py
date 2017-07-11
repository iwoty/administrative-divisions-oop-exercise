
from application.model.obszar_administracyjny import Obszar_administracyjny


class Obszar_administracyjnyController:
    """
    Represent Obszar_administracyjnyController objects.

    Instance Attributes:
        view: object of view class
        input: object of input class
    """
    def __init__(self, user_input, view):
        self.user_input = user_input
        self.view = view
