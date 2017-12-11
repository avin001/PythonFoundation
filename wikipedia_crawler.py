import time
import urllib

import bs4
import requests


start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"


def find_first_link(url):
    repsonse = requests.get(url)
    html = repsonse.text
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # This div contains the article's body
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    # stores the first link found in the article, if the article contains no
    # links this value will remain None
    article_link = None

    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)
    return first_link


def continue_crawl(search_history_list, target_url, max_steps=25):
    if search_history_list[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history_list) > max_steps:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    for index, element in enumerate(search_history_list):
        if search_history_list[index] in search_history_list[index + 1:]:
            print("We've arrived at an article we've already seen, aborting search!")
            return False
    return True


article_chain = [start_url]

while continue_crawl(article_chain, target_url):
    print(article_chain[-1])
    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break
    article_chain.append(first_link)
    time.sleep(2)
