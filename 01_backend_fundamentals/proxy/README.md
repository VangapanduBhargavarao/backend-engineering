# Forward and Reverse Proxy Fundamentals

This project is a small FastAPI demonstration of two common backend networking patterns: a **forward proxy** and a **reverse proxy**. It also includes two simple backend services so you can send requests directly to a service or through a proxy and compare the results.

## What is a proxy?

A proxy sits between a client and another server and relays requests and responses. The main difference is which side the proxy represents:

- A **forward proxy** is used on behalf of the client. The client tells it which destination URL to contact.
- A **reverse proxy** is used in front of a server or group of servers. The client calls the proxy, and the proxy chooses the backend.

## Project layout

```text
backend1/             Backend service on port 8001
backend2/             Second standalone backend on port 8002
forward_proxy/        Forward proxy on port 9000
Reversre_proxy/       Reverse proxy on port 8000 (directory spelling as in this project)
tests/                Test file placeholders
client/               Client test file placeholder
requirements.txt      Python dependencies
```

## Requirements

- Python 3.9 or newer
- `pip`

Install the dependencies from the project root:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, you can run the commands below with `.venv\Scripts\python.exe` instead of `python`.

## Start the services

Open a separate PowerShell terminal for each command. Run them from the project root and leave each terminal running:

```powershell
python -m uvicorn backend1.main:app --host 127.0.0.1 --port 8001
```

```powershell
python -m uvicorn backend2.main:app --host 127.0.0.1 --port 8002
```

```powershell
python -m uvicorn Reversre_proxy.main:app --host 127.0.0.1 --port 8000
```

```powershell
python -m uvicorn forward_proxy.main:app --host 127.0.0.1 --port 9000
```

Backend 1, backend 2, and both proxies can then be reached at `http://127.0.0.1:8001`, `http://127.0.0.1:8002`, `http://127.0.0.1:8000`, and `http://127.0.0.1:9000`, respectively.

## Try the backends directly

Both backend apps provide `GET /`, `GET /users`, and `GET /health` routes. For example:

```powershell
curl.exe http://127.0.0.1:8001/users
curl.exe http://127.0.0.1:8002/users
```

The responses identify which backend handled the request and return that backend's sample user list.

## Try the forward proxy

The forward proxy listens on port `9000` and exposes `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` at `/proxy`. Supply the destination as the `url` query parameter:

```powershell
curl.exe -G --data-urlencode "url=http://127.0.0.1:8001/users" http://127.0.0.1:9000/proxy
```

This sends the request through the forward proxy to backend 1's `/users` endpoint. Change the destination URL to contact a different reachable service, for example backend 2:

```powershell
curl.exe -G --data-urlencode "url=http://127.0.0.1:8002/health" http://127.0.0.1:9000/proxy
```

If `url` is missing, the proxy returns HTTP `400` with the detail `Missing target URL`. The proxy forwards the incoming method, request body, and most request headers, then returns the destination response.

## Try the reverse proxy

The reverse proxy listens on port `8000`. It forwards the requested path and query parameters to backend 1, which is configured in `Reversre_proxy/main.py` as `http://127.0.0.1:8001`:

```powershell
curl.exe http://127.0.0.1:8000/
curl.exe http://127.0.0.1:8000/users
curl.exe "http://127.0.0.1:8000/health?check=1"
```

For example, a request to `http://127.0.0.1:8000/users` is relayed to `http://127.0.0.1:8001/users`. The response comes from backend 1. Backend 2 is not currently selected by the reverse proxy; it runs independently so you can compare its responses or extend the routing behavior.

## Forward proxy vs. reverse proxy

|                              | Forward proxy                           | Reverse proxy                          |
| ---------------------------- | --------------------------------------- | -------------------------------------- |
| Represents                   | The client                              | The backend service(s)                 |
| Destination chosen by        | Client, using the `url` parameter       | Proxy configuration and routing logic  |
| Project address              | `http://127.0.0.1:9000/proxy`           | `http://127.0.0.1:8000/{path}`         |
| Current destination behavior | Sends to the URL supplied by the caller | Always sends to backend 1 on port 8001 |

## Run tests

The `tests/` and `client/` Python files are currently empty placeholders, so this repository does not yet contain executable test cases. Once tests have been added, run them from the project root with:

```powershell
python -m pytest
```

## Current scope and safety

This is a learning example, not a production-ready proxy. In particular, the forward proxy accepts a caller-provided URL without destination restrictions. Do not expose it to an untrusted network: an unrestricted proxy can be abused to make requests to internal or otherwise unintended services. The reverse proxy uses a fixed backend URL and does not currently load-balance between backend 1 and backend 2.
