
import csv
from application.model.obszar_administracyjny import *


class Program:

    @staticmethod
    def read_obszary_administracyjne_from_csv(file_name):
        """
        Create models and fill class lists with data from csv files at the begining of program

        Raises *FileNotFoundError* if a file doesn't exist.

        Every item is written to a separate line in the following format:
        `woj	pow	gmi	rgmi	nazwa	typ`

        Args:
            file_name (str): name of the file or path to the file
        """
        try:
            obszar_classes = {'województwo': Wojewodztwo,
                              'powiat': Powiat,
                              'gmina miejska': Gmina_miejska,
                              'gmina wiejska': Gmina_wiejska,
                              'gmina miejsko-wiejska': Gmina_miejsko_wiejska,
                              'obszar wiejski': Obszar_wiejski,
                              'miasto': Miasto,
                              'miasto na prawach powiatu': Miasto_na_prawach_powiatu,
                              'delegatura': Delegatura}

            with open(file_name) as source:
                obszary_csv_list = csv.DictReader(source)

                for obszar in obszary_csv_list:
                    for key in obszar:
                        name = obszar[key].split('\t')[4].strip()
                        obszar_kind = obszar[key].split('\t')[5].strip()

                        new_obszar = obszar_classes[obszar_kind](name)

                        if type(new_obszar) is Wojewodztwo:
                            new_obszar.add_to_wojewodztwa()
                        elif type(new_obszar) is Powiat:
                            new_obszar.add_to_powiaty()
                        elif type(new_obszar) is Gmina_miejska:
                            new_obszar.add_to_gminy_miejskie()

                            # obszar[key].split('\t')[3].strip()

                            # Powiat.add_to_communities_list(powiat_name, community)

                        elif type(new_obszar) is Gmina_wiejska:
                            new_obszar.add_to_gminy_wiejskie()

                        elif type(new_obszar) is Gmina_miejsko_wiejska:
                            new_obszar.add_to_gminy_miejsko_wiejskie()

                        elif type(new_obszar) is Obszar_wiejski:
                            new_obszar.add_to_obszary_wiejskie()

                        elif type(new_obszar) is Miasto:
                            new_obszar.add_to_miasta()

                        elif type(new_obszar) is Miasto_na_prawach_powiatu:
                            new_obszar.add_to_miasta_na_prawach_powiatu()
                        elif type(new_obszar) is Delegatura:
                            new_obszar.add_to_delegatury()
            #
            # print(POWIAT.get_communities_list())

        except FileNotFoundError:
            raise FileNotFoundError('File ' + file_name + ' doesn\'t exist')
