from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import generic
from pyexpat.errors import messages

from .form import CustomUserCreationForm
from  .models import Car

# Create your views here.

class CarList(generic.ListView):
    queryset = Car.objects.filter(status=1).order_by('-pub_date')
    template_name = 'index.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Car.objects.filter(
                 Q(marque__icontains=query) | Q(prix__icontains=query),
                status=1
            ).order_by('-created')

        return Car.objects.filter(status=1).order_by('-created')

class CarDetail(generic.DetailView):
    model = Car
    template_name = 'detail.html'


from django.shortcuts import render
from .models import Car  # N'oublie pas l'import !


def home(request):
    cars_from_db = Car.objects.all()
    context = {
        'cars': cars_from_db
    }
    return render(request, 'index.html', context)

def inscription(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('CarList')
        else:
            messages.error(request, 'Email ou password incorrect')
    return render(request, 'connexion.html')

