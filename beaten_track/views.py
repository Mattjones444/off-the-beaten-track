def custom_403(request, exception=None):
    return render(request, '403.html', status=403)

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)