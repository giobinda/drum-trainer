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
    "usb": "M15,7v4h1v2h-3V5h2l-3,-4l-3,4h2v8H8v-2.07c0.7,-0.37 1.2,-1.08 1.2,-1.93c0,-1.21 -0.99,-2.2 -2.2,-2.2"
           "S4.8,7.79 4.8,9c0,0.85 0.5,1.56 1.2,1.93V13c0,1.11 0.89,2 2,2h3v3.05c-0.71,0.37 -1.2,1.1 -1.2,1.95"
           "c0,1.22 0.99,2.2 2.2,2.2s2.2,-0.98 2.2,-2.2c0,-0.85 -0.49,-1.58 -1.2,-1.95V15h3c1.11,0 2,-0.89 2,-2v-2h1V7h-4z",
    "lock": "M18,8h-1V6c0,-2.76 -2.24,-5 -5,-5S7,3.24 7,6v2H6c-1.1,0 -2,0.9 -2,2v10c0,1.1 0.9,2 2,2h12"
            "c1.1,0 2,-0.9 2,-2V10c0,-1.1 -0.9,-2 -2,-2zM9,6c0,-1.66 1.34,-3 3,-3s3,1.34 3,3v2H9V6z",
}

EN = dict(
    lang="en", root="", other_lang="de/", other_label="Deutsch",
    title="Drum Trainer & Metronome – learn the drums in time",
    description="A metronome made for learning the drums: 26 lessons, a timing coach that hears whether you're early or late, and practice streaks. For Android.",
    nav=("Features", "E-drums", "Pricing", "FAQ", "Support"),
    h1="Learn the drums with a metronome that <em>listens</em>.",
    lead="Drum Trainer &amp; Metronome takes you from your very first beat to full grooves: step-by-step lessons, a timing coach that hears whether you're early or late, and a practice streak to keep you going. Plug in your e-drum over USB and every pad is timed exactly.",
    soon="Coming soon to Google Play", soon_small="Android 8 and newer", see="Connect your e-drum",
    features_h="Everything a beginner needs, nothing in the way",
    features_intro="Built by a beginner drummer, for beginner drummers on acoustic kits, e-drums and practice pads.",
    free="Free", premium="Premium",
    features=[
        ("metronome", "A clear, steady metronome", "Every common time signature, quarters to sixteenths and triplets, tap tempo and a choice of click sounds. The rhythm is drawn as real notation, so you see what you hear.", False),
        ("lessons", "26 step-by-step lessons", "From counting along and your first strokes to the basic rock beat, fills and sixteenths. Each lesson has a start tempo, a goal, tips and a two-bar count-in.", True),
        ("mic", "A timing coach that listens", "Play and two dials show whether you're ahead of or behind the click, and how even your strokes are. It hears an acoustic kit or a practice pad through the microphone, and an e-drum exactly over USB.", True),
        ("hands", "Every limb on its own", "Practise with the right hand, the left, hands only or kick only. With an e-drum, each drum gets its own timing, and the coach tells you when kick and snare don't land together.", True),
        ("progress", "Progress you can see", "A practice calendar, timing trends over your sessions and a journal for notes on each day.", True),
        ("streak", "Streaks, badges and reminders", "Set how often you want to practise, get a reminder at your time, and earn badges for days and weeks in a row.", True),
    ],
    edrum_callout="<strong>Made for electronic kits.</strong> Plug your e-drum into the phone with a USB cable and the coach reads every pad directly: exact to the millisecond, each drum timed on its own, no microphone needed.",
    edrum_link="How to connect",
    private="<strong>Your microphone stays private.</strong> What the timing coach hears is analysed on your phone, never saved and never sent anywhere. No account, no ads, no tracking.",
    shots_h="A look inside",
    shots=[("metronome", "The free metronome"), ("lesson", "A lesson, ready to play"), ("coach", "The timing coach"),
           ("lessons", "26 lessons in four levels"), ("progress", "Calendar and badges"), ("badges", "Badges for your streaks")],
    pricing_h="Simple pricing",
    pricing_intro="The metronome is free, always. Premium unlocks the coaching, and you can try all of it free for 7 days.",
    plans=[
        ("Free", "€0", "", "", ["The full metronome", "Notation for every rhythm", "Tap tempo and click sounds", "Light and dark themes"], False),
        ("Premium monthly", "€1.99", " / month", "7 days free", ["All 26 lessons", "The timing coach, for e-drums over USB too", "Progress, journal and calendar", "Streak badges and reminders", "Cancel anytime in Google Play"], False),
        ("Premium lifetime", "€19.99", " once", "Best value", ["Everything in Premium", "Pay once, keep it forever", "No subscription to manage", "Restores on a new phone"], True),
    ],
    pricing_note="Prices in euros; Google Play shows the price for your country. Cancel the monthly plan during the free week and you pay nothing.",
    faq_h="Questions",
    faq=[
        ("Does it work with an electronic drum kit?", "Yes, and that's where it's best. Connect the module by USB (see <a href=\"#edrum\">Connect your e-drum</a>) and the coach reads every pad directly: exact timing for each drum, no microphone, any volume. If your module has no USB port, choose “Pad / e-drum” in the Mic settings and the microphone listens for the stick tapping the pads."),
        ("Which e-drums work?", "Any module that sends MIDI over USB, which includes most current kits. Look for a port marked USB, USB MIDI or “to host” on the module. Older modules with only a round 5-pin MIDI socket work through a USB-MIDI interface cable."),
        ("Does the app record me?", "No. The microphone is analysed live on your phone to time your strokes. The last few seconds are kept in memory for “listen back” and then thrown away. Nothing is saved or uploaded."),
        ("Why should I calibrate?", "Every phone plays and records sound with a small delay, often 50–100 ms. Calibrating once, in a quiet room, measures that delay so the coach can tell a few milliseconds early from late."),
        ("Can my child use it?", "Yes. The app has no accounts, ads or chat and collects no personal data. Purchases go through Google Play, so Family Link can ask a parent to approve them."),
        ("How do I cancel the subscription?", "In the Google Play app: tap your profile picture, then Payments &amp; subscriptions, then Subscriptions. You can also open it from the app's Premium screen."),
        ("I have a new phone. Do I pay again?", "No. Sign in with the same Google account and tap “Restore purchases” on the Premium screen."),
    ],
    edrum_h="Connect your e-drum",
    edrum_intro="With an electronic kit the coach doesn't need the microphone. The module tells the app which pad you hit and when, to the millisecond. Kick, snare and hi-hat each get their own timing, and the click can never be mistaken for a hit.",
    edrum_steps=[
        ("Find the USB port on your drum module", "Usually on the back or side, marked USB, USB MIDI or “to host”. It's one of these shapes:", "connectors"),
        ("Get a cable to your phone", "One cable with the module's plug on one end and USB-C on the other, or the module's usual USB cable plus a small USB-C adapter (often sold as “OTG”). It must be a data cable: some cheap ones only charge.", None),
        ("Plug in and switch the module on", "The phone sees the kit straight away. There's nothing to install or pair.", "setup"),
        ("Choose your kit in the app", "Tap <strong>Mic</strong>, and under <strong>Listen to</strong> pick your kit. It's remembered for next time.", "midi-dialog"),
        ("Play", "Each drum gets its own timing, and the coach points out drums that should sound together but don't, like a kick landing before the snare.", "midi-panel"),
    ],
    edrum_notes=[
        "Only a round 5-pin MIDI socket? A USB-MIDI interface cable connects it the same way.",
        "Hear the click through the phone's speaker or wired headphones. Bluetooth headphones add a delay, so avoid them for the click.",
    ],
    setup_labels=("Drum module", "USB data cable", "Phone"),
    connector_labels=("On the module, one of these:", "USB-B", "Micro-USB", "USB-C", "On the phone:", "USB-C"),
    shot_alts=("The Mic settings with the e-drum chosen under Listen to", "The timing coach with each drum's timing"),
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
    nav=("Funktionen", "E-Drums", "Preise", "Fragen", "Support"),
    h1="Schlagzeug lernen mit einem Metronom, das <em>zuhört</em>.",
    lead="Drum Trainer &amp; Metronome bringt dich vom allerersten Schlag bis zu ganzen Grooves: Lektionen Schritt für Schritt, ein Timing-Coach, der hört, ob du zu früh oder zu spät bist, und Übungsserien, die dich dranbleiben lassen. Schließ dein E-Drum per USB an, und jedes Pad wird genau getimt.",
    soon="Bald bei Google Play", soon_small="Android 8 und neuer", see="E-Drum verbinden",
    features_h="Alles, was Einsteiger brauchen, nichts, was stört",
    features_intro="Von einem Schlagzeug-Anfänger für Anfänger gebaut, für akustische Sets, E-Drums und Übungspads.",
    free="Gratis", premium="Premium",
    features=[
        ("metronome", "Ein klares, stabiles Metronom", "Alle gängigen Taktarten, Viertel bis Sechzehntel und Triolen, Tap-Tempo und verschiedene Klicks. Der Rhythmus wird als echte Notenschrift gezeigt, damit du siehst, was du hörst.", False),
        ("lessons", "26 Lektionen Schritt für Schritt", "Vom Mitzählen und ersten Schlägen bis zum einfachen Rockbeat, Fills und Sechzehnteln. Jede Lektion hat ein Starttempo, ein Ziel, Tipps und zwei Takte zum Einzählen.", True),
        ("mic", "Ein Timing-Coach, der zuhört", "Spiel los, und zwei Anzeigen zeigen, ob du vor oder hinter dem Klick liegst und wie gleichmäßig deine Schläge sind. Er hört akustische Sets und Übungspads übers Mikrofon und E-Drums exakt per USB.", True),
        ("hands", "Jede Hand, jeder Fuß einzeln", "Übe nur mit rechts, nur mit links, nur mit den Händen oder nur mit dem Fuß. Mit E-Drums bekommt jede Trommel ihr eigenes Timing, und der Coach sagt dir, wenn Bassdrum und Snare nicht zusammen kommen.", True),
        ("progress", "Fortschritt, den du siehst", "Ein Übungskalender, dein Timing-Verlauf über die Einheiten und ein Tagebuch für Notizen zu jedem Tag.", True),
        ("streak", "Serien, Abzeichen und Erinnerungen", "Leg fest, wie oft du üben willst, lass dich zu deiner Zeit erinnern und sammle Abzeichen für Tage und Wochen in Folge.", True),
    ],
    edrum_callout="<strong>Gemacht für E-Drums.</strong> Schließ dein E-Drum per USB-Kabel ans Handy an, und der Coach liest jedes Pad direkt: millisekundengenau, jede Trommel einzeln getimt, ganz ohne Mikrofon.",
    edrum_link="So verbindest du es",
    private="<strong>Dein Mikrofon bleibt privat.</strong> Was der Timing-Coach hört, wird auf deinem Handy ausgewertet, nie gespeichert und nirgendwohin gesendet. Kein Konto, keine Werbung, kein Tracking.",
    shots_h="Ein Blick hinein",
    shots=[("metronome", "Das kostenlose Metronom"), ("lesson", "Eine Lektion, bereit zum Spielen"), ("coach", "Der Timing-Coach"),
           ("lessons", "26 Lektionen in vier Stufen"), ("progress", "Kalender und Abzeichen"), ("badges", "Abzeichen für deine Serien")],
    pricing_h="Einfache Preise",
    pricing_intro="Das Metronom ist kostenlos, für immer. Premium schaltet das Coaching frei, und du kannst alles 7 Tage gratis testen.",
    plans=[
        ("Gratis", "0 €", "", "", ["Das komplette Metronom", "Notenschrift für jeden Rhythmus", "Tap-Tempo und Klick-Klänge", "Helle und dunkle Designs"], False),
        ("Premium monatlich", "1,99 €", " / Monat", "7 Tage gratis", ["Alle 26 Lektionen", "Der Timing-Coach, auch für E-Drums per USB", "Fortschritt, Tagebuch und Kalender", "Serien-Abzeichen und Erinnerungen", "Jederzeit in Google Play kündbar"], False),
        ("Premium dauerhaft", "19,99 €", " einmalig", "Bester Preis", ["Alles aus Premium", "Einmal zahlen, für immer behalten", "Kein Abo zu verwalten", "Auch auf einem neuen Handy"], True),
    ],
    pricing_note="Preise in Euro; Google Play zeigt den Preis für dein Land. Kündigst du das Monatsabo in der Gratiswoche, zahlst du nichts.",
    faq_h="Fragen",
    faq=[
        ("Funktioniert es mit einem E-Drum-Set?", "Ja, und damit am besten. Verbinde das Modul per USB (siehe <a href=\"#edrum\">E-Drum verbinden</a>), und der Coach liest jedes Pad direkt: genaues Timing für jede Trommel, ohne Mikrofon, bei jeder Lautstärke. Hat dein Modul keinen USB-Anschluss, wähle in den Mikro-Einstellungen „Pad / E-Drum“, dann hört das Mikrofon auf das Tippen der Sticks."),
        ("Welche E-Drums funktionieren?", "Jedes Modul, das MIDI über USB sendet, und das tun die meisten aktuellen Sets. Such am Modul einen Anschluss mit der Aufschrift USB, USB MIDI oder „to host“. Ältere Module mit nur einer runden 5-poligen MIDI-Buchse gehen über ein USB-MIDI-Interface-Kabel."),
        ("Nimmt die App mich auf?", "Nein. Das Mikrofon wird live auf deinem Handy ausgewertet, um deine Schläge zu timen. Die letzten Sekunden bleiben für „Anhören“ im Arbeitsspeicher und werden dann verworfen. Nichts wird gespeichert oder hochgeladen."),
        ("Warum soll ich kalibrieren?", "Jedes Handy spielt und nimmt Ton mit kleiner Verzögerung auf, oft 50–100 ms. Einmal in einem ruhigen Raum kalibrieren misst diese Verzögerung, damit der Coach wenige Millisekunden zu früh von zu spät unterscheiden kann."),
        ("Darf mein Kind die App nutzen?", "Ja. Die App hat keine Konten, keine Werbung, keinen Chat und erhebt keine personenbezogenen Daten. Käufe laufen über Google Play, also kann Family Link die Zustimmung eines Elternteils verlangen."),
        ("Wie kündige ich das Abo?", "In der Google-Play-App: auf dein Profilbild tippen, dann Zahlungen &amp; Abos, dann Abos. Du erreichst es auch über den Premium-Bildschirm der App."),
        ("Ich habe ein neues Handy. Zahle ich noch mal?", "Nein. Melde dich mit demselben Google-Konto an und tippe auf dem Premium-Bildschirm auf „Käufe wiederherstellen“."),
    ],
    edrum_h="E-Drum verbinden",
    edrum_intro="Mit einem E-Drum braucht der Coach kein Mikrofon. Das Modul sagt der App, welches Pad du wann getroffen hast, auf die Millisekunde. Bassdrum, Snare und Hi-Hat bekommen ihr eigenes Timing, und der Klick kann nie für einen Schlag gehalten werden.",
    edrum_steps=[
        ("Such den USB-Anschluss am Drum-Modul", "Meist hinten oder seitlich, beschriftet mit USB, USB MIDI oder „to host“. Er hat eine dieser Formen:", "connectors"),
        ("Besorg ein Kabel zum Handy", "Ein Kabel mit dem Stecker des Moduls an einem Ende und USB-C am anderen, oder das übliche USB-Kabel des Moduls plus ein kleiner USB-C-Adapter (oft als „OTG“ verkauft). Es muss ein Datenkabel sein: Manche billigen Kabel laden nur.", None),
        ("Einstecken und Modul einschalten", "Das Handy erkennt das Set sofort. Nichts zu installieren oder zu koppeln.", "setup"),
        ("Set in der App wählen", "Tippe auf <strong>Mikro</strong> und wähle unter <strong>Hören auf</strong> dein Set. Die Wahl bleibt gespeichert.", "midi-dialog"),
        ("Spielen", "Jede Trommel bekommt ihr eigenes Timing, und der Coach zeigt dir Trommeln, die zusammen kommen sollten, es aber nicht tun, etwa eine Bassdrum vor der Snare.", "midi-panel"),
    ],
    edrum_notes=[
        "Nur eine runde 5-polige MIDI-Buchse? Ein USB-MIDI-Interface-Kabel verbindet sie genauso.",
        "Hör den Klick über den Handylautsprecher oder kabelgebundene Kopfhörer. Bluetooth-Kopfhörer verzögern den Klick, also besser nicht.",
    ],
    setup_labels=("Drum-Modul", "USB-Datenkabel", "Handy"),
    connector_labels=("Am Modul, eine dieser Formen:", "USB-B", "Micro-USB", "USB-C", "Am Handy:", "USB-C"),
    shot_alts=("Die Mikro-Einstellungen mit dem E-Drum unter Hören auf", "Der Timing-Coach mit dem Timing jeder Trommel"),
    support_h="Support",
    support_text="Einen Fehler gefunden, eine Idee für eine Lektion oder Hilfe bei einem Kauf nötig? Schreib uns, und bei einem Problem nenn bitte dein Handymodell und deine Android-Version.",
    write="An den Support schreiben",
    privacy="Datenschutzerklärung", privacy_url="privacy/#de",
    footer="Drum Trainer &amp; Metronome",
)


