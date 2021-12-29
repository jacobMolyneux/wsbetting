import collections
import requests
import json


API_Key = '4PMmhcfwKg0DsZBddMS8nXRHsyAnxECU'
# checks to see if the word is a stock
def checker(word):
    if len(word) < 2:
        return False
    else:
        return word.isupper()


# goes through the reddit comment and adds stocks to the list of mentioned stocks
def parse_comment(comment, stock_list):
    for i in comment.split():
        if checker(i) == True:
            stock_list.append(i)
        else:
            pass
    


dummy_data = ['BB', 'IM', 'AT', 'HOME', 'DEPOT,', 'WHERE', 'THE', 'HOES', 'AT??', 'SPY', '$WISH.', 'SPY', 'TSLA', 'WSB', 'WISH', 'FKKK', 'TSLA', 'CALLS']

def clean_data(stock_mentions):
    new_dict = collections.defaultdict(lambda: 0)
    for i in stock_mentions:
        if i not in new_dict:
            new_dict[i] = 1
        elif i in new_dict:
            new_dict[i] += 1
        else:
            pass
    return new_dict

def valid_ticker(ticker, api_key):
    response = requests.get(f"https://api.polygon.io/v3/reference/tickers?ticker={ticker}&active=true&sort=ticker&order=asc&limit=10&apiKey={api_key}")
    response.json()
    # rough_data = json.dumps(response.text)
    # print(type(rough_data))
    # print(type(json.loads(rough_data)))
    data = response.json()
    if str(data['results']) == 'None':
        return False
    else:
        return True
    
print(valid_ticker('AAPL', API_Key))
print(valid_ticker('MMM', API_Key))
print(valid_ticker('THE', API_Key))