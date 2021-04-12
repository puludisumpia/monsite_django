from datetime import datetime


def inject_site_name(request):
    return {"site_name": "mpia.com"}


def inject_date(request):
    return {"date": datetime.utcnow()}
