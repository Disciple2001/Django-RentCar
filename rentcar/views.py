from http.client import HTTPResponse

from django.http import response
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Brand, Tourist
from .models import Car
from .models import Model
from django.views import generic
from . import forms


# Create your views here.
def index(request):
    return render(request, "rentcar/pages/index.html")


class CarView(generic.ListView):
    model = Car
    template_name = 'rentcar/pages/cars.html'


class CarCreateView(generic.CreateView):
    model = Car
    template_name = 'rentcar/pages/car_create.html'
    form_class = forms.CarCreateForm
    success_url = "/"

class CarDetailView(generic.DetailView):
    model = Car
    template_name = 'rentcar/pages/car_detail.html'


class BrandView(generic.ListView):
    model = Brand
    template_name = 'rentcar/pages/brands.html'


class BrandDetailView(generic.DetailView):
    model = Brand
    template_name = 'rentcar/pages/brand_detail.html'


class BrandCreateView(generic.CreateView):
    model = Brand
    template_name = 'rentcar/pages/brand_create.html'
    form_class = forms.BrandCreateForm
    success_url = reverse_lazy('brands')


class BrandDeleteView(generic.DeleteView):
    model = Brand
    template_name = 'rentcar/pages/brand_delete.html'
    success_url = reverse_lazy('brands')


class BrandUpdateView(generic.UpdateView):
    model = Brand
    template_name = 'rentcar/pages/brand_update.html'
    form_class = forms.BrandUpdateForm
    success_url = reverse_lazy('brands')


class ModelView(generic.ListView):
    model = Model
    template_name = 'rentcar/pages/models.html'


class ModelCreateView(generic.CreateView):
    model = Model
    template_name = 'rentcar/pages/model_create.html'
    form_class = forms.ModelCreateForm
    success_url = "/"


class ModelDetailView(generic.DetailView):
    model = Model
    template_name = 'rentcar/pages/model_detail.html'


class ModelUpdateView(generic.UpdateView):
    model = Model
    template_name = 'rentcar/pages/model_update.html'
    form_class = forms.ModelUpdateForm
    success_url = reverse_lazy('models')



class ModelDeleteView(generic.DeleteView):
    model = Model
    template_name = "rentcar/pages/model_delete.html"
    success_url = reverse_lazy('models')


class TouristListView(generic.ListView):
    model = Tourist
    template_name = 'rentcar/pages/tourist/tourist_list.html'


class TouristView(generic.View):
    def get(self, request):
        return render(request, 'rentcar/pages/tourist/tourist_index.html')


class TouristDeleteView(generic.DeleteView):
    model = Tourist

    def form_valid(self, form):
        self.object.delete()
        return response.JsonResponse({})


class TouristDetailView(generic.DetailView):
    model = Tourist
    template_name = 'rentcar/pages/tourist/tourist_detail.html'

class TouristUpdateView(generic.UpdateView):
    model = Tourist
    template_name = 'rentcar/pages/tourist/tourist_form.html'
    form_class = forms.TouristForm

class TouristCreateView(generic.CreateView):
    model = Tourist
    template_name = 'rentcar/pages/tourist/tourist_form.html'
    form_class = forms.TouristForm
    success_url = reverse_lazy('tourist')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form),status=400)

class BrandIndexView(generic.View):
    def get(self, request):
        return render(request, 'rentcar/pages/brand/brand_index.html')

class BrandListView(generic.ListView):
    model = Brand
    template_name = 'rentcar/pages/brand/brand_list.html'

class BrandDeleteView(generic.DeleteView):
    model = Brand

    def form_valid(self, form):
        self.object.delete()
        return response.JsonResponse({})


class BrandDetailView(generic.DetailView):
    model = Brand
    template_name = 'rentcar/pages/brand/brand_detail.html'

class BrandUpdateView(generic.UpdateView):
    model = Brand
    template_name = 'rentcar/pages/brand/brand_form.html'
    form_class = forms.BrandForm

class BrandCreateView(generic.CreateView):
    model = Brand
    template_name = 'rentcar/pages/brand/brand_form.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brandv2')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form),status=400)
