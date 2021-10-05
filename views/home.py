import fastapi
from fastapi import Request
from fastapi_jinja import template

router = fastapi.APIRouter()


@router.get('/')
@template('home/index.j2')
async def home(request: Request):
    return {
        'username':'som valid username'
    }