# Home Assistant automatiseerimise süsteem Prologiga

## Kuidas rakendust käivitada?
1. Laadige alla kõik vajalikud teegid. Kõik vajalikud teegid on requirements.txt failis ning seda kasutades on võimalik teha näiteks käsuga *python -m pip install -r requirements.txt*.
2. Järgmiseks on vaja *main.py* failis ära seadistama *token* muutuja. Selleks võite kasutada kas HA *refresh token*-i või *Long-Lived Access Token*-i. Selle rakenduse puhul on soovitatav kasutada *Long-Lived Access Token*-i
3. *main.py* anda õiged HA WebSocketi ja REST API aadressid. Näiteks WebSocketi aadressiks oleks *ws://SINU_AADRESS/api/websocket*.
4. Kui vastavad muudatused on tehtud, siis võite jooksutada rakendust näiteks käsureal käsuga *python main.py*.
## Kuidas seadmeid/teenuseid automatiseerida?
1. Tutvuge *prolog_files* kaustas olevate Prolog failidega. 
2. Enne jooksutage ühe korra rakendust, et kätte saada *automation_final.pl* failist kõik seadmed/teenused Prologis.
3. Kasutades *init_preds.pl* leiduvaid abipredikaate ning *automation_final.pl* failist leiduvaid seadmete/teenuste fakte, looge *automation_rules.pl* faili automatsiooni reeglid.

**NB! Automatsiooni reeglite defineerimisel ei tohi reegli päisesse defineerida muutujaid.**
