import requests


def get_rate(from_currency, to_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    print (response.status_code)

   

if __name__ == "__main__":
            api_key = "a23c88406575a6194ee8921e"         
            from_currency = input ("Type currency you want to change from e.g USD or GBP: ")
            to_currency = input (" Add currency you want to change to e.g USD or GBP : ")
            amount = input (" Enter the amount : ")

            
            
