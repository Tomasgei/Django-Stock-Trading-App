from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from django.contrib import messages
from .forms import StockForm
from . models import Stock,TradingSignal


# Create your views here.
class Signal_list_view(ListView):
    '''
    Class based view to render page
    Render page with trading signals from database
    '''
    #model = TradingSignal
    queryset = TradingSignal.objects.order_by("-EntryDate").all()
    template_name = "market_dashboard.html"



# Tady vpisuju funkce a vlastnost které bude stránka mít
def home_view(request):
    '''
    Download stock info from api 
    Render page with basic info for stock ticker
    '''
    import requests
    import json

    if request.method == "POST":
        ticker = request.POST["ticker_lookup"]
        base_url = "https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token=pk_e3fa0c44f3714325960230ada76fba10"
        comp_details = "https://cloud.iexapis.com/stable/stock/"+ticker+"/company?token=pk_e3fa0c44f3714325960230ada76fba10"
        my_query = requests.get(base_url)
        my_query_2 = requests.get(comp_details)

        try: 
            api = json.loads(my_query.content)
            api_2 = json.loads(my_query_2.content)

        except Exception as e:
            api = "You entered wrong ticker or symbol doesnt exists!"
        return render(request,"home.html", {"api": api,"api_2": api_2 } ) #vykresli stránku za použití definovaného  html templatu

    else:
        return render(request,"home.html", {"ticker": "enter ticker symbol above"} ) #vykresli stránku za použití definovaného  html templatu
    
# About page
def about_view(request):
    '''
    Function based view
    Render about page
    '''
    return render(request,"about.html", {})


# Portfolio page
def portfolio_view(request):
    '''
    Function based view with some api and database queries
    Render porfolio page with table, where you can add or delete stock to portfolio and pull some data for ticker from api
   
    '''
    import requests
    import json
    
    if request.method == "POST":
        form = StockForm(request.POST or None)
        if  form.is_valid():
            form.save()
            messages.success(request, "Stock Has Been Added To Portfolio")
            return redirect(portfolio_view)

    else:
        ticker = Stock.objects.order_by("-id").all()
        output = [] #temporary save data from api call

        for ticker_item in ticker:
            base_url = "https://cloud.iexapis.com/stable/stock/"+str(ticker_item)+"/quote?token=pk_e3fa0c44f3714325960230ada76fba10"
            api_request = requests.get(base_url)   
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error...."
    mylist = zip(ticker, output)
    context = {'mylist': mylist,}
    return render(request,"portfolio.html", context)


# Portfolio page stock from portfolio

def delete(request, stock_id):
    '''
    Function to delete item from portfolio database
    Deletes item from portfolio database based on id
   
    '''
    item = Stock.objects.get(pk = stock_id )
    item.delete()
    messages.success(request, ("Stock Has Been Deleted!"))
    return redirect(portfolio_view)




# Delete stock page
def delete_stock_view(request):
    ticker = Stock.objects.order_by("-id").all()
    return render(request,"delete_stock.html", {"ticker": ticker})


#def market_dashboard_view(request):

 #   return render(request,"market_dashboard.html", {})


