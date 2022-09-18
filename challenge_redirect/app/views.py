from django.core.cache import cache
from django.http import JsonResponse
from django.views import View

class RedirectView(View):
    
    def get(self, request, key:str):
        """ Se recibira la key, se realizara una busqueda
        en la cache y devolveremos su respectiva url.
        """
        url = cache.get(key)
        if url == None:
            return JsonResponse({'error': 'Url not found'}, status=404)
        return JsonResponse({'key': [key], 'url': [url]}, status=200)