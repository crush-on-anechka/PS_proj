from django.core.paginator import Paginator

LIMIT_LINES: int = 10


def paginator(request, objs):
    paginator = Paginator(objs, LIMIT_LINES)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return page_object
