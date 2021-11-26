from django.db import models
import uuid


class Application(models.Model):
    """
        Application model provides information about what websites are allowed to send data.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    host = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

class Session(models.Model):
    """
        Session model provides a unique identifier for each event session.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '%s' % self.id

class Event(models.Model):
    """
        Event model save all kind of events and your data associated with a Section.
    """
    class Meta:
        ordering = ['timestamp']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, db_index=True)
    name = models.CharField(max_length=120)
    data = models.JSONField(default=dict)
    timestamp = models.DateTimeField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '%s' % self.id