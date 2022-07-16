from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about_us/", views.about_us, name="AboutUs"),
    path("contact_us/", views.contact_us, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("product_view/<int:my_id>", views.product_view, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
]
