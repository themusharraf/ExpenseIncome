from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')  # foydalanuvchi username ega bo'lishi kerak
        if email is None:
            raise TypeError('Users should have a email')  # foydalanuvchi email ega bo'lishi kerak
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Users should have a password')  # foydalanuvchi password ega bo'lishi kerak
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
