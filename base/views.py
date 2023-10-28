from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect  
from django.contrib import messages
from django.contrib.auth.models import User
from AcadMat import settings
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str, force_bytes
from django.contrib.auth import authenticate, login, logout
from .tokens import generate_token
from .models import Book, Institution, BookCategory, Material, MaterialCategory
from .forms import BookDonationForm, BookCategoryForm, MaterialDonationForm, MaterialCategoryForm, ProductSearchForm

@login_required(login_url='login')
def donate_book(request):
    if request.method == 'POST':
        form = BookDonationForm(request.POST, request.FILES)
        category_form = BookCategoryForm(request.POST)  

        if form.is_valid():
            book = form.save(commit=False)

            category_name = request.POST.get('category')
            category, created = BookCategory.objects.get_or_create(name=category_name)

            book.category = category
            book.donor = request.user
            book.save()
            messages.success(request, "Added the book on the site!")
            return redirect('home') 
    else:
        form = BookDonationForm()
        category_form = BookCategoryForm()

    context = {'form': form, 'category_form': category_form}
    return render(request, 'base/give_away_book.html', context)

@login_required(login_url='login')
def donate_material(request):
    if request.method == 'POST':
        form = MaterialDonationForm(request.POST, request.FILES)
        category_form = MaterialCategoryForm(request.POST)  

        if form.is_valid():
            item = form.save(commit=False)

            category_name = request.POST.get('category')
            category, created = MaterialCategory.objects.get_or_create(name=category_name)

            item.category = category
            item.donor = request.user
            item.save()
            messages.success(request, "Added the item on the site!")
            return redirect('home') 
    else:
        form = MaterialDonationForm()
        category_form = MaterialCategoryForm()

    context = {'form': form, 'category_form': category_form}
    return render(request, 'base/give_away_material.html', context)


def user_profile(request, username):
    user = User.objects.get(username = username)
    book_donations = Book.objects.filter(donor = user)
    material_donations = Material.objects.filter(donor = user)
    book_donations_count = book_donations.count()
    material_donations_count = material_donations.count()
    context = {'user': user, 
               'book_donations': book_donations,
               'material_donations': material_donations,
               'book_donations_count': book_donations_count, 
               'material_donations_count':material_donations_count}
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first-name')
        user.last_name = request.POST.get('last-name')
        user.city = request.POST.get('city')
        user.phone_number = request.POST.get('phone-number')
        user.email = request.POST.get('email')
        user.save()  # Save the updated user data
        messages.success(request, "Profile updated successfully!")
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})



def home(request):
    books = Book.objects.filter(available=True)
    institutions = Institution.objects.all()
    context = {'books': books, 'institutions': institutions}
    return render(request, 'base/index.html', context)


def free_books(request):
    category_name = request.GET.get('q')
    publication_name = request.GET.get('publication')
    condition = request.GET.get('condition')
    if category_name:
        books = Book.objects.filter(category__name=category_name, available=True)
    elif publication_name:
        books = Book.objects.filter(publication=publication_name, available=True)
    elif condition:
        books = Book.objects.filter(condition=condition, available=True)
    else:
        books = Book.objects.filter(available=True)
    categories = BookCategory.objects.all()
    sort_by = request.GET.get('sort_by')
    if sort_by == 'title':
        books = books.order_by('title')
    elif sort_by == 'author':
        books = books.order_by('author')
    unique_conditions = set()
    for book in books:
        unique_conditions.add(book.condition)
    context = {'books': books, 'categories': categories, 'unique_conditions': unique_conditions}
    return render(request, 'base/free_books.html', context)

def priced_books(request):
    category_name = request.GET.get('q')
    publication_name = request.GET.get('publication')
    condition = request.GET.get('condition')
    if category_name:
        books = Book.objects.filter(category__name=category_name, available=True)
    elif publication_name:
        books = Book.objects.filter(publication=publication_name, available=True)
    elif condition:
        books = Book.objects.filter(condition=condition, available=True)
    else:
        books = Book.objects.filter(available=True)
    categories = BookCategory.objects.all()
    sort_by = request.GET.get('sort_by')
    if sort_by == 'title':
        books = books.order_by('title')
    elif sort_by == 'author':
        books = books.order_by('author')
    unique_conditions = set()
    for book in books:
        unique_conditions.add(book.condition)
    context = {'books': books, 'categories': categories, 'unique_conditions': unique_conditions}
    return render(request, 'base/priced_books.html', context)

