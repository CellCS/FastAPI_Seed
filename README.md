# FastAPI_Seed

FastAPI_Seed is one project to help to build FastAPI more fast with adopted modules. It is easy to be adopted to build any API service for AI projects with connection with local LLMs providers or OpenAI, Azure OpenAI Service, or other providers.

## Begin

init.sh will creat python venv. If your project requires more libs, add into api_service/requirements.txt.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r api_service/requirements.txt
deactivate
```

```bash
source .venv/bin/activate
python main.py
```

```bash
http://127.0.0.1:8000/docs#/
```

```bash
curl http://localhost:8000
```

```bash
curl http://localhost:8000/apikey
```

(Remember: change api-key, username and pwd in consts py file)

```bash
curl --location 'http://localhost:8000/hit' \
--header 'Authorization: Basic dGVzdGVyOnRlc3Rlcg==' \
--header 'From: fastapiuserA'
```

## Create releated service in your server

copy 'FASTAPI_SEED" in /opt/

Create service:

```bash
sudo cat /etc/systemd/system/fastapi.service
```

Modify the service file to use an existing user. (check utils/fastapi.service file.)

Reload and Start the Service:

```bash
sudo systemctl daemon-reload
sudo systemctl start fastapi
sudo systemctl enable fastapi
```

Check the Status:

```bash
sudo systemctl status fastapi
```
