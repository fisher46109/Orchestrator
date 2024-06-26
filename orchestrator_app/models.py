from django.db import models


class Machine(models.Model):
    machine_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.machine_name


class User(models.Model):
    user_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.user_name


class Robot(models.Model):
    robot_name = models.CharField(max_length=100, unique=True)
    # Robot file

    def __str__(self):
        return self.robot_name


class Process(models.Model):
    process_name = models.CharField(max_length=100, unique=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    state = models.CharField(max_length=100, blank=True, default="-")
    result = models.CharField(max_length=100, blank=True, default="-")
    ssk_flag = models.CharField(max_length=100, blank=True, default="-")
    robot_update_flag = models.CharField(max_length=100, blank=True, default="-")

    class Meta:
        unique_together = [['machine', 'user']]

    def __str__(self):
        return self.process_name
