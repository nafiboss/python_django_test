import datetime

def custom_context(request):
    now = datetime.datetime.now()
    return {'current_date_time': now.strftime("%Y-%m-%d %H:%M")}