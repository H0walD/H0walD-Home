# Änderungen

## 1.5.0 – Rahmen, Schatten und Ecken

### Neu
- **Rahmenbreite** (kein Rahmen bis 4 px), **Rahmenfarbe** per Farbwähler und **Deckkraft** des Rahmens im Kachel-Design.
- **Schatten** in vier Stufen: kein, leicht, mittel, stark.
- **Ecken** von leicht rund bis Pille.
- Rahmen, Schatten und Ecken gelten auf Wunsch auch für die **Lampen-Kacheln**.
- **Breite im Dashboard** wie in Home Assistant: Einfach, Doppelt, Dreifach, Volle Breite.
- Wie alle Design-Einstellungen für **alle Räume gleichzeitig** („Für alle Räume“) oder nur für einen Raum.

### Behoben
- Einstellungen, die direkt in Home Assistant unter „Abschnitt anpassen“ gemacht wurden (z. B. **Hintergrund** oder **Breite**), gingen beim Speichern aus dem Editor verloren. Sie bleiben jetzt erhalten.

## 1.4.0 – Brandmelder-Symbole, Lampengruppen und Lampen entfernen

### Neu
- **Brandmelder-Darstellung im Kachel-Design:** Wahlweise wie bisher als **Text unter dem Raumnamen** oder als **Symbol mit Farbe** direkt unter dem Raumnamen (antippen öffnet den Brandmelder).
- **Für jeden Zustand einstellbar** (Alles OK, Offline, Alarm): eigenes MDI-Symbol (z. B. `mdi:smoke-detector`), eigene Farbe per Farbwähler und eigener Text. Vorschläge für passende Symbole erscheinen beim Tippen.
- Text neben dem Symbol ein- oder ausblendbar.
- Wie alle Design-Einstellungen gilt das für alle Räume oder nur für einen Raum, mit Live-Vorschau.
- **Lampengruppe per Klick erstellen:** Im Raum-Editor legt „Lampengruppe aus den Lampen erstellen“ in Home Assistant eine Licht-Gruppe mit allen eingetragenen Lampen an, ordnet sie dem Bereich des Raums zu und trägt sie als „Ganzer Raum“ ein.
- **Lampen aus einem Bereich entfernen:** Im Bereichs-Manager hat jede Lampe ein ✕. Zweimal klicken entfernt sie aus dem Bereich (sie landet unter „Lampen ohne Bereich“) und aus dem Raum im Editor. Erbt die Lampe ihren Bereich vom Gerät, wird das Gerät aus dem Bereich genommen; die Meldung sagt dann, wie viele Lampen betroffen sind.

## 1.3.1 – Lampen ohne eigenen Namen verschieben

### Behoben
- **„Verschieben fehlgeschlagen: An entity without a name of its own cannot have an area of its own“:** Manche Lampen haben in Home Assistant keinen eigenen Namen, sondern nutzen den Namen ihres Geräts. Solche Lampen dürfen keinen eigenen Bereich haben. Der Editor verschiebt in diesem Fall jetzt automatisch das **Gerät** in den neuen Bereich. Hat das Gerät mehrere Lampen, wandern alle mit, und die Meldung sagt, wie viele es waren. Die Räume im Editor werden für alle verschobenen Lampen angepasst.

## 1.3.0 – Kachel-Design und neues Dashboard per Klick

