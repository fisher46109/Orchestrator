from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .forms import MachineForm, RobotForm, UserForm, ProcessForm
from .models import Process, User, Machine, Robot
from .serializers import ProcessSerializer


class ProcessView(viewsets.ModelViewSet):
    """  Class to handle API"""
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    http_method_names = ['get', ' put', 'patch', 'post']

    def get_object(self):
        """ Get process object for specified conditions (user and machine) based on url query
            Ensures data acquisition from ForeignKeys arguments
        """

        # Get parameters from url query (.../get_object/?user=<user>&machine=<machine>)
        user_name = self.request.query_params.get('user')
        machine_name = self.request.query_params.get('machine')

        # Get objects from specified classes (where object corresponds to query arguments)
        user = get_object_or_404(User, user_name=user_name)
        machine = get_object_or_404(Machine, machine_name=machine_name)

        # return object from Process where user and machine corresponds to processed query
        return get_object_or_404(Process, user=user, machine=machine)

    @action(detail=False, methods=['patch'])
    def update_info(self, request):
        """ Update attribute "state" for specified object """

        try:
            process = self.get_object()
            # Get parameter result from dictionary in data section in request

            ssk_flag_value = request.data.get('ssk_flag')
            state_value = request.data.get('state')
            result_value = request.data.get('result')
            robot_update_flag_value = request.data.get('robot_update_flag')

            if ssk_flag_value and state_value and result_value and robot_update_flag_value:
                process.ssk_flag = ssk_flag_value
                process.state = state_value
                process.result = result_value
                process.robot_update_flag = robot_update_flag_value
                process.save()

                serializer = self.get_serializer(process)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "control values not provided"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def home_view(request):
    processes = Process.objects.all()
    return render(request, 'orchestrator_app/processes_table.html', {'processes': processes})


def machines_view(request):
    machines = Machine.objects.all()
    return render(request, 'orchestrator_app/machines.html', {'machines': machines})


def new_machine(request):
    if request.method == "POST":
        form = MachineForm(request.POST)
        if form.is_valid():
            machine = form.save(commit=False)
            machine.machine_name = form.cleaned_data['machine_name']
            machine.save()
            return redirect('machines-view')
    else:
        form = MachineForm()
    return render(request, 'orchestrator_app/machine_edit.html', {'form': form})


def remove_machine(request, machine_id):
    machine = get_object_or_404(Machine, pk=machine_id)
    machine.delete()
    return redirect('machines-view')


def edit_machine(request, machine_id):
    machine = get_object_or_404(Machine, pk=machine_id)

    if request.method == "POST":
        form = MachineForm(request.POST, instance=machine)
        if form.is_valid():
            form.save()
            return redirect('machines-view')
    else:
        form = MachineForm(instance=machine)

    return render(request, 'orchestrator_app/machine_edit.html', {'form': form})


def users_view(request):
    users = User.objects.all()
    return render(request, 'orchestrator_app/users.html', {'users': users})


def new_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_name = form.cleaned_data['user_name']
            user.save()
            return redirect('users-view')
    else:
        form = UserForm()
    return render(request, 'orchestrator_app/user_edit.html', {'form': form})


def remove_user(request, user_id):
    machine = get_object_or_404(User, pk=user_id)
    machine.delete()
    return redirect('users-view')


def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users-view')
    else:
        form = UserForm(instance=user)

    return render(request, 'orchestrator_app/user_edit.html', {'form': form})


def robots_view(request):
    robots = Robot.objects.all()
    return render(request, 'orchestrator_app/robots.html', {'robots': robots})


def new_robot(request):
    if request.method == "POST":
        form = RobotForm(request.POST)
        if form.is_valid():
            robot = form.save(commit=False)
            robot.robot_name = form.cleaned_data['robot_name']
            robot.save()
            return redirect('robots-view')
    else:
        form = RobotForm()
    return render(request, 'orchestrator_app/robot_edit.html', {'form': form})


def remove_robot(request, robot_id):
    robot = get_object_or_404(Robot, pk=robot_id)
    robot.delete()
    return redirect('robots-view')


def edit_robot(request, robot_id):
    robot = get_object_or_404(Robot, pk=robot_id)

    if request.method == "POST":
        form = RobotForm(request.POST, instance=robot)
        if form.is_valid():
            form.save()
            return redirect('robots-view')
    else:
        form = RobotForm(instance=robot)

    return render(request, 'orchestrator_app/robot_edit.html', {'form': form})

def scheduler_view(request):
    return render(request, 'orchestrator_app/scheduler.html')


def new_process(request):
    if request.method == "POST":
        form = ProcessForm(request.POST)
        if form.is_valid():
            process = form.save(commit=False)
            process.process_name = form.cleaned_data['process_name']
            process.machine = form.cleaned_data['machine']
            process.user = form.cleaned_data['user']
            process.robot = form.cleaned_data['robot']
            process.save()
            return redirect('home-view')
    else:
        form = ProcessForm()
    return render(request, 'orchestrator_app/process_edit.html', {'form': form})


def edit_process(request, process_id):
    process = get_object_or_404(Process, pk=process_id)

    if request.method == "POST":
        form = ProcessForm(request.POST, instance=process)
        if form.is_valid():
            form.save()
            return redirect('home-view')
    else:
        form = ProcessForm(instance=process)

    return render(request, 'orchestrator_app/process_edit.html', {'form': form})



def remove_process(request, process_id):
    process = get_object_or_404(Process, pk=process_id)
    process.delete()
    return redirect('home-view')


def start_process(request, process_id):
    if request.method == "POST":
        process = get_object_or_404(Process, pk=process_id)
        process.ssk_flag = "START"
        process.save()
        return redirect('home-view')


def stop_process(request, process_id):
    if request.method == "POST":
        process = get_object_or_404(Process, pk=process_id)
        process.ssk_flag = "STOP"
        process.save()
        return redirect('home-view')


def kill_process(request, process_id):
    if request.method == "POST":
        process = get_object_or_404(Process, pk=process_id)
        process.ssk_flag = "KILL"
        process.save()
        return redirect('home-view')

