import requests
import re

def get_h3_headings(url):
    response = requests.get(url)
    headings = re.findall(r'<h3.*?>(.*?)</h3>', response.text)
    return headings

if __name__ == "__main__":
    url = "http://www.columbia.edu/~fdc/sample.html"
    headings = get_h3_headings(url)
    print(headings)