def icon(name: str) -> str:
    return f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{ICONS[name]}"/></svg>'


def svg_setup(t: dict) -> str:
    module, cable, phone = t["setup_labels"]
    pads = "".join(f'<rect x="{70 + i * 52}" y="168" width="40" height="22" rx="6" fill="var(--bg)"/>' for i in range(4))
    return f"""<svg class="illustration" viewBox="0 0 720 300" role="img" aria-label="{module} → {cable} → {phone}">
  <text x="165" y="50" text-anchor="middle" class="label">{module}</text>
  <rect x="40" y="66" width="250" height="150" rx="18" fill="var(--raised)" stroke="var(--outline)" stroke-width="2"/>
  <rect x="68" y="92" width="112" height="50" rx="8" fill="var(--bg)"/>
  <text x="124" y="124" text-anchor="middle" class="screen">KIT 01</text>
  <circle cx="220" cy="117" r="17" fill="var(--bg)"/><circle cx="262" cy="117" r="11" fill="var(--bg)"/>
  {pads}
  <rect x="284" y="134" width="18" height="24" rx="3" fill="var(--text)"/>
  <path d="M302,146 C400,146 420,286 556,286 L586,286 L586,266" fill="none" stroke="var(--accent)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="370" y="262" text-anchor="middle" class="label accent">{cable}</text>
  <text x="586" y="22" text-anchor="middle" class="label">{phone}</text>
  <rect x="516" y="34" width="140" height="232" rx="24" fill="var(--raised)" stroke="var(--outline)" stroke-width="2"/>
  <rect x="528" y="56" width="116" height="190" rx="10" fill="var(--bg)"/>
  <rect x="540" y="76" width="64" height="8" rx="4" fill="var(--outline)"/>
  <rect x="540" y="100" width="92" height="26" rx="13" fill="var(--accent)"/>
  <text x="586" y="118" text-anchor="middle" class="chip">USB</text>
  <rect x="540" y="140" width="80" height="8" rx="4" fill="var(--outline)"/>
  <rect x="540" y="160" width="60" height="8" rx="4" fill="var(--outline)"/>
  <circle cx="560" cy="210" r="18" fill="var(--accent)"/>
</svg>"""


