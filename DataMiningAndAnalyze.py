from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd
import re
import urllib.parse
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as ss
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import model_selection

def get_pages(num_pages_to_scrape):
    pages = []
    for i in range (1,num_pages_to_scrape+1):
        url = ('https://smallacademy.co/page/{}/').format(i)
        pages.append(url)
    return pages

def get_soup(url):
    page = requests.get(url)
    soup = bs4(page.text,'html.parser')
    return soup
    
def get_coupon_urls(soup):
    coupon_urls = []
    for i in soup.findAll('h3',class_='entry-title mh-loop-title'):
        coupon_urls.append(i.a.get('href'))
    return coupon_urls

def get_course_name(soup):
    while(True):
        h1 = soup.findAll('h1',class_='entry-title')
        if (len(h1)>0):
            break
    course_name = h1[0].getText()
    print("getting course name...: ",course_name)
    return course_name
def get_cp_category(soup):
    while(True):
        span = soup.findAll('span',class_='entry-meta-categories')
        if (len(span)>0):
            break
    category = span[0].a.getText()
    print("getting category...: ",category)
    return category

def get_cp_date(soup):
    while(True):
        span = soup.findAll('span',class_='entry-meta-date updated')
        if (len(span)>0):
            break
    date = span[0].a.getText()
    print("getting post date...: ", date )
    return date

def get_udemy_url(soup):
    while(True):
        div = soup.findAll('div',class_='readmore')
        if (len(div)>0):
            break
    url = div[0].a.get('href')
    udemy_url_search = re.search('(?<=next\=).+',url)
    udemy_url_encoded = udemy_url_search.group(0)
    udemy_url = urllib.parse.unquote(udemy_url_encoded)
    print("getting udemy url...: ",udemy_url)
    return udemy_url

def get_num_students(soup):
    div = soup.find_all("div", attrs={"data-purpose": "enrollment"})
    num_students = div[0].getText()
    num_students = num_students.replace('\n','')
    num_students = num_students.replace('.','')
    num_students = num_students.replace(',','')
    num_students = re.search('\d+',num_students).group()
    print("getting number of students...: ",num_students)
    return num_students

def get_ratings(soup):
    div = soup.find_all("div",attrs = {"data-purpose":"rating"})
    ratings = div[0].getText()
    num_stars = ratings.split(' ')[1]
    num_stars = num_stars.replace(',','.')
    num_ratings = re.search('(?<=\()\d+',ratings)
    
    num_ratings = num_ratings.group()
    print("getting stars...: ",num_stars)
    print("getting ratings...: ",num_ratings)
    return [num_stars,num_ratings]

def MiningData():
    pages = get_pages(10)
    coupon_urls = []
    course_names = []
    coupon_categories = []
    coupon_dates = []
    udemy_urls = []
    num_students = []
    num_ratings = []
    num_stars = []
    
    for item in pages:
        soup = get_soup(item)
        coupon_urls.extend(get_coupon_urls(soup))

    for item in coupon_urls:
        soup = get_soup(item)
        course_names.append(get_course_name(soup))
        coupon_categories.append(get_cp_category(soup))
        coupon_dates.append(get_cp_date(soup))

        udemy_url = get_udemy_url(soup)
        udemy_soup = get_soup(udemy_url)
        num_students.append(get_num_students(udemy_soup))
        ratings = get_ratings(udemy_soup)
        num_stars.append(ratings[0])
        num_ratings.append(ratings[1])
        udemy_urls.append(udemy_url)

    data = {'Course Name':course_names,
            'Category':coupon_categories,
            'Post Date':coupon_dates,'Udemy Url':udemy_urls,
            'Number of Students':num_students,
            'Number of Ratings':num_ratings,
            'Stars':num_stars}

    df = pd.DataFrame(data = data)
    df.index+=1
    df.to_csv("data.csv")
    #df.to_excel("output.xlsx")

import math as m

def get_avg(X):
    
    return sum (X)/len(X)
        

def get_pearson_subf1(X,Y):
    sum_f1 = 0
    for i in range(len(X)):
        
        sum_f1 += (X[i] - get_avg(X))*(Y[i] - get_avg(Y))
    return sum_f1

def get_pearson_subf2(X):
    sum_f2=0
    for x in X:
       sum_f2 += (x - get_avg(X))**2
    return sum_f2

def my_pearson(X,Y):
    if len(X) != len(Y):
        print('invalid length X and length Y')
        return
    r  =  get_pearson_subf1(X,Y)/m.sqrt(get_pearson_subf2(X)*get_pearson_subf2(Y))
    return r

