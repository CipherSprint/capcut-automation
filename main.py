import random
from pathlib import Path
import logging
from importlib import import_module
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Form, Request, BackgroundTasks, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from apscheduler.schedulers.background import BackgroundScheduler
from typing import Optional

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/run_script/")
async def run_script(request: Request, background_tasks: BackgroundTasks, 
                     number_of_variation: Optional[int] = Form(None),
                     badbunny: bool = Form(False), tuileries: bool = Form(False), sardinia: bool = Form(False), berlin: bool = Form(False), dolce: bool = Form(False), humble: bool = Form(False), 
                     clear: bool = Form(False), copper: bool = Form(False), plum: bool = Form(False), urbanoid: bool = Form(False), robust: bool = Form(False), 
                     salt: bool = Form(False), metal: bool = Form(False), gray: bool = Form(False), shadow: bool = Form(False), taro: bool = Form(False), mistletoe: bool = Form(False), 
                     pine: bool = Form(False), gingerbread: bool = Form(False), nature: bool = Form(False), autumn: bool = Form(False), cold: bool = Form(False), 
                     tan: bool = Form(False), umber: bool = Form(False), holiday: bool = Form(False), snack: bool = Form(False), french: bool = Form(False), bake: bool = Form(False), 
                     cuisine: bool = Form(False), western: bool = Form(False), eclipse: bool = Form(False), peach : bool = Form(False), cold_brew : bool = Form(False), latte : bool = Form(False), 
                     veggie : bool = Form(False), fling : bool = Form(False), hope : bool = Form(False), freedom : bool = Form(False), barbie : bool = Form(False), oppenheimer : bool = Form(False), 
                     budapest : bool = Form(False), dispatch : bool = Form(False), flipped : bool = Form(False), scent : bool = Form(False), inception : bool = Form(False), 
                     oasis : bool = Form(False), dunkirk : bool = Form(False), woodland : bool = Form(False), maple : bool = Form(False), radiance : bool = Form(False), hawaii : bool = Form(False), 
                     voyage : bool = Form(False), maldives : bool = Form(False), hiking : bool = Form(False), nightfall : bool = Form(False), garden : bool = Form(False), 
                     december : bool = Form(False), picnic : bool = Form(False), dusk : bool = Form(False), hasselblad : bool = Form(False), fuji : bool = Form(False), 
                     shade : bool = Form(False), remote : bool = Form(False), friends : bool = Form(False), miami : bool = Form(False), beverly : bool = Form(False), 
                     princeton : bool = Form(False), film : bool = Form(False), tunnel : bool = Form(False), fade : bool = Form(False), warlock : bool = Form(False), jazz : bool = Form(False), 
                     brown : bool = Form(False), weird : bool = Form(False), yandere : bool = Form(False), negative : bool = Form(False), dope : bool = Form(False), sunset : bool = Form(False), 
                     burgundy : bool = Form(False), ghost : bool = Form(False), pumpkin : bool = Form(False), vaporwave : bool = Form(False), sepia: bool = Form(False), red: bool = Form(False)
                    ):
    
    x = ["badbunny", "tuileries", "sardinia", "berlin", "dolce", "humble", "clear", "copper", "plum", "urbanoid", "robust", "salt", "metal", "gray", "shadow", "taro", "mistletoe", "pine", "gingerbread", "nature", "autumn", "cold", "tan", "umber", "holiday", "snack", "french", "bake", "cuisine", "western", "eclipse", "peach", "cold_brew", "latte", "veggie", "fling", "hope", "freedom", "barbie", "oppenheimer", "budapest", "dispatch", "flipped", "scent", "inception", "oasis", "dunkirk", "woodland", "maple", "radiance", "hawaii", "voyage", "maldives", "hiking", "nightfall", "garden", "december", "picnic", "dusk", "hasselblad", "fuji", "shade", "remote", "friends", "miami", "beverly", "princeton", "film", "tunnel", "fade", "warlock", "jazz", "brown", "weird", "yandere", "negative", "dope", "sunset", "burgundy", "ghost", "pumpkin", "vaporwave", "sepia", "red"]

    y = [badbunny, tuileries, sardinia, berlin, dolce, humble, clear, copper, plum, urbanoid, robust, salt, metal, gray, shadow, taro, mistletoe, pine, gingerbread, nature, autumn, cold, tan, umber, holiday, snack, french, bake, cuisine, western, eclipse, peach, cold_brew, latte, veggie, fling, hope, freedom, barbie, oppenheimer, budapest, dispatch, flipped, scent, inception, oasis, dunkirk, woodland, maple, radiance, hawaii, voyage, maldives, hiking, nightfall, garden, december, picnic, dusk, hasselblad, fuji, shade, remote, friends, miami, beverly, princeton, film, tunnel, fade, warlock, jazz, brown, weird, yandere, negative, dope, sunset, burgundy, ghost, pumpkin, vaporwave, sepia, red]

    selected_filters = [value.capitalize() for value, condition in zip(x, y) if condition]

    try:
        crawler_module = import_module("capcut")                                 
        start_parse = crawler_module.start_parse
    except (ImportError, AttributeError) as e:
        logging.error(f"Failed to import capcut.start_parse: {e}")
        raise HTTPException(status_code=500, detail="Failed to import crawler")

    background_tasks.add_task(start_parse, number_of_variation, *selected_filters)

    result_message = "Scraper is running in the background"

    return templates.TemplateResponse("result.html", {"request": request, "result_message": result_message})


scheduler = BackgroundScheduler()
scheduler.start()
