import datetime
import codecs

EVENTS = {
    "christmas": {
        "begin": datetime.date(2021, 12, 1),
        "end": datetime.date(2021, 12, 31),
        "poster": "christmas-2022-colour.txt"
    }
}

if __name__=="__main__":
    today = datetime.date.today()

    for event in EVENTS:
        if ( today >= EVENTS[event]["begin"]) and ( today <= EVENTS[event]["end"]):
            with open(EVENTS[event]["poster"], 'r') as poster_file:
                poster_raw = poster_file.read()
                poster = codecs.getdecoder('unicode_escape')(poster_raw)[0]
                print(poster)
            break


