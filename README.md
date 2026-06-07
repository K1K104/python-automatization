# Projekt - Repozytorium i Github Actions

## Quick Start
Aby przygotować środowisko i zainstalować narzędzia, uruchom:
`bash scripts/create_venv.sh`

## Testy i jakość kodu
* Formatowanie: `bash scripts/format.sh`
* Sprawdzenie formatu: `bash scripts/format_check.sh`
* Linting: `bash scripts/lint.sh`
* Testy: `bash scripts/test.sh`

## Pipeline CI
Projekt zawiera GitHub Actions, który automatycznie uruchamia powyższe testy przy każdym Pull Request do gałęzi głównej.