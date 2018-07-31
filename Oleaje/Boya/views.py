from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages


from .forms import DateForm
from .models import Boya

@login_required
def register(request):
    Boyas = []
    form = DateForm()

    if request.method == "POST":
        Boyas = Boya.objects.filter(date__range=[request.POST['start_date'],
                                                request.POST['final_date']])
        if (Boyas.count() == 0) :
            messages.info(request, 'No hay registro de datos en las fechas selecionadas')

    return render(request, "Boya/register.html",
                        {'form' : form,
                        'mesuares' : Boyas })
