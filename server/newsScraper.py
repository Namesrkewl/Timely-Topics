from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import csv
import requests
import io
import itertools
import time

root = 'https://news.google.com/'
#root = 'https://i.pinimg.com/736x/af/5d/86/af5d86bcdb988c9d96a6eeba92e198cc--memes-aldnoah-zero-funny.jpg'
filename = 'C:/Users/khada/Desktop/Google_Hackathon/server/worldcities.csv'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')
options.add_argument('log-level=2')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(chrome_options=options)
driver.get(root)

def InputCity():
    print("Enter a city: ")
    return input()

def InputState():
    print("Enter a state: ")
    return input()

def GetCapitalNews(city, state):
    searchBar = driver.find_element(By.XPATH, '//*[@id="gb"]/div[2]/div[2]/div[2]/form/div[1]/div/div/div/div/div[1]/input[2]')
    searchBar.clear()
    with open(filename, encoding="utf8") as in_file:
        csv_reader = csv.DictReader(in_file, delimiter=",")
        for row in csv_reader:
            #print(row)
            if row['country'] == state and row['capital'] == "primary":
                #print(row)
                city = row['city']
                break
    searchBar.send_keys(city) #Default case
    time.sleep(0.5)
    try:
        location = driver.find_element(By.XPATH, "//div[(@class='jNjBJf') and (contains(text(), 'Location'))]")
    except:
        return None
    parent = location.find_element(By.XPATH, "./..")
    for _ in range(1):
      parent = parent.find_element(By.XPATH, "./..")
    parent.click()
    return city, state

def GetNews(city, state):
    searchBar = driver.find_element(By.XPATH, '//*[@id="gb"]/div[2]/div[2]/div[2]/form/div[1]/div/div/div/div/div[1]/input[2]')
    searchBar.clear()
    searchBar.send_keys(city)
    time.sleep(0.5)
    try:
        location = driver.find_element(By.XPATH, "//div[(@class='jNjBJf') and (contains(text(), 'Location'))]")
        parent = location.find_element(By.XPATH, "../..")
        parent.click()
        return city, state
    except:
        return GetCapitalNews(city, state)
    
def testNews(time):
    driver.get(root)
    #city = "Atlanta"
    #state = "Georgia"
    city = InputCity()
    state = InputState()
    print("Loading search results...")
    time.sleep(0.5)
    address = GetNews(city, state)
    while (address == None):
        print("City News Not Found!\nPlease try again.")
        city = InputCity()
        state = InputState()
        address = GetNews(city, state)
    city = address[0]
    state = address[1]

    newsFound = False
    while(newsFound == False):
        newsFound = True
        print("Loading local news for " + city + "...")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        driver.get(driver.current_url)
        posts = driver.find_elements(By.CSS_SELECTOR, "article[jslog^='85008']")
        #print(posts)
        if not posts:
            newsFound = False
            print("No news found\nFinding capital city...")
            location = GetCapitalNews(city, state)
            city = location[0]
            state = location[1]

        newsPostsFound = False
        for post in itertools.islice(posts, 30):
            id = posts.index(post)
            try:
                title = post.find_element(By.XPATH,'.//div[1]/div[2]/div/h4').text
                newsPostsFound = True
            except:
                continue
                print("Invalid Location. Please try again.")
                initNews(time)
                return
            try:
                time = post.find_element(By.XPATH,'.//div/time').text
            except:
                continue
            try:
                provider = post.find_element(By.XPATH,'.//div[1]/div[2]/div/div/img')
            except: provider = None
            try:
                image = post.find_element(By.XPATH,'.//div[1]/figure/img') or None
            except: 
                image = None
            print(id,title,time)
        if newsPostsFound == False:
            print("Invalid Location. Please try again.")
            initNews(time)
        else:
            print("News Initialized Successfully!")

#@testNews(time)



#print(location)
#print(parent)
#parent.click()


