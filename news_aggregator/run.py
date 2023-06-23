import sys

import NewsAggregator
import exceptions

def main():
    news_aggregator = NewsAggregator.NewsAggregator()

    try:
        news_aggregator.run()
    except exceptions.HttpError:
        print("Network Error")
        sys.exit()

if __name__ == "__main__":
    main()