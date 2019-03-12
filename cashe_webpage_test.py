from cashe_webpage import WebPage
import time


webpage = WebPage("https://edition.cnn.com")
content1 = webpage.content
print("Sleeping")
time.sleep(900)
content2 = webpage.content
print(content1 == content2)
