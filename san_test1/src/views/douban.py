from sanic import Sanic
from sanic.response import json, text, html
from jinja2 import Environment, PackageLoader, select_autoescape
from sanic import Blueprint
from sanic.response import html
import sys
from src.config import CONFIG



index_bp = Blueprint('index_html', url_prefix='html')
index_bp.static('/static/douban', CONFIG.BASE_DIR + '/static/douban')


# https://github.com/channelcat/sanic/blob/5bb640ca1706a42a012109dc3d811925d7453217/examples/jinja_example/jinja_example.py
# 开启异步特性  要求3.6+
enable_async = sys.version_info >= (3, 6)



# jinjia2 config
env = Environment(
    loader=PackageLoader('views.rss', '../templates'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']),
    enable_async=enable_async
    )


async def template(tpl, **kwargs):
    template = env.get_template(tpl)
    rendered_template = await template.render_async(**kwargs)
    return html(rendered_template)



@index_bp.route("/")
async def index(request):
    return await template('douban/index.html')





