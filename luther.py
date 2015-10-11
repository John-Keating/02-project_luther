# 02 Project Luther: Webscraping and regression
'''
This is the first clean draft of the Project Luther
It is the second project of the
It is an attempt to predict box office results of foreign films based on
the number of nominations for awards and the number of favorable reviews
the film received

It scrapes data from Box Office Mojo and used the imdb api to gather information
then combines this information into pandas dataframe.

The dataframe is run through a linear regresion model returning the summary
statistics of the regression, the parameters of the model, and the plots

As the regression was seen to have little explanatory power, no diagnostics were
undertaken.

As an addendum, the functions will also return a histogram of the box office
returns which was found to illuminate the issues with the data.

For more on the conlusions, the analysis, and reasons for the analysis, please
see ???????.

John Keating
Sat Oct 10 15:18:02 EDT 2015
'''


# import libraries

import pandas as pd
import requests
from bs4 import BeautifulSoup
import string


#  Main page Foreign Lanague Films



def get_foreign_table_links(url):
    '''
    This function takes the main url of the foreign films section of Box Office
    Mojo
    It then scrapes the links to subsequent pages in the section.
    It then converts these links into a list of usable urls and returns this
    list
    '''
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page)
    link_soup = soup.find_all('b')[2]

    link_list = []
    for link in link_soup.find_all('a'):
        link_list.append(str(link))

    url_list = [url]
    for url in link_list:
        x = url.replace('<a href="',
                        'http://www.boxofficemojo.com').partition('">')
        y = x[0].replace('amp;', '')  # ampersands did not soup well
        url_list.append(y)

    return url_list


def get_movie_table(url):
    '''
    given a url for an Box Office Mojo site with a table
    this function will return a dataframe based on the table
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    table1 =  soup.find_all('table')[2].find('table').find_all('tr')

    data = []
    for row in table1:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    df = pd.DataFrame(data)

    return df


def get_film_urls(series):
    '''
    given a series of titles based on Box Office Mojo table
    return a list of urls for the main pages of these films
    '''
    title_ser = series.apply(lambda x: x.split('('))

    title_url_list = []
    for title in title_ser.iteritems():
        urlA = 'http://www.boxofficemojo.com/movies/?id='
        urlB = '.htm'
        title = title[1][0].lower().replace(' ', '')
        title = title.encode('utf-8').translate(None, string.punctuation)
        title_url_list.append(urlA + title + urlB)

    return title_url_list


def all_movie_tables(url):
    '''
    This function takes a url for Box Office Mojo category.
    It then scrapes each page in the list for information on films that is
    contained in tables.
    It concatenates these tables and returns a dataframe.
    it makes use of the get movie table function
    '''
    url_list = get_foreign_table_links(url)

    # for loop over all the urls
    df = pd.DataFrame()
    for url in url_list:
        table = get_movie_table(url)
        df = df.append(table, ignore_index=True)

    drop_list = ['Rank', 'TOTAL (All Movies):',
            'AVERAGE (All Movies):', 'TOTAL(Wide Releases Only):',
            'AVERAGE(Wide Releases Only):']

    df.columns = ['rank', 'title',
                  'studio', 'gross',
                  'theatres_life', 'opening',
                 'theaters_opening', 'date']


    df_clean_titles = df[~df['rank'].isin(drop_list)]

    return df_clean_titles


def get_foreign_movie_titles(df):
    '''
    given the dataframe produced by all_movies_tables this function will take
    the title column and remove the '(countries)' part from each entry and
    then return a list of strings
    '''
    list_countries = list(df['title'])

    titles = []
    for title in list_countries:
        x = title.split('(')
        titles.append(x[0])

    return titles


def imdb_api_list(titles):
    '''
    given a list of film titles, this function will convert them into the omdb
    api format and return them as a list
    it makes use of the dataframe returned by all_movie_table
    '''
    imdb_list = []
    for title in titles:
        title = title.strip()
        title = title.replace(' ', '+')
        title = title.replace(',', '%2C')
        api_start = 'http://www.omdbapi.com/?t='
        api_end = '&y=&plot=short&r=json'
        api = api_start + title + api_end
        imdb_list.append(api)

    return imdb_list


def get_imdb_info(imdb_urls):
    '''
    given a list of url strings formatted for the OMDB api (see omdb.com)
    the function will return a list of json files with IMDB data in case of an
    error it will return an empty json file with an error message in one field
    '''
    imdb_data = []
    for api in imdb_urls:
        r = requests.get(api)
        imdb_data.append(r.json())
    return pd.DataFrame(imdb_data)
