from django import forms
from .models import Machine, User, Robot, Process


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['machine_name']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name']


class RobotForm(forms.ModelForm):
    class Meta:
        model = Robot
        fields = ['robot_name']


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ['process_name', 'machine', 'user', 'robot']
