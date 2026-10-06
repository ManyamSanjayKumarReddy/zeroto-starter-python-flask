# Starter: a Python (Flask) app

A minimal Flask app served by gunicorn: `GET /` and `GET /health`.

## Deploy it on ZeroTo
**Fastest (no GitHub needed):** in ZeroTo press **Deployments → New deployment → Start from a sample app**, pick this one and deploy. When it is **Live**, open the address and `/health`.

**Your own copy (so you can change it and have it redeploy on every push):**
1. Here on GitHub press **Use this template → Create a new repository**.
2. In ZeroTo open **Connectors** and connect GitHub (once).
3. **New deployment**, choose your copy, deploy. Then turn on **auto-deploy** in its settings (if your plan includes it).

> Anything that edits the code (here and below) needs **your own copy** — the one-click sample is read-only. Settings, variables, logs and releases work on both.

## Try these
- **Variables → Add** `GREETING`, **Redeploy**, reload `/`.
- Add a route `/hello/<name>` that greets the name. Push, redeploy, test.
- Open the **Builds** tab and read how ZeroTo installed your requirements.

## Break it on purpose (and fix it)
- Delete the `Procfile` and redeploy: the build works, but does the app start? What does the build log suggest? (You can also set a **Start command** in the app's Settings.)
- Add a package to `app.py` (`import requests`) without adding it to `requirements.txt`. Read the crash in **Logs**.
