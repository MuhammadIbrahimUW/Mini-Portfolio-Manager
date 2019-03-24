class Stock:
    '''Fields: symbol (Str), prices (Float)'''
    def __init__(self, symbol, prices):
        '''
        Constructor: Create a Stock object by calling stock(self,symbol,prices)
        
        __init__: Stock Str Float -> None
        '''
        self.symbol = symbol
        self.prices = [prices]
   
    def __repr__(self):
        '''
        String Representation: Implicitly called by print(s) where s is a Stock
        object.
        
        __repr__: Stock -> Str
        '''
        return "Stock: {0.symbol}".format(self) + "\n" \
               "Current Value: " +  str(self.prices[-1])
    
    def update_prices(self,lof):
        '''
        returns nothing
        
        Effects: mutates Stock arguement self by appending the list of floating
        point numbers in lof to the prices of the Stock
        
        updates_prices: Stock -> None
        
        Example:
        apple = Stock("APPL", 3.0)
        apple.update_prices([5.13,4.66,5.21,5.31,5.5,5.57,4.56])
        mutates apple.prices to: [3.0,5.13,4.66,5.21,5.31,5.5,5.57,4.56]
        '''
        self.prices += lof
        
    def average(self, n):
        '''
        returns the average of the last n prices of the Stock arguement self
        
        average: Stock Nat -> Float
        requires: n <= len(self.prices)
        
        Example:
        apple = Stock("APPL", 3.0)
        apple.update_prices([5.13,4.66,5.21,5.31,5.5,5.57,4.56])
        apple.average(3) => 5.21
        '''
        the_average = sum(self.prices[-n:]) / n
        return the_average

class Trader:
    '''Fields: name (Str), stocks owned (dictof Str Float), cash (Float)'''
    def __init__(self, name, stocks, cash):
        '''
        Constructor: Create a Trader object by calling 
        trader(self,name,stocks,cash)
        
        __init__: Trader Str (dictof Str Float) Float -> None
        '''        
        self.name = name
        self.stocks_owned = stocks
        self.cash = cash
        
    def __repr__(self):
        '''
        String Representation: Implicitly called by print(t) where t is a Trader
        object.
        
        __repr__: Trader -> Str
        '''
        los = []
        keys = list(self.stocks_owned.keys())
        amounts = list(self.stocks_owned.values())
        
        for i in range(len(keys)):
            los += [str(keys[i]) + " Shares: " + str(amounts[i])]
                
        return "Trader: {0.name}".format(self) + "\n" \
               "Stocks: " + str(los) + "\n" \
               "Current Cash Value: {0.cash}".format(self)
    
    def buy_stocks(self, s, n):
        '''
        returns True if given Trader arguement self has enough cash to purchase
        n number of Stock s, and False otherwise
        
        Effects: if there is enough cash, mutates self.cash by deducting the
        price of the trade and mutates self.stocks_owned by adding the number
        of stocks to the dictionary of holdings
        
        buy_stocks: Trader Stock Nat -> Bool
        
        example:
        apple = Stock('APPL', 4.56)
        warren_buffet = Trader("Warren Buffet", {}, 1000000000.0)
        warren_buffet.buy_stocks(apple, 100) => True and updates 
        warren_buffet.cash to 999999544.0 and warren_buffet.stocks to
        {'APPL': 100}
        '''
        cost = s.prices[-1] * n
        if cost <= self.cash:
            self.cash -= cost
            if s.symbol in self.stocks_owned:
                self.stocks_owned[s.symbol] += n
                return True
            else:
                self.stocks_owned[s.symbol] = n
                return True
        else:
            return False
    
    def sell_stocks(self, s, n):
        '''
        returns True if given Trader arguement self owns enough to sell
        n number of Stock s, and False otherwise
        
        Effects: if enough Stock s is owned, mutates the self.stocks_owned to
        remove n number of stock s and adds n times s.price to the self.cash
        amount
        
        sell_stocks: Trader Stock Nat -> Bool
        
        example:
        apple = Stock('APPL', 4.56)
        warren_buffet = Trader("Warren Buffet", {'APPL': 100}, 999999544.0)
        warren_buffet.sell_stocks(apple, 90) => True and changes
        warren_buffet.cash to 999999954.4 and warren_buffet.stocks_owned to
        {'APPL': 10}
        '''
        if s.symbol in self.stocks_owned:
            if n <= self.stocks_owned[s.symbol]:
                self.stocks_owned[s.symbol] -= n
                self.cash += s.prices[-1] * n
                if self.stocks_owned[s.symbol] == 0:
                    self.stocks_owned.pop(s.symbol)
                    return True
                else:
                    return True
            else:
                return False
        else:
            return False
        
## example Stock objects
apple = Stock("APPL", 3.0)
samsung = Stock("SMSG", 2.0)

## example Trader object
warren_buffet = Trader("Warren Buffet", {}, 1000000000.0)
