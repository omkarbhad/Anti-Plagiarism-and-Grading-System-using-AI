from django.db import models


class ApiGrade(models.Model):
    string = models.TextField()
    custom_marks = models.IntegerField()

    def take_string(self):
        return {
            'string': self.string,
            'custom_marks': self.custom_marks
        }
