import xml.etree.ElementTree as ET
import requests

class Article:
    @staticmethod
    def search_arxiv(query, max_results):
        url = 'http://export.arxiv.org/api/query'
        params = {
            'search_query': query,
            'start': 0,
            'max_results': max_results
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.text  
        else:
            return None
        
    @staticmethod
    def parse_arxiv_response(xml_data):
        parsed_articles = []
        root = ET.fromstring(xml_data)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        for entry in root.findall('atom:entry', ns):
            article = {
                'id': entry.find('atom:id', ns).text,
                'title': entry.find('atom:title', ns).text,
                'summary': entry.find('atom:summary', ns).text,
                'link': entry.find('atom:link[@rel="alternate"]', ns).attrib['href']
            }
            parsed_articles.append(article)
        return parsed_articles
