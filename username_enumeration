import requests
from bs4 import BeautifulSoup

username =""
password=""
response1_text = ""
response2_text = ""
payload = {}


def get_login_form_params(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    form = soup.find('form', attrs={'name': 'login'})

    params = {}
    for input_tag in form.find_all('input'):
        name = input_tag.get('name')
        value = input_tag.get('value', '')
        if name:
            params[name] = value

    return params

def credentials(parameters):

    payload = parameters.copy()

    possible_user_keys = ['user', 'username', 'uid', 'email', 'login']
    possible_pass_keys = ['pass', 'password', 'passw', 'pwd']

    username_field = None
    password_field = None

    for key in parameters:
        lower_key = key.lower()
        if not username_field and any(p in lower_key for p in possible_user_keys):
            username_field = key
        if not password_field and any(p in lower_key for p in possible_pass_keys):
            password_field = key

    payload[username_field] = input("Enter username: ")
    payload[password_field] = input("Enter password: ")

    #print(payload)

    return  payload



def response(url1, payload):

    session = requests.Session()
    req = requests.Request('POST', url1, data=payload)
    #print(payload)
    prepared = session.prepare_request(req)
    body_str = prepared.body
    if isinstance(body_str, bytes):
        body_str = body_str.decode('utf-8')

    print("\n--- Request Body ---")
    print(body_str)

    response = requests.post(url1, data=payload)
    response_text = response.text

    #print (response_text)

    print("Response saved")
    #for k, v in response.headers.items():
     #   print(f"{k}: {v}")
    print("\n")

    return response_text


def comparing_responses(response1_text, response2_text):
    soup1 = BeautifulSoup(response1_text, 'html.parser')
    soup2 = BeautifulSoup(response2_text, 'html.parser')


    body_text1 = soup1.body.get_text(separator=' ', strip=True) if soup1.body else ''
    body_text2 = soup2.body.get_text(separator=' ', strip=True) if soup2.body else ''

    if body_text1 == body_text2:
        print("Username Enumeration Not Possible")
    else:
        print("Username Enumeration Possible")



def main():
    url = "https://demo.testfire.net/login.jsp"
    url1 = "https://demo.testfire.net/doLogin"
    parameters = get_login_form_params(url)
    print(parameters)


    payload1 = credentials(parameters)
    response1_text= response(url1, payload1)

    payload2 = credentials(parameters)
    response2_text = response(url1, payload2)
    print("\n")
    print(len(response1_text))
    print(len(response2_text))

    comparing_responses(response1_text, response2_text)


if __name__ == "__main__":
    main()

