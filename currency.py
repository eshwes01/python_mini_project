import requests

# retriving exchange rate with api key from the remote url 
def get_rate(from_currency, to_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    print (response.status_code)

    if response.status_code == 200:
        data = response.json()
        print (data['conversion_rates'])
    
        if ('result'== "success") :
            rate = data['conversion_rates']
            to_currency_rate = rate.get(to_currency)
            print (to_currency_rate)
            return to_currency_rate
        else :
            print ("Error with API Key")
            return None 

# function to covert the currency from the amount that user input
def convert_currency(amount, from_currency, to_currency, api_key):
    rate = get_rate(from_currency, to_currency, api_key)
    print (rate)

    if rate:
        converted_amount = amount * rate
        print (converted_amount)

    else:
        print("Failed")

# main 
if __name__ == "__main__":
            api_key = "a23c88406575a6194ee8921e"         
            from_currency = input ("Type currency you want to change from e.g USD ,GBP  : ")
            to_currency = input (" Type currency you want to change to e.g USD or GBP : ")
            amount = input (" Enter the amount : ")
            convert_currency(amount,from_currency,to_currency,api_key)

            
            
