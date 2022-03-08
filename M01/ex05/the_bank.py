class Bank(object):
    """The bank"""
    account = []

    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)
    
    def get_id(self, name):
        for ac in self.account:
            if ac.name == name:
                return ac.id - 1
        return -1

    def transfer(self, origin, dest, amount):
        if amount < 0:
            return False
        if type(origin) is str:
            origin = self.get_id(origin)
        if type(dest) is str:
            dest = self.get_id(dest)
        if not origin + 1 or not dest + 1:
            return False
        if origin > len(self.account) or dest > len(self.account):
            return False
        if self.account[origin].value >= amount:
            self.account[origin].value -= amount
            self.account[dest].value += amount
            return True
        else:
            return False
        

    def fix_account(self, account):
        return 0

class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1
    
    def transfer(self, amount):
        self.value += amount

    def __repr__(self):
        return(f'\nid: {self.id}\nowner: {self.name}\nsolde: {self.amount}')
