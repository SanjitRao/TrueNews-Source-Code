import requests
import json

send_url = "http://api.ipstack.com/check?access_key=870ce3560bdbce7092ea20499c6bda1c"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
state_code = geo_json['region_code']
state_name = geo_json['region_name']
country_code = geo_json['country_code']

# OBSOLETE API
# covid_url = f"https://api.covidtracking.com/v1/states/{state_code}/current.json"
# covid_req = requests.get(covid_url)
# covid_json = json.loads(covid_req.text)
# total_cases = covid_json['positive']

# print(state_name,"total cases: ", total_cases)

a = 0
while a != 1:
    try:
        print("Region:", country_code)

        print("News types:", "\n", "Top","\n", "Other (you will need to specify a keyword)", "\n", "Business", "\n", "Entertainment", "\n", "Science", "\n", "Health", "\n", "General", "\n", "Sports", "\n", "Technology")

        news_type = input("What news do you want? (Enter 'change region' to change your region.): ")

        if news_type == "top" or news_type == "Top":
            news_url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey=a0ffaa35067a490fb73ba682f3949bfb"
            news_req = requests.get(news_url)
            news_json = json.loads(news_req.text)
            n = 0
            print("\n")
            for value in news_json['articles']:
                news_title = news_json['articles'][n]['title']
                news_author = news_json['articles'][n]['author']
                news_articles = news_json['articles'][n]['url']
                n+=1
                print(news_title, "\n", news_articles, "\n", "Author:", news_author, "\n")
        elif news_type == "change region":
            country_code = input("Enter two letter country code: ")


        elif news_type == "other" or news_type == "Other":
            res = input("Enter keyword: ")
            news_url = f"https://newsapi.org/v2/everything?q={res}&apiKey=a0ffaa35067a490fb73ba682f3949bfb"
            news_req = requests.get(news_url)
            news_json = json.loads(news_req.text)
            n = 0
            print("\n")
            for value in news_json['articles']:
                news_title = news_json['articles'][n]['title']
                news_author = news_json['articles'][n]['author']
                news_articles = news_json['articles'][n]['url']
                n += 1
                print(news_title, "\n", news_articles, "\n", "Author:", news_author, "\n")

        elif news_type == "business" or "Business":
            news_url = f"https://newsapi.org/v2/sources?country={country_code}&category=business&apiKey=a0ffaa35067a490fb73ba682f3949bfb"
            news_req = requests.get(news_url)
            news_json = json.loads(news_req.text)
            n = 0
            print("\n")
            for value in news_json['sources']:
                news_title = news_json['sources'][n]['name']
                news_author = news_json['sources'][n]['description']
                news_articles = news_json['sources'][n]['url']
                n+=1
                print(news_title, "\n", news_articles, "\n", "Description:", news_author, "\n")

        elif news_type == "Entertainment" or "entertainment":
            news_url = f"https://newsapi.org/v2/sources?country={country_code}&category=entertainment&apiKey=a0ffaa35067a490fb73ba682f3949bfb"
            news_req = requests.get(news_url)
            news_json = json.loads(news_req.text)
            n = 0
            print("\n")
            for value in news_json['sources']:
                news_title = news_json['sources'][n]['name']
                news_author = news_json['sources'][n]['description']
                news_articles = news_json['sources'][n]['url']
                n+=1
                print(news_title, "\n", news_articles, "\n", "Description:", news_author, "\n")

        elif news_type == "Science" or "science":
            news_url = f"https://newsapi.org/v2/sources?country={country_code}&category=science&apiKey=a0ffaa35067a490fb73ba682f3949bfb"
            news_req = requests.get(news_url)
            news_json = json.loads(news_req.text)
            n = 0
            print("\n")
            for value in news_json['sources']:
                news_title = news_json['sources'][n]['name']
                news_author = news_json['sources'][n]['description']
                news_articles = news_json['sources'][n]['url']
                n+=1
                print(news_title, "\n", news_articles, "\n", "Description:", news_author, "\n")

        elif news_type == "Health" or "health":
            news_url = f"https://newsapi.org/v2/sources?country={country_code}&category=health&apiKey=a0ffaa35067a490fb73ba682f3949bfb"
            news_req = requests.get(news_url)
            news_json = json.loads(news_req.text)
            n = 0
            print("\n")
            for value in news_json['sources']:
                news_title = news_json['sources'][n]['name']
                news_author = news_json['sources'][n]['description']
                news_articles = news_json['sources'][n]['url']
                n+=1
                print(news_title, "\n", news_articles, "\n", "Description:", news_author, "\n")

        elif news_type == "General" or "general":
            news_url = f"https://newsapi.org/v2/sources?country={country_code}&category=general&apiKey=a0ffaa35067a490fb73ba682f3949bfb"
            news_req = requests.get(news_url)
            news_json = json.loads(news_req.text)
            n = 0
            print("\n")
            for value in news_json['sources']:
                news_title = news_json['sources'][n]['name']
                news_author = news_json['sources'][n]['description']
                news_articles = news_json['sources'][n]['url']
                n+=1
                print(news_title, "\n", news_articles, "\n", "Description:", news_author, "\n")

        elif news_type == "Sports" or "sports":
            news_url = f"https://newsapi.org/v2/sources?country={country_code}&category=sports&apiKey=a0ffaa35067a490fb73ba682f3949bfb"
            news_req = requests.get(news_url)
            news_json = json.loads(news_req.text)
            n = 0
            print("\n")
            for value in news_json['sources']:
                news_title = news_json['sources'][n]['name']
                news_author = news_json['sources'][n]['description']
                news_articles = news_json['sources'][n]['url']
                n+=1
                print(news_title, "\n", news_articles, "\n", "Description:", news_author, "\n")

        elif news_type == "Technology" or "technology":
            news_url = f"https://newsapi.org/v2/sources?country={country_code}&category=technology&apiKey=a0ffaa35067a490fb73ba682f3949bfb"
            news_req = requests.get(news_url)
            news_json = json.loads(news_req.text)
            n = 0
            print("\n")
            for value in news_json['sources']:
                news_title = news_json['sources'][n]['name']
                news_author = news_json['sources'][n]['description']
                news_articles = news_json['sources'][n]['url']
                n+=1
                print(news_title, "\n", news_articles, "\n", "Description:", news_author, "\n")
        res1 = input("Want more news?[y/n]: ")
        if res1 == "n":
            a = 1
        print("\n")
    except:
        n = 1