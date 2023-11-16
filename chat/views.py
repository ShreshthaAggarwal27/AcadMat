from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from base.models import Book, Material
from .models import ChatMessage
from .forms import ChatMessageForm
from django.db.models import Q


def chat(request, owner_name):
    receiver = User.objects.get(username=owner_name)
    sender_profile = request.user
    receiver_profile = receiver
    form = ChatMessageForm()
    chats = ChatMessage.objects.all()

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = sender_profile
            chat_message.msg_receiver = receiver_profile
            chat_message.save()
            return redirect('chat', owner_name=owner_name)

    context = {'receiver': receiver, 'form': form, 'sender_profile': sender_profile, 'receiver_profile': receiver_profile, 'chats': chats}
    return render(request, 'chat/chatroom.html', context)

@login_required
def all_chats(request):
    receiver_profile = request.user

    # Get a list of unique senders with whom the receiver has chatted
    senders = User.objects.filter(
        Q(msg_sender__msg_receiver=receiver_profile) | Q(msg_receiver__msg_sender=receiver_profile)
    ).distinct()

    # Get the latest chat message with each sender
    chats = ChatMessage.objects.all()        

    # Display the chat form
    form = ChatMessageForm()

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = receiver_profile
            chat_message.msg_receiver = User.objects.get(username=request.POST.get('receiver_username'))
            chat_message.save()
            return redirect('all_chats')

    context = {'senders': senders, 'receiver_profile': receiver_profile, 'chats': chats, 'form': form}
    return render(request, 'chat/all_chats.html', context)

@login_required
def receiver_chat(request, receiver):
    receiver_profile = request.user

    # Get a list of unique senders with whom the receiver has chatted
    senders = User.objects.filter(
        Q(msg_sender__msg_receiver=receiver_profile) | Q(msg_receiver__msg_sender=receiver_profile)
    ).distinct()

    receiver = User.objects.get(username=receiver)
    sender_profile = request.user
    receiver_profile = receiver
    form = ChatMessageForm()
    chats = ChatMessage.objects.all()

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = sender_profile
            chat_message.msg_receiver = receiver_profile
            chat_message.save()
            return redirect('receiver_chat', receiver=receiver_profile.username)

    context = {'receiver': receiver, 'form': form, 'sender_profile': sender_profile, 'receiver_profile': receiver_profile, 'chats': chats, 'senders': senders}
    return render(request, 'chat/receiver_chat.html', context)


