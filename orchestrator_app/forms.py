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
        fields = ['robot_name', 'zip_file']

    def clean_zip_file(self):
        """ Function automatically started while form validation (as all clean_... functions)
            Check if file has .zip or .rar extension
        """
        zip_file = self.cleaned_data.get('zip_file')
        if zip_file:
            if not zip_file.name.endswith('.zip'):
                raise forms.ValidationError("Only .zip files allowed.")
        return zip_file


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ['process_name', 'machine', 'user', 'robot']
