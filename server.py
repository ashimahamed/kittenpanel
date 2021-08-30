from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import uvicorn
import sys
import git
from routes import api_admin, api_client, api_oauth, auth, dashboard, default

with open("config.json", "rb") as file:
    config = json.load(file)
app = FastAPI(title=config['appname'], docs_url="/api/docs", redoc_url="/api/docs")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

routes = [api_admin, api_client, api_oauth, auth, dashboard, default]
for route in routes:
    app.include_router(route.router)


if __name__ == "__main__":
    print(f"""\
██   ██ ██ ████████ ████████ ███████ ███    ██ ██████   █████  ███    ██ ███████ ██      
██  ██  ██    ██       ██    ██      ████   ██ ██   ██ ██   ██ ████   ██ ██      ██      
█████   ██    ██       ██    █████   ██ ██  ██ ██████  ███████ ██ ██  ██ █████   ██      
██  ██  ██    ██       ██    ██      ██  ██ ██ ██      ██   ██ ██  ██ ██ ██      ██      
██   ██ ██    ██       ██    ███████ ██   ████ ██      ██   ██ ██   ████ ███████ ███████ 
Version - {git.Repo(search_parent_directories=True).git.rev_parse("HEAD", short=7)}

Copyright © 2021 MythicalKitten

 Source:  https://github.com/kittensaredabest/kittenpanel
License:  https://github.com/kittensaredabest/kittenpanel/blob/main/LICENSE

This software is made available under the terms of the MIT license.
The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.
    """)
    uvicorn.run("server:app", host=config['webserver']['host'], port=config['webserver']['port'], reload=config['webserver']['debug'], debug=config['webserver']['debug'], workers=config['webserver']['workers'])