def svg_connectors(t: dict) -> str:
    module, b, micro, c, phone, phone_c = t["connector_labels"]
    return f"""<svg class="illustration" viewBox="0 0 720 210" role="img" aria-label="{module} {b}, {micro}, {c}. {phone} {phone_c}">
  <text x="20" y="34" class="label">{module}</text>
  <g transform="translate(40,60)">
    <path d="M16,0 H64 L80,16 V80 H0 V16 Z" fill="var(--raised)" stroke="var(--text)" stroke-width="3"/>
    <rect x="22" y="26" width="36" height="34" rx="3" fill="var(--text)"/>
  </g>
  <text x="80" y="176" text-anchor="middle" class="label small">{b}</text>
  <g transform="translate(170,84)">
    <path d="M6,0 H82 L74,30 H14 Z" fill="var(--raised)" stroke="var(--text)" stroke-width="3" stroke-linejoin="round"/>
    <rect x="20" y="10" width="48" height="8" rx="2" fill="var(--text)"/>
  </g>
  <text x="214" y="176" text-anchor="middle" class="label small">{micro}</text>
  <g transform="translate(300,82)">
    <rect x="0" y="0" width="96" height="34" rx="17" fill="var(--raised)" stroke="var(--text)" stroke-width="3"/>
    <rect x="18" y="13" width="60" height="8" rx="4" fill="var(--text)"/>
  </g>
  <text x="348" y="176" text-anchor="middle" class="label small">{c}</text>
  <path d="M440,99 H530" stroke="var(--accent)" stroke-width="6" stroke-linecap="round"/>
  <path d="M516,85 L534,99 L516,113" fill="none" stroke="var(--accent)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="560" y="34" class="label">{phone}</text>
  <g transform="translate(570,82)">
    <rect x="0" y="0" width="96" height="34" rx="17" fill="var(--accent)"/>
    <rect x="18" y="13" width="60" height="8" rx="4" fill="var(--on-accent)"/>
  </g>
  <text x="618" y="176" text-anchor="middle" class="label small">{phone_c}</text>
</svg>"""