def free_material(request):
    category_name = request.GET.get('q')
    company_name = request.GET.get('company')
    condition = request.GET.get('condition')
    if category_name:
        material = Material.objects.filter(category__name=category_name, available=True)
    elif company_name:
        material = Material.objects.filter(company=company_name, available=True)
    elif condition:
        material = Material.objects.filter(condition=condition, available=True)
    else:
        material = Material.objects.filter(available=True)

    categories = MaterialCategory.objects.all()
    unique_conditions = set()

    for item in material:
        cleaned_condition = item.condition.strip().lower()
        unique_conditions.add(cleaned_condition)

    context = {'material': material, 'categories': categories, 'unique_conditions': unique_conditions}
    return render(request, 'base/free_material.html', context)

def priced_material(request):
    category_name = request.GET.get('q')
    company_name = request.GET.get('company')
    condition = request.GET.get('condition')

    if category_name:
        material = Material.objects.filter(category__name=category_name, available=True)
    elif company_name:
        material = Material.objects.filter(company=company_name, available=True)
    elif condition:
        material = Material.objects.filter(condition=condition, available=True)
    else:
        material = Material.objects.filter(available=True)

    categories = MaterialCategory.objects.all()
    unique_conditions = set()

    for item in material:
        cleaned_condition = item.condition.strip().lower()
        unique_conditions.add(cleaned_condition)

    context = {'material': material, 'categories': categories, 'unique_conditions': unique_conditions}
    return render(request, 'base/priced_material.html', context)


def search_products(request):
    products = []

    if request.method == 'GET':
        query = request.GET.get('query')

        if query:

            if query == 'books' or query == 'Books' or query == 'BOOKS':
                books = Book.objects.all()
                for book in books:
                     products.append({'name': book.title, 'price': book.price, 'category': book.category.name, 'condition': book.condition, 'images': book.images.url})

            else:
                book_results = Book.objects.filter(title__icontains=query)
                book_results |= Book.objects.filter(author__icontains=query)
                book_results |= Book.objects.filter(publication__icontains=query)
                book_results |= Book.objects.filter(description__icontains=query)
                book_results |= Book.objects.filter(price__icontains=query)
                book_results |= Book.objects.filter(condition__icontains=query)
                book_results |= Book.objects.filter(category__name__icontains=query)


                material_results = Material.objects.filter(name__icontains=query)
                material_results |= Material.objects.filter(company__icontains=query)
                material_results |= Material.objects.filter(description__icontains=query)
                material_results |= Material.objects.filter(price__icontains=query)
                material_results |= Material.objects.filter(condition__icontains=query)
                material_results |= Material.objects.filter(category__name__icontains=query)
                

                for book in book_results:
                    products.append({'name': book.title, 'price': book.price, 'category': book.category.name, 'condition': book.condition, 'images': book.images.url})
                for material in material_results:
                    products.append({'name': material.name, 'price': material.price, 'category': material.category.name, 'condition': material.condition, 'images': material.images.url})

    return render(request, 'base/search.html', {'products': products})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'base/book_detail.html', {'book': book})

def material_detail(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    return render(request, 'base/material_detail.html', {'material': material})


def signup(request):
    page = 'register'
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')
    
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

        subject = "Welcome to AcadMat"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to AcadMat!! \nThank you for visiting our website.\n We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n Team AcadMat"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ AcadMat!!"
        message2 = render_to_string('base/email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        send_mail(email_subject, message2, from_email, to_list, fail_silently=True)
        return redirect('login')
        
    context = {'page' : page}
    return render(request, 'base/login_signup.html', context)


def login_page(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username = username, password = password)

        if user is not None and user.is_authenticated:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('profile', username = user.username)
        else:
            messages.error(request, 'Incorrect username or password')
            
    context = {'page': page}
    return render(request, 'base/login_signup.html', context)


def logout_page(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('profile', username= myuser.username)
    else:
        return render(request,'confirmation_failed.html')

