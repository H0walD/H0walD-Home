# Änderungen

## 1.2.0 – Ziehen & Ablegen und Live-Vorschau

Der Editor lässt sich jetzt fast komplett mit der Maus oder dem Finger bedienen.

### Neu
- **Ziehen & Ablegen:** Geschosse, Räume, Lampen und Szenen-Knöpfe sortierst du am Griff ⠿. Das klappt mit der Maus, per Touch am Handy und mit den Pfeiltasten.
- **Räume verschieben:** Einen Raum auf einen Geschoss-Tab ziehen, schon liegt er in diesem Geschoss.
- **Lampen verschieben:** Eine Lampe auf einen anderen Raum in der Raumliste ziehen.
- **Szenen kopieren:** Einen Szenen-Knopf auf einen anderen Raum ziehen. Die Kopie schaltet dort automatisch die Lampengruppe dieses Raums.
- **HA-Bereiche per Ziehen:** Im Bereichs-Manager Lampen direkt in eine andere Bereichs-Karte oder zu „Lampen ohne Bereich“ ziehen. Die Änderung wird sofort in Home Assistant gespeichert.
- **Live-Vorschau:** Über dem Raum-Formular zeigt eine Vorschau den Raum im Dashboard-Look, mit echten Zuständen aus Home Assistant (Lampen an/aus, Helligkeit, Temperatur, Feuchte, Brandmelder). Ein Tipp auf Titel, Gruppe, Lampe oder Szene springt zum passenden Feld. Lampen und Szenen lassen sich auch direkt in der Vorschau sortieren.
- **Namen statt IDs:** Die Vorschlagslisten zeigen neben der Entitäts-ID den Namen aus Home Assistant. Leere Anzeigenamen von Lampen zeigen den HA-Namen als Platzhalter.

### Geändert
- Die Pfeil-Knöpfe ↑ ↓ bei Räumen, Lampen und Szenen wurden durch den Griff ⠿ ersetzt. Die ← → Knöpfe bei Geschossen bleiben als Alternative.

### Update
Über HACS aktualisieren oder den Ordner `custom_components/h0wald_home` ersetzen und Home Assistant neu starten. Falls noch die alte Fassung angezeigt wird, die Seite einmal neu laden.
