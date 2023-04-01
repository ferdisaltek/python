from torrequest import TorRequest

with TorRequest(proxy_port=9050, ctrl_port=9051, password='mypassword') as tr:
    response = tr.get('https://httpbin.org/ip')
    print(response.text)
