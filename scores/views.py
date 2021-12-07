from django.db.models import Q
from django.shortcuts import render
from .models import Fixture

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def fixtures(request):
    fixtures = Fixture.objects.all()

    # check if all are completed
    all_completed = all(f.game_finished for f in fixtures)

    search = request.GET.get('search')
    if search:
        fixtures = fixtures.filter(
            Q(home_team__name__icontains=search) | Q(away_team__name__icontains=search)
        )

    context = {
        'fixtures': fixtures,
        'all_completed': all_completed
    }

    if request.htmx:
        import time
        time.sleep(0.6)
        if all_completed:
            response = render(request, 'partials/fixturelist.html', context)
            response['HX-Refresh'] = "true"
            return response
        return render(request, 'partials/fixturelist.html', context)
    else:
        return render(request, 'fixtures.html', context)
