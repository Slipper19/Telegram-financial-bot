import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}


def USD_Value():
    url = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0"
    request = requests.get(url, headers=headers)

    soup = BeautifulSoup(request.text, "html.parser")
    data = soup.find("span", {"class": "DFlfde SwHCTb"})
    return data.text


def EUR_Value():
    url = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&sxsrf=ALiCzsa20Am5Mxx8aULeQqQ7scK3Ia1PpQ%3A1666972259948&ei=Y_pbY96lOcmRrgTZ27X4DQ&oq=regc+&gs_lcp=Cgdnd3Mtd2l6EAEYAzIMCCMQsQIQJxBGEIICMgcIIxCxAhAnMgcIIxCxAhAnMg0IABCABBCxAxCDARAKMg0IABCABBCxAxCDARAKMg0IABCABBCxAxCDARAKMgcIABCABBAKMgoIABCxAxCDARBDMgcIABCABBAKMgcIABCABBAKOgcIIxDqAhAnOgQIIxAnOg4ILhCABBCxAxCDARDUAjoLCAAQgAQQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCxAxCDAToLCC4QgAQQsQMQgwE6CAgAEAoQARBDOhAILhCxAxCDARDHARDRAxBDOgQIABBDOgQILhBDOhAILhCxAxCDARDHARCvARBDOhAIABCABBCHAhCxAxCDARAUOgoIABCABBCHAhAUOggIABCABBCxAzoKCC4QxwEQ0QMQQzoPCAAQgAQQsQMQgwEQChAqOgkIABCABBAKEAE6BQgAEIAESgQIQRgASgQIRhgAUKwLWNUUYMklaAJwAXgAgAF-iAHZA5IBAzMuMpgBAKABAbABCsABAQ&sclient=gws-wiz"
    request = requests.get(url, headers=headers)

    soup = BeautifulSoup(request.text, "html.parser")
    data = soup.find("span", {"class": "DFlfde SwHCTb"})
    return data.text


def GBP_Value():
    url = "https://www.google.com/search?q=%D1%84%D1%83%D0%BD%D1%82%D1%8B+%D1%81%D1%82%D0%B5%D1%80%D0%BB%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2&sxsrf=ALiCzsYB4V1z7F0Db1gwGzHeO6bgKmZNVw%3A1666972566414&ei=lvtbY_zvGLmQwPAPiKmJsAQ&oq=%D1%84%D1%83&gs_lcp=Cgdnd3Mtd2l6EAEYADIECCMQJzIECCMQJzIECCMQJzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzoHCCMQ6gIQJzoGCCMQJxATOgsIABCABBCxAxCDAToFCAAQgAQ6CAgAEIAEELEDOgcIABCxAxBDOgoIABCxAxCDARBDOhAILhCxAxCDARDHARDRAxBDOhAILhCABBCHAhDHARCvARAUOhEILhCABBCxAxCDARDHARDRA0oECEEYAEoECEYYAFDRDVj7UWD6XGgFcAF4AIABU4gBtQKSAQE0mAEAoAEBsAEKwAEB&sclient=gws-wiz"
    request = requests.get(url, headers=headers)

    soup = BeautifulSoup(request.text, "html.parser")
    data = soup.find("span", {"class": "DFlfde SwHCTb"})
    return data.text


def СNY_Value():
    url = "https://www.google.com/search?q=%D1%8E%D0%B0%D0%BD%D1%8C"
    request = requests.get(url, headers=headers)

    soup = BeautifulSoup(request.text, "html.parser")
    data = soup.find("span", {"class": "DFlfde SwHCTb"})
    return data.text


def AED_Value():
    url = "https://www.google.com/search?q=%D0%B4%D0%B8%D1%80%D1%85%D0%B0%D0%BC"
    request = requests.get(url, headers=headers)

    soup = BeautifulSoup(request.text, "html.parser")
    data = soup.find("span", {"class": "DFlfde SwHCTb"})
    return data.text


def TRY_Value():
    url = "https://www.google.com/search?q=%D1%82%D1%83%D1%80%D1%86%D0%B8%D1%8F+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D0%B0&sxsrf=ALiCzsZOrHbJ_2nL00mbGwQmICDB8YtsIg%3A1666974796751&ei=TARcY_W7LdCSrgSknYaADA&oq=%D0%A2%D1%83%D1%80%D1%86%D0%B8%D1%8F+%D0%B2%D0%B0&gs_lcp=Cgdnd3Mtd2l6EAEYADINCAAQgAQQhwIQsQMQFDIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyCAguEIAEENQCOgoIABBHENYEELADOgwIABCxAxBDEEYQ-wE6BwgAELEDEEM6CggAELEDEIMBEEM6BAgAEEM6CAgAEIAEELEDOgsIABCABBCxAxCDAUoECE0YAUoECEEYAEoECEYYAFASWNwUYJsdaAFwAXgAgAFOiAHXAZIBATOYAQCgAQHIAQjAAQE&sclient=gws-wiz"
    request = requests.get(url, headers=headers)

    soup = BeautifulSoup(request.text, "html.parser")
    data = soup.find("span", {"class": "DFlfde SwHCTb"})
    return data.text