### Neu
- **Kachel-Design bearbeiten:** Im Raum-Editor gibt es den Bereich „Kachel-Design“. Jede Einstellung gilt wahlweise **für alle Räume** oder **nur für einen Raum**. Eigene Werte eines Raums sind markiert und lassen sich mit „Wie alle Räume“ zurücksetzen. Die Vorschau zeigt jede Änderung sofort.
  - **Inhalt der Kachel:** Art, Temperatur, Feuchte, Brandmelder-Status, Helligkeitsregler, Regler-Knopf, Szenen-Knöpfe und das Aufklappen der Lampen einzeln ein- und ausschalten.
  - **Reihenfolge:** Raum-Kachel, Szenen-Knöpfe und Lampen-Kacheln per Ziehen anordnen.
  - **Raum-Kachel:** Rahmen ein/aus, Leuchten wenn Licht an ist ein/aus, Leuchtfarbe (Farbe der Lampen oder Warmweiß), Breite im Dashboard (1 oder 2 Spalten).
  - **Lampen-Symbole:** Position (in der Raum-Kachel, eigene Zeile darüber oder ausgeblendet), Aussehen (Punkt, Glühbirne oder Symbol der Lampe), Größe (klein, mittel, groß) und Farbe wenn an (Bernstein, Gelb, Orange, Weiß oder die Farbe der Lampe).
  - **Lampen-Kacheln:** 1 bis 4 pro Zeile, Aufbau Standard, waagrecht oder senkrecht. Szenen-Knöpfe mittig oder links.
- **Raum-Symbol per Auswahl:** Häufige Symbole (Sofa, Bett, Küche, Bad …) direkt anklicken.
- **Räume nebeneinander pro Geschoss:** Im Geschoss-Editor einstellen, wie viele Räume höchstens nebeneinander stehen.
- **Neues Dashboard mit Helfern erstellen:** Ein Klick legt ein neues Dashboard an, übernimmt Geschosse und Bereiche, erstellt die Schalter-Helfer und speichert alles.
- **Wer sieht das Dashboard:** Alle Benutzer, nur Administratoren oder ausgewählte Benutzer. Wird beim Erstellen und beim Speichern übernommen.
- **Lampe in der Vorschau entfernen:** Jede Lampen-Kachel in der Vorschau hat ein ✕.

### Technisch
- Design-Einstellungen, Sichtbarkeit und die Zuordnung zu HA-Bereichen werden im Dashboard selbst gespeichert (Schlüssel `h0wald_home`). Nach dem Laden ist alles wieder da, auch auf anderen Geräten.

## 1.2.2 – Bereiche und Geschosse umbenennen

### Neu
- **Bereiche umbenennen:** Im Bereichs-Manager auf den Namen eines Bereichs klicken (✎), neuen Namen eingeben und mit Enter bestätigen. Der Name wird sofort in Home Assistant geändert. Der zugehörige Raum im Editor wird mit umbenannt, wenn er bisher gleich hieß.
- **Geschosse umbenennen:** Genauso über den Geschoss-Namen im Bereichs-Manager. Das passende Geschoss im Editor wird mit umbenannt.
- **Raumname nach Home Assistant übernehmen:** Ist ein Raum mit einem HA-Bereich verknüpft, gibt es im Raum-Editor den Knopf „Name auch als HA-Bereich übernehmen“.

## 1.2.1 – Leere Räume bearbeiten

### Behoben
- **Räume ohne Lampen sind jetzt bearbeitbar.** Bisher wurde ein Raum ohne Einzellampen beim Laden gesperrt („bleibt unverändert“), sodass man nichts hinzufügen konnte. Jetzt kannst du dort jederzeit Lampen, Fühler, Brandmelder und Szenen ergänzen.
- **Räume nur mit Fühlern oder Brandmeldern** (z. B. Bad, Flur) werden im Dashboard als Raumname mit Temperatur, Feuchte und Brandmelder-Status angezeigt, ohne leere Lampen-Karte.

### Neu
- **Gesperrten Abschnitt umwandeln:** Fremde Abschnitte, die unverändert übernommen werden, lassen sich per Knopf in einen bearbeitbaren Raum umwandeln.
- **„Geschosse & Bereiche übernehmen“ ergänzt neue Geräte:** Bei bestehenden Räumen kommen neu zugeordnete Lampen und Brandmelder automatisch dazu. Bereiche ohne Lampen, aber mit Fühlern oder Brandmeldern werden nicht mehr übersprungen.
- Schalter-Helfer werden nur noch für Räume mit Lampen angelegt.

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
