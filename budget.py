"""
BUDGET APP
"""

def print_info(i, selfd, selfa, str):
    import math
    if len(selfd[i]) < 24:
        if selfa[i] > 0:
            digits = int(math.log10(selfa[i]))+1
        elif selfa[i] == 0:
            digits = 1
        elif selfa[i] < 0:
            digits = int(math.log10(-selfa[i]))+2
        if digits > 7:
            print(f'{selfd[i]:40}- More than 7 digits')
        else:
            print(f'{selfd[i]:40}-{selfa[i]}')
    else:
        cont = 0
        str_f = None
        for k in selfd[i]:
            if cont < 24:
                str.append(k)
                cont += 1
            else:

                str_f = "".join(str)
                cont = 0
        if selfa[i] > 0:
            digits = int(math.log10(selfa[i]))+1
        elif selfa[i] == 0:
            digits = 1
        elif selfa[i] < 0:
            digits = int(math.log10(-selfa[i]))+2
        if digits > 7:
            print(f'{str_f:40}- More than 7 digits')
        else:
            print(f'{str_f:40}-{selfa[i]}')
    return selfa



class Category:
    def __init__(self, category, initial_de=0.0):
        self.category = category
        self.initial_deposit = initial_de
        self.ledger = initial_de
        self.amount_depo = list()
        self.discount_depo = list()
        self.amount_withdraw = list()
        self.discount_withdraw = list()
        self.str = list()
        self.amount_withdraw_total = 0


    def deposit(self, amount, description=''):
        self.ledger += amount
        self.amount_depo.append(amount)
        self.discount_depo.append(description)
        return

    def check_funds(self, amount):
        if amount <= self.ledger:
            return True
        else:
            return False

    def withdraw(self, amount=0.0, description='', category=''):
        if self.check_funds(amount):
            if category != '':
                print(f'\nTransfer to {category}:')
            self.ledger -= amount
            self.amount_withdraw_total += amount
            self.discount_withdraw.append(description)
            self.amount_withdraw.append(amount)
            return True, self.amount_withdraw, self.initial_deposit
        else:
            return False

    def get_balance(self):
        print(f'\n\n{"*"*20}{self.category}{"*"*20}\n\n{"Initial deposit:":41}{self.initial_deposit}')
        for i in range(len(self.amount_withdraw)):
            print_info(i, self.discount_withdraw, self.amount_withdraw, self.str)
        for j in range(len(self.amount_depo)):
            print_info(j, self.discount_depo, self.amount_depo, self.str)
        print(f'Total: {self.ledger}')
        return


    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            print(f'{other_category}')
            b = Category(other_category)
            self.withdraw(amount, other_category)
            b.initial_deposit += amount
            b.ledger = {'amount': amount, 'description': other_category}
            print(f'\namount: {b.ledger["amount"]}, description: Transfer from {self.category}')
            return True
        else:
            return False

    def aux(self):
        return self.initial_deposit, self.amount_withdraw_total, self.category


def create_spend_chart(categories):
    print('Percentage spent by category\n\n')
    names = []
    r = []
    for arg in args:
        names.append(arg.aux()[2])
        x = arg.aux()[0]
        n = arg.aux()[1]
        z = (n*100) // x
        r.append(z)

    cont = 0
    for name in range(len(names)):
        print(f'{names[name]:5}|', end='')
        aux = (r[name]//10)
        print(f' o ', end='')
        for j in range(int(aux)):
            print(f' o ', end='')
            cont += 1
        print('\n')
    d = ''
    print(f'{d:5}', 35*'-')
    print(f'{d:5}', end=' ')
    for num in range(0, 100, 10):
        print(f'{num:2}', end=' ')
    print(f'%{d:5}')
    return
