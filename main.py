from bs4 import BeautifulSoup
import requests

def get_news():
    html_text = requests.get('https://www.bbc.com/sport/basketball').text
    soup = BeautifulSoup(html_text, 'lxml')
    all_news = soup.find_all('div', class_ = 'gs-c-promo-body gs-u-mt@m gel-1/2@xs gel-1/1@m')
    for index, news in enumerate(all_news):
        publish_date_span = news.find('span', class_ = 'gs-u-vh')
        if publish_date_span != None:
            publish_date = publish_date_span.text
            publish_time = publish_date.split(' ')[2]
            if publish_time == 'hour' or publish_time == 'hours':
                recent_publish_date = publish_date
                title = news.find('h3', class_ = 'gs-c-promo-heading__title gel-pica-bold sp-o-link-split__text').text
                raw_link = news.find('a', class_ = 'gs-c-promo-heading gs-o-faux-block-link__overlay-link sp-o-link-split__anchor gel-pica-bold')['href']
                if raw_link.split('/')[0] != 'https:':
                    link = f'https://www.bbc.co.uk{raw_link}'
                else:
                    link = raw_link

                with open(f'news/{index}.txt', 'w') as f:
                    f.write(f'Headline: {title} \n')    
                    f.write(f'Link: {link} \n')    
                    f.write(f'Published: {recent_publish_date}')  
                print(f'File saved: {index}')  
                

get_news()                