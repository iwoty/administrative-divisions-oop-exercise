
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
        statistics = [[str(len(Wojewodztwo.get_wojewodztwa())), 'województw'],
                      [str(len(Powiat.get_powiaty())+len(Miasto_na_prawach_powiatu.get_miasta_na_prawach_powiatu())), 'powiatów'],
                      [str(len(Gmina_miejska.get_gminy_miejskie())), 'gmin miejskich'],
                      [str(len(Gmina_wiejska.get_gminy_wiejskie())), 'gmin wiejskich'],
                      [str(len(Gmina_miejsko_wiejska.get_gminy_miejsko_wiejskie())), 'gmin miejsko-wiejskich'],
                      [str(len(Obszar_wiejski.get_obszary_wiejskie())), 'obszarów wiejskich'],
                      [str(len(Miasto.get_miasta())), 'miast'],
                      [str(len(Miasto_na_prawach_powiatu.get_miasta_na_prawach_powiatu())), 'miast na prawach powiatu'],
                      [str(len(Delegatura.get_delegatury())), 'delegatur']]

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

        input('Enter anykey ')

    def cities_longest_names(self):
        cities_names = []
        for miasto in Miasto.get_miasta():
            cities_names.append(miasto.name)
        cities_names.sort(key=len, reverse=True)
        for i in range(0, 3):
            print(cities_names[i])
        input('Enter anykey ')
