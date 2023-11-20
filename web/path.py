from web.handler import *
ROUTE_PATH = [
    (r'/', root),
    (r'/static(.*)', STATIC),
    (r'/API(.*)', APIs)
]
