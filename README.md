# Currency Conversion using Exchange Rate API 

* Description :
This Python script allows you to convert an amount of money from one currency to another by fetching real-time exchange rates from an online API. It utilizes the requests library to make an HTTP request to the ExchangeRate-API, which provides the latest conversion rates.

* Features :
Converts from any supported currency to any other supported currency.
Fetches real-time exchange rates from the ExchangeRate-API.
Outputs the converted amount in the desired currency.

* Requirements :
Python 3.x
requests library (to fetch the latest exchange rates)

 
 # Overview
 
API Request:
The script uses the requests library to make an API request to https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}.

Currency Conversion:
It retrieves the exchange rate for the source currency (e.g., USD) and converts the input amount to the target currency (e.g., EUR).
Output:

The script prints the result or today rate and converted output in the format: {amount} {from_currency} converted amount is:  {converted_amount} {to_currency}.


* Save the Python Script:

Save the code in a .py file, for example, currency.py.

* Run the Python Script:

* Open a terminal or command prompt.

Navigate to the folder where you saved the Python file:

cd path/to/your/script
Run the script with:
python currency.py

The script will display the converted amount in the terminal or command prompt.

Example Output

100 USD is equal to 85.50 EUR 

# "The status code" 
200 in an HTTP response indicates that the request was successful and the server has returned the expected data.

HTTP status codes are part of the standard response given by web servers when they process a request. Each status code provides information about the outcome of the request.

200 OK: This is the most common status code, meaning the request has succeeded, and the response body contains the requested data. In the case of your currency conversion API, this means that the server successfully processed the request and returned valid exchange rate data.
Other common HTTP status codes include:

404 Not Found: The requested resource could not be found.
500 Internal Server Error: The server encountered an error while processing the request.
400 Bad Request: The server could not understand the request due to incorrect syntax.
401 Unauthorized: The request requires user authentication.
