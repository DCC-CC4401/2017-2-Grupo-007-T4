from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.conf import settings

from CholitoProject.userManager import get_user_index
from complaint.models import AnimalType
from naturalUser.forms import PersonRegisterForm
from municipality.forms import MunicipalidadRegisterForm
from ong.forms import ONGRegisterForm
from ong.models import ONG


class IndexView(TemplateView):
    context = {}

    def get(self, request, **kwargs):
        c_user = get_user_index(request.user)
        self.context['c_user'] = c_user
        animals = AnimalType.objects.all()
        self.context['animals'] = animals
        ongs = ONG.objects.all()
        self.context['ongs'] = ongs
        self.context['key'] = settings.GOOGLE_API_KEY
        if c_user is None:
            return render(request, 'index.html', context=self.context)
        return c_user.get_index(request, context=self.context)


class LogInView(TemplateView):
    template_name = 'login.html'
    animals = AnimalType.objects.all()
    context = {'animals': animals}

    def get(self, request, **kwargs):
        return render(request, self.template_name, context=self.context)


class SignUpView(View):
    person_form = PersonRegisterForm()
    muni_form = MunicipalidadRegisterForm()
    ong_form = ONGRegisterForm()

    animals = AnimalType.objects.all()
    context = {'person': person_form, 'muni': muni_form, 'ong': ong_form, 'animals': animals}
    template_name = 'sign_up.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name, context=self.context)

    def post(self, request, **kwargs):
        person = PersonRegisterForm(request.POST, request.FILES)
        muni = MunicipalidadRegisterForm(request.POST, request.FILES)
        ong = ONGRegisterForm(request.POST, request.FILES)

        if person.is_valid():
            person.save()

        if muni.is_valid():
            muni.save()

        if ong.is_valid():
            ong.save()

        return redirect('/')


class UserDetail(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'naturalUser.natural_user_access'

    def post(self, request, **kwargs):
        c_user = get_user_index(request.user)
        c_user.user.first_name = request.POST['f_name']
        c_user.user.last_name = request.POST['l_name']
        if 'avatar' in request.FILES:
            c_user.avatar = request.FILES['avatar']
        c_user.save()
        return redirect('/')


class OngInViewTemplate(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    permission_required = 'naturalUser.natural_user_access'
    template_name = 'usuario-in-ong.html'
    context = {}

    def get(self, request, **kwargs):
        c_user = get_user_index(request.user)
        self.context['c_user'] = c_user
        animals = AnimalType.objects.all()
        self.context['animals'] = animals
        return render(request, self.template_name, context=self.context)


class OngOutViewTemplate(TemplateView):
    template_name = 'usuario-out-ong.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)
