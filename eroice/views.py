from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, CreateUserFormLanding, WriteForm, CommentForm
from .models import Story, Genre, Profile, Like, Comment
from django.core.mail import send_mail

# Helper function for user registration and landing views
def registration_logic(request, form_class, template_name):
    if request.user.is_authenticated:
        return redirect("home")

    form = form_class(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        user = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        messages.success(
            request,
            f"Hi, {user}! Your Eroice account is successfully created! Please Log in.",
        )
        send_mail(
            f"Welcome to Eroice, {user}",
            f"Dear {user},\n\nThank you for choosing Eroice. We're delighted to welcome you to our community!\n\nBelow are your account details:\n\nUsername: {user}\nEmail: {email}\n\nFeel free to explore our platform, share your stories, and engage with fellow writers and readers.\n\nIf you have any questions or need assistance, please don't hesitate to contact us.\n\nBest regards,\nThe Eroice Team",
            "eroice.id@gmail.com",
            [email],
            fail_silently=False,
        )
        return redirect("login")

    context = {"form": form}
    return render(request, template_name, context)

# Login page view
def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or password incorrect")

    return render(request, "login/index.html", {})

# Logout user view
def logout_view(request):
    logout(request)
    return redirect("landing")

# User registration view
def register_view(request):
    return registration_logic(request, CreateUserForm, "signup/index.html")

# Landing page view
def landing_view(request):
    return registration_logic(request, CreateUserFormLanding, "landing/index.html")


# Home page view


@login_required(login_url="login")
def home_view(request):
    username = request.user.username
    stories = Story.objects.all()
    genres = Genre.objects.all()

    return render(
        request,
        "home/index.html",
        {"username": username, "stories": stories, "genres": genres},
    )


# Write view


@login_required(login_url="login")
def write_view(request):
    username = request.user.username
    if request.method == "POST":
        form = WriteForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.user = Profile.objects.get(user=request.user)
            stock.save()
            form.save_m2m()
            return redirect("/")
    else:
        form = WriteForm()

    genres = Genre.objects.all()
    context = {"form": form, "genres": genres, "username": username}
    return render(request, "write/index.html", context)


@login_required(login_url="login")
def story_view(request, pk_story):
    username = request.user.username
    story = get_object_or_404(Story, id=pk_story)
    user_profile = Profile.objects.get(user=request.user)
    liked_by_user = story.like_set.filter(user=user_profile).exists()
    
    if request.method == "POST":
        if request.POST.get("comment"):
            form = CommentForm(request.POST)
            if form.is_valid():
                stock = form.save(commit=False)
                stock.user = user_profile
                stock.story = story
                stock.save()
        else:
            if liked_by_user:
                story.like_set.filter(user=user_profile).delete()
            else:
                Like.objects.create(user=user_profile, story=story)

    else:
        form = CommentForm()
        story.view += 1
        story.save()

    likes = story.like_set.all().count()
    genres = Genre.objects.all()

    like_icon = (
        "bxs-heart text-red-500 dark:text-red-500"
        if liked_by_user
        else "bx-heart text-primary dark:text-gray-50"
    )
    
    comments = Comment.objects.filter(story=story)

    context = {
        "story": story,
        "genres": genres,
        "likes": likes,
        "like_icon": like_icon,
        "form": form,
        "comments": comments,
        "username": username,
    }
    
    return render(request, "story/index.html", context)


# 404 error view


def handle_not_found(request, exception):
    return render(request, "404/index.html", {})


# 500 error view


def handle_server_error(request):
    return render(request, "500/index.html", {})


# Genre view


@login_required(login_url="login")
def genre_view(request, pk_genre):
    username = request.user.username
    stories = Story.objects.filter(genre__name=pk_genre)
    genres = Genre.objects.all()

    context = {
        "genre": pk_genre,
        "stories": stories,
        "genres": genres,
        "username": username,
    }
    return render(request, "genre/index.html", context)
