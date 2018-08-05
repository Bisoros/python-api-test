from googletrans import Translator
from  textblob import TextBlob as tb
translator = Translator(service_urls=[
      'translate.google.com',
    ])

def SentimentAnalysis(text):
    translations = translator.translate([text], dest='en')
    return tb(translations[0].text)

