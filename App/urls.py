from django.urls import path
from . import views
urlpatterns = [
path('',views.home),
path('logouts',views.logouts),    
path('user_reg',views.user_reg),
path('log',views.user_log),
path('user_home',views.user_home),
path('user_profile',views.user_profile),
path('user_update',views.user_update),
path('user_draftss',views.user_draft),
path('user_book',views.user_book),
path('user_book_viwess',views.user_book_viwess),
path('user_book_edit<str:pk>',views.user_book_edit,name='ubupa'),
path('user_book_delete<str:pk>',views.user_book_delete,name='ubdel'),
path('user_assigment',views.user_assigment),
path('user_assigment_views',views.user_assigment_views),
path('user_assigment_edit<str:pk>',views.user_assigment_edit,name='uaupa'),
path('user_assigment_delete<str:pk>',views.user_assigment_delete,name='uadel'),
path('note_submit<str:pk>',views.note_submit,name='updraft'),
path('delete<str:pk>',views.dele,name='del',),
path('purshase',views.purshase),
path('purchase_note<str:pk>',views.purchase_note,name='purchasee_note'),
path('purchase_book<str:pk>',views.purchase_book,name='purchase_book'),
path('purchase_assigment<str:pk>',views.purchase_assigment,name='purchase_assigment'),
path('search',views.search),
path('buy',views.buy),
path('waiting_for_confirmation',views.waiting_for_confirmation),
path('single_note_view',views.single_note_view),
path('single_book_view',views.single_book_view),
path('single_assignment_view',views.single_assignment_view),
# path('buy_purchase',views.buy_purchase),
path('scucess',views.scucess),
path('download',views.download),
path('profile_single_view<str:pk>',views.profile_single_view,name='psw'),
path('download_assignment',views.download_assignment),
path('view_payment',views.view_payment),
path('Note_Send_Request',views.Note_Send_Request),
path('Recive_send_request',views.Recive_send_request),
path('Accept<str:pk>',views.Accept,name='Accept'),
path('Rejectss<str:pk>',views.Rejectss,name='Rejectss'),
path('pay_accepts<str:pk>',views.pay_accepts,name='pay_acceptss'),
path('pay_Rejects<str:pk>',views.pay_Rejects,name='pay_Rejectss'),
path('Buy_Book<str:pk>',views.Buy_Book,name='Buy_Book'),
path('Buy_Note<str:pk>',views.Buy_Note,name='Buy_Note'),
path('Buy_Assigments<str:pk>',views.Buy_Assigments,name='Buy_Assigmentsss'),
path('user_notes',views.user_notes,name='user_notes'),
path('enlarge<str:pk>',views.enlarge,name='enlarge'),
path('user_note_dele<str:pk>',views.user_note_dele,name='user_note_dele'),
path('note_up<str:pk>',views.note_update,name='note_up'),









]