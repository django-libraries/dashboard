# Django Template Dashboards

A dashboard based on Django template.

## Installation

Install the package via pip:

```bash
pip install django-dashboards
```

## Configuration

After installing the package, add it to your `INSTALLED_APPS` in the `settings.py` file of your Django project:

```python
INSTALLED_APPS = [
    # ... other apps,
    'dashboards',
]
```

Include the dashboard urls in your project's `urls.py` file:

```python
from django.urls import include, path

urlpatterns = [
    # ... other urls,
    path('dashboards/', include('dashboards.urls')),
]
```

## Usage

Navigate to `/dashboards/` in your browser to access the dashboard.

## Development

To contribute or report issues, please visit
the [dashboards](https://github.com/django-libraries/dashboards).

## License

This project is licensed under the [MIT License](LICENSE).