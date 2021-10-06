from django.db import models

# Create your models here.

# Stock portfolio model
class Stock(models.Model):
    '''
    Database entry for stock portfolio
   
    '''
    ticker =  models.CharField(max_length=6)

    def __str__(self):
        return self.ticker



# Trading signal model
class TradingSignal(models.Model):
    '''
    Database entry for trading signals
   
    '''
    ticker = models.CharField(max_length=6)
    EntryDate = models.DateField()
    Direction = models.CharField(max_length=10)
    EntryPrice = models.CharField(max_length=10)
    StopLoss = models.CharField(max_length=10)
    ProfitTarget = models.CharField(max_length=10)
    ExitDate = models.DateField()

    def __str__(self):
        return self.ticker
        
