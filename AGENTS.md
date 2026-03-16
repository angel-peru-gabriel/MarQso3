# AGENTS

## Architecture
- `facturafast/app/main_whatsapp.py` is bootstrap only. Keep wiring there and avoid flow logic.
- `facturafast/channels/whatsapp/` only adapts PyWa messages to internal DTOs, calls services, and presents responses.
- `facturafast/services/` contains application logic and must not perform direct IO.
- `facturafast/integrations/` is the only place for real IO such as Google Sheets, WhatsApp API, storage, or Selenium.
- `facturafast/domain/` contains core models and domain-level validations.
- `facturafast/shared/` contains framework-agnostic utilities.
- Keep tests under the root `tests/` package, not inside `facturafast/`.

## Environment
- Use the Python interpreter from the virtual environment chosen by the user for this repository.
- Current interpreter for this repo: `C:\Users\Aquino\PycharmProjects\AQUINO_SELENIUM\venv\Scripts\python.exe`
- Do not hardcode a virtual environment path unless the user explicitly provides it.
- Do not create or switch virtual environments automatically without user approval.

## Python environment (Windows)
- Always run Python commands using this interpreter (do not use system Python):
  - `C:\Users\Aquino\PycharmProjects\AQUINO_SELENIUM\venv\Scripts\python.exe`

Examples:
- Install deps:
  - `"C:\Users\Aquino\PycharmProjects\AQUINO_SELENIUM\venv\Scripts\python.exe" -m pip install -r requirements.txt`
- Run module:
  - `"C:\Users\Aquino\PycharmProjects\AQUINO_SELENIUM\venv\Scripts\python.exe" -m facturafast.app.main_whatsapp`

- Do not create or use a local `.venv` for this repo unless the user asks explicitly.


## Security
- Never commit `.env`, tokens, secrets, or credential files.
- Never print or log secrets in plaintext.
