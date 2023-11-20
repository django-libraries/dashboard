from django.urls import path


class DashboardSite:
    def __init__(self):
        self._registry = {}

    def register(self, dashboard_cls):
        # 获取 dashboard_cls 的 __module__
        module = dashboard_cls.__module__
        # 分割 __module__，获取 app_name
        module_list = module.split('.')
        if len(module_list) == 2:
            app_name = module_list[0]
        elif len(module_list) > 2:
            app_name = module_list[len(module_list) - 2]
        else:
            raise ValueError(f"Dashboard module error: {module}")
        self._registry[app_name] = dashboard_cls
        # dashboard_name = dashboard_cls.__name__
        # if dashboard_name in self._registry:
        #     raise ValueError(f"Dashboard already registered: {dashboard_name}")
        #
        # self._registry[dashboard_name] = dashboard_cls

    def get_dashboard(self, name):
        return self._registry.get(name)

    def get_registered_dashboards(self):
        return self._registry


dashboard_site = DashboardSite()
