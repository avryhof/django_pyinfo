# Frontend Assets
```bash
pip install django_pyinfo
```

A phpinfo() like page for your django project.

## settings.py
```python
INSTALLED_APPS = [
    ...,
    django_pyinfo,
    ...,
]

# Only works if debug is true... this is NOT a view that should be accessible in production.
DEBUG = True
```

## urls.py
```python
url(r'^', include('django_pyinfo.urls')),
```

Now go to - http://your-staging-site.com/pyinfo/