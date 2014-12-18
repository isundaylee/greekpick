from django.db import models

class VoteManager(models.Manager):
  def count_choice(self, c):
    return self.get_query_set().filter(choice = c).count()

class Vote(models.Model):
    choice = models.TextField()

    objects = VoteManager()

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"

    def __str__(self):
        pass


