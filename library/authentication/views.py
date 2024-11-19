import os

from author.models import Author
from book.models import Book
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from order.models import Order
from .forms import RegistrationForm, LoginForm

from .models import CustomUser


def myroom(request):
    msg_admin_create_author = " "
    msg_admin_create_book = " "
    msg_admin_find = " "

    if request.method == 'POST':
        form_num = int(request.POST.get('unique_number'))

        if form_num == 1:
            name = request.POST['book_name']
            description = request.POST['book_description']
            count = request.POST['book_count']

            Book.create(name=name, description=description, count=count)
            msg_admin_create_book = "You just add the new book"

        elif form_num == 2:
            name = request.POST['author_name']
            surname = request.POST['author_surname']
            patronimic = request.POST['author_patronimic']

            Author.create(name=name, surname=surname, patronymic=patronimic)
            msg_admin_create_author = "Successfull added!"

        elif form_num == 3:
            selected_option = request.POST.get('option')

            if selected_option == "user":
                input_value = request.POST.get('search')
                msg_admin_find = find_user(input_value)
            elif selected_option == "author":
                input_value = request.POST.get('search')
                msg_admin_find = find_author(input_value)
            elif selected_option == "book":
                input_value = request.POST.get('search')
                msg_admin_find = find_book(input_value)
            elif selected_option == "order":
                input_value = request.POST.get('search')
                msg_admin_find = find_order(input_value)

    modules_dir = os.path.join(settings.BASE_DIR, 'templates/modules/')
    all_module_files = [f for f in os.listdir(modules_dir) if f.endswith('.html')]

    module_files = []

    if request.user.is_authenticated:
        if request.user.role == 2:
            module_files = all_module_files
        elif request.user.role == 1:
            module_files = [f for f in all_module_files if (f.startswith('user_') or f.startswith('guest_'))]
        elif request.user.role == 0:
            module_files = [f for f in all_module_files if f.startswith('guest_')]
    else:
        module_files = []

    return render(request, 'myroom/myroom.html', {'module_files': module_files,
                                                  'msg_admin_create_author': msg_admin_create_author,
                                                  'msg_admin_create_book': msg_admin_create_book,
                                                  'msg_admin_find_book': msg_admin_find})




def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            middle_name = form.cleaned_data.get('middle_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                email=email,
                password=password
            )
            user.is_active = True
            user.save()

            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')

        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')


def find_book(part):
    books = Book.objects.all()
    part = str(part)
    finded = []
    response = "Your Results: "

    for i in books:

        if part.lower() in i.name.lower():
            finded.extend([i.id])

    for i in finded:
        book = Book.objects.get(id=i)
        response += f"The Book: {book.name} with id: {book.id}.  "

    return response


def find_author(part):
    authors = Author.objects.all()
    part = str(part)
    finded = set()
    response = "Your Results: "

    for i in authors:

        if part.lower() in i.name.lower():
            finded.update([i.id])

        if part.lower() in i.surname.lower():
            finded.update([i.id])

        if part.lower() in i.patronymic.lower():
            finded.update([i.id])

    for i in finded:
        author = Author.objects.get(id=i)
        response += f"The Author: {author.name} with id: {author.id}.  "

    return response


def find_user(part):
    users = CustomUser.objects.all()
    part = str(part)
    finded = set()
    response = "Your Results: "
    for i in users:
        if type(i.first_name) is str:
            if part.lower() in i.first_name.lower():
                finded.update([i.id])

        if type(i.last_name) is str:
            if part.lower() in i.last_name.lower():
                finded.update([i.id])

        if type(i.middle_name) is str:
            if part.lower() in i.middle_name.lower():
                finded.update([i.id])

    for i in finded:
        user = CustomUser.objects.get(id=i)
        response += f"The User: {user.first_name} with id: {user.id}, user email {user.email} and role {user.role}.  "

    return response


def find_author(part):
    authors = Author.objects.all()
    part = str(part)
    finded = set()
    response = "Your Results: "

    for i in authors:

        if part.lower() in i.name.lower():
            finded.update([i.id])

        if part.lower() in i.surname.lower():
            finded.update([i.id])

        if part.lower() in i.patronymic.lower():
            finded.update([i.id])

    for i in finded:
        author = Author.objects.get(id=i)
        response += f"The Author: {author.name} with id: {author.id}.  "

    return response


def find_order(id):
    orders = Order.objects.all()
    id = str(id)

    for i in orders:
        if str(i.id) == id:
            user = CustomUser.objects.get(id=i.user_id)
            book = Book.objects.get(id=i.book_id)
            return f"The order ID is {i.id}. User: {user.email}. Book: {book.name}"

    return "There are no orders like this()"
