from django.shortcuts import render

from tasks.forms import TodoForm, TodoFormset, TodoForm2
from tasks.models import Todo
from tasks.services import ModelTodosService as Todos


def tasks_list(request):

    form = TodoForm2()
    formset = TodoFormset()

    if request.method == "POST":

        with Todos() as todos:

            form = TodoForm2(data=request.POST)
            # title = request.POST.get("title")
            # description = request.POST.get("description")
            # done = request.POST.get("done", False)
            if form.is_valid():
                task = form.cleaned_data
                # task = {
                #     "title": title,
                #     "description": description,
                #     "done": done
                # }

                todo = todos.create(task)
                print("Utworzono todo", todo)

    with Todos() as todos:
        tasks = todos.all()

    return render(
        request,
        "tasks/list.html",
        {"todos": tasks, "form": form, "formset": formset}
    )


def task_details(request, id):

    if request.method == "POST":
        data = dict(request.POST)
        data.pop("csrfmiddlewaretoken")
        print(data)
        with Todos() as todos:
            data = {k: v[0] for k, v in data.items()}
            todos.update(id, data)

    with Todos() as todos:
        task = todos.get(id)

    form = TodoForm2(instance=task)

    return render(
        request,
        "tasks/details.html",
        {"todo": task, "form": form}
    )


def add_task(request):

    if request.method == "POST":

        t = Todo.objects.create()

