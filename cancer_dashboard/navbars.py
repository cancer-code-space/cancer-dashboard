from django.conf import settings

from edc_navbar import NavbarItem, site_navbars, Navbar


if settings.APP_NAME == 'cancer_dashboard':
    no_url_namespace = None
else:
    no_url_namespace = 'cancer_dashboard'

cancer_dashboard = Navbar(name='cancer_dashboard')

cancer_dashboard.append_item(
    NavbarItem(
        name='consented_subject',
        title='Subjects',
        label='subjects',
        fa_icon='fa-user-circle-o',
        url_name=settings.DASHBOARD_URL_NAMES['consent_listboard_url'],
        no_url_namespace=no_url_namespace))

cancer_dashboard.append_item(
    NavbarItem(
        name='enrollment_checklist',
        title='Enrollment Checklist',
        label='Enrollment',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES['checklist_listboard_url'],
        no_url_namespace=no_url_namespace))


site_navbars.register(cancer_dashboard)