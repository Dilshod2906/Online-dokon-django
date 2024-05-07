from django.urls import path
from .views import IndexView, ProductView, Product_detail, savatga_qushish, savat_list, deletel, QidirishView,category, savol_javob, heartht,javob_list, deletel2

urlpatterns = [
    path('', IndexView, name='index'),
    path('products/', ProductView, name='product'),
    path('products_detail/<int:id>', Product_detail, name='Product_detail'),
    path('qoshish/<int:product_id>', savatga_qushish, name='savatga_qushish'),
    path('saqlan/<int:product_idd>', heartht, name='saqlan'),
    path('saralangan/', javob_list, name='s_list'),
    path('savat_list/', savat_list, name='savatl'),
    path('savol_javob/', savol_javob, name='savol_javob'),
    # path('change_password/', change_password, name='change_password'),
    path('deletel/<int:idd>', deletel, name='deletel'),
    path('deletel2/<int:idd>', deletel2, name='deletel2'),
    path('kateg/<int:id>', category, name='kateg'),
    path('search/', QidirishView.as_view(), name='search'),

    



]