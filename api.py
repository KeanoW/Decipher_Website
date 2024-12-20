import requests
import jsonpickle
import time

def get_quote_api(type):
    response = jsonpickle.decode(requests.get("https://zenquotes.io/api/quotes/mode=random").text)
    info = response[1]
    auther = info['a']
    quote = info['q']
    # count = 0

    # while (count < 480):
    #     time.sleep(7)
    #     response = jsonpickle.decode(requests.get("https://zenquotes.io/api/quotes/mode=random").text)
    #     with open("Quotes.txt", "a") as file:
    #
    #         for i in range(len(response)):
    #             info = response[i]
    #             auther = info['a']
    #             quote = info['q'].strip()
    #
    #             text = f"\n{quote} * {auther}"
    #             file.write(text)
    #
    #     count += 1
    #     print(count)

    if type == "a":
        return auther

    elif type == "q":
        return quote

def get_qoutes_from_file(filename):
    with open(filename, "r") as file:
        authers = []
        quotes_list = []
        for line in file.readlines():
            line_content = line.split(" * ")
            for item in range(len(line_content)):
                if item < 1:
                    quotes_list.append(line_content[item])
                else:
                    authers.append(line_content[item].strip("\n"))

        quotes = quotes_list[1:]

        dict_authors_quotes = dict(zip(authers, quotes))
        return dict_authors_quotes

def filter_quotes():
    with open("Quotes.txt", "r") as quotes:
        for line in quotes.readlines():
            line_quote = line.split(" * ")
            auther = line_quote[-1].replace("\n", "")
            # print(line_quote[-1])
            with open("Stoics.txt", "a+") as stoics:
                if auther == "Senneca" or auther == "Epictetus" or auther == "Aristotle" or auther == "Aristophanes" or auther == "Marcus Aurelius" or auther == "Socrates":
                    if line not in stoics.readlines():
                        stoics.write(line)
                        print(line)

# print(get_quote_api("q"))
# print(get_quote_api("a"))