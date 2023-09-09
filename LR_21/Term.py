from LR_18 import SuperMarketDatabase
from LR_18 import SaleOfGoods
import os
from art import tprint

class SuperMarketTerm(object):
    def __init__(self):
        self.db_file = 'supermarket_db.pickle'
        if os.path.exists(self.db_file):
            self.supermarket_database = SuperMarketDatabase.load_database(self.db_file)
        else:
            self.supermarket_database = SuperMarketDatabase()

    def print_db(self):
        for sale in self.supermarket_database._sales:
            print('Sale of {0} by {1}, count: {2}'.format(sale.goods, sale.seller, sale.count))

    def add_sale(self):
        goods = input('Enter the name of the goods: ')
        seller = input('Enter the name of the seller: ')
        count = int(input('Enter the count of goods sold: '))
        sale = SaleOfGoods(goods, seller, count)
        self.supermarket_database.add_sale(sale)
    
    def delete_sale(self):
        index = int(input('Enter the index of the sale to delete: '))
        sale_to_delete = self.supermarket_database._sales[index]
        self.supermarket_database.remove_sale(sale_to_delete)

    def run(self):
        choice = 0
        choices = {
            1: lambda: self.print_db(),
            2: lambda: self.add_sale(),
            3: lambda: self.delete_sale(),
            4: lambda: self.supermarket_database.save_database(self.db_file),
            5: lambda: self.supermarket_database.delete_database(self.db_file),
            6: lambda: exit()
        }
        while True:
            print()
            print('1. Print database')
            print('2. Add sale')
            print('3. Delete sale')
            print('4. Save database')
            print('5. Delete database')
            print('6. Exit')
            print('Choose: ')
            try:
                choice = int(input())
                if choice in choices:
                    choices[choice]()
                else:
                    print('Invalid choice, try again')
            except ValueError:
                print('Invalid choice, try again')

if __name__ == "__main__":
    tprint("Supermarket")
    term = SuperMarketTerm()
    term.run()