#class for posts: class="NiLAwe y6IFtc R7GTQ keNKEd j7vNaf"
#news provider: //*[@id="yDmH0d"]/div[1]/img[1]  //*[@id="yDmH0d"]/c-wiz/div/main/c-wiz/div[3]/div/c-wiz/c-wiz[1]/c-wiz/article/div[1]/div[2]/div/div/img
#title: //*[@id="yDmH0d"]/h3/a  //*[@id="yDmH0d"]/c-wiz/div/main/c-wiz/div[3]/div/c-wiz/c-wiz[1]/c-wiz/article/div[1]/div[2]/div/h4
#time since posted: //*[@id="yDmH0d"]/div[2]/div/time
#image: //*[@id="c412"] //*[@id="yDmH0d"]/c-wiz/div/main/c-wiz/div[3]/div/c-wiz/c-wiz[1]/c-wiz/article/div[1]/figure/img
#link button: //*[@id="yDmH0d"]/c-wiz/div/div[2]/div[2]/div/main/c-wiz/div[1]/div[1]/a/figure
#jslog 93789 for searches
#jslog 85008 for local news


def downloadImage(downloadPath, ur2l, name, folderName, fileName):
    imageContent = requests.get(url).content
    imageFile = io.BytesIO(imageContent)
    image = Image.open(imageFile)
    filePath = downloadPath + '/' + name + '/' + folderName + '/' + fileName

    with open(filePath, 'wb') as f:
        image.save(f, 'JPEG')

    print("Success")

#downloadImage('C:/Users/khada/Desktop/Google_Hackathon/server', driver.current_url, name, folderName, fileName)


def initNews(city, state, time, name):
    driver.get(root)
    print("Loading search results...")
    time.sleep(0.5)
    address = GetNews(city, state)
    while (address == None):
        print("City News Not Found!\nPlease enter a different location.")
        return None
    city = address[0]
    state = address[1]

    newsFound = False
    while(newsFound == False):
        newsFound = True
        print("Loading local news for " + city + "...")
        driver.get(driver.current_url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        posts = driver.find_elements(By.CSS_SELECTOR, "article[jslog^='85008']")
        #print(posts)
        if not posts:
            newsFound = False
            print("No news found\nFinding capital city...")
            location = GetCapitalNews(city, state)
            city = location[0]
            state = location[1]

        newsPostsFound = False
        listOfPosts = []
        providerUrls = []
        imageUrls = []
        id = 0
        for post in itertools.islice(posts, 30):
            try:
                title = post.find_element(By.XPATH,'.//div[1]/div[2]/div/h4').text
                newsPostsFound = True
            except:
                continue
                print("Invalid Location. Please try again.")
                initNews(time)
                return
            try:
                time = post.find_element(By.XPATH,'.//div/time').text
            except:
                continue
            try:
                link = post.find_element(By.XPATH,'.//div[1]/div[1]/a').get_attribute('href')
            except:
                continue
            try:
                provider = post.find_element(By.XPATH,'.//div[1]/div[2]/div/div/img').get_attribute('src')
                #print("Found provider " + str(id))
                providerUrls.append(provider)
                #print("Provider added")
            except: 
                providerUrls.append(str(id))
            try:
                image = post.find_element(By.XPATH,'.//div[1]/figure/img').get_attribute('src')
                #print("Found image " + str(id))
                imageUrls.append(image)
                #print("Image added")
            except: 
                imageUrls.append(image)
            item = {'id': id, 'title': title, 'time': time, 'link': link}
            #print(item)
            listOfPosts.append(item)
            id += 1
        if newsPostsFound == False:
            print("Invalid Location. Please try again.")
            initNews(time)
        else:
#            for i, provider in enumerate(providerUrls):
#                try:
#                    downloadImage('C:/Users/khada/Desktop/Google_Hackathon/client/public', provider, name, 'providers', str(i) + '.jpg')
#                    print("Provider " + str(i) + " downloaded successfully!")
#                except:
#                    continue
#            for i, image in enumerate(imageUrls):
#                try:
#                    downloadImage('C:/Users/khada/Desktop/Google_Hackathon/client/public', image, name, 'images', str(i) + '.jpg')
#                    print("Image " + str(i) + " downloaded successfully!")
#                except:
#                    continue
            print("News Initialized Successfully!")
            return listOfPosts