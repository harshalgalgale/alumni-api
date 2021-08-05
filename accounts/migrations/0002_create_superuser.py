import os

from django.db import migrations

import google.auth
from google.cloud import secretmanager_v1 as sm

from accounts.models import UserManager


def access_secrets(secret_keys):
    secrets = {}
    _, project = google.auth.default()

    if project:
        client = sm.SecretManagerServiceClient()

        for s in secret_keys:
            name = f"projects/{project}/secrets/{s}/versions/latest"
            payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")
            secrets[s] = payload

    return secrets


def createsuperuser(apps, schema_editor):
    settings = ["ALUMNI_SUPERUSER", "ALUMNI_SUPERPASS"]
    if not all (k in os.environ.keys() for k in set(settings)):
        secrets = access_secrets(settings)
        username = secrets["ALUMNI_SUPERUSER"]
        password = secrets["ALUMNI_SUPERPASS"]
    else:
        username = os.environ["ALUMNI_SUPERUSER"]
        password = os.environ["ALUMNI_SUPERPASS"]

    email = username + '@alumni.com'

    # Create a new user using acquired password
    UserManager.create_superuser(username=username,
                                 email=email,
                                 password=password)


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [migrations.RunPython(createsuperuser)]
