def create_news_ticker():
    headlines = ["Local Bear Eaten by Man", "Legislature Announces New Laws", "Peasant Discovers Violence Inherent in System", "Cat Rescues Fireman Stuck in Tree", "Brave Knight Runs Away", "Papperbok Review: Totally Triffic"]
    news_ticker = ""
    limit_reached = False
    for item in headlines:
        news_snippet = str(item + " ")
        for x in range(len(news_snippet)):
            if len(news_ticker) < 140:
                news_ticker += news_snippet[x]
            else:
                limit_reached = True
                break
        if limit_reached:
            break
    return news_ticker


print(create_news_ticker())
