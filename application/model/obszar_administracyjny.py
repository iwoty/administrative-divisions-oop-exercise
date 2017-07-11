
class Obszar_administracyjny:
    """
    Parent class for classes:
        Wojewodztwo,
        Powiat,
        Gmina_miejska,
        Gmina_wiejska,
        Gmina_miejsko_wiejska,
        Obszar_wiejski,
        Miasto,
        Miasto_na_prawach_powiatu,
        Delegatura.

    Attributes:
        name (str): instance attribute storing name of 'obszar administracyjny'
    """

    def __init__(self, name):
        """
        Create Obszar_administracyjny object.

        Parameters:
            name (str)
        """
        self.name = name

    def get_name(self):
        """
        Returns name of instance.

        Returns:
            name (str): name of obszar administracyjny
        """
        return self.name


class Wojewodztwo(Obszar_administracyjny):
    """
    Obszar_administracyjny child class.

    Class attributes:
        wojewodztwa_list (list of :obj: 'Wojewodztwo'): list of Wojewodztwo objects
    """
    wojewodztwa_list = []

    def add_to_wojewodztwa(self):
        """
        Adds Wojewodztwo to wojewodzwa list.
        """
        self.wojewodztwa_list.append(self)

    @classmethod
    def get_wojewodztwa(cls):
        """
        Returns wojewodztwa list (class attribute).

        Returns:
            wojewodztwa_list (list of :obj: 'Wojewodztwo'): list of Wojewodztwo objects
        """
        return cls.wojewodztwa_list


class Powiat(Obszar_administracyjny):
    """
    Obszar_administracyjny child class.

    Class attributes:
        powiaty_list (list of :obj: 'Powiat'): list of Powiat objects
    """
    powiaty_list = []

    def add_to_powiaty(self):
        """
        Adds Powiat to powiaty list.
        """
        self.powiaty_list.append(self)

    @classmethod
    def get_powiaty(cls):
        """
        Returns powiaty list (class attribute).

        Returns:
            powiaty_list (list of :obj: 'Powiat'): list of Powiat objects
        """
        return cls.powiaty_list


class Gmina_miejska(Obszar_administracyjny):
    """
    Obszar_administracyjny child class.

    Class attributes:
        gminy_miejskie_list (list of :obj: 'Gmina_miejska'): list of Gmina_miejska objects
    """
    gminy_miejskie_list = []

    def add_to_gminy_miejskie(self):
        """
        Adds Gmina_miejska to gminy miejskie list.
        """
        self.gminy_miejskie_list.append(self)

    @classmethod
    def get_gminy_miejskie(cls):
        """
        Returns gminy miejskie list (class attribute).

        Returns:
            gminy_miejskie_list (list of :obj: 'Gmina_miejska'): list of Gmina_miejska objects
        """
        return cls.gminy_miejskie_list


class Gmina_wiejska(Obszar_administracyjny):
    """
    Obszar_administracyjny child class.

    Class attributes:
        gminy_wiejskie_list (list of :obj: 'Gmina_wiejska'): list of Gmina_wiejska objects
    """
    gminy_wiejskie_list = []

    def add_to_gminy_wiejskie(self):
        """
        Adds Gmina_wejska to gminy wiejskie list.
        """
        self.gminy_wiejskie_list.append(self)

    @classmethod
    def get_gminy_wiejskie(cls):
        """
        Returns gminy wiejskie list (class attribute).

        Returns:
            gminy_wiejskie_list (list of :obj: 'Gmina_wiejska'): list of Gmina_wiejska objects
        """
        return cls.gminy_wiejskie_list


class Gmina_miejsko_wiejska(Obszar_administracyjny):
    """
    Obszar_administracyjny child class.

    Class attributes:
        gminy_miejsko_wiejskie_list (list of :obj: 'Gmina_miejsko_wiejska'): list of Gmina_miejsko_wiejska objects
    """
    gminy_miejsko_wiejskie_list = []

    def add_to_gminy_miejsko_wiejskie(self):
        """
        Adds Gmina_miejsko_wiejska to gminy miejsko wiejskie list.
        """
        self.gminy_miejsko_wiejskie_list.append(self)

    @classmethod
    def get_gminy_miejsko_wiejskie(cls):
        """
        Returns gminy miejsko wiejskie list (class attribute).

        Returns:
            gminy_miejsko_wiejskie_list (list of :obj: 'get_gminy_miejsko_wiejskie'):
                                                                            list of Gmina_miejsko_wiejska objects
        """
        return cls.gminy_miejsko_wiejskie_list


class Obszar_wiejski(Obszar_administracyjny):
    """
    Obszar_administracyjny child class.

    Class attributes:
        obszar_wiejski_list (list of :obj: 'Obszar_wiejski'): list of Obszar_wiejski objects
    """
    obszary_wiejskie_list = []

    def add_to_obszary_wiejskie(self):
        """
        Adds Obszar_wiejski to obszary wiejskie list.
        """
        self.obszary_wiejskie_list.append(self)

    @classmethod
    def get_obszary_wiejskie(cls):
        """
        Returns obszary wiejskie list (class attribute).

        Returns:
            obszary_wiejskie_list (list of :obj: 'Obszar_wiejski'): list of Obszar_wiejski objects
        """
        return cls.obszary_wiejskie_list


class Miasto(Obszar_administracyjny):
    """
    Obszar_administracyjny child class.

    Class attributes:
        maista_list (list of :obj: 'Miasto'): list of Miasto objects
    """
    miasta_list = []

    def add_to_miasta(self):
        """
        Adds Miasto to miasta list.
        """
        self.miasta_list.append(self)

    @classmethod
    def get_miasta(cls):
        """
        Returns miasta list (class attribute).

        Returns:
            miasta_list (list of :obj: 'Miasto'): list of Miasto objects
        """
        return cls.miasta_list


class Miasto_na_prawach_powiatu(Obszar_administracyjny):
    """
    Obszar_administracyjny child class.

    Class attributes:
        miasta_na_prawach_powiatu_list (list of :obj: 'Miasto_na_prawach_powiatu'):
                                                            list of Miasto_na_prawach_powiatu objects
    """
    miasta_na_prawach_powiatu_list = []

    def add_to_miasta_na_prawach_powiatu(self):
        """
        Adds Miasto_na_prawach_powiatu to miasta na prawach powiatu list.
        """
        self.miasta_na_prawach_powiatu_list.append(self)

    @classmethod
    def get_miasta_na_prawach_powiatu(cls):
        """
        Returns miasta na prawach powiatu list (class attribute).

        Returns:
            miasta_na_prawach_powiatu_list (list of :obj: 'Miasto_na_prawach_powiatu'):
                                                            list of Miasto_na_prawach_powiatu objects
        """
        return cls.miasta_na_prawach_powiatu_list


class Delegatura(Obszar_administracyjny):
    """
    Obszar_administracyjny child class.

    Class attributes:
        delegatury_list (list of :obj: 'Delegatura'): list of Delegatura objects
    """
    delegatury_list = []

    def add_to_delegatury(self):
        """
        Adds Delegatura to delegatury list.
        """
        self.delegatury_list.append(self)

    @classmethod
    def get_delegatury(cls):
        """
        Returns delegatury list (class attribute).

        Returns:
            delegatury_list (list of :obj: 'Delegatura'): list of Delegatura objects
        """
        return cls.delegatury_list
