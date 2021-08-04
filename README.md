# alumni-api
Alumni Backend is a database-backed serverless Django application, that uses: 

 * [Django 3.2.6](https://docs.djangoproject.com/en/3.2.6/) as the web framework,
 * [Google Cloud Run](https://cloud.google.com/run/) as the hosting platform,
 * [Google Cloud SQL](https://cloud.google.com/sql/) as the managed database (via [django-environ](https://django-environ.readthedocs.io/en/latest/)), 
 * [Google Cloud Storage](https://cloud.google.com/storage/) as the media storage platform (via [django-storages](https://django-storages.readthedocs.io/en/latest/)),
 * [Google Cloud Build](https://cloud.google.com/cloud-build/) for build and deployment automation, and
 * [Google Secret Manager](https://cloud.google.com/secret-manager/) for managing encrypted values.

## Deployment

Deployment using Terraform.  

## Application Design

### Alumni API

### Service design - one deployment per Google Cloud project

Alumni API runs as a Cloud Run service. 
Using the Python package `django-storages`, it's been configured to take a `GS_BUCKET_NAME` as a storage place for its media. 
Using the Python package `django-environ` it takes a complex `DATABASE_URL`, which will point to a Cloud SQL PostgreSQL database. 
The `settings.py` is also designed to pull a specific secret into the environment. 
These are all designed to live in the same Google Cloud Project.

In this way, Alumni API runs 1:1:1 -- 
one Cloud Run Service, 
one Cloud SQL Database, 
one Google Storage bucket. 

It also assumes that there is *only* one service/database/bucket. 
