from fastapi import FastAPI
import os
import fastapi_jinja
import uvicorn
from starlette.staticfiles import StaticFiles
from views import home,movie,tvshow,account,plan

app = FastAPI()



dev_mode = True

folder = os.path.dirname(__file__)
template_folder = os.path.join(folder, 'templates')
template_folder = os.path.abspath(template_folder)

fastapi_jinja.global_init(template_folder, auto_reload=dev_mode)


app.mount('/static',StaticFiles(directory = 'static'),name='static')

app.include_router(home.router)
app.include_router(movie.router)
app.include_router(tvshow.router)
app.include_router(account.router)
app.include_router(plan.router)

if __name__ == '__main__':
    uvicorn.run(app)