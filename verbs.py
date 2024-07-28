import csv

# List of German verbs
verbs = [
    "arbeiten", "baden", "bauen", "bedeuten", "beginnen", "bekommen", "bestellen", "besuchen", "bezahlen", "bleiben",
    "brauchen", "bringen", "danken", "denken", "diskutieren", "dürfen", "einkaufen", "einladen", "empfangen",
    "empfehlen", "entscheiden", "entschuldigen", "erklären", "erzählen", "essen", "fahren", "fallen", "feiern",
    "finden", "fliegen", "fragen", "freuen", "fühlen", "gehen", "gehören", "gewinnen", "glauben", "grillen", "haben",
    "halten", "hängen", "heiraten", "heißen", "helfen", "hören", "interessieren", "joggen", "kaufen", "kennen",
    "kochen", "kommen", "kosten", "kriegen", "küssen", "lachen", "laufen", "leben", "legen", "lernen", "lesen",
    "lieben", "liegen", "machen", "meinen", "mögen", "müssen", "nehmen", "öffnen", "passen", "passieren", "putzen",
    "rauchen", "reden", "regnen", "reisen", "reparieren", "rufen", "sagen", "schlafen", "schließen", "schmecken",
    "schreiben", "schwimmen", "sehen", "sein", "sitzen", "sollen", "sprechen", "stehen", "stellen", "studieren",
    "suchen", "tanzen", "teilen", "telefonieren", "tragen", "treffen", "trinken", "tun", "übersetzen", "vergessen",
    "verkaufen", "verstehen", "versuchen", "vorbereiten", "vorlesen", "vorschlagen", "wählen", "warten", "waschen",
    "weggehen", "weinen", "weitergehen", "wohnen", "wünschen", "zahlen", "zeichnen", "zeigen", "zerstören", "ziehen",
    "zuhören", "zumachen", "zurückgeben", "zurückkommen", "zusammenarbeiten", "zusammenkommen", "aufräumen", "ausgehen",
    "aussehen", "aussteigen", "einkaufen", "einsteigen", "umsteigen", "abfahren", "ankommen", "ausziehen", "einziehen",
    "umziehen", "abschließen", "anfangen", "anrufen", "aufstehen", "ausgehen", "aussehen", "aufwachen", "mitbringen",
    "mitkommen", "mitnehmen", "nachdenken", "fernsehen", "einschlafen", "zurückkommen", "verstehen", "verzeihen",
    "vermissen", "verpassen", "zerbrechen", "zerschneiden", "bezahlen", "erzählen", "erklären", "vergleichen",
    "vergessen", "verletzen", "verlieren", "verschicken", "versprechen", "vorbereiten", "vorschlagen", "wegnehmen",
    "weitergeben", "wegrennen", "zurückbringen", "zusammenarbeiten", "zusammenbringen", "kennenlernen", "herunterfahren",
    "hochfahren", "losfahren", "wegfahren", "zusammenfahren", "weiterfahren", "hinfahren", "anfahren", "fortfahren",
    "abholen", "ausmachen", "einmachen", "anmachen", "ummachen", "zumachen", "herausfinden", "ausprobieren", "aufmachen",
    "ablegen", "anziehen", "ausziehen", "umziehen", "überqueren", "wiederholen"
]

# Create a CSV file and write the verbs to it
with open('german_verbs.csv', 'w', newline='') as csvfile:
    verb_writer = csv.writer(csvfile)
    verb_writer.writerow(["Verb"])  # Write the header
    for verb in verbs:
        verb_writer.writerow([verb])

print("CSV file 'german_verbs.csv' created successfully.")
