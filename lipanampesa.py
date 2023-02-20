import requests
import keys

def mpesa_payment(request):
    access_token_url = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    consumer_key = "your_consumer_key"
    consumer_secret = "your_consumer_secret"
    r = requests.get(access_token_url, auth=(consumer_key, consumer_secret))
    access_token = r.json()['access_token']
    api_url = "https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": keys.businessShortCode,
        "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjMwMjIwMDgzNDQ3",
        "Timestamp": "20230220083518",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.phone_number,
        "PartyB": keys.businessShortCode,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://prototype.regmotechnologies.co.ke/api/payments/lnm/",
        "AccountReference": "your_account_reference",
        "TransactionDesc": "your_transaction_description"
    }
    response = requests.post(api_url, json = request, headers=headers)
    print(response.text)
   
