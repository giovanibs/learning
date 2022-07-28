from bs4 import BeautifulSoup
with open('home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        print(f'{course.h5.text} costs {course.a.text.split()[-1]}')