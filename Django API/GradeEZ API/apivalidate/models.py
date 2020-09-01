from django.db import models


class ApiValidate(models.Model):
    string = models.TextField()

    def take_string(self):
        return {
            'string': self.string
        }
