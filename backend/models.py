import uuid

from django.db import models


"""
Instead of generating and re-trying logic for creating unique short url 'on-the-fly',
for the sake of this quick project I'll be generating the unique 'shortcuts" (url links)
in the project creation, and afterwards will be popping once a new Link is shortened
"""
temp = [uuid.uuid4().hex[:6] for _ in range(100000)]  # Create 100.000 almost unique shortcuts using UUID
shortcuts = set(temp)  # Convert the list to a set to remove any duplicates from it
print("Generated {} unique shortcuts".format(len(shortcuts)))  # Tell us how many have been created (around 99.700)
del temp  # Delete the temporary list as it's not used anymore


class Shortener(models.Model):
    original_url = models.URLField(max_length=255, blank=False, null=False)
    short_url = models.CharField(max_length=100, unique=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    times_visited = models.PositiveIntegerField(default=0)

    # user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.short_url + " : " + self.original_url

    def save(self, *args, **kwargs):
        if not self.pk:
            self.short_url = shortcuts.pop()
            print('Poped value {} and mapped it to URL: {}'.format(self.short_url, self.original_url))
        super().save(*args, **kwargs)

    def get_short_url(self):
        return "http://localhost:80/" + self.short_url

    def get_original_url(self):
        return self.original_url