##def get_rg(X,Y):
##    XY_bind = [(X[i],Y[i])for i in range(len(X))]
##    XY_bind = sorted(XY_bind)
##    new_Y = sorted (Y)
##    rgY_dict = {}
##
##    for i in range (len(Y)):
##        rgY_dict[new_Y[i]] = i+1    
##    rgY = [rgY_dict[i[1]] for i in XY_bind]
##    rgX = [i+1 for i in range (len(X))]
##    return rgX,rgY

def get_rg(X,Y):
    rgX = ss.rankdata(X)
    rgY = ss.rankdata(Y)
    return rgX,rgY

def get_spearman_di(rgx,rgy):
    return rgx - rgy

def get_spearman_subf1(X,Y):
    sum_di = 0
    rgX,rgY = get_rg(X,Y)
    for i in range(len(X)):
        sum_di+= get_spearman_di(rgX[i],rgY[i])**2
    return sum_di
    
def my_spearman(X,Y):
    n = len(X)
    r = 1 - ((6*get_spearman_subf1(X,Y))/(n*(n**2-1)))
    return r

def print_pearson_corr(df):
    print("Pearson Function to test: \n",df.corr(method = 'pearson'))
    pearson_corr = df.corr(method = my_pearson)
    print("My Pearson Function: \n",pearson_corr)
    sns.heatmap(pearson_corr,annot=True)
    plt.show()


def print_spearman_corr(df):    
    print("Spearman Function to test: \n",df.corr(method = 'spearman'))
    spearman_corr = df.corr(method = my_spearman)
    print("My Spearman Function: \n",spearman_corr)
    sns.heatmap(spearman_corr,annot=True)
    plt.show()
    
from sklearn.metrics import make_scorer
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import plot_confusion_matrix

def AnalyzeData():
    #read data
    df = pd.read_csv('data.csv').drop(['Unnamed: 0'],axis=1)
#    print(df)
    title_names = df.columns.values.tolist()
    print(title_names)
    max_values = df.max().tolist()
    min_values = df.min().tolist()
    mean_values = df.mean()
    mode_values = df.mode()
    
##    print(mode_values)
##    print([mode_values[title][0]for title in title_names])

    mode_values = []
    for title in title_names:
        print("The most frequent elements of ",title,"collumn:",df[title].mode()[0])
        print(len(df[df[title] == df[title].mode()[0]]))
        mode_value = df[title].mode()[0]
        count  = len(df[df[title] == df[title].mode()[0]])
        if count <2:
            mode_value = None
        mode_values.append(mode_value)
        print("Most frequent: ",df[title].value_counts().idxmax()," ",df[title].value_counts().max())
    print("Maximum values: \n",max_values)
    print("Minimum values: \n",min_values)
    print("Average values: \n",mean_values)
    print(mode_values)
##    print_pearson_corr(df)
##    print_spearman_corr(df)
##    print("The most frequent elements of category collumn:\n",df.Category.mode())
##    print("The most frequent elements of stars collumn:\n",df.Stars.mode())
##    print("The most frequent elements of ratings collumn:\n",df['Number of Ratings'].mode())
#    print(df['Post Date'])
    analyze_data = {"Max values": max_values,
                    "Min values": min_values,
                    "Average values": mean_values,
                    "Most frequent values": mode_values}
    analyze_df = pd.DataFrame(data = analyze_data, index = title_names)
    print(analyze_df)
    analyze_df.to_excel("analyze_data.xlsx")
##    trainfeat_df = df.drop(["Course Name","Category","Post Date","Udemy Url"],axis =1)
##    print(trainfeat_df)
##    trainfeat_df.to_csv("dataset.csv",index = False)
    train_df = pd.read_csv("dataset.csv")
    print(train_df)
    x = train_df.drop(["Quality"],axis=1).to_numpy().tolist()
    y = train_df["Quality"].tolist()
##    print(x)
##    print(y)
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=1)
    navie_bayes = GaussianNB()
    navie_bayes.fit(x_train,y_train)
##    print("Test result: ",navie_bayes.predict(x_test))    
##    print(y_test)
    y_pred = navie_bayes.predict(x_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average = None)
    confusion = confusion_matrix(y_test, y_pred, labels = [0,1,2])

    print("Accuracy: ",accuracy)
    print("F1 Score: ",f1)
    print("Confusion: ",confusion)
    
    plot_confusion_matrix(navie_bayes, x_test, y_test)
    plt.show()
    
AnalyzeData()
