from rest_framework import serializers
from .models import Process


class ProcessSerializer(serializers.ModelSerializer):

    # Use __str__ representation to show foreign values
    machine = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    robot = serializers.StringRelatedField()

    class Meta:
        model = Process
        fields = ['machine', 'user', 'robot', 'state', 'result', 'ssk_flag', 'robot_update_flag']

