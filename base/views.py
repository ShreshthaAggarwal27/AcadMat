from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Book, UserProfile, Institution, Category
from .forms import DonationForm

@login_required(login_url='login')
def donate_book(request):
    
    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.donor = request.user
            book.save()
            return redirect('home')  # Redirect to the home page or a success page
    else:
        form = DonationForm()
    return render(request, 'base/donate_book.html', {'form': form})



@login_required(login_url='login')
def donate_to_institution(request):
    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.donor = request.user
            book.save()
            return redirect('home')  # Redirect to the home page or a success page
    else:
        form = DonationForm()
    return render(request, 'base/donate_to_institution.html', {'form': form})

@login_required(login_url='login')
def view_profile(request, username):
    user = get_object_or_404(UserProfile, user__username=username)
    return render(request, 'base/profile.html', {'user': user})

def home(request):
    books = Book.objects.filter(available=True)
    institutions = Institution.objects.all()
    
    return render(request, 'base/index.html', {'books': books, 'institutions': institutions})


def all_books(request):
    books = Book.objects.filter(available=True)
    categories = Category.objects.all()
    sort_by = request.GET.get('sort_by')
    if sort_by == 'title':
        books = books.order_by('title')
    elif sort_by == 'author':
        books = books.order_by('author')
    context = {'books': books, 'categories': categories}
    return render(request, 'base/all_books.html', context)

def signup(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred while registering!')
    context = {'form': form, 'page' : page}
    return render(request, 'base/login_register.html', context)

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username = username, password = password)

        if user is not None and user.is_authenticated:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Incorrect username or password')
            
    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')

