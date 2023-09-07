from django.shortcuts import render, redirect  
from django.contrib import messages
from django.contrib.auth.models import User
from AcadMat import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str, force_bytes
from django.contrib.auth import authenticate, login, logout
from .tokens import generate_token
from .models import Book, Institution, Category
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
    context = {'form': form}
    return render(request, 'base/donate_book.html', context)

@login_required(login_url='login')
def donate_material(request):
    
    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.donor = request.user
            book.save()
            return redirect('home')  # Redirect to the home page or a success page
    else:
        form = DonationForm()
    context = {'form': form}
    return render(request, 'base/donate_material.html', context)


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
    context = {'form': form}
    return render(request, 'base/donate_to_institution.html', context)


def user_profile(request, username):
    user = User.objects.get(username = username)
    context = {'user': user}
    return render(request, 'base/profile.html', context)


def home(request):
    books = Book.objects.filter(available=True)
    institutions = Institution.objects.all()
    context = {'books': books, 'institutions': institutions}
    return render(request, 'base/index.html', context)


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

