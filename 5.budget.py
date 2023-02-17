class Category:

    def __init__(self, name):
        self.name = name
        self.category = {}
        self.ledger = []
    
    def __str__(self):
        ans = ''
        self.a = '*' * ((30 - len(self.name)) // 2)
        ans += (f"{self.a}{self.name}{self.a}\n")
        for i in self.ledger:
            descr = i['description']
            price = i['amount']
            if len(descr) > 23:
                descr = descr[:23]
                ans += "{:<22} {:>6}\n".format(descr, f"{price:.2f}")
            else:
                ans += "{:<22} {:>7}\n".format(descr, f"{price:.2f}")
        ans += (f"Total: {self.get_balance():.2f}")
        return str(ans)

    def deposit(self, amount, description=''):
        self.amount = amount
        self.description = description
        self.category['amount'] = self.amount
        self.category['description'] = self.description
        self.ledger.append(self.category)
    
    def check_funds(self, arg):
        self.arg = arg
        if self.ledger[0]['amount'] - self.arg >= 0:
            return True
        else:
            return False

    def withdraw(self, amount, description=''):
        self.amount = amount
        self.description = description
        if self.check_funds(self.amount) is True:
            self.category = {}
            self.category['amount'] = (-self.amount)
            self.category['description'] = self.description
            self.ledger.append(self.category)
            return True
        else:
            return False

    def get_balance(self):
        self.all_amount = []
        [self.all_amount.append(i['amount']) for i in self.ledger]
        return sum(self.all_amount)

    def transfer(self, how_much, kuda):
        self.how_much = how_much
        if self.check_funds(self.how_much) is True:
            kuda.cat = {}
            self.category = {}
            self.category['amount'] = (- self.how_much)
            self.category['description'] = (f'Transfer to {kuda.name}')
            self.ledger.append(self.category)
            kuda.cat['amount'] = self.how_much
            kuda.cat['description'] = (f'Transfer from {self.name}')
            kuda.ledger.append(kuda.cat)
            print(kuda.ledger)
            print(self.ledger)
            return True
        else:
            return False


def create_spend_chart(cat):
    categories_percent, amount, lenght = [], [], []
    for k in cat:
        amount.append(abs(k.category['amount']))
    all_withdraw = sum(amount)
    for j in amount:
        categories_percent.append((round((j * 100 // all_withdraw) / 10)) * 10)  # округляем до ближ значения
    print("Percentage spent by category")
    for m in range(100, -1, -10):
        print("{:3d}".format(m) + '|' + ' ' * (len(cat) * 2) + "'")
    print('    ' + '-' * (len(cat) * 2))
    [lenght.append(len(cat[i].name)) for i in range(len(cat))]  # считаем длины категорий
    for letter in range(max(lenght)):
        print('     ', end='')
        for categ in range(len(cat)):
            try:
                print(cat[categ].name[letter] + ' ', end='')
            except:
                print('  ', end='')
                
        print()
    

#print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(business.ledger)
print(food.ledger)
print(entertainment.ledger)
categories = [business, food, entertainment]
print(create_spend_chart(categories))

# self.assertEqual(actual, expected, 'Expected `check_funds` method to be False')
# expected = True
# self.assertEqual(actual, expected, 'Expected `check_funds` method to be True')'''
'''
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")
food.deposit(1000, "initial deposit")
clothing.deposit(900, "ineteal dipasit")
auto.deposit(500, "Dipasit")
food.withdraw(10, "groceries")
clothing.withdraw(2000)
print(food)
#print(food.get_balance())
#print(clothing.get_balance())
print(food.ledger)
print(clothing.ledger)
food.transfer(50, auto)
print(food.get_balance())'''

'''
food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))
'''