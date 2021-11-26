from celery import shared_task

from core.models import Session, Event

@shared_task(bind=True, ignore_result=True, name='core.tasks.save_event')
def save_event(self, validated_data):
    session_id = validated_data.pop('session_id')
    application_id = validated_data.pop('application_id')
    validated_data['session'] = Session.objects.get_or_create(id=session_id, application_id=application_id)[0]
    Event.objects.create(**validated_data)
    return 'event saved'