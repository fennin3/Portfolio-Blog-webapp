
def portfolios(request):
    from .models import Portfolio
    return {'portfolios':Portfolio.objects.all()}