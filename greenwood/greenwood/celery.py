import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greenwood.settings')

app = Celery('greenwood',broker='redis://127.0.0.1:6379/0')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule={
    'renew_data_base':{'task':'homepage.tasks.create_data','schedule':60.00*60*3},
                        'select_listings_for_catalog':{'task':'homepage.tasks.select_listings_for_catalog','schedule':60*60.00},
                        'select_listings_for_hp':{'task':'homepage.tasks.select_listings_for_hp','schedule':200.00},
'test_task':{'task':'homepage.tasks.test_task','schedule':60.00},
}
