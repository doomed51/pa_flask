from trafilatura import fetch_url


def load():
    document = fetch_url('https://www.example.org/')
    return document