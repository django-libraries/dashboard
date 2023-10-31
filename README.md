# Django Template Dashboard

A dashboard based on Django template.

## Installation

Install the package via pip:

```bash
pip install django-template-dashboard
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
the [project page](https://github.com/fuqiang-code/django-template-dashboard).

## License

This project is licensed under the [MIT License](LICENSE).