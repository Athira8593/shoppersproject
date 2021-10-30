from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, first_name, last_name,phone_no, username, email, password = None):
        if not email:
            raise ValueError('email is not valid')
        if not username:
            raise ValueError('user is not valid')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            phone_no = phone_no,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self,first_name, last_name, username, password, email):
        user = self.create_user(
                email = self.normalize_email(email),
                username = username,
                password = password,
                first_name = first_name,
                last_name = last_name
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using = self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone_no = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50 , blank=True)
    town = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100, blank=True)
    pin = models.CharField(max_length=6, blank=True)
    image = models.ImageField(upload_to='pf', blank=True)

    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = AccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True



