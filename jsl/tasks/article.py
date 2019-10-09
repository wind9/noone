from worker import app
import requests


@app.task()
def do_article():
    pass


