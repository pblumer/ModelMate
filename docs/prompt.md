# ModelMates Prompt

**Anwendungszweck:**  
Dieser Prompt dient dazu, in einer neuen KI-Session an das ModelMates-Projekt anzuknüpfen, falls die vorherige Konversation nicht mehr vorhanden ist. Indem du diesen Prompt an eine neue KI-Session schickst, kannst du die KI schnell an den aktuellen Stand erinnern.

## Inhalt des Prompts

Bitte den folgenden Prompt einfach kopieren und in eine neue KI-Session einfügen:

---

**Prompt:**

Hallo!  
Ich arbeite an einem Open-Source-Projekt namens **ModelMates**. Dieses Projekt soll ein zentrales, Graph-basiertes Repository für verschiedene Modelle (Geschäftsmodelle, Softwarearchitekturen, Prozessmodelle etc.) bereitstellen. Die KI dient als Hilfsmittel, um diese Modelle über eine API/CLI einfach zu erstellen, zu pflegen und automatisch in bekannten Notationen wie ArchiMate, UML oder BPMN zu visualisieren.

Bisher haben wir:  
- Ein Git-Repository unter [Link zum Repo einfügen], mit einer Dokumentenstruktur (README, CONTRIBUTING, CODE_OF_CONDUCT, ROADMAP, ARCHITECTURE, DOMAIN MODEL).
- Ein erstes einfaches Domain Model (siehe `docs/modeling/domain-model.md`).
- Ein Proof-of-Concept (PoC)-Gerüst in Python (siehe `src/`-Verzeichnis), welches:
  - `FastAPI` für ein einfaches REST-API nutzt
  - `Click` für eine einfache CLI nutzt
  - `networkx` für einen In-Memory-Graph zur Modellierung nutzt
- Ein `requirements.txt` zur Installation der benötigten Dependencies.
- Ein virtuelles Python-Environment (`venv`) empfohlen, um Abhängigkeiten isoliert zu verwalten.
- Eine `.gitignore`, um unerwünschte Dateien nicht zu versionieren.

Die technische Basis ist noch sehr einfach, aber wir können darauf aufbauen. Bitte beziehe dich auf diese Struktur und den aktuellen Stand, wenn wir weitere Schritte planen oder umsetzen. Unser Ziel ist es, den PoC schrittweise auszubauen und später auf persistente Graph-Datenbanken (z. B. Neo4j) sowie erweiterte Visualisierungs- und KI-Features umzustellen.

---

## Verwendungshinweise

1. Öffne eine neue Session in deinem KI-Tool.
2. Kopiere den gesamten Prompt (von "Hallo!" bis zum Ende) und füge ihn in die neue Session ein.
3. Die KI wird dann versuchen, auf den bisherigen Wissensstand aufzubauen.  
   Falls Informationen fehlen, kannst du sie aus dem Git-Repo (z. B. Code-Auszüge, Dokumentation) erneut in die neue Session einspielen.
4. Von hier aus kannst du mit der KI wieder interagieren, als würdet ihr dort weitermachen, wo ihr aufgehört habt.

---

Mit diesem Prompt stellen wir sicher, dass wir jederzeit wieder auf den aktuellen Projektstand zugreifen können, selbst wenn die laufende Session verloren geht.
