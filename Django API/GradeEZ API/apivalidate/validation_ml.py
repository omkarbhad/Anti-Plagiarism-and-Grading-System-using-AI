
def detect(data):
    import pandas as pd
    def splited(data):
        import nltk
        nltk.download('punkt')

        from nltk.tokenize import sent_tokenize, word_tokenize
        sentences = sent_tokenize(data)

        import re
        search = []
        for i in range(0, len(sentences)):
            filter2 = re.sub('[^A-ZÜÖÄa-z0-9]+', ' ', sentences[i].lower())
            final = '"{}"'.format(filter2)
            search.append(final)
            print(sentences[i])
            print('-------------------------------------------------')

        return search, sentences

    def getlinks(tosearch):

        getlinks = []

        from googlesearch import search
        for i in range(0, len(tosearch)):
            query = tosearch[i]
            links = []
            for j in search(query, tld="co.in", num=1, stop=1, pause=2):
                # print(j)
                links.append(j)
            print(links)

            if len(links) == 0:
                getlinks.append("None")
            else:
                getlinks.append(links[0])

        return getlinks

    def plagiarism_percent(alllinks, tosearch):
        import re
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        wd = webdriver.Chrome(executable_path="./apivalidate/chromedriver.exe",
                              options=chrome_options)

        plagiarism = []

        for i in range(0, len(alllinks)):
            if alllinks[i] == 'None':
                plagiarism.append(0)
            else:
                wd.get(alllinks[i])
                scrape = wd.page_source
                lowercase = scrape.lower()
                finallower = re.sub('[^A-ZÜÖÄa-z0-9]+', ' ', lowercase)
                filter2 = re.sub('[^A-ZÜÖÄa-z0-9]+', ' ', tosearch[i])
                tofind = filter2.lower().split(" ")

                found = []
                for i in range(0, len(tofind)):
                    if lowercase.find(tofind[i].lower()) != -1:
                        found.append(tofind[i])

                similar = (len(found) / len(tofind)) * 100
                plagiarism.append(similar)
        wd.quit()
        return plagiarism

    tosearch, sentences = splited(data)
    alllinks = getlinks(tosearch)
    percent = plagiarism_percent(alllinks, tosearch)
    # result = pd.DataFrame({"Filtered": sentences, "Plagiarised Percent": percent, "Potential Link": alllinks})
    # result = result.to_json()
    json = {"filtered": sentences, "percent": percent, "links": alllinks}

    #
    # sentences = ['Yet, perhaps, due to modern technology people spend less time doing certain sociable activities, '
    #              'like shopping, which can be done from the home now.',
    #              'Although it can be said, that this leaves them time for other social activities.',
    #              'Another downside to the social significance of developments in modern technology an increasing '
    #              'number of people '
    #              'don’t know there neighbours.',
    #              'This lack of interaction with people in their community leads to a breakdown in community spirit.']
    # percent = [100.0, 90.0, 0.0, 65.0]
    # alllinks = ['https://essaypride.com/ex/information-studies-essay-developments-in-modern-technology-61653',
    #             'https://to-order-100-word-essay-on-responsibility-admission-cheaper.peatix.com/',
    #             'https://essaypride.com/ex/information-studies-essay-developments-in-modern-technology-61653',
    #             'https://to-order-100-word-essay-on-responsibility-admission-cheaper.peatix.com/']
    #
    # json = {"filtered": sentences, "percent": percent, "links": alllinks}

    return json
