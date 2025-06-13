from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import EventSerializer



@login_required
def home(request):
    events = Event.objects.filter(user=request.user).order_by('date', 'time')

    # Prepare event data for JSON rendering (for FullCalendar or JS)
    event_data = [
        {
            "id": event.id,
            "title": event.title,
            "start": f"{event.date}T{event.time}",  # ISO 8601 format
            "description": event.description,
        }
        for event in events
    ]

    return render(request, 'home.html', {
        'events': events,          # For manual list view if needed
        'event_data': event_data   # For JSON rendering in template
    })


@login_required
def create_event(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        date = request.POST['date']
        time = request.POST['time']

        Event.objects.create(
            user=request.user,
            title=title,
            description=description,
            date=date,
            time=time
        )
        return redirect('home')

    return render(request, 'create_event.html')


@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    event.delete()
    return redirect('home')


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)

    if request.method == 'POST':
        event.title = request.POST['title']
        event.description = request.POST.get('description', '')
        event.date = request.POST['date']
        event.time = request.POST['time']
        event.save()
        return redirect('home')

    return render(request, 'edit_event.html', {'event': event})


@login_required
def event_list(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'event_list.html', {'events': events})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("register")

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Registration successful! You can now log in.")
        return redirect("login")

    return render(request, "register.html")

class EventListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)
    
class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Event deleted successfully"}, status=status.HTTP_200_OK)