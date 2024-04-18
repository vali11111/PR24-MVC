## Vpliv Legalizacije Konoplje na Družbeno-Ekonomsko Stanje v ZDA

Matej, Črt, Valerija

### Podatki

Podatke smo pridobivali iz več virov:

1. Podatki o brezdomstvu v ZDA (2007-2023) (https://www.hudexchange.info/resource/3031/pit-and-hic-data-since-2007/)
- Namen: Sledenje in analiza trendov brezdomstva v ZDA, uporabno za oblikovalce politik, raziskovalce in organizacije, ki delujejo na področju brezdomstva.
- Obseg podatkov: Strukturirani v obliki tabele, vključno z atributi kot so država, število CoC (Continuum of Care), zvezna država in število brezdomcev. Težave: Nekaj manjkajočih podatkov in nekonsistentnost v navedenih zveznih državah.
 - Predprocesiranje: Uporaba Pythona za čiščenje in preoblikovanje podatkov.
 
 2. Legalizacija marihuane v ZDA (MJBizDaily) (https://mjbizdaily.com/map-of-us-marijuana-legalization-by-state/):
- Namen: Zagotavljanje informacij o legalizaciji marihuane, vključno z medicinsko in rekreacijsko uporabo, projekcijami prodaje konoplje in multistate operaterji.
- Obseg podatkov: Besedilni podatki v obliki tabele, ki vsebujejo podrobnosti o legalizaciji marihuane po državah.
- Predprocesiranje: Minimalno, saj so bili podatki že v obliki tabele. 
- Zbiranje podatkov: Spletno strganje, obdelava in shranjevanje v obliki CSV datoteke. 

3. Complete List of US State Abbreviations (https://www.lovetoknow.com/parenting/kids/list-all-50-states-abbreviations)
- Namen: Pomagati pri učenju kratic vseh ameriških zveznih držav, koristno za geografski pouk. Obseg: Seznam vseh 50 zveznih držav ZDA in njihovih ustrezajočih kratic.
- Težave: Ni zaznanih težav, saj gre za preprost seznam, vendar bilo potrebno preveriti točnost podatkov.
- Predprocesiranje: Minimalno ali ni potrebno, saj so podatki že v obliki seznama.
- Zbiranje (web scraping): Podatki so zbrani s spletne strani, kjer so bile kratic držav objavljene.

4. Brezposlenost (https://www.ers.usda.gov/data-products/county-level-data-sets/county-level-data-sets-download-data/)
- Namen: Zagotoviti podatke na ravni okrožja za raziskovalce in oblikovalce politik, ki se ukvarjajo s socio-ekonomskimi vprašanji na lokalni ravni v ZDA.
- Obseg: Podatki vključujejo FIPS kodo, ime države, ime območja, kodo ruralno-urbane ter podatke o civilni delovni sili, zaposlenih, brezposelnih in stopnji brezposelnosti za vsako leto od leta 2000 do leta 2017.
- Težave: Zaradi razširjenosti podatkov so možne težave z obdelavo velike količine podatkov in potrebnih virov za shranjevanje.
- Predprocesiranje: Potrebno je obsežno predprocesiranje, vključno s čiščenjem podatkov, pretvorbo formatov in združevanjem različnih virov.

5. Housing Price Index (https://stats.oecd.org/Download.ashx?type=csv&Delimiter=%2c&IncludeTimeSeriesIdentifiers=False&LabelType=CodeAndLabel&LanguageCode=en)
- Namen: Analiza povezave cen nepremičnin po različnih zveznih državah z legalizacijo marihuane. Zbrali smo bazo podatkov za obdobja pred in po legalizaciji v posamičnih državah.
- Obseg: Podatki so zelo obsežni; vsebujejo podatke med 1990 in 2022 za povprečje v ZDA, po državah in celo po nekaj posamečnih mestih. Čas beleženja je letno, indeks pa je podan absolutno in relativno.
- Težave: Večjih težav s to bazo ni bilo. Večino težav je povzročajo čiščenje podatkov in podvojeni atributi.
- Predprocesiranje: Predprocesiranje ni bilo preveč zahtevno, saj je v večini vključevalo le odstranjevanje odvečnih stolpcev in vrstic.

6. Happiness Report (World Happiness Report)
- Namen: Ugotavljanje povezav med legalizacijo marihuane in indeksom sreče v ZDA. Primerjati želimo kako se je indeks sreče v ZDA spreminjal s številom držav, ki so legalizirale marihuano. To spreminjanje spremljamo tudi v povezavi s svetovnim trendom.
- Obseg: Podatki zajemajo krajše časovno obdobje (2007 - 2022) in poleg indeksa sreče vsebujejo tudi razne socialno-ekonomske vrednosti, ki so bile vključene pri izračunu indeksa. Podatki zajemajo večje število držav na svetu.
- Težave: Podatki so podani v Excelovi tabeli, kjer so podatki za posamezna leta v ločenih tabelah po listih. Imena in vrstni red atributov se po posameznih listih spreminja - ni enotnega formata.
- Predprocesiranje: Predprocesiranje je bilo obsežnejše. Potrebno je bilo preimenovati atribute, spreminjati vrstni red, dodati letnice in združiti vrednosti iz posameznih tabel v eno tabelo za smiselno primerjavo spreminjanja indeksa v ZDA skozi leta. Poleg tega je bilo nekaj odvečnih podatkov potrebno tudi odrezati.

7. Kriminal (https://corgis-edu.github.io/corgis/csv/state_crime/)
- Namen: Ugotavljanje korelacije med legalizacijo marihuane in kriminalom v ZDA. Primerjati želimo stopnjo prisotnega kriminala v ZDA po posamičnih zvezdnih državah, s stopnjo legalizacije marihuane po le teh državah.
- Obseg: Podatki zajemajo časovno obdobje (2000 - 2019) Zajeti so podatki različnih zločinov. Te pa se primarno delijo na Property Crime in Violent Crime.
- Težave: Večjih težav ni bilo. Obdelava je bila dokaj preprosta.
- Predprocesiranje: Obdelava je bla obsežna vendar preprosta, saj je že sam dataset zelo kvalitetno narejen brez podvojenih podatkov ali drugih sitnosti.

### Glavna vprašanja/cilji podatkovnega rudarjenja

- Pridobiti in analizirati informacije o tem, katere zvezne države imajo legalizirano konopljo (medicinska ali rekreacijska) in kako to vpliva na različne ekonomske (brezposelnost, cene nepremičnin) in družbene (kriminal, kazalniki sreče, brezdomstvo) faktorje.
- Primerjava učinkov medicinske in rekreacijske legalizacije marihuane lahko razkrije pomembne razlike v njihovem vplivu na soci-ekonomske .
- Napovedati, kaj bi se zgodilo, če bi države, ki nimajo legalizirane, legalizirale konopljo, torej kako bi to vplivalo na njihove soci-ekonomske razmere.- Raziskati in analizirati medsebojni vpliv vseh ostalih socio-ekonomskih dejavnikov.

### Podroben opis ciljev in metod

1.  Analiza vpliva legalizacije na ekonomske in družbene faktorje:

-   Cilj: Raziskati vpliv legalizacije konoplje na socio-ekonomske faktorje, kot so brezposelnost, cene nepremičnin, kriminal, sreča in brezdomstvo.
-   Metode: Analiza podatkov (grafi) za ugotavljanje povezav med legalizacijo konoplje ter socio-ekonomskimi kazalci.

2.  Primerjava učinkov medicinske in rekreacijske legalizacije:

-   Cilj: Primerjati učinke medicinske in rekreacijske legalizacije konoplje na socio-ekonomske faktorje.
-   Metode: Primerjalna analiza socio-ekonomskih kazalcev v državah z medicinsko in rekreacijsko legalizacijo ter identifikacija morebitnih razlik v njihovem vplivu na ekonomske in družbene aspekte.

3.  Napoved učinkov legalizacije v državah brez legalizacije:

-   Cilj: Napovedati vpliv legalizacije konoplje na socio-ekonomske razmere v državah brez legalizacije.
-   Metode: Uporaba  primerjalnih študij in napovednih analiz za oceno potencialnih učinkov legalizacije konoplje na brezposelnost, cene nepremičnin, kriminal in druge socio-ekonomske faktorje.

4.  Raziskovanje medsebojnega vpliva socio-ekonomskih dejavnikov:

-   Cilj: Analizirati medsebojni vpliv vseh socio-ekonomskih faktorjev ter ugotoviti kompleksne povezave med legalizacijo konoplje in drugimi družbenimi ter ekonomskimi dejavniki.
-   Metode: Uporaba statističnih analiz, regresijskih analiz za razumevanje celovite slike o vplivu legalizacije konoplje na družbo in gospodarstvo.

### Rezultati in dosedanje ugotovitve

Dosedanje ugotovitve kažejo, da je trenutno 24 držav v celoti legaliziralo konopljo. 16 držav je legaliziralo samo medicinsko uporabo, medtem ko nobena država ni legalizirala samo rekreativne uporabe. Poleg tega obstaja 10 držav, ki še vedno niso legalizirale konoplje v nobeni obliki.

Ugotovitve kažejo na več pomembnih dejstev glede legalizacije konoplje in njenega vpliva na število brezdomcev v Združenih državah Amerike:

- Povezava med legalizacijo konoplje in številom brezdomcev: Opazili smo, da je skupno največ brezdomcev tam, kjer je legalizacija konoplje v celoti dovoljena. To nas spodbuja k razmišljanju o morebitnih socialnih izzivih in ekonomskih posledicah, povezanih z izvajanjem politik legalizacije.
- Razlika med medicinsko in rekreacijsko legalizacijo: Ugotovili smo, da je največji delež brezdomcev v državah, kjer je konoplja v celoti legalizirana zgolj za medicinske namene, sledijo ji države, kjer dovoljena medicinska uporaba, medtem ko nobena država nima samo rekreacijsko legalizirane politike. To kaže na kompleksnost vpliva različnih vrst legalizacije na socialno-ekonomske razmere.

### Odprta vprašanja

-  Kako legalizacija vpliva na ostale ekonomske in družbene faktorje in kako vplivajo drug ana drugega?

- Kakšne so razlike med medicinsko in rekreacijsko legalizacijo ter kako bi legalizacija vplivala na države brez nje?
