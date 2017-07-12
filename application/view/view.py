
import os
from application.model.obszar_administracyjny import *


class View:
    """
    Creates View obj.
    """
    def show_menu_option(self, options):
        """
        Prints menu options.
        Parameters:
        options: list
        """
        os.system('clear')
        print('What would you like to do:')
        for index, option in enumerate(options):
            print("({}) {}".format(index + 1, option))

    def list_statistics(self):
        """
        Prints main statistics about administration zones.
        """
        number_of_wojewodztwa = len(Wojewodztwo.get_wojewodztwa())
        number_of_miasto_na_prawach_powiatu = len(Miasto_na_prawach_powiatu.get_miasta_na_prawach_powiatu())
        number_of_powiaty = len(Powiat.get_powiaty()) + number_of_miasto_na_prawach_powiatu
        number_of_gmina_miejska = len(Gmina_miejska.get_gminy_miejskie())
        number_of_gmina_wiejska = len(Gmina_wiejska.get_gminy_wiejskie())
        number_of_gmina_miejsko_wiejska = len(Gmina_miejsko_wiejska.get_gminy_miejsko_wiejskie())
        number_of_obszar_wiejski = len(Obszar_wiejski.get_obszary_wiejskie())
        number_of_miasto = len(Miasto.get_miasta())
        number_of_delegatura = len(Delegatura.get_delegatury())

        statistics = [[str(number_of_wojewodztwa), 'województw'],
                      [str(number_of_powiaty), 'powiatów'],
                      [str(number_of_gmina_miejska), 'gmin miejskich'],
                      [str(number_of_gmina_wiejska), 'gmin wiejskich'],
                      [str(number_of_gmina_miejsko_wiejska), 'gmin miejsko-wiejskich'],
                      [str(number_of_obszar_wiejski), 'obszarów wiejskich'],
                      [str(number_of_miasto), 'miast'],
                      [str(number_of_miasto_na_prawach_powiatu), 'miast na prawach powiatu'],
                      [str(number_of_delegatura), 'delegatur']]

        COLUMN1_WIDTH = 5
        COLUMN2_WIDTH = 26
        TABLE_WIDTH = COLUMN1_WIDTH + COLUMN2_WIDTH + 1     # 1 because of 'pipe' between columns
        LINE = '|' + COLUMN1_WIDTH*'-' + '+' + COLUMN2_WIDTH*'-' + '|'

        print(LINE)
        print('|' + '{}'.format('MALOPOLSKIE').center(TABLE_WIDTH) + '|')
        print(LINE)

        for stat in statistics:
            print('|' + '{}'.format(stat[0]).center(COLUMN1_WIDTH) + '|' + '{}'.format(stat[1]).center(COLUMN2_WIDTH) + '|')
            print(LINE)

    def cities_longest_names(self):
        cities_names = []
        for miasto in Miasto.get_miasta():
            cities_names.append(miasto.name)
        cities_names.sort(key=len, reverse=True)
        for i in range(0, 3):
            print(cities_names[i])
