import requests
import lxml.html as html

HOME_URL = 'https://www.larepublica.co/'

XPATH_LINK_TO_ARTICLE ='//div/div/h2/a/@href'
XPATH_TITLE = '/div[@class="mb-auto"]/h2/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p/text()'

def parse_home():
    try:
        # Trae todo el contenido de la paguira 
        response = requests.get(HOME_URL)
        # status_code, es el codigo que devuelve si la peticion a la web fue efectiva
        if response.status_code ==200:
            # response.content: Trae todo el contenido de la paguina
            # decode: convierte las caracteres especiles como la ñ para py lo puede entender
            home = response.content.decode('utf-8')
            # Convierte el html en xlm para poder hacer las consulta en XPath
            parsed = html.fromstring(home)
            # Se pasa la consulta al documento xmle
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            print(links_to_notices)

        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == '__main__':
    run()