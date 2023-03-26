from django.http import HttpResponse
from django.shortcuts import render
from calculus.services import handle_calculation, operations, examples


# Create your views here.


def calculator(request, op, a, b):
    result = handle_calculation(op, a, b)
    return render(
        request,
        "calculus/calculations.html",
        {"result": result}
    )


def home(request):
    # return HttpResponse(f"Dostępne operacje: {[x for x in operations]}")
    return render(
        request,
        "calculus/home.html",
        {"operations": [x for x in operations]}
    )


def operation(request, op):
    path_example, result, op_long = examples[op]
    return render(
        request,
        "calculus/examples.html",
        {
            "path_example": path_example,
            "result": result,
            "op_long": op_long
        }

    )