def edrum_section(t: dict) -> str:
    r = t["root"]
    alts = dict(zip(("midi-dialog", "midi-panel"), t["shot_alts"]))

    def figure(kind):
        if kind is None:
            return ""
        if kind == "setup":
            return f'<figure class="art">{svg_setup(t)}</figure>'
        if kind == "connectors":
            return f'<figure class="art">{svg_connectors(t)}</figure>'
        return (f'<figure class="shot"><img src="{r}assets/shots/{t["lang"]}/{kind}.webp" width="640" '
                f'loading="lazy" alt="{alts[kind]}"></figure>')

    steps = "".join(
        f'<li><div class="step-text"><h3>{h}</h3><p>{p}</p></div>{figure(kind)}</li>'
        for h, p, kind in t["edrum_steps"]
    )
    notes = "".join(f"<li>{n}</li>" for n in t["edrum_notes"])
    return f"""<section id="edrum"><div class="wrap">
  <h2>{t['edrum_h']}</h2>
  <p class="intro">{t['edrum_intro']}</p>
  <ol class="steps">{steps}</ol>
  <ul class="notes">{notes}</ul>
</div></section>"""


def page(t: dict) -> str:
    r = t["root"]
    nav_ids = ("features", "edrum", "pricing", "faq", "support")
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
      <a class="button ghost" href="#edrum">{icon('usb')} {t['see']}</a>
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
  <div class="callout">{icon('usb')}<p>{t['edrum_callout']} <a href="#edrum">{t['edrum_link']} →</a></p></div>
  <div class="private">{icon('lock')}<p>{t['private']}</p></div>
</div></section>

<section><div class="wrap">
  <h2>{t['shots_h']}</h2>
  <div class="gallery">{shots}</div>
</div></section>

{edrum_section(t)}

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
