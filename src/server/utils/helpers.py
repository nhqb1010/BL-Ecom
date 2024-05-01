from django.http import HttpRequest

def is_admin_add_url(request: HttpRequest) -> bool:
    url = request.get_full_path()

    return "/add" in url and "admin" in url