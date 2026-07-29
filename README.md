\# Farfetch ETL



\## Projektziel



Dieses Projekt ersetzt den bisherigen Google-Sheets-Prozess zur Erstellung der Farfetch-CSV durch eine performante ETL-Anwendung in Python.



Die Anwendung verarbeitet große CSV-Dateien (>150 MB), transformiert die Daten anhand definierter Geschäftsregeln und erzeugt automatisiert die fertige Farfetch-Importdatei.



\---



\## Projektstatus



\*\*Version:\*\* 0.1.0



Aktueller Meilenstein:



\- Projektgrundlage

\- Git

\- Logging

\- CSV-Import

\- CSV-Export



\---



\## Projektstruktur



```text

farfetch-etl/

│

├── src/

│   ├── core/

│   ├── transformations/

│   └── main.py

│

├── config/

├── input/

├── output/

├── archive/

├── logs/

├── tests/

│

├── pyproject.toml

├── README.md

├── .gitignore

└── start.bat

```



\---



\## Technologien



\- Python 3.13

\- Pandas

\- DuckDB

\- OpenPyXL

\- Loguru

\- PyArrow



\---



\## Entwicklungsprinzipien



\- Saubere Architektur

\- Modulare Komponenten

\- Vollständige Typisierung

\- Logging

\- Unit-Tests

\- Git-Workflow

\- Hohe Performance



\---



\## Roadmap



\### Version 0.2



\- CSV-Import Engine



\### Version 0.3



\- Transformationen



\### Version 0.4



\- Matching



\### Version 0.5



\- Farfetch Export



\### Version 1.0



\- Produktivbetrieb



\---



\## Lizenz



MIT

