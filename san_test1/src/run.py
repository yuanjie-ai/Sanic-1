# !/usr/bin/env python
import sys

from sanic import Sanic

sys.path.append('../')
from src.views import index_bp

app = Sanic(__name__)

app.blueprint(index_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
