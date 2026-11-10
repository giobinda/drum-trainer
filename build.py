#!/usr/bin/env python3
"""Builds index.html (English) and de/index.html (German) from one template.

Edit the texts below, run `python3 build.py`, and commit the generated pages.
"""
from pathlib import Path

ROOT = Path(__file__).parent
MAIL = "app_support.keenly472@passmail.com"

ICONS = {
    "metronome": "M9.5,3h5l4,18H5.5zM11.2,5l-1.1,5h3.8l-1.1,-5zM11.4,13l5.4,-7.6l1.2,0.9l-4.7,6.7z",
    "lessons": "M3,13h2v-2H3v2zm0,4h2v-2H3v2zm0,-8h2V7H3v2zm4,4h14v-2H7v2zm0,4h14v-2H7v2zM7,7v2h14V7H7z",
    "mic": "M12,14c1.66,0 2.99,-1.34 2.99,-3L15,5c0,-1.66 -1.34,-3 -3,-3S9,3.34 9,5v6c0,1.66 1.34,3 3,3z"
           "m5.3,-3c0,3 -2.54,5.1 -5.3,5.1S6.7,14 6.7,11H5c0,3.41 2.72,6.23 6,6.72V21h2v-3.28c3.28,-0.48 6,-3.3 6,-6.72h-1.7z",
    "hands": "M7,2h2v10H7zM15,2h2v10h-2zM5,14h6v8H5zM13,14h6v8h-6z",
    "progress": "M5,9.2h3V19H5zM10.6,5h2.8v14h-2.8zM16.2,13H19v6h-2.8z",
    "streak": "M12,2l2.9,6.3l6.9,0.7l-5.2,4.6l1.5,6.8L12,16.9l-6.1,3.5l1.5,-6.8L2.2,9l6.9,-0.7z",
    "lock": "M18,8h-1V6c0,-2.76 -2.24,-5 -5,-5S7,3.24 7,6v2H6c-1.1,0 -2,0.9 -2,2v10c0,1.1 0.9,2 2,2h12"
            "c1.1,0 2,-0.9 2,-2V10c0,-1.1 -0.9,-2 -2,-2zM9,6c0,-1.66 1.34,-3 3,-3s3,1.34 3,3v2H9V6z",
}

