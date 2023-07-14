#a class handling the tables
class tables:
    #initing the table object
    def __init__(self, tableNum = '' , waiter = '' , customers = 0 , orders = {}, billPrepared = False):
        self.tableNum = tableNum
        self.waiter = waiter
        self.customers = customers
        self.orders = orders
        self.billPrepared = billPrepared
        
        