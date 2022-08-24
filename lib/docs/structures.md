# Information to make the scrapes possible

As I go through the sites I will be adding information about:

- XHR requests,
- XPATH selectors,
- CSS selectors,
- API endpoints, and
- Data structures.

## Sites to scrape

- [Gwasi.com](https://gwasi.com)
  - Contains a much more easily accessible list of what content is available and whether or not it is on Soundgasm.
- [Soundgasm.com](https://soundgasm.com)
  - The site's creator has expressed his feelings that it is not worth obfuscating the content in a way that prevents scraping.

### Gwasi approach

While the Gwasi site refers to GoneWildAudio on Reddit, it may be possible to create a list of Soundgasm usernames from the information it pulls down.

The front page of Gwasi pulls down two requests for json, one from [delta.json](https://gwasi.com/delta.json) and one from [base_8e9caeff4e.json](https://gwasi.com/base_8e9caeff4e.json).

The json from delta.json seemed cleaner and more complete, so at first we're using that. It returns a json document with the following top-level objects:

```javascript
base	"8e9caeff4e"
entries	[ […], […], […], […], […], […], […], […], […], […], … ]
fills	Object { 5lwcs5: […], 8ri33v: […], 8yphfg: […], … }
flairs	Object { "...wut?": "#dadada", "2nd Cumming": "#349e48", 2ndCumming: "#46d160", … }
newest	1661312676
oldest	1661301844
removed	[ "34bbfl", "3ec45o", "3pfr1n", "4o35fy", "72upd5", "8mla8t", "b8qqr5", "faz22s", "fbtq2h", "fvibph", … ]
scores	[ 3, 5, 0, 2, -1, 2, -3, 0, 7, 0, … ]
```

The "entries" object contained a list of the results for each audio that means the most for us. So while the whole document will be backed up, we'll only be using the "entries" key for actual scraping.

The value for the "entries" key is a list of lists, an example of their structure below:

```json
[
    [
        "wsn9qb",
        "GonewildAudible",
        "AEMCE",
        "",
        "[FF4M] Helping You Rape Our Hot Virgin Roommate [FDom][fsub][MDom Listener][Script Fill][Collab][Rape][Noncon][Slaps][Cruel][Forced][Struggling][Doggy][Hand Gag][Muffled][Whimpers][Begging][Pain][Creampie][Rough][SFX][AMC][12m37s]",
        1660938941,
        100,
    ],
    [
        "wu8sqr",
        "gonewildaudio",
        "AGreatView",
        "Ramblefap",
        "[M4F]Ride My Edge [Two Orgasms][Edging][using my cum as lube][Pre-cum][wet sounds][fleshlight][shakey moans][laughing][mdom][msub][stroking] mentions of:[69][edgeplay][mutual masturbation][Public teasing][Public edging][Facial][fingering][Creampie][Ramblefap]",
        1661112197,
        122,
    ],
    [
        "wsytww",
        "gonewildaudio",
        "ASMRdotWav",
        "Script Fill",
        "[Script Fill] [F4M] Nine Tails of Love [Azur Lane] [Kaga] [Romance] [Bride] [Married Sex] [Wife Experience] [Consent] [L-Bombs] [Kitsune] [Virgins] [Impregnation] [Aftercare] [Reverse Comfort] [Kuudere] [Small Tits]",
        1660971997,
        57,
    ],
    [
        "wvqbqs",
        "GWAScriptGuild",
        "ASirenAndAScribe",
        "Script Offer",
        "[F4M] [Script Offer] Silent Angel [Established Relationship] [Crying] [Grief] [Consolation] [FDom] [Msub] [Kissing] [Fingering] [Strapon] [Pegging] [Handjob] [Biting] [Love] [Marking] [Cunnilingus] [Snuggles]",
        1661265022,
        12,
    ],
    [
        "wsliux",
        "gonewildaudio",
        "A_Plutonian_Bird",
        "Ramblefap",
        "[M4F]I've been thinking about something...[Ramblefap][Moaning][Breathy][Wet Sounds][Breathy][Real Orgasm][Countdown][Cumming Together][Mutual Masturbation][Fantasy][Leg Grinding][Relaxed]",
        1660934506,
        13,
    ],
]

```

## The problem with this data

Sadly this doesn't give us a link to any soundgasm pages or even tell us which users are on soundgasm or not. It is worth making a list of users:

```python
user_list = []

for entry in payload['entries']:
    user_list.append(entry[2])
```

With this we can iterate through potential soundgasm user pages:

