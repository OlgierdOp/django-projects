from django import forms

from tasks.models import Todo


class TodoForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    done = forms.BooleanField(required=False)


TodoFormset = forms.formset_factory(TodoForm, extra=3)


class TodoForm2(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "done", "group"]