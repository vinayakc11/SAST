import requests
from urllib.parse import urlencode, urlparse, parse_qs, urlunparse

def http_method(method):
    if method == "POST":
        post_body_data = input("Enter the POST request body (param1=value1, param2=value2): ")
        post_data = parse_qs(urlparse(post_body_data).query)

        post_data = {k: v[0] for k, v in post_data.items()}

    return post_data

def inject_colab_url(target_url, colab_url, method, post_data):
    if method == "POST":
        response = requests.post(colab_url, data=post_data)

    elif method == "GET":
        response = requests.get(target_url)


def main():
    colab_url = input(["Enter the COLAB URL: "])
    #print("Enter the Collaborator/ Public server URL for hit: ", input(colab_url[0]))
    target_url = input("Enter the URL: ").strip()
    vulnerable_parameter = input("Enter the vulnerable parameter: ").strip()
    method = input("Enter the HTTP method (GET/POST): ").strip()

    post_data = http_method(method)

    inject_colab_url(target_url, colab_url, method, post_data)

if __name__ == "__main__":
    main()
