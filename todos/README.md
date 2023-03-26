#

## cwiczenie - routing + views

1. Utwórz aplikację - calculus
2. Utwórz widok/i obsługujące adresy

```
   /calculus/add/1/2
   /calculus/sub/1/2 
   ...
```


## cwiczenie - include

1. zrób include urls dla aplikacji calculus
2. dodaj widok
    
    /calculus/ - wypisz dostępne operacje


    Dostępne operacje to: add, sub, mul, div

## Dodanie szablonu

Dodaj szablon w aplikacji calculus - dla operacji. 

## Uzycie szablonu

Popraw szablon (z użyciem extends ) dla widoku calculus/home

przekaż do kontekstu zestaw dostępnych operacji. 


Jeśli chcesz wykoma dodawanie, to wejdź na adres

/calculus/add/1/2/

rezultatem będzie wypisane 

Result: 3


## tworzymy aplikacje tasks

wykorzystujac kod przygotowany do aplikacji flaskowej

https://github.com/rkorzen/python_17_12_2022/blob/master/web_projects/flask_projects/todos/db.py
 
wykorzystaj istniejący todos.json

wyświetlamy todosy:

1. widok wyświetlający listę todos
2. widok szczegółów


##  dodajemy update todo

   - formularz na stronie szczegółów
   - obsługa metody POST w widoku details
   - akutalizacja serwisu - dodanie metody update


## Dodanie końcówki /contact/

Obsługa formularza contact
- przeniesc w całosci formularz contact do aplikacji main
- dodac widok (+ url)
- wyprintowac dane wysłane z formularza

## przerobic formularz kontaktowy na bootstrapowy - przy pomocy crispy

## Django extensions

https://django-extensions.readthedocs.io/en/latest/shell_plus.html?highlight=print%20sql#sql-queries

# Migracje

python manage.py showmigrations   # pokazuje stan wykonania migracji
python manage.py makemigrations   # przygotowuje migracje
python manage.py makemigrations --empty tasks  # tworzy pustą migrację w aplikacji tasks
python manage.py sqlmigrate tasks 0002   # pokazuje sql jaki bedzie wykonany dla migracji 0002 z aplikacji tasks

python manage.py migrate # wykona niewykoanne migracje

jakby trzeba było wykona migrację... nie wykonując sqla

https://stackoverflow.com/questions/46772762/django-migrate-fake-and-fake-initial-explained


python manage.py inspectdb  # tworzenie modeli na podstawie istniejącej bazy danych


## django management commands(in shell)

https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

## cofanie migracji

jesli w tasks mamy 3 migracje o numerach 0001, 0002, 0003

i są one wykonane

to cofniecie sie do 0002 realizujemy poleceniem:

python manage.py migrate tasks 0002

jeżeli to była custom migration to musi by reverse code


migrations.RunPython(add_tasks, reverse_code=reverse_code),

reverse_code - to jakaś funkcja - może nic nie robic

```
def reverse_code(apps, schema_editor):
    pass
```


## ORM 


### tworzenie
Todo.objects.create(title="costam", description="costam") # tworzenie instancji i zapisywanie

```
   # alternatywnie
   t = Todo()
   t.title = "costam"
   t.description = "csota"
   t.save()
```

### Pobieranie

Task.objects.all()
Task.objects.first()
Task.objects.last()

Task.objects.filter(title__endswith="k")   # zwraca queryset obiektow ktorych tytul konczy sie na k
Task.objects.get(id=1)  # zwraca obiekt o id=1


## Cwiczenie - napisz nowy serwis

Ma dzialac jak poprzedni (mam miec te same metody) ale implementcja oparat o Djangowy model


## Cwiczenie

- tworzymy nowa aplikację books
- tworzymy model Book
  - title
  - description
  - year
  - author
- widok listy ksiażek
- widok szczegółów książki
- do tego szablony
- formularz - do dodania i aktualizacji ksiazki

Można zrobi serwis. Lub korzysta z metod ORM w widoku


## Cwiczenie - forms.ModelForm

- zmien w books formularze na formularze oparte o model
- tworz instancje w oparciu o model


# Panel Admina

## Logowanie


http://127.0.0.1:8000/admin


     python manage.py createsuperuser 


# Relacje

## cwiczenie

w aplikacji books utwórz model reprezentujący autora oraz model profil autora któ®y będzie w relacji O2O 
z Autorem.

## cwiczenie

W PA dla książki dodaj inline z autorem


## cwiczenie

Utwórz aplikację posts.
Oprócz pól takich jak title, description powinna byc tam relacja O2M / M2O (ForeginKey) z userem (auth.User)
Dodaj to do PA


## cwiczenei

wprowadz relację M2M pomiedzy Book a Tag (po stronie Book ) + PA

## Cwiczenie

Dodaj kolejny mixin rozszerzając klasę abstrakcujna timestamped - niech sprawdza czy był modyfikowany w ciagu ostatnich x minut

## Cwiczenie

wyodrebnij stworzone mixiny do common.mixins
wyodrębnij nasz model abstrakcyjny do common.models
rozszerz Book o Timestamped

## Cwiczenie

export ksiazek w Panelu Admina


## Cwiczenie

Dodaj okładkę (ImageField) dla Book

## Cwiczenie 

wyświetl okłądkę w widoku szczegółów książki

## Cwiczenia

Dodaj w UserProfile zdjecie. Uzyj formularza opartego o model by w nowym widoku i szablonie uzyc formularza do edycji profilu

## Zadanie

wygeneruj 100 postów

## Zadanie

1. wygeneruj 10 losowych autorów
2. Generowanie 100 ksiażek (z losowym autorem) + dodanie paginacji w widoku listy ksiazek

## Zadanie

Dodaj header - pasek nawigacji na górze strony

link do listy postów
link do listy ksiażek

link do strony zalogowania
link do strony wylogowania

## Zadanie

Powtórzenie dla postów - dodanie nazw dla ścieżek w urls i dodanie namespace