EN = dict(
    lang="en", root="", other_lang="de/", other_label="Deutsch",
    title="Drum Trainer & Metronome – learn the drums in time",
    description="A metronome made for learning the drums: 26 lessons, a timing coach that hears whether you're early or late, and practice streaks. For Android.",
    nav=("Features", "Pricing", "FAQ", "Support"),
    h1="Learn the drums with a metronome that <em>listens</em>.",
    lead="Drum Trainer &amp; Metronome takes you from your very first beat to full grooves: step-by-step lessons, a timing coach that hears whether you're early or late, and a practice streak to keep you going.",
    soon="Coming soon to Google Play", soon_small="Android 8 and newer", see="See what's inside",
    features_h="Everything a beginner needs, nothing in the way",
    features_intro="Built by a beginner drummer, for beginner drummers on acoustic kits, e-drums and practice pads.",
    free="Free", premium="Premium",
    features=[
        ("metronome", "A clear, steady metronome", "Every common time signature, quarters to sixteenths and triplets, tap tempo and a choice of click sounds. The rhythm is drawn as real notation, so you see what you hear.", False),
        ("lessons", "26 step-by-step lessons", "From counting along and your first strokes to the basic rock beat, fills and sixteenths. Each lesson has a start tempo, a goal, tips and a two-bar count-in.", True),
        ("mic", "A timing coach that listens", "Turn on the microphone and play: two dials show whether you're ahead of or behind the click, and how even your strokes are. Listen back to your last bars at half speed.", True),
        ("hands", "Every limb on its own", "Practise a lesson with the right hand, the left hand, hands only or kick only, before putting it all together.", True),
        ("progress", "Progress you can see", "A practice calendar, timing trends over your sessions and a journal for notes on each day.", True),
        ("streak", "Streaks, badges and reminders", "Set how often you want to practise, get a reminder at your time, and earn badges for days and weeks in a row.", True),
    ],
    private="<strong>Your microphone stays private.</strong> What the timing coach hears is analysed on your phone, never saved and never sent anywhere. No account, no ads, no tracking.",
    shots_h="A look inside",
    shots=[("metronome", "The free metronome"), ("lesson", "A lesson, ready to play"), ("coach", "The timing coach"),
           ("lessons", "26 lessons in four levels"), ("progress", "Calendar and badges"), ("badges", "Badges for your streaks")],
    pricing_h="Simple pricing",
    pricing_intro="The metronome is free, always. Premium unlocks the coaching, and you can try all of it free for 7 days.",
    plans=[
        ("Free", "€0", "", "", ["The full metronome", "Notation for every rhythm", "Tap tempo and click sounds", "Light and dark themes"], False),
        ("Premium monthly", "€1.99", " / month", "7 days free", ["All 26 lessons", "The timing coach", "Progress, journal and calendar", "Streak badges and reminders", "Cancel anytime in Google Play"], False),
        ("Premium lifetime", "€19.99", " once", "Best value", ["Everything in Premium", "Pay once, keep it forever", "No subscription to manage", "Restores on a new phone"], True),
    ],
    pricing_note="Prices in euros; Google Play shows the price for your country. Cancel the monthly plan during the free week and you pay nothing.",
    faq_h="Questions",
    faq=[
        ("Does it work with an electronic drum kit?", "Yes. Choose “Pad / e-drum” in the Mic settings: the timing coach then listens for the quiet tap of the stick on the pad, so you can practise with headphones on."),
        ("Does the app record me?", "No. The microphone is analysed live on your phone to time your strokes. The last few seconds are kept in memory for “listen back” and then thrown away. Nothing is saved or uploaded."),
        ("Why should I calibrate?", "Every phone plays and records sound with a small delay, often 50–100 ms. Calibrating once, in a quiet room, measures that delay so the coach can tell a few milliseconds early from late."),
        ("Can my child use it?", "Yes. The app has no accounts, ads or chat and collects no personal data. Purchases go through Google Play, so Family Link can ask a parent to approve them."),
        ("How do I cancel the subscription?", "In the Google Play app: tap your profile picture, then Payments &amp; subscriptions, then Subscriptions. You can also open it from the app's Premium screen."),
        ("I have a new phone. Do I pay again?", "No. Sign in with the same Google account and tap “Restore purchases” on the Premium screen."),
    ],
    support_h="Support",
    support_text="Found a bug, have an idea for a lesson, or need help with a purchase? Write to us, and if it's about a problem, tell us your phone model and Android version.",
    write="Write to support",
    privacy="Privacy policy", privacy_url="privacy/",
    footer="Drum Trainer &amp; Metronome",
)

DE = dict(
    lang="de", root="../", other_lang="../", other_label="English",
    title="Drum Trainer & Metronome – Schlagzeug lernen im Takt",
    description="Ein Metronom zum Schlagzeuglernen: 26 Lektionen, ein Timing-Coach, der hört, ob du zu früh oder zu spät bist, und Übungsserien. Für Android.",
    nav=("Funktionen", "Preise", "Fragen", "Support"),
    h1="Schlagzeug lernen mit einem Metronom, das <em>zuhört</em>.",
    lead="Drum Trainer &amp; Metronome bringt dich vom allerersten Schlag bis zu ganzen Grooves: Lektionen Schritt für Schritt, ein Timing-Coach, der hört, ob du zu früh oder zu spät bist, und Übungsserien, die dich dranbleiben lassen.",
    soon="Bald bei Google Play", soon_small="Android 8 und neuer", see="Was drin ist",
    features_h="Alles, was Einsteiger brauchen, nichts, was stört",
    features_intro="Von einem Schlagzeug-Anfänger für Anfänger gebaut, für akustische Sets, E-Drums und Übungspads.",
    free="Gratis", premium="Premium",
    features=[
        ("metronome", "Ein klares, stabiles Metronom", "Alle gängigen Taktarten, Viertel bis Sechzehntel und Triolen, Tap-Tempo und verschiedene Klicks. Der Rhythmus wird als echte Notenschrift gezeigt, damit du siehst, was du hörst.", False),
        ("lessons", "26 Lektionen Schritt für Schritt", "Vom Mitzählen und ersten Schlägen bis zum einfachen Rockbeat, Fills und Sechzehnteln. Jede Lektion hat ein Starttempo, ein Ziel, Tipps und zwei Takte zum Einzählen.", True),
        ("mic", "Ein Timing-Coach, der zuhört", "Mikrofon an und los: Zwei Anzeigen zeigen, ob du vor oder hinter dem Klick liegst und wie gleichmäßig deine Schläge sind. Hör dir deine letzten Takte in halbem Tempo an.", True),
        ("hands", "Jede Hand, jeder Fuß einzeln", "Übe eine Lektion nur mit rechts, nur mit links, nur mit den Händen oder nur mit dem Fuß, bevor du alles zusammensetzt.", True),
        ("progress", "Fortschritt, den du siehst", "Ein Übungskalender, dein Timing-Verlauf über die Einheiten und ein Tagebuch für Notizen zu jedem Tag.", True),
        ("streak", "Serien, Abzeichen und Erinnerungen", "Leg fest, wie oft du üben willst, lass dich zu deiner Zeit erinnern und sammle Abzeichen für Tage und Wochen in Folge.", True),
    ],
    private="<strong>Dein Mikrofon bleibt privat.</strong> Was der Timing-Coach hört, wird auf deinem Handy ausgewertet, nie gespeichert und nirgendwohin gesendet. Kein Konto, keine Werbung, kein Tracking.",
    shots_h="Ein Blick hinein",
    shots=[("metronome", "Das kostenlose Metronom"), ("lesson", "Eine Lektion, bereit zum Spielen"), ("coach", "Der Timing-Coach"),
           ("lessons", "26 Lektionen in vier Stufen"), ("progress", "Kalender und Abzeichen"), ("badges", "Abzeichen für deine Serien")],
    pricing_h="Einfache Preise",
    pricing_intro="Das Metronom ist kostenlos, für immer. Premium schaltet das Coaching frei, und du kannst alles 7 Tage gratis testen.",
    plans=[
        ("Gratis", "0 €", "", "", ["Das komplette Metronom", "Notenschrift für jeden Rhythmus", "Tap-Tempo und Klick-Klänge", "Helle und dunkle Designs"], False),
        ("Premium monatlich", "1,99 €", " / Monat", "7 Tage gratis", ["Alle 26 Lektionen", "Der Timing-Coach", "Fortschritt, Tagebuch und Kalender", "Serien-Abzeichen und Erinnerungen", "Jederzeit in Google Play kündbar"], False),
        ("Premium dauerhaft", "19,99 €", " einmalig", "Bester Preis", ["Alles aus Premium", "Einmal zahlen, für immer behalten", "Kein Abo zu verwalten", "Auch auf einem neuen Handy"], True),
    ],
    pricing_note="Preise in Euro; Google Play zeigt den Preis für dein Land. Kündigst du das Monatsabo in der Gratiswoche, zahlst du nichts.",
    faq_h="Fragen",
    faq=[
        ("Funktioniert es mit einem E-Drum-Set?", "Ja. Wähle in den Mikro-Einstellungen „Pad / E-Drum“: Der Timing-Coach achtet dann auf das leise Tippen des Sticks auf dem Pad, du kannst also mit Kopfhörern üben."),
        ("Nimmt die App mich auf?", "Nein. Das Mikrofon wird live auf deinem Handy ausgewertet, um deine Schläge zu timen. Die letzten Sekunden bleiben für „Anhören“ im Arbeitsspeicher und werden dann verworfen. Nichts wird gespeichert oder hochgeladen."),
        ("Warum soll ich kalibrieren?", "Jedes Handy spielt und nimmt Ton mit kleiner Verzögerung auf, oft 50–100 ms. Einmal in einem ruhigen Raum kalibrieren misst diese Verzögerung, damit der Coach wenige Millisekunden zu früh von zu spät unterscheiden kann."),
        ("Darf mein Kind die App nutzen?", "Ja. Die App hat keine Konten, keine Werbung, keinen Chat und erhebt keine personenbezogenen Daten. Käufe laufen über Google Play, also kann Family Link die Zustimmung eines Elternteils verlangen."),
        ("Wie kündige ich das Abo?", "In der Google-Play-App: auf dein Profilbild tippen, dann Zahlungen &amp; Abos, dann Abos. Du erreichst es auch über den Premium-Bildschirm der App."),
        ("Ich habe ein neues Handy. Zahle ich noch mal?", "Nein. Melde dich mit demselben Google-Konto an und tippe auf dem Premium-Bildschirm auf „Käufe wiederherstellen“."),
    ],
    support_h="Support",
    support_text="Einen Fehler gefunden, eine Idee für eine Lektion oder Hilfe bei einem Kauf nötig? Schreib uns, und bei einem Problem nenn bitte dein Handymodell und deine Android-Version.",
    write="An den Support schreiben",
    privacy="Datenschutzerklärung", privacy_url="privacy/#de",
    footer="Drum Trainer &amp; Metronome",
)


