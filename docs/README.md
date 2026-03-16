# Docs

## Environment variables
- `WA_TOKEN`
- `WA_PHONE_ID`
- `WA_VERIFY_TOKEN`
- `WA_APP_SECRET` (optional)
- `SHEETS_ID`
- `SHEETS_WORKSHEET` defaults to `Items`
- `SHEETS_RANGE` defaults to `A:D`
- `GOOGLE_APPLICATION_CREDENTIALS`
- `PORT` defaults to `8000`

## Run locally
- Use the repo interpreter: `C:\Users\Aquino\PycharmProjects\AQUINO_SELENIUM\venv\Scripts\python.exe`
- Start the app:
  - `python -m facturafast.app.main_whatsapp`

## Tunnel
- `cloudflared tunnel --url http://localhost:8000`

## Meta webhook
- PyWa is configured with `webhook_endpoint="/webhook"`.
- Set the Meta Callback URL to your public tunnel URL plus `/webhook`.
