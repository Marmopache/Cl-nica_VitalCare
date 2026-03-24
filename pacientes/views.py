from django.shortcuts import render
from .models import Paciente, Doctor, HoraMedica
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PacienteForm, DoctorForm, HoraMedicaForm
from django.contrib.auth.decorators import login_required

@login_required
def panel_control(request):
    """
    Vista del panel de control, accesible solo para usuarios logueados.
    """
    return render(request, 'clinica/panel_control.html')


# =========================
# PACIENTES
# =========================
class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
    template_name = 'pacientes/paciente_list.html'
    context_object_name = 'pacientes'


class PacienteCreateView(LoginRequiredMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('paciente_list')

    def form_valid(self, form):
        messages.success(self.request, "Paciente creado correctamente.")
        return super().form_valid(form)


class PacienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'pacientes/paciente_form.html'
    success_url = reverse_lazy('paciente_list')

    def form_valid(self, form):
        messages.success(self.request, "Paciente actualizado correctamente.")
        return super().form_valid(form)


class PacienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Paciente
    template_name = 'pacientes/paciente_confirm_delete.html'
    success_url = reverse_lazy('paciente_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Paciente eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
    
# =========================
# DOCTORES
# =========================
class DoctorListView(LoginRequiredMixin, ListView):
    model = Doctor
    template_name = 'doctores/doctor_list.html'
    context_object_name = 'doctores'


class DoctorCreateView(LoginRequiredMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctores/doctor_form.html'
    success_url = reverse_lazy('doctor_list')

    def form_valid(self, form):
        messages.success(self.request, "Doctor creado correctamente.")
        return super().form_valid(form)


class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctores/doctor_form.html'
    success_url = reverse_lazy('doctor_list')

    def form_valid(self, form):
        messages.success(self.request, "Doctor actualizado correctamente.")
        return super().form_valid(form)


class DoctorDeleteView(LoginRequiredMixin, DeleteView):
    model = Doctor
    template_name = 'doctores/doctor_confirm_delete.html'
    success_url = reverse_lazy('doctor_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Doctor eliminado correctamente.")
        return super().delete(request, *args, **kwargs)
    
# =========================
# HORAS MÉDICAS
# =========================
class HoraMedicaListView(LoginRequiredMixin, ListView):
    model = HoraMedica
    template_name = 'horas/hora_list.html'
    context_object_name = 'horas'


class HoraMedicaCreateView(LoginRequiredMixin, CreateView):
    model = HoraMedica
    form_class = HoraMedicaForm
    template_name = 'horas/hora_form.html'
    success_url = reverse_lazy('hora_list')

    def form_valid(self, form):
        messages.success(self.request, "Hora médica registrada correctamente.")
        return super().form_valid(form)


class HoraMedicaUpdateView(LoginRequiredMixin, UpdateView):
    model = HoraMedica
    form_class = HoraMedicaForm
    template_name = 'horas/hora_form.html'
    success_url = reverse_lazy('hora_list')

    def form_valid(self, form):
        messages.success(self.request, "Hora médica actualizada.")
        return super().form_valid(form)


class HoraMedicaDeleteView(LoginRequiredMixin, DeleteView):
    model = HoraMedica
    template_name = 'horas/hora_confirm_delete.html'
    success_url = reverse_lazy('hora_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Hora médica eliminada.")
        return super().delete(request, *args, **kwargs)