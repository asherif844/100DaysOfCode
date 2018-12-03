import requests
import bs4

def main():
    print_the_header()
    zipCode = input('What ZipCode do you want to get the weather for (60115)?')
    print(zipCode)
    html = get_html_from_web(zipCode) 
    get_weather_from_html(html)
    # display for the forecasts

def print_the_header():
    print('-----------------')
    print('  Weather App')
    print('-----------------')
    print()

def get_html_from_web(zipCode):
    url = 'http://wunderground.com/weather-forecast/{}'.format(zipCode)
    # print(url)
    response = requests.get(url) 
    # print(response.text[0:250])
    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # print (soup)
    loc = soup.find(class_ = 'region-content-header').find('h1').get_text()
    loc = cleanup_text(loc)
    condition = soup.find(class_ = 'condition-icon').get_text()
    condition = cleanup_text(condition)
    temp = soup.find(class_ = 'wu-unit-temperature').find(class_ = 'wu-value').get_text()
    temp = cleanup_text(temp)
    scale = soup.find(class_ = 'wu-unit-temperature').find(class_='wu-label').get_text()
    scale = cleanup_text(scale)
    print(loc, condition, temp, scale)

def cleanup_text(text):
    if not text:
        return text
    else:
        return text.strip()    


if __name__ == '__main__':
    main()
