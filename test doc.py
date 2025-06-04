import json
from lingua import Language, LanguageDetectorBuilder
import re
def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    

data = load_json('data.json')

def init_languages(a = Language.ENGLISH, b = Language.FRENCH, c = Language.DANISH, d = Language.LATVIAN):
    languages = [a, b, c, d]
    return languages


def init_model(languages):
    LanguageDetectorBuilder.from_languages(*languages).build()


def analyze_data(model, data):
    results = []
    for item in data:
        text = item.get('text', '')
        english = 0
        danish = 0
        latvian = 0
        text = re.sub(r'[^\w\s]', '', text)
        for i in text.split():
            if model.detect_language_of(i) == Language.ENGLISH:
                english += 1
            if model.detect_language_of(i) == Language.DANISH:
                danish += 1
            if model.detect_Language_of(i) == Language.LATVIAN:
                latvian += 1

        if english > 0:
            results.append({
                'text': text,
                'english words': english ,
                "total words": len(text.split()),
                'contains english': 1 
            })
        else:
            results.append({
                'text': text,
                'english words': english ,
                "total words": len(text.split()),
                'contains english': 0 
            })
    return results

def simple_stats(results):
    total_words = 0
    total_english = 0
    contains_english = 0
    for result in results:
        total_words += result['total words']
        total_english += result['english words']
        contains_english += result['contains english']
    
    return {
        'total words': total_words,
        'total english words': total_english,
        'percentage english': (total_english / total_words) * 100 if total_words > 0 else 0,    
        "mean of texts with english": (1/len(results)) * contains_english if len(results) > 0 else 0,
        "variance" : 1/(len(results)-1) * sum((result['contains english'] - (1/len(results)) * contains_english) ** 2 for result in results) if len(results) > 1 else 0,
        "standard deviation": ((1/(len(results)-1) * sum((result['contains english'] - (1/len(results)) * contains_english) ** 2 for result in results)) ** 0.5) if len(results) > 1 else 0
    }

