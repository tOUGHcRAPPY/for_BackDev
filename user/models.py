from django.db import models


class Gender(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class User(models.Model):
    nickname = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # TODO Django's make_password
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    gender = models.OneToOneField(
        Gender, null=True, blank=True, on_delete=models.SET_NULL
    )


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=50)
    expiration_date = models.DateTimeField()


class LoginAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class PasswordRecovery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recovery_code = models.CharField(max_length=50)
    expiration_date = models.DateTimeField()