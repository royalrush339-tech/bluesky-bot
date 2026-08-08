import os, json, datetime, urllib.request

HANDLE = "gravitaquotidiano.bsky.social"
APP_PASSWORD = znai-uqom-eh7n-ltmq

QUOTES = [
"Il soffitto era la sua mappa dell'inerzia.",
"La povertà non è una scusa per il disordine.",
"Non era un tic. Era il metronomo di quella casa.",
"Qualcuno aveva alzato il guadagno dell'universo.",
"Lui camminava sul fondo di una piscina vuota.",
"Tutto luccicava. Niente era vivo.",
"Ognuna conteneva un sogno di plastica e silicio.",
"Un piccolo assedio della materia.",
"Una bolla di normalità.",
"Non veniva da un punto nello spazio. Veniva da oltre.",
"Un secondo cuore. Un richiamo.",
"La gravità revocata.",
"Marco precipitò nel vuoto più profondo che avesse mai conosciuto.",
"Come un richiamo. Come un avvertimento.",
"Il senso si sfaldava prima di arrivare al cervello.",
"Esistenze intercambiabili.",
"Non era suono. Era pressione.",
"Un contatto umano oltre la superficie.",
"Il silenzio arrivò all'improvviso.",
"Guardare il soffitto non è tempo perso: è il preludio a un viaggio.",
"La normalità è un superpotere.",
"Perché la vera guerra non è là fuori, tra le stelle. È dentro di lui.",
"Non sei stato scelto perché eri forte. Sei stato scelto perché avresti combattuto anche senza certezze.",
"La capacità di scegliere. Di dubitare. Di amare. Di sacrificarsi per qualcosa di più grande di sé.",
"C'è una crepa sul soffitto di Marco. L'ha fissata per anni. Poi, una notte, la crepa si spalanca.",
"A chi ha passato ore a fissare una crepa sul soffitto, in attesa che il mondo cominciasse a muoversi.",
]

def post():
    req = urllib.request.Request(
        "https://bsky.social/xrpc/com.atproto.server.createSession",
        data=json.dumps({"identifier": HANDLE, "password": APP_PASSWORD}).encode(),
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        s = json.load(r)

    day = datetime.date.today().toordinal()
    q = QUOTES[day % len(QUOTES)]
    text = f'"{q}"\n\n— La Gravità del Quotidiano\n#BookSky #citazioni'
    if day % 5 == 0:
        text += "\n🌐 lagravitadelquotidiano.neocities.org"
    if len(text) > 300:
        text = text[:297] + "…"

    record = {
        "repo": s["did"],
        "collection": "app.bsky.feed.post",
        "record": {
            "$type": "app.bsky.feed.post",
            "text": text,
            "createdAt": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
        },
    }
    req = urllib.request.Request(
        "https://bsky.social/xrpc/com.atproto.repo.createRecord",
        data=json.dumps(record).encode(),
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {s['accessJwt']}"})
    with urllib.request.urlopen(req) as r:
        print("Pubblicato:", json.load(r)["uri"])

post()
