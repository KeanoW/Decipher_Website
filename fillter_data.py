def unique_quotes_dict(file):
    authers = []
    single_quotes = []
    quotes = []

    with open(file, "r+") as file:

        for phrase in file:
            if phrase not in quotes:
                quotes.append(phrase)

        for q in quotes:
            quote_split = q.split(" * ")
            quote = quote_split[0]
            if len(quote) > 30:
                single_quotes.append(quote)
                auther = quote_split[-1].replace("\n", "")
                authers.append(auther)

    unique_quotes = dict(zip(single_quotes, authers))
    return unique_quotes

# unique_quotes_dict("Stoics.txt")