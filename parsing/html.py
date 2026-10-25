import logging

#import requests
from selectolax.lexbor import LexborHTMLParser, LexborNode

logger = logging.getLogger(__name__)

def parse_html(response_text : str) -> LexborHTMLParser:
    if not isinstance(response_text, str):
        raise TypeError("response_text must be a string")

    return LexborHTMLParser(response_text)

def extract_text(element : LexborNode) -> str:
    if element:
        return element.text()
    else:
        return None

def extract_attribute(element : LexborNode, attribute : str):
    if element:
        return element.attributes.get(attribute)
    else:
        return None


    
    
        