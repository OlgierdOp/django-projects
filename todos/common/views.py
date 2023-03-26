from django.core.paginator import Paginator


def paginate(request, klass):

    objects = klass.objects.all()

    per_page = request.GET.get("per_page", 10)
    page_number = request.GET.get("page", 1)
    paginator = Paginator(objects, per_page)
    page_obj = paginator.get_page(page_number)

    return page_obj
