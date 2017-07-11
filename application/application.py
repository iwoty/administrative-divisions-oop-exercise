
from application.menu.menu import *
from application.read_write_csv.csv_read_write import *
from application.user_input.user_input import UserInput
from application.view.view import View
from application.controller.obszar_administracyjny_controller import Obszar_administracyjnyController


class Application:
    """
    Creates Application object.

    Class attributes:
        options: list

    Omstamce attributes:
        is running: bool
        menu: None/Menu obj
        user_input: UserInput obj
        view: View obj
        malopolska_data_file_path: str
    """
    option = ['List statistics',
              'Display 3 cities with the longest names',
              'Display county\'s name with the largest number of communities',
              'Display locations, that belong to more than one category',
              'Advanced search',
              'Exit program']

    def __init__(self):
        """
        Creates application object.
        """
        self.is_running = True
        self.menu = None
        self.user_input = UserInput()
        self.view = View()
        self.malopolska_data_file_path = "application/data/malopolska.csv"

    def handle_menu(self):
        """
        Shows menu.
        """
        self.view.show_menu_option(self.options)
        user_option = self.user_input.get_option(self.options)
        if user_option == 'List statistics':
            pass
        elif user_option == 'Display 3 cities with the longest names':
            pass
        elif user_option == 'Display county\'s name with the largest number of communities':
            pass
        elif user_option == 'Display locations, that belong to more than one category':
            pass
        elif user_option == 'Advanced search':
            pass
        elif user_option == 'Exit program':
            self.is_running = False
            return

    def run(self):
        """
        Entry method for the main module which read csv file at the beginning.
        """
        read_obszary_administracyjne_from_csv(self.malopolska_data_file_path)

        while self.is_running:
            self.handle_menu()
