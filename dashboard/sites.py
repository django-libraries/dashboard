from django.urls import path

class DashboardSite:
    def __init__(self):
        self._registry = {}

    def register(self, dashboard_cls):
        dashboard_name = dashboard_cls.__name__
        if dashboard_name in self._registry:
            raise ValueError(f"Dashboard already registered: {dashboard_name}")

        self._registry[dashboard_name] = dashboard_cls

    def get_dashboard(self, name):
        return self._registry.get(name)

    def get_registered_dashboards(self):
        return self._registry


dashboard_site = DashboardSite()
