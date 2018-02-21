import pickle


class Transaction(object):
    
    def __init__(self, amount, date, currency="Euro", 
            eur_conversion_rate=1, description=None):
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__eur_conversion_rate = eur_conversion_rate
        self.__description = description
        
        #self.__dict__.update({k: v for k,v in locals().items() if k != "self"})#
    
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


class Account(Transaction):
    
    def __init__(self, number, name):
        self.__number = number
        self.__name = name
        self.__transactions = []
    
    @property
    def number(self):
        return self.__number
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        assert len(accname) > 3, "Account name must be at least 4 chars long.."
        self.name = name
    
    def __len__(self):
        return len(self.__transactions)
    
    def apply(self, transaction):
        self.__transactions.append(transaction)

    @property
    def balance(self):
        total = 0.0
        for transaction in self.__transactions:
            total += transaction.eur
        return total
    
    @property
    def all_eur(self):
        for transaction in self.__transactions:
            if transaction.currency != "Euro":
                return False
        return True
    
    def save(self):
        fh = None
        try:
            data = [self.number, self.name, self.__transactions]
            fh = open(self.number + ".acc", "wb")
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()
    
    def load(self):
        fh = None
        try:
            fh = open(self.number, "rb")
            data = pickle.load(fh)
            assert self.number = data[0], "account number doesn't match"
            self.__name, self.__transactions = data[1:]
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()


if __name__ == "__main__":
    import doctest
    doctest.testmod()

        
