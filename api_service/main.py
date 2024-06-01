from fastapi import FastAPI, Depends,BackgroundTasks
from contextlib import asynccontextmanager
import asyncio
import uvicorn
import base64

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html

from libs import lib_basic_auth as lib_basic_auth
from libs import lib_consts as lib_consts

origins = ['*']
background_tasks = BackgroundTasks()

# need rename based on your bussiness logic
oneserviceobj = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global oneserviceobj
    print("Starting up the application...")
    if oneserviceobj is None:
        print("init oneserviceobj")
        #inii oneserviceobj
    yield
    print("Shutting down the application...")

app = FastAPI(
    title="FastAPI_Project",
    description="Provide FastAPI for XXXXXXX",
    summary="",
    version="0.0.1",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

basic_auth = lib_basic_auth.BasicAuth(auto_error=False)
security = HTTPBasic()
def authenticate_user(username: str, password: str):
    if username == '' or password =='':
        return False
    return username == lib_consts.apiuser and password == lib_consts.apipwd

def authenticate_test(auth: lib_basic_auth.BasicAuth = Depends(basic_auth)):
    if not auth:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password 1",
            headers={"WWW-Authenticate": "Basic"},
            )
    try:
        decoded = base64.b64decode(auth).decode("ascii")
        username, _, password = decoded.partition(":")
        islogin = authenticate_user(username, password)
        if islogin is False:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password 2",
                headers={"WWW-Authenticate": "Basic"},
                )
        return True
    except (base64.binascii.Error, UnicodeDecodeError) as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Incorrect username or password 3 {e}",
            headers={"WWW-Authenticate": "Basic"},
            )
    except HTTPException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password 4",
            headers={"WWW-Authenticate": "Basic"},
            )
    return False

################### business logic##############################################
        
async def run_health_check():
    try:
        while True:
            print("Running health check, do something")
            await asyncio.sleep(lib_consts.healthcheck_interval * 60)
    except Exception as e:
        print(f"Health check failed: {e}")



@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return app.openapi()

@app.get("/docs", include_in_schema=False)
async def get_documentation():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")

@app.get("/apikey")
def get_apikey():
    encoded = base64.b64encode(('tester:tester').encode('ascii')).decode('ascii')
    return {"CommentOut this function": encoded}

@app.get("/")
def connection_test():
    return {"Happy": "Coding"}

@app.get("/hit")
def hit_test(isauth: str = Depends(authenticate_test)):
    return {"Happy": "Coding"}

#schedule
@app.get("/firehealthcheck")
async def fire_healthcheck_josb(background_tasks: BackgroundTasks,isauth: str = Depends(authenticate_test)):
    if background_tasks.tasks.count < 1:
        background_tasks.add_task(run_health_check)
    return {"message": "Live database is running now"}

if __name__ == "__main__":
    uvicorn.run("main:app", host=lib_consts.apihostip, port = lib_consts.apiport, reload=False)