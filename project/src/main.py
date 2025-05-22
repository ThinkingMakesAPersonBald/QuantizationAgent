import requests
def main():
    print('Hello from python 3.13!')
    response = requests.get("https://httpbin.org/get")
    print(response)

if __name__ == "__main__":
    main()
