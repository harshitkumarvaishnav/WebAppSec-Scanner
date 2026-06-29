from Wappalyzer import Wappalyzer, WebPage


def detect_technologies(url):

    try:

        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(url)

        technologies = wappalyzer.analyze(webpage)

        return {
            "technologies": sorted(list(technologies))
        }

    except Exception as e:

        return {
            "error": str(e)
        }