import datetime
import codecs
import warnings
import os

base_path = os.path.dirname(__file__)

warnings.filterwarnings("ignore")

EVENTS = {
    "christmas": {
        "begin": datetime.date(2021, 12, 20),
        "end": datetime.date(2022, 1, 5),
        "poster": "christmas-2022-colour.txt"
    }
}

if __name__=="__main__":
    today = datetime.date.today()

    for event in EVENTS:
        if ( today >= EVENTS[event]["begin"]) and ( today <= EVENTS[event]["end"]):
            with open(os.path.join(base_path, EVENTS[event]["poster"]), 'r') as poster_file:
                poster_raw = poster_file.read()
                poster = codecs.getdecoder('unicode_escape')(poster_raw)[0]
                print(poster)
            break