def icon(name: str) -> str:
    return f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{ICONS[name]}"/></svg>'


def page(t: dict) -> str:
    r = t["root"]
    nav_ids = ("features", "pricing", "faq", "support")
    nav = "".join(f'<a href="#{i}">{label}</a>' for i, label in zip(nav_ids, t["nav"]))
    features = "".join(
        f'<article class="feature"><div class="icon">{icon(ic)}</div>'
        f'<h3>{h}<span class="tag{" premium" if prem else ""}">{t["premium"] if prem else t["free"]}</span></h3><p>{p}</p></article>'
        for ic, h, p, prem in t["features"]
    )
    shots = "".join(
        f'<figure><div class="phone"><img src="{r}assets/shots/{t["lang"]}/{n}.webp" width="720" height="1600" loading="lazy" alt="{c}"></div><figcaption>{c}</figcaption></figure>'
        for n, c in t["shots"]
    )
    plans = "".join(
        f'<div class="plan{" best" if best else ""}"><h3>{name}</h3><div class="price">{price}<small>{per}</small></div>'
        f'<div class="note">{note}</div><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></div>'
        for name, price, per, note, items, best in t["plans"]
    )
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['description']}">
<meta property="og:title" content="{t['title']}">
<meta property="og:description" content="{t['description']}">
<meta property="og:image" content="https://giobinda.github.io/drum-trainer/assets/shots/en/coach.webp">
<link rel="icon" href="{r}assets/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/apple-touch-icon.png">
<link rel="alternate" hreflang="en" href="https://giobinda.github.io/drum-trainer/">
<link rel="alternate" hreflang="de" href="https://giobinda.github.io/drum-trainer/de/">
<link rel="stylesheet" href="{r}assets/style.css">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="./"><img src="{r}assets/icon.svg" alt="">Drum Trainer</a>
  <nav>{nav}<a class="lang" href="{t['other_lang']}">{t['other_label']}</a></nav>
</div></header>

<main>
<div class="wrap hero">
  <div>
    <h1>{t['h1']}</h1>
    <p class="lead">{t['lead']}</p>
    <div class="buttons">
      <span class="button soon">{t['soon']}</span>
      <a class="button ghost" href="#features">{t['see']}</a>
    </div>
    <p class="small">{t['soon_small']}</p>
  </div>
  <div class="phones">
    <div class="phone"><img src="{r}assets/shots/{t["lang"]}/coach.webp" width="720" height="1600" alt="{t['shots'][2][1]}"></div>
    <div class="phone"><img src="{r}assets/shots/{t["lang"]}/lesson.webp" width="720" height="1600" alt="{t['shots'][1][1]}"></div>
  </div>
</div>

<section id="features"><div class="wrap">
  <h2>{t['features_h']}</h2>
  <p class="intro">{t['features_intro']}</p>
  <div class="features">{features}</div>
  <div class="private">{icon('lock').replace('<svg', '<svg')}<p>{t['private']}</p></div>
</div></section>

<section><div class="wrap">
  <h2>{t['shots_h']}</h2>
  <div class="gallery">{shots}</div>
</div></section>

<section id="pricing"><div class="wrap">
  <h2>{t['pricing_h']}</h2>
  <p class="intro">{t['pricing_intro']}</p>
  <div class="plans">{plans}</div>
  <p class="small">{t['pricing_note']}</p>
</div></section>

<section id="faq"><div class="wrap">
  <h2>{t['faq_h']}</h2>
  {faq}
</div></section>

<section id="support"><div class="wrap">
  <div class="support">
    <h2>{t['support_h']}</h2>
    <p>{t['support_text']}</p>
    <a class="button" href="mailto:{MAIL}">{t['write']}</a>
    <p class="small">{MAIL}</p>
  </div>
</div></section>
</main>

<footer><div class="wrap">
  <span>© 2026 {t['footer']}</span>
  <span><a href="{r}{t['privacy_url']}">{t['privacy']}</a> · <a href="mailto:{MAIL}">{MAIL}</a> · <a href="{t['other_lang']}">{t['other_label']}</a></span>
</div></footer>
</body>
</html>
"""


(ROOT / "index.html").write_text(page(EN))
(ROOT / "de").mkdir(exist_ok=True)
(ROOT / "de" / "index.html").write_text(page(DE))
print("built index.html and de/index.html")
