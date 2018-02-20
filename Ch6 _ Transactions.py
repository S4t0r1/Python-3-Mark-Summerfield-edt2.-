
USE_GETATTR = False


class Transaction(object):
    
    def __init__(self, amount, date, currency="Euro", 
             eur_conversion_rate=1, description=None)
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__eur_conversion_rate = eur_conversion_rate
        self.__description = description
        
        #self.__dict__.update({k: v for k,v in locals().items() if k != "self"})#
    
    
    if USE_GETATTR:
        def __getattr__(self, name):
            if name in frozenset({"amount", "date", "currency", 
                        "eur_conversion_rate", "description"}):
                return self.__dict__["_{classname}__{name}".format(**locals())]
            else:
                raise AttributeError("'{classname}' object has no "
                    "attribute '{name}'".format(**locals()))
    else:
        @property
        def amount(self):
            return self.__amount
        
        @property
        def date(self):
            return self.__date
        
        @property
        def currency(self):
            return self.__currency
        
        @property
        def eur_conversion_rate(self):
            return self.__eur_conversion_rate
        
        @property
        def description(self):
            return self.__description
        
        @property
        def eur(self):
            return self.__amount * self.__eur_conversion_rate
