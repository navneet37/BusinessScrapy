import random
import itertools
from fp.fp import FreeProxy
import requests
from itemloaders.processors import TakeFirst, MapCompose
proxies_list = FreeProxy().get_proxy_list()
print(type(proxies_list))
proxy = itertools.cycle(proxies_list)
# pr = random.choice(proxies)
def set_proxy(proxy):
    _proxy = next(proxy)
    proxies = {
      "http": _proxy,
        "https": _proxy
    }
    print(proxies)
    return proxies
print(F"length of proxy = > {len(proxies_list)}")
proxies = set_proxy(proxy)
response = requests.get("https://api.ipify.org/", proxies=proxies)
print(response.text)

