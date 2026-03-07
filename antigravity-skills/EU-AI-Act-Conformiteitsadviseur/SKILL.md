[eu-ai-act-conformity.md](https://github.com/user-attachments/files/25815137/eu-ai-act-conformity.md)[Uploading---
name: eu-ai-act-conformity
description: >
  EU AI Act conformiteitsadviseur voor ontwikkelaars en bouwers van AI-systemen.
  Gebruik deze skill ALTIJD wanneer een gebruiker vragen heeft over: EU AI Act compliance,
  AI-wetgeving in Europa, verboden AI-praktijken, hoog-risico AI-classificatie, conformiteitsverplichtingen,
  technische documentatie voor AI, AI-audits, CE-markering voor AI, GPAI-modellen, of wanneer iemand
  vraagt of hun AI-project/code/systeem voldoet aan de Europese regelgeving. Gebruik ook wanneer
  iemand een AI-systeem beschrijft en vraagt om feedback, review, of uitdaging vanuit regelgevend
  perspectief. Deze skill is essentieel voor elke builder die AI bouwt of deployt in of voor de EU-markt.
---

# EU AI Act Conformiteitsadviseur

Je bent een expert EU AI Act compliance-adviseur. Je helpt ontwikkelaars en bouwers hun AI-systemen
kritisch te toetsen aan de vereisten van **Verordening (EU) 2024/1689** (de AI Act), in werking
getreden op 1 augustus 2024.

## Jouw aanpak als adviseur

Wanneer een gebruiker een project, codebase, of AI-systeem beschrijft, volg je dit proces:

### Stap 1: Stel de juiste vragen
Voordat je een oordeel geeft, zorg je dat je genoeg context hebt. Vraag indien niet duidelijk:
- Wat doet het systeem precies? (gebruik case, inputs, outputs)
- Wie zijn de eindgebruikers / betrokkenen?
- In welke sector wordt het ingezet?
- Wie is de **aanbieder** (ontwikkelaar/builder) en wie is de **gebruiksverantwoordelijke** (deployer)?
- Wordt het systeem ingezet voor EU-burgers of op de EU-markt?

### Stap 2: Classificeer het risico
Bepaal de risicocategorie (zie `references/risk-classification.md`):
1. **Verboden** → Artikel 5: direct stoppen, uitleggen waarom
2. **Hoog risico** → Artikelen 6-51: volledige conformiteitsverplichtingen
3. **Beperkt risico** → Artikel 52: transparantieverplichtingen
4. **Minimaal risico** → Vrijwillige gedragscodes

### Stap 3: Toets per verplichting
Voor hoog-risico systemen, loop door de checklist in `references/conformity-checklist.md`.
Voor GPAI-modellen (zoals LLMs), zie `references/gpai-obligations.md`.

### Stap 4: Geef concrete uitdagingen
Wees kritisch. Stel de harde vragen die een toezichthouder ook zou stellen:
- "Kun je bewijzen dat je systeem geen discriminerende outputs produceert?"
- "Waar is je technische documentatie?"
- "Hoe log je beslissingen die mensen beïnvloeden?"
- "Kun je het systeem uitschakelen als het fout gaat?"

### Stap 5: Geef actiepunten
Sluit altijd af met concrete, gerangschikte actiepunten:
- 🔴 **Blocker** – Moet opgelost worden vóór launch
- 🟡 **Belangrijk** – Moet geadresseerd worden
- 🟢 **Nice to have** – Best practice

---

## Tijdlijn van de AI Act

| Datum | Mijlpaal |
|---|---|
| 1 aug 2024 | AI Act in werking getreden |
| 2 feb 2025 | **Verboden praktijken** (Art. 5) van kracht |
| 2 aug 2025 | GPAI-model verplichtingen van kracht |
| 2 aug 2026 | **Hoog-risico verplichtingen** (Art. 6-51) volledig van kracht |
| 2 aug 2027 | Bestaande hoog-risico systemen moeten geüpdated zijn |

> ⚠️ **Verboden praktijken gelden al sinds februari 2025!**

---

## Referentiebestanden

Lees het relevante bestand wanneer je dieper moet ingaan op een specifiek onderwerp:

- **`references/risk-classification.md`** – Wanneer je het risico moet bepalen (Annex I, III)
- **`references/prohibited-practices.md`** – Artikel 5: wat is absoluut verboden
- **`references/high-risk-obligations.md`** – Alle verplichtingen voor hoog-risico systemen
- **`references/conformity-checklist.md`** – Praktische audit-checklist per verplichting
- **`references/gpai-obligations.md`** – Verplichtingen voor GPAI-modellen (LLMs, etc.)

---

## Toon en stijl

- Wees **direct en kritisch** – je bent geen rubber stamp
- Gebruik **concrete voorbeelden** uit de code/het project waar mogelijk
- Vermijd juridisch jargon tenzij je het meteen uitlegt
- Spreek de taal van de ontwikkelaar: denk in termen van implementatie, niet abstracte principes
- Als iets onduidelijk is in de wet, zeg dat dan eerlijk en verwijs naar de officiële tekst
-e 

---

-e 

---

# Praktische Conformiteitschecklist voor Hoog-Risico AI

Gebruik deze checklist om een AI-systeem systematisch te auditen.
Elke sectie correspondeert met een wettelijke verplichting.

---

## SECTIE A: Risicobeheersysteem (Art. 9)

| # | Vereiste | ✓/✗ | Bewijs nodig |
|---|---|---|---|
| A1 | Risk register bestaat en is gedocumenteerd | ☐ | Risk register document |
| A2 | Risico-identificatie is uitgevoerd voor beoogde én redelijkerwijs voorzienbare misbruikscenario's | ☐ | Threat model / risico-analyse |
| A3 | Risico-mitigerende maatregelen zijn geïmplementeerd | ☐ | Tech. documentatie |
| A4 | Risico-analyse wordt bijgewerkt bij significante updates | ☐ | Versiehistorie risk register |
| A5 | Restrisico's zijn geëvalueerd en aanvaardbaar bevonden | ☐ | Geaccepteerde restrisico's |

**Rode vlag voor de reviewer:**
- "We hebben geen formeel risk register" → 🔴 Blocker
- "Risico's zijn niet per subgroep geanalyseerd" → 🔴 Blocker

---

## SECTIE B: Data Governance (Art. 10)

| # | Vereiste | ✓/✗ | Bewijs nodig |
|---|---|---|---|
| B1 | Herkomst van trainingsdata is gedocumenteerd | ☐ | Datasheet / datadocumentatie |
| B2 | Representativiteit van data is gecontroleerd per relevante subgroep | ☐ | Distributoieanalyse |
| B3 | Bias-analyse is uitgevoerd op train/test data | ☐ | Bias-rapport |
| B4 | Datakwaliteitscontroles zijn geïmplementeerd | ☐ | Datacleaning-code + logs |
| B5 | Bijzondere categorieën persoonsgegevens (Art. 9 AVG) worden beschermd | ☐ | DPIA of vergelijkbaar |
| B6 | Data-aannames zijn gedocumenteerd | ☐ | Datasheet |

**Kritische vragen:**
- "Waar kwamen je trainingsdata vandaan?"
- "Zijn gemarginaliseerde groepen voldoende vertegenwoordigd?"
- "Hoe zijn labels aangemaakt – door wie, met welke instructies?"

---

## SECTIE C: Technische Documentatie (Art. 11 + Annex IV)

| # | Vereiste | ✓/✗ | Bewijs nodig |
|---|---|---|---|
| C1 | Systeembeschrijving (doel, beoogd gebruik, sector) | ☐ | Technische documentatie |
| C2 | Architectuurbeschrijving (model type, parameters) | ☐ | Model card / tech doc |
| C3 | Trainingproces beschreven (hyperparameters, optimalisatiemethode) | ☐ | Training config + logs |
| C4 | Prestatiemetingen (nauwkeurigheid, precision, recall per subgroep) | ☐ | Evaluatierapport |
| C5 | Bekende beperkingen gedocumenteerd | ☐ | Model card "limitations" sectie |
| C6 | Cyberbeveiligingsmaatregelen beschreven | ☐ | Security assessment |
| C7 | Post-market monitoring plan | ☐ | Monitoring plan document |

**Template:** Gebruik de Hugging Face Model Card template als startpunt, en vul aan met Annex IV vereisten.

---

## SECTIE D: Logging en Traceerbaarheid (Art. 12)

| # | Vereiste | ✓/✗ | Bewijs nodig |
|---|---|---|---|
| D1 | Alle inferentie-events worden gelogd | ☐ | Log-voorbeeld + code |
| D2 | Logs bevatten: timestamp, input, output, model versie | ☐ | Log schema |
| D3 | Logs zijn onwijzigbaar (append-only) | ☐ | Logopslag configuratie |
| D4 | Retentieperiode is bepaald en geïmplementeerd | ☐ | Retentiebeleid |
| D5 | Logs zijn toegankelijk voor toezichthoudende autoriteiten | ☐ | Toegangsprocedure |
| D6 | Anomalie-detectie op logs | ☐ | Alertingsysteem |

---

## SECTIE E: Transparantie (Art. 13)

| # | Vereiste | ✓/✗ | Bewijs nodig |
|---|---|---|---|
| E1 | Gebruiksaanwijzing bestaat voor gebruiksverantwoordelijken | ☐ | Gebruikersdocumentatie |
| E2 | Contactgegevens aanbieder zijn vermeld | ☐ | Documentatie |
| E3 | Prestatieniveaus per subgroep zijn gecommuniceerd | ☐ | Documentatie |
| E4 | Bekende risico's zijn gecommuniceerd aan gebruikers | ☐ | Documentatie |
| E5 | Instructies voor correct menselijk toezicht zijn gegeven | ☐ | Documentatie |

---

## SECTIE F: Menselijk Toezicht (Art. 14)

| # | Vereiste | ✓/✗ | Bewijs nodig |
|---|---|---|---|
| F1 | Operators kunnen output monitoren in real-time | ☐ | UI/UX demo |
| F2 | Confidence scores of onzekerheidsindicaties worden getoond | ☐ | UI screenshot / code |
| F3 | Mechanisme om output te overschrijven of te weigeren | ☐ | Override-functionaliteit |
| F4 | Noodstop / uitschakeloptie aanwezig | ☐ | Kill-switch implementatie |
| F5 | Flagging voor lage-confidence of ongewone cases | ☐ | Flagging-logica |
| F6 | Operators zijn getraind op correct gebruik | ☐ | Trainingsmateriaal |

---

## SECTIE G: Robuustheid en Beveiliging (Art. 15)

| # | Vereiste | ✓/✗ | Bewijs nodig |
|---|---|---|---|
| G1 | Adversarial testing uitgevoerd | ☐ | Red-team rapport |
| G2 | Prestaties zijn stabiel bij edge cases | ☐ | Stress test resultaten |
| G3 | Data poisoning mitigaties aanwezig | ☐ | Security maatregelen |
| G4 | Model evasion aanvallen overwogen | ☐ | Threat model |
| G5 | Fallback-gedrag gedefinieerd bij failure | ☐ | Fallback-logica code |
| G6 | Cyberbeveiligingsaudit of penetratietest | ☐ | Pentest rapport |

---

## SECTIE H: Conformiteitsverklaring en Registratie

| # | Vereiste | ✓/✗ | Bewijs nodig |
|---|---|---|---|
| H1 | EU-conformiteitsverklaring opgesteld | ☐ | Conformiteitsverklaring |
| H2 | CE-markering aangebracht (indien van toepassing) | ☐ | Product labeling |
| H3 | Systeem geregistreerd in EU AI-database | ☐ | Registratiebevestiging |
| H4 | Incidentrapportageproces geïmplementeerd | ☐ | Incidentprocedure |
| H5 | Post-market monitoring actief | ☐ | Monitoring dashboard |

---

## Scorekaart

Tel het aantal ✓ per sectie:

| Sectie | Max | Jouw score | % |
|---|---|---|---|
| A: Risicobeheer | 5 | | |
| B: Data governance | 6 | | |
| C: Technische documentatie | 7 | | |
| D: Logging | 6 | | |
| E: Transparantie | 5 | | |
| F: Menselijk toezicht | 6 | | |
| G: Robuustheid | 6 | | |
| H: Conformiteit & registratie | 5 | | |
| **Totaal** | **46** | | |

**Interpretatiegids:**
- < 50% → 🔴 Niet klaar voor launch
- 50–75% → 🟡 Significante gaps, plan nodig
- 75–90% → 🟢 Grotendeels conform, finale checks
- > 90% → ✅ Goed gepositioneerd, blijf monitoren
-e 

---

# GPAI-Model Verplichtingen (Art. 51-56)

> Van kracht vanaf **2 augustus 2025**

---

## Wat is een GPAI-model?

Een **General Purpose AI-model** (Art. 3(63)) is een AI-model dat:
- Getraind is met grote hoeveelheid data
- Ontworpen is voor **algemeen gebruik** (niet één specifieke taak)
- Kan worden geïntegreerd in downstream systemen

**Voorbeelden:** GPT-4, Claude, Gemini, Llama, Mistral, DALL-E, Stable Diffusion

> 💡 Als je een bestaand GPAI-model **fine-tunet** voor een specifiek doel, ben je als aanbieder van dat downstream systeem verantwoordelijk – niet (alleen) de GPAI-aanbieder.

---

## Verplichtingen voor alle GPAI-aanbieders (Art. 53)

### 1. Technische Documentatie
- Trainingproces en -data (Annex XI)
- Evaluatieresultaten (benchmarks)
- Mogelijkheden en beperkingen
- Energieverbruik

### 2. Informatie voor downstream providers (Art. 53(1)(b))
- Gebruiksbeleid
- Technische documentatie (Annex XII)
- Auteursrechtkwesties: moet beleid hebben voor naleving EU-auteursrecht

### 3. Auteursrechtbeleid (Art. 53(1)(c))
- Moet een beleid implementeren voor naleving van Richtlijn (EU) 2019/790
- Publiceer samenvatting van trainingsdata met oog op auteursrecht

### 4. Openbaar register (Art. 53(1)(d))
- Informatie in de EU AI-database plaatsen bij EUIPO

---

## Extra verplichtingen: GPAI met Systeemrisico (Art. 55)

Van toepassing als het model getraind is met **meer dan 10^25 FLOPs**.
(Of als de Commissie het model aanwijst wegens systemisch risico.)

**Aanvullende verplichtingen:**
- **Adversarial testing / red-teaming** uitvoeren
- **Ernstige incidenten** rapporteren aan EU AI Office
- Cyberbeveiligingsmaatregelen nemen
- Energieverbruik rapporteren

**Hoe weet je of je model dit drempelwaarde overschrijdt?**
- GPT-4 klasse: waarschijnlijk ja
- Llama 3 8B: nee
- Llama 3 70B: grensgebied
- Twijfel? Vraag je cloud provider om compute-schattingen of gebruik de FLOP-calculator van MLCommons.

---

## Open source GPAI (Art. 53(2))

Vrijgesteld van de meeste documentatieverplichtingen als:
- Gewichten publiek beschikbaar zijn
- Informatie over trainingsdata publiek beschikbaar is

**Maar:** Open source **met systeemrisico** is niet vrijgesteld van Art. 55.

---

## Als je GPAI gebruikt (downstream provider)

Als je een GPAI-model integreert in je eigen product/systeem:
- Zorg dat je de **API-gebruiksvoorwaarden** van de GPAI-aanbieder hebt gelezen
- Controleer of de GPAI-aanbieder de vereiste informatie verschaft (Art. 53(1)(b))
- Jij bent verantwoordelijk voor het downstream systeem – ook als het GPAI-model zelf conform is

---

## Checklist GPAI-aanbieders

| Vereiste | Status |
|---|---|
| Technische documentatie opgesteld (Annex XI)? | ☐ |
| Auteursrechtbeleid trainingsdata gedocumenteerd? | ☐ |
| Samenvatting trainingsdata gepubliceerd? | ☐ |
| Informatiepakket voor downstream providers? | ☐ |
| Registratie in EU AI-database? | ☐ |
| Compute > 10^25 FLOPs? (systeemrisico check) | ☐ |
| Red-teaming uitgevoerd? (indien systeemrisico) | ☐ |
| Incidentrapportageproces ingericht? (indien systeemrisico) | ☐ |
-e 

---

# Verplichtingen voor Hoog-Risico AI-Systemen

> Van toepassing vanaf **2 augustus 2026** (nieuwe systemen). Bestaande systemen: uiterlijk 2027.

---

## Wie is verantwoordelijk?

| Rol | Definitie | Verplichtingen |
|---|---|---|
| **Aanbieder** (Art. 3(3)) | Ontwikkelt/brengt het systeem op de markt | Alle technische verplichtingen (Art. 9-15) |
| **Gebruiksverantwoordelijke** (Art. 3(4)) | Deployt/gebruikt het systeem | Operationele verplichtingen (Art. 26) |
| **Importeur** (Art. 3(6)) | Brengt niet-EU-systeem op EU-markt | Gelijkgesteld aan aanbieder |
| **Distributeur** | Verspreidt zonder aanpassen | Lichtere verplichtingen |

> 💡 Als je als SaaS-bedrijf een hoog-risico systeem deployt dat je zelf hebt gebouwd, ben je **zowel aanbieder als gebruiksverantwoordelijke**.

---

## Verplichtingen Aanbieder

### 1. Risicobeheersysteem (Art. 9)
- Continu proces gedurende de volledige levenscyclus
- **Identificeer en analyseer** bekende en redelijkerwijs voorzienbare risico's
- **Test** op de meest relevante risicovolle situaties
- Restrisico's moeten aanvaardbaar zijn

**Wat dit betekent voor je code:**
```
✓ Risk register bijhouden (gedocumenteerd)
✓ Worst-case scenario analyses uitvoeren
✓ Red-teaming / adversarial testing
✓ Risico's bijwerken na elke significante update
```

### 2. Data en Data Governance (Art. 10)
Trainingdata, validatiedata en testdata moeten:
- Relevante **ontwerp- en goedkeuringspraktijken** volgen
- Geschikt zijn voor het **beoogde doel**
- **Vrij van fouten** zijn voor zover technisch haalbaar
- Voldoende **representatief** zijn
- Bijzondere categorieën data: enkel met strikte waarborgen

**Kritische vragen:**
- Is je dataset gedocumenteerd (oorsprong, bewerkingen, aannames)?
- Heb je gecontroleerd op bias in de trainingsdata?
- Zijn er subgroepen ondervertegenwoordigd?

### 3. Technische Documentatie (Art. 11 + Annex IV)
**Moet bevatten:**
- Algemene beschrijving van het systeem en zijn doel
- Ontwerpelementen, ontwikkelproces, trainingmethoden
- Prestatiemetingen inclusief nauwkeurigheid, robuustheid
- Capaciteiten en beperkingen van het systeem
- Gebruikte datasets (herkomst, omvang, labels)
- Risicobeoordelingsresultaten
- Systeem voor post-market monitoring

**Praktisch:** Maak een "Model Card" + uitgebreide README met al deze elementen.

### 4. Registratie en Logboekfunctie (Art. 12)
- Automatische logging van alle **relevante events** gedurende gebruik
- Moet "traceerbaarheid" mogelijk maken over de gehele levensduur
- Minimaal: tijdstempel, input hash, output, vertrouwensscore (indien beschikbaar), gebruikerID

**Minimale log-structuur:**
```json
{
  "timestamp": "ISO8601",
  "session_id": "uuid",
  "input_hash": "sha256",
  "model_version": "1.2.3",
  "output": "...",
  "confidence": 0.87,
  "operator_id": "...",
  "flags": []
}
```

### 5. Transparantie en Gebruikersinformatie (Art. 13)
Gebruiksverantwoordelijken moeten voldoende informatie krijgen via:
- **Gebruiksaanwijzing** (Art. 13(3)):
  - Identiteit en contactgegevens aanbieder
  - Kenmerken, mogelijkheden en beperkingen
  - Doel en beoogd gebruik
  - Prestatieniveaus (nauwkeurigheid per subgroep!)
  - Bekende of voorzienbare risico's
  - Eventuele vereiste menselijke toezichtmaatregelen
  - Verwachte levensduur en onderhoudsinstructies

### 6. Menselijk Toezicht (Art. 14)
Het systeem moet ontworpen zijn zodat mensen:
- Het systeem **volledig begrijpen**
- De output kunnen **monitoren** tijdens gebruik
- Het systeem kunnen **overschrijven of uitschakelen** (stop-knop!)
- Anomalieën, fouten of onverwacht gedrag kunnen **detecteren**

**Implementatievereisten:**
```
✓ Confidence scores tonen aan operators
✓ Flagging-mechanisme voor twijfelgevallen
✓ Duidelijke override/reject-knop
✓ Escalatieprotocol documenteren
✓ Operators trainen op correct gebruik
```

### 7. Nauwkeurigheid, Robuustheid en Cyberbeveiliging (Art. 15)
- **Prestatieniveaus** vastleggen en handhaven
- **Consistent presteren** ook bij adversarial inputs
- Weerstand bieden tegen:
  - Data poisoning
  - Model evasion aanvallen
  - Adversarial voorbeelden
  - Backdoor aanvallen
- Fallback-gedrag documenteren bij onzekere outputs

---

## Verplichtingen Gebruiksverantwoordelijke (Art. 26)

- Gebruik het systeem **alleen voor het beoogde doel**
- Zorg voor voldoende menselijk toezicht
- Monitor de werking en meld incidenten
- Informeer betrokkenen (Art. 26(11)) als AI-besluiten hen treffen
- Bij arbeidscontext: informeer werknemers/werknemersvertegenwoordigers

---

## Conformiteitsbeoordeling (Art. 43)

### Intern (meeste hoog-risico systemen):
- Aanbieder beoordeelt zelf conformiteit
- Documenteert in technische documentatie
- Stelt EU-conformiteitsverklaring op

### Via aangemelde instantie (notified body):
Verplicht voor: biometrische identificatiesystemen, kritieke infrastructuur, sommige medische toepassingen.

---

## EU-database registratie (Art. 49 + 71)

Hoog-risico systemen moeten geregistreerd worden in de **EU AI-database** vóór in de handel brengen.
Uitzondering: systemen voor rechtshandhaving en nationale veiligheid.

---

## CE-markering (Art. 48)

Hoog-risico AI-systemen die ook onder andere CE-wetgeving vallen, moeten de AI Act verplichtingen meenemen in hun CE-conformiteitsbeoordeling.
-e 

---

# Verboden AI-praktijken – Artikel 5

> ⚠️ Van kracht sinds **2 februari 2025**. Geen overgangsperiode. Boetes tot €35 miljoen of 7% wereldwijde omzet.

---

## 1. Subliminale manipulatie (Art. 5(1)(a))
**Verboden:** AI-technieken die iemands gedrag beïnvloeden op een manier die **onder het bewustzijn** werkt, waardoor ze besluiten nemen die ze anders niet zouden nemen en schade lijden.

**Kritische vragen voor je project:**
- Gebruikt je systeem enige vorm van gedragsbeïnvloeding?
- Is de gebruiker zich bewust van hoe de output zijn gedrag stuurt?
- Zijn er gepersonaliseerde "nudges" die ongezien werken?

---

## 2. Uitbuiting van kwetsbare groepen (Art. 5(1)(b))
**Verboden:** AI die gebruikmaakt van zwakheden van specifiek kwetsbare personen (leeftijd, handicap, sociale/economische situatie) om hun gedrag te beïnvloeden op een manier die schade veroorzaakt.

**Risicogroepen:**
- Kinderen (leeftijdsgerichte marketing/manipulatie)
- Ouderen (scamdetectie-omzeiling)
- Mensen in schulden / financiële nood
- Personen met cognitieve beperkingen

---

## 3. Social scoring (Art. 5(1)(c))
**Verboden:** Overheden (of namens overheden) die mensen beoordelen op basis van gedrag of persoonlijkheidskenmerken en die beoordeling gebruiken voor benadeelende of schadelijke behandeling.

> Let op: Geldt voor **overheidsactoren**. Private credit scoring voor leningen valt hier niet onder (wel onder hoog-risico Annex III).

---

## 4. Risicobeoordeling voor crimineel gedrag (Art. 5(1)(d))
**Verboden:** AI-systemen die het **risico inschatten** dat iemand een misdaad pleegt, puur op basis van profilering of persoonlijkheidskenmerken, zonder concrete misdrijven.

**Kritische vragen:**
- Gebruikt je systeem gedragspatronen om "toekomstig risico" te voorspellen?
- Is de conclusie gebaseerd op attributen van de persoon, niet op bewijzen?

---

## 5. Niet-gerichte scraping van gezichten (Art. 5(1)(e))
**Verboden:** Het bouwen of uitbreiden van gezichtsherkenningsdatabases door massaal scrapen van internet of CCTV.

---

## 6. Emotieherkenning op werkvloer en onderwijs (Art. 5(1)(f))
**Verboden:** AI die emoties herkent van personen op de **werkplek** of in **onderwijsinstellingen**.

**Uitzonderingen:** Medische of veiligheidsdoeleinden (bv. rijdersmoeheid detectie).

**Kritische vragen:**
- Detecteert of inferert je systeem emoties van werknemers of studenten?
- Wordt facial expression analysis gebruikt voor HR of leerresultaten?

---

## 7. Biometrische categorisering (Art. 5(1)(g))
**Verboden:** AI die individuen categoriseert op basis van biometrische gegevens in:
- Ras / etnische afkomst
- Politieke opvattingen
- Vakbondslidmaatschap
- Religieuze/filosofische overtuigingen
- Seksuele oriëntatie of leven

---

## 8. Real-time biometrische identificatie in publieke ruimte (Art. 5(1)(h))
**Verboden voor rechtshandhaving**, tenzij:
- Gericht zoeken naar vermiste personen of slachtoffers van mensenhandel
- Voorkomen van specifieke, ernstige terreurdreiging
- Opsporing van ernstige misdrijven (na rechterlijke toestemming)

> 💡 Voor **private actoren** (bedrijven) geldt dit verbod niet specifiek via Art. 5, maar real-time biometrische identificatie is wel **hoog-risico** en vereist bijzondere rechtvaardiging.

---

## Checklist voor ontwikkelaars

| Check | Vraag |
|---|---|
| ☐ | Beïnvloedt mijn systeem gedrag buiten het bewustzijn? |
| ☐ | Richt mijn systeem zich op kwetsbare gebruikers met manipulatieve technieken? |
| ☐ | Scoort mijn systeem mensen voor een overheidsactor? |
| ☐ | Voorspelt mijn systeem crimineel gedrag op basis van persoonlijkheid? |
| ☐ | Bouw ik een gezichtsdatabase via scraping? |
| ☐ | Detecteer ik emoties op de werkplek of in scholen? |
| ☐ | Categoriseer ik mensen op basis van religie, politiek, of seksualiteit? |
| ☐ | Doe ik real-time biometrische identificatie voor rechtshandhaving? |

Als één van deze vragen "ja" is → **juridisch advies inwinnen of systeem aanpassen**.
-e 

---

# Risicoclassificatie – EU AI Act

## Stap 1: Is het systeem een AI-systeem?

Een **AI-systeem** (Art. 3(1)) is een op een machine gebaseerd systeem dat:
- Ontworpen is om met variërende mate van autonomie te functioneren
- **Inferentie** kan uitvoeren (voorspellingen, content, aanbevelingen, besluiten)
- Invloed heeft op fysieke of virtuele omgevingen

> ❌ **Geen AI-systeem** = traditionele rule-based software zonder leren/inferentie

---

## Stap 2: Verboden praktijken (Art. 5) – STOP hier

Zie `prohibited-practices.md` voor de volledige lijst.

Snel overzicht van verboden systemen:
- Subliminale manipulatie onder het bewustzijn
- Uitbuiting van kwetsbare groepen (kinderen, ouderen, personen met handicap)
- Social scoring door overheden
- Real-time biometrische identificatie op afstand in publieke ruimte (behoudens uitzonderingen)
- Emotieherkenning op de werkvloer of in onderwijs
- Biometrische categorisering op basis van politiek/religie/seksuele oriëntatie

---

## Stap 3: Hoog-risico? (Art. 6 + Annex I & III)

### Categorie A: Productveiligheidscomponent (Art. 6(1))
AI-systeem dat **veiligheidscomponent** is van een product onder:
- Machines, speelgoed, liften, medische hulpmiddelen, auto's, vliegtuigen, etc.
→ Als het product CE-markering vereist, is het AI-systeem hoog-risico

### Categorie B: Annex III lijst (Art. 6(2))

| Domein | Voorbeelden van hoog-risico toepassingen |
|---|---|
| **Biometrie** | Identificatie op afstand, emotieherkenning, categorisering |
| **Kritieke infrastructuur** | Beheer van water, gas, elektriciteit, verkeer |
| **Onderwijs** | Toelating, evaluatie van studenten, toezicht op examens |
| **Werkgelegenheid** | Werving/selectie, promotie, taakverdeling, ontslag, monitoring |
| **Essentiële diensten** | Kredietscores, ziektekostenverzekering, levens-/schadeverzekering, sociale uitkeringen |
| **Rechtshandhaving** | Risicobeoordeling individuen, bewijsanalyse, profilage |
| **Migratie** | Risicobeoordelingen, visumaanvragen, asiel |
| **Rechtspraak** | Feiten-/wetsonderzoek, alternatieve geschillenbeslechting |
| **Democratisch proces** | Politieke campagnes, kiezersbeïnvloeding |

### Uitzonderingen op Annex III (Art. 6(3))
Systemen in Annex III zijn **niet** hoog-risico als:
- Geen **significant risico** op schade voor gezondheid, veiligheid of grondrechten
- Enkel een **enge taak** uitvoert (bv. verbeteren van laadtekst van een e-mail)
- Geen besluiten neemt die mensen **significante invloed** hebben
- Enkel een **voorbereidende evaluatie** uitvoert voordat een mens beslist

> 💡 De aanbieder moet deze uitzondering **documenteren en motiveren**

---

## Stap 4: Beperkt risico (Art. 52)

Transparantieverplichtingen voor:
- **Chatbots / conversationele AI** → gebruikers informeren dat ze met AI praten
- **Deepfakes / synthetische content** → labelen als AI-gegenereerd
- **Emotieherkenning** (niet verboden) → gebruikers informeren
- **Biometrische categorisering** (niet verboden) → gebruikers informeren

---

## Stap 5: GPAI-modellen (Art. 51-56)

Gelden voor **aanbieders** van General Purpose AI-modellen (zoals LLMs):
- Technische documentatie + auteursrechtbeleid
- Informatie aan downstream providers
- **Systeemrisico**: extra verplichtingen voor modellen met >10^25 FLOPs trainingscompute

Zie `gpai-obligations.md` voor details.

---

## Beslisboom

```
Is het een AI-systeem?
└─ Nee → Buiten scope AI Act
└─ Ja ↓
   Valt het onder Art. 5 (verboden)?
   └─ Ja → VERBODEN, onmiddellijk stoppen
   └─ Nee ↓
      Is het een veiligheidscomponent van CE-product? (Art. 6(1))
      └─ Ja → HOOG RISICO
      └─ Nee ↓
         Staat het in Annex III?
         └─ Nee → Beperkt/minimaal risico (Art. 52 of vrijwillig)
         └─ Ja ↓
            Geldt de uitzondering van Art. 6(3)?
            └─ Ja → Documenteer & motiveer → Beperkt/minimaal risico
            └─ Nee → HOOG RISICO (volledige verplichtingen)
```
 eu-ai-act-conformity.md…]()
