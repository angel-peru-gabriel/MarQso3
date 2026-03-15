# MarQso3
Implementar Pywa + API Wasap + Selenenium todo en Python 

# Repo Rules

- `channels/whatsapp`: solo parseo, routing y presentacion; sin logica de negocio.
- `services/`: logica de aplicacion; sin IO directo.
- `integrations/`: unico lugar con IO real (selenium, sheets, storage).
- `domain/`: modelos y validaciones.
- `shared/`: utilidades agnosticas.

# Repo Rules (MarQso2)

## Python environment (Windows)
- Always run Python commands using this interpreter (do not use system Python):
  - `C:\Users\Aquino\PycharmProjects\AQUINO_SELENIUM\venv\Scripts\python.exe`

Examples:
- Install deps:
  - `"C:\Users\Aquino\PycharmProjects\AQUINO_SELENIUM\venv\Scripts\python.exe" -m pip install -r requirements.txt`
- Run module:
  - `"C:\Users\Aquino\PycharmProjects\AQUINO_SELENIUM\venv\Scripts\python.exe" -m facturafast.app.main_whatsapp`

## Architecture rules
- `channels/whatsapp/`: only parsing/routing/presentation (no business logic, no IO).
- `services/`: application logic (no direct IO).
- `integrations/`: the only place with real IO (WhatsApp API, Google Sheets, Selenium).
- `domain/`: models and validators.
- `shared/`: reusable utilities.

## Safety
- Do not commit `.env` or credentials JSON files.
- Never print secrets (tokens, credentials).

- Do not create or use a local `.venv` for this repo unless the user asks explicitly.