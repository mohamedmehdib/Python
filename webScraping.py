from bs4 import BeautifulSoup
def send():
    url = 'web.html'
    with open(url, 'r') as html_file :
        content = html_file.read()

        soup = BeautifulSoup(content, 'html5lib')
        courses_tags = soup.find_all('h5')
        res = ""
        for course in courses_tags:
            res += f"{course.text}\n"
        return res
    
print(send())