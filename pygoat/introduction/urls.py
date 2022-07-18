from django.urls import path,include

from .import views
from . import apis
from introduction.playground.A9.api import log_function_target

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='homepage'),
    path('xss', views.xss,name="xss"),
    path('xssL',views.xss_lab,name='xss_lab'),
    path('xssL1',views.xss_lab,name='xss_lab'),
    path("sql",views.sql,name='sql'),
    path("sql_lab",views.sql_lab,name="sql_lab"),
    path("sql_lab1",views.sql_lab,name="sql_lab"),
    path("insec_des",views.insec_des,name="insec_des"),
    path("insec_des_lab",views.insec_des_lab,name="insec_des_lab"),
    path("xxe",views.xxe,name="xxe"),
    path("xxe_lab",views.xxe_lab,name="xxe_lab"),
    path("xxe_see",views.xxe_see,name="xxe_see"),
    path("xxe_parse",views.xxe_parse,name="xxe_parse"),
    path("auth_lab",views.auth_lab,name="auth_lab"),
    path("auth_lab/signup",views.auth_lab_signup,name="auth_lab_signup"),
    path("auth_lab/login",views.auth_lab_login,name="auth_lab_login"),
    path("auth_lab/logout",views.auth_lab_logout,name="auth_lab_logout"),
    path("auth",views.auth_home,name="auth_home"),
    path("ba",views.ba,name="Broken Access Control"),
    path("ba_lab",views.ba_lab,name="Broken Access Control Lab"),
    path("data_exp",views.data_exp,name="data_exp"),
    path("data_exp_lab",views.data_exp_lab,name="data_exp_lab"),
    path("robots.txt",views.robots,name="robots.txt"),
    path("500error",views.error,name="500error"),
    path("cmd",views.cmd,name="Command Injection"),
    path("cmd_lab",views.cmd_lab,name="Command Injection Lab"),
    path("bau", views.bau, name="Broken Authe"),
    path("bau_lab", views.bau_lab, name="LAB"),
    path("login_otp", views.login_otp, name="OTP Login"),
    path("otp", views.Otp, name="OTP Verification"),
    path("sec_mis", views.sec_mis, name="Security Misconfiguration"),
    path("sec_mis_lab", views.sec_mis_lab, name="Security Misconfiguration Lab"),
    path("sec_mis_lab3", views.sec_misconfig_lab3, name="Security Misconfiguration Lab"),
    path("secret", views.secret, name="Secret key for A6"),
    path("a9",views.a9,name="A9"),
    path("a9_lab",views.a9_lab,name="A9 LAb"),
    path("a9_lab2",views.a9_lab2,name="A9 LAb 2"),
    path("get_version",views.get_version,name="Get Version"),
    path("a10",views.a10,name="A10"),
    path("a10_lab",views.a10_lab,name="A10 LAb"),
    path("a10_lab_2",views.a10_lab2,name="A10 LAb 2"),
    path("debug",views.debug,name="debug"),
    path("insecure-design",views.insec_desgine,name="insecure-design"),
    path("insecure-design_lab",views.insec_desgine_lab,name="insecure-design_lab"),
    path("broken_access_control", views.a1_broken_access, name="broken_access"),
    path("broken_access_lab_1", views.a1_broken_access_lab_1, name="broken_access_lab_1"),
    path("broken_access_lab_2", views.a1_broken_access_lab_2, name="broken_access_lab_2"),
    path("broken_access_lab_3", views.a1_broken_access_lab_3, name="broken_access_lab_3"),
    path("broken_access_controle/secret", views.a1_broken_access_lab3_secret, name="broken_access_controle_secret"),
    path("ssrf",views.ssrf,name="SSRF"),
    path("ssrf_discussion", views.ssrf_discussion, name="SSRF Discussion"),
    path("ssrf_lab",views.ssrf_lab,name="SSRF LAB"),
    path("ssrf_lab2",views.ssrf_lab2,name="SSRF LAB"),
    path("ssrf_target",views.ssrf_target,name="SSRF LAB"),
    path("injection",views.injection,name="injection"),
    path("injection_sql_lab",views.injection_sql_lab,name="injection"),
    path("api/ssrf",apis.ssrf_code_checker,name="api/ssrf"),
    path("ssti", views.ssti, name="SSTI"),
    path("ssti/lab", views.ssti_lab, name="SSTI Lab"),
    path("ssti/blog/<str:blog_id>", views.ssti_view_blog, name="SSTI Blog"),
    path("cryptographic_failure",views.crypto_failure,name="cryptographic_failure"),
    path("cryptographic_failure/lab",views.crypto_failure_lab,name="cryptographic_failure_lab"),
    path("cryptographic_failure/lab2",views.crypto_failure_lab2,name="cryptographic_failure_lab2"),
    path("cryptographic_failure/lab3",views.crypto_failure_lab3,name="cryptographic_failure_lab3"),
    path("auth_failure",views.auth_failure,name="auth_failure"),
    path("auth_failure/lab2/admin12983gfugef81e8yeryepanel",views.auth_failure_lab2,name="auth_failure_lab2"),
    path("auth_failure/lab3",views.auth_failure_lab3,name="auth_failure_lab2"),
    path("2021/A8",views.software_and_data_integrity_failure,name="A8"),
    path("2021/A8/lab2",views.software_and_data_integrity_failure_lab2,name="A8"),
    path("2021/A8/lab3",views.software_and_data_integrity_failure_lab3,name="A8"),
    path("2021/discussion/A9",views.A9_discussion,name="A9 discussion"),
    path("2021/discussion/A9/api",apis.log_function_checker,name="A10 discussion"),
    path("2021/discussion/A9/target",log_function_target,name="A9 discussion"),
    path("2021/discussion/A7",views.A7_discussion,name="A7 discussion"),
    path("2021/discussion/A7/api",apis.A7_disscussion_api,name="A7 discussion api"),
]
