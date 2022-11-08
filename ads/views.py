import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import DetailView

from ads.models import Ad, Category


def index(request):
    response = {'status': 'ok'}
    return JsonResponse(response, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    """Get all ads"""

    def get(self, request):
        ads = Ad.objects.all()
        response = []
        for ad in ads:
            response.append(
                {
                    'id': ad.id,
                    'name': ad.name,
                    'author': ad.author,
                    'price': ad.price,
                    'description': ad.description,
                    'address': ad.address,
                    'is_published': ad.is_published
                }
            )

        return JsonResponse(response, safe=False, status=200)

    """Get a new ad"""

    def post(self, request):
        data = json.loads(request.body)
        ad = Ad(**data)
        ad.save()

        return JsonResponse(
            {
                'id': ad.id,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
            }, status=201
        )


class AdView(DetailView):
    model = Ad

    """Get ad by pk"""

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse(
            {
                'id': ad.id,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
                'description': ad.description,
                'address': ad.address,
                'is_published': ad.is_published
            }
        )


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    """Get all categories"""

    def get(self, request):
        categories = Category.objects.all()
        response = []
        for cat in categories:
            response.append(
                {
                    'id': cat.pk,
                    'name': cat.name,
                }
            )

        return JsonResponse(response, safe=False, status=200)

    """Get a new ad"""

    def post(self, request):
        data = json.loads(request.body)
        cat = Category(**data)
        cat.save()

        return JsonResponse(
            {
                'id': cat.id,
                'name': cat.name,
            }, status=201
        )


class CategoryView(DetailView):
    model = Category

    """Get category by pk"""

    def get(self, request, *args, **kwargs):
        cat = self.get_object()

        return JsonResponse(
            {
                'id': cat.id,
                'name': cat.name,
            }
        )
