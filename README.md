# FakeNews-Detection-NLP-RandomForest

## Project Overview

The goal of this project is to identify Persian tweets that contain news and to classify their truthfulness as either **True** or **False** using machine learning algorithms. Additionally, we analyze the spread and propagation patterns of these news tweets.

## Background

First, we define what constitutes "news" in the context of our project. Any tweet that includes a **claim** is considered a news tweet.

Inspired by the methodology presented in the paper *"The spread of true and false news online"*, we detect news tweets based on their interaction with other tweets:

- Tweets that reply to other tweets and include links to news sources (such as IRNA, ISNA, BBC Persian, Eghtesad News, etc.) are likely responses to claim tweets.
- We then identify the original tweets to which these responses relate and label those original tweets as news tweets.

An alternative approach is also proposed that can be used interchangeably.

## Methodology

1. **Data Collection:**  
   We crawled Persian tweets from 2014 to 2020 using a Twitter scraping tool. We specifically collected tweets containing links to reliable news websites and separated these news tweets from non-news tweets.

2. **Data Processing:**  
   We extracted original tweet metadata using the Tweepy library, including:
   - Username and user ID
   - Number of followers and followings
   - Timestamp
   - Tweet text and ID
   - Number of retweets, likes, and replies
   - Hashtags, links, symbols, mentioned users
   - Polls and media presence

3. **Labeling:**  
   Using the replies with news links, we labeled the original tweets as news tweets (True or False claims).

4. **Model Training:**  
   We collected diverse tweet categories (news, jokes, personal stories, etc.) and trained classification models using clustering and machine learning algorithms to identify and predict new news tweets.

5. **Statistical Analysis:**  
   We analyze tweet engagement metrics such as likes, replies, and retweets to study the importance and spread of news in the community.

## Usage

- Run the scraper to collect Persian tweets with news-related links.
- Use the provided code to extract tweet metadata and label news tweets.
- Train and test classification models on the dataset.
- Analyze the spread patterns of true and false news using the engagement metrics.

## Tools and Libraries

- Python
- Tweepy (for Twitter API access)
- TwitterScraper (for historical tweet crawling)
- Machine Learning libraries (e.g., scikit-learn, TensorFlow )
- Data processing libraries (e.g., pandas, numpy)

## References

- Vosoughi, S., Roy, D., & Aral, S. (2018). *The spread of true and false news online*. Science, 359(6380), 1146-1151.

