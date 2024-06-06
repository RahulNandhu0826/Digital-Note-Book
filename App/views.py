from django.shortcuts import render,redirect
from  . models import *
from django.urls import reverse
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout


# Create your views here.
def logouts(request):
    logout(request)
    return redirect(user_log)
def home(request):
    return render(request,'home.html')


def user_home(request):  
    
    usersi=reg.objects.get(usersname=request.user)
#    views=pic.objects.get(account=usersi.Account) 
    view=pic.objects.filter(account="Public")
    looka={
               'key':usersi,
               'keyy':view,
        }   
          
    return render(request,'user_home.html',looka)
    
   
def user_log(request):
    if request.method=='POST':
        usr=request.POST['UN']
        pwd=request.POST['PW']
        if reg.objects.filter(usersname=usr).exists():
            use=auth.authenticate(username=usr,password=pwd)
            if use is not None:
             auth.login(request,use)
             print('sucess login')
             return redirect(user_home)
            else:
             print('invalid')
             return render(request,'user_log.html',{'key':'INVALID USERNAME AND PASSWORD'})
        else:
             print('Not found')
             return render(request,'user_log.html',{'key':'USERNAME NOT FOUND'})
    return render(request,'user_log.html')



   

def user_reg(request):
    if request.method=='POST':
        F_name=request.POST['f_name']
        S_name=request.POST['s_name']
        Dob=request.POST['dob']
        Gende=request.POST['gender']
        Emaill=request.POST['mail']
        U_name=request.POST['u_name']
        Acc_type=request.POST['acc_type']
        Pas=request.POST['passe']
        Cpas=request.POST['con_pass']
        if Pas==Cpas:
            user=None
            if User.objects.filter(username=U_name).exists():
                user=User.objects.get(username=U_name)
                if reg.objects.filter(user_register=user).exists():
                    print("username alerady exists ")
                    return render(request,'user_Reg.html',{'key':'username already exists'}) 
            else:
                User.objects.create_user(username=U_name,email=Emaill,password=Pas,first_name=F_name,last_name=S_name).save()
                user=User.objects.get(username=U_name)  
            if user:
                if reg.objects.filter(usersname=U_name).exists():
                    print("user alerady exists ")
                    return render(request,'user_Reg.html',{'key':'user already exists'})
                else:               
                    reg(user_register=user,DOB=Dob,Gender=Gende,usersname=U_name,Account=Acc_type).save()
                    print('REGISTERED SUCCESSFULLY')
                    return redirect(user_log)
        else:
            print('password does not match')
            return render(request,'user_Reg.html',{'key':'password does not match'})
    return render(request,'user_Reg.html')

def user_profile(request):
    print(request.user)
    user_viewss=reg.objects.get(usersname=request.user)
    disc={'key':user_viewss
          }
    context={
        'key':user_viewss,
        'key1':'successfully upload draft '
    }
    contextss={
        'key':user_viewss,
        'key1':'Saved'
    }
    if'Draft'in request.POST:
        subss=request.POST['sub']
        pics=request.FILES['pic']
        notes=request.POST['text2']
        note_rates=request.POST['note_rate']
        # note_thingsss=request.POST['note_things']
        pic(note_books=user_viewss,subs=subss,pic=pics,bookss=notes,rate=note_rates).save()      
       
        return render (request,'user_profile.html',context)
    if 'Save' in request.POST:
        userss=reg.objects.get(usersname=request.user)
        subss=request.POST['sub']
        pics=request.FILES['pic']
        notes=request.POST['text2']
        note_rates=request.POST['note_rate']
        note_account=request.POST['Acc']
        note_thingsss=request.POST['note_things']
        pic(note_books=userss,subs=subss,pic=pics,bookss=notes,rate=note_rates,note_thingss=note_thingsss,account=note_account).save()      
        return render (request,'user_profile.html',contextss)
    return render(request,'user_profile.html',disc)

def user_update(request):
    userss=reg.objects.get(usersname=request.user)
    print(userss.usersname)
    dra=reg.objects.get(user_register=userss.id) 
    if request.method=='POST':
        tabb=User.objects.get(username=request.user)    
        tabb.first_name=request.POST['f_names']
        tabb.last_name=request.POST['s_names']
        tabb.email=request.POST['mails']
        dra.DOB=request.POST['dobs']
        dra.Account_num=request.POST['accnum']
        dra.Account=request.POST['acc_types']
        tabb.save()   
        dra.save()    
        return redirect(user_profile)       
    return render(request,'user_update.html',{'key':userss})



def user_draft(request):
    usersi=reg.objects.get(usersname=request.user)
    view=pic.objects.filter(note_books=usersi,account=None)

    return render(request,'user_draft.html',{'keys':view})

def note_submit(request,pk):
    di=reg.objects.get(usersname=request.user)
    print(di.usersname)
    dra=pic.objects.get(note_books=di.id,id=pk) 
    if request.method=='POST':
              
        ra=pic.objects.get(id=pk)        
        ra.bookss=request.POST['content']
        ra.account=request.POST['Acc']
        ra.note_thingss="Note"
        ra.save()
        return redirect(user_draft)  
    return render(request,'note_submit.html',{'key':dra})


 



def dele (request,pk): 
    userss=reg.objects.get(usersname=request.user)
    print(userss.usersname)
    taabb=pic.objects.filter(note_books=userss,id=pk) 
    taabb.delete()  
    return redirect(user_draft)




def user_assigment(request):
    usersi=reg.objects.get(usersname=request.user)
    view=assignmentss.objects.filter(assignment=usersi)
   
    dra=reg.objects.get(user_register=request.user)
    print(dra.usersname)
    if request.method=='POST':
        accoun=request.POST['acc']
        subss=request.POST['sub']
        pics=request.FILES['pic']
        assing_rates=request.POST['assing_rate']
        assing_rates=request.POST['assing_rate']
        assing_thingsss=request.POST['assing_things']
        assignmentss(assignment=dra,subs=subss,pic=pics,account=accoun,rate=assing_rates,assign_thingss=assing_thingsss).save()  
        subcontxt={
        'key':'Assigment submitted',    
        'key1':view ,
        'key2':dra,
    }     
        return render (request,'user_assigment.html',subcontxt)
    contxt={
        'key1':view ,
        'key2':dra,
    }
    return render(request,'user_assigment.html',contxt)

def user_assigment_views(request):
    usersi=reg.objects.get(usersname=request.user)
    view=assignmentss.objects.filter(assignment=usersi)
 
    return render(request,'user_assigment_views.html',{'key':view})

def user_assigment_edit(request,pk):
    di=reg.objects.get(usersname=request.user)
    print(di.usersname)
    dra=assignmentss.objects.get(assignment=di.id,id=pk) 
    if request.method=='POST':
              
        ra=assignmentss.objects.get(id=pk)        
        ra.subs=request.POST['sub1']
        ra.pic=request.FILES['pic1']
        ra.rate=request.FILES['rate1']
        ra.save()
        return redirect(user_assigment_views)  
    return render(request,'user_assigment_edit.html',{'key':dra})
def user_assigment_delete(request,pk):
    userss=reg.objects.get(usersname=request.user)
    print(userss.usersname)
    taabb=assignmentss.objects.filter(assignment=userss,id=pk) 
    taabb.delete()  
    return redirect(user_assigment_views)


def user_book(request):
    usersi=reg.objects.get(usersname=request.user)
    view=Books.objects.filter(brooks=usersi)
   
    dra=reg.objects.get(user_register=request.user)
    print(dra.usersname)
    if request.method=='POST':
        accoun=request.POST['acc']
        subss=request.POST['sub']
        pics=request.FILES['pic']
        notes=request.POST['text2']
        book_rates=request.POST['book_rate']
        book_things=request.POST['books_thingss']
        Books(brooks=dra,subs=subss,pic=pics,bookss=notes,account=accoun,rate=book_rates,book_thingss=book_things).save() 
        subcontxt={
        'key':'Assigment submitted',    
        'key1':view ,
        'key2':dra,
    }              
        return render (request,'user_book.html',subcontxt)
    contxt={
        'key1':view ,
        'key2':dra,
    }
    return render(request,'user_book.html',contxt)
def user_book_viwess(request):
    usersi=reg.objects.get(usersname=request.user)
    view=Books.objects.filter(brooks=usersi)
    return render(request,'user_book_viwess.html',{'key':view})
def user_book_edit(request,pk):
    di=reg.objects.get(usersname=request.user)
    print(di.usersname)
    dra=Books.objects.get(brooks=di.id,id=pk) 
    if request.method=='POST':
              
        ra=Books.objects.get(id=pk)        
        ra.subs=request.POST['sub1']
        ra.pic=request.FILES['pic1']
        ra.bookss=request.POST['text21']
        ra.rate=request.POST['rate2']
        ra.save()
        return redirect(user_book_viwess)  
    return render(request,'user_book_edit.html',{'key':dra})
def user_book_delete (request,pk): 
    userss=reg.objects.get(usersname=request.user)
    print(userss.usersname)
    taabb=Books.objects.filter(brooks=userss,id=pk) 
    taabb.delete()  
    return redirect(user_book_viwess)
def purshase(request):
    tab=pic.objects.filter(note_thingss='Note')
    tabb=Books.objects.all()
    tabbb=assignmentss.objects.all()
    di={'key':tab,
        'key1':tabb,
        'key2':tabbb,}
    return render (request,'purshase.html',di)
def search(request):
    if request.method=='POST':
        sreach=request.POST['arch']
        picc=pic.objects.filter(subs=sreach)
        Booksss=Books.objects.filter(subs=sreach)
        assign=assignmentss.objects.filter(subs=sreach)
        arch={'key':picc,
              'key1':Booksss,
              'key2':assign}
        return render (request,'purshase.html',arch)
def Note_Send_Request(request):
    dra=reg.objects.get(user_register=request.user)
    print(dra.usersname)
    if request.method=='POST':
        names=request.POST['name']
        sends=request.POST['send']
        unmae=request.POST['username']
        accepts(accepted=dra,name=names,urnmae=unmae).save() 
        dr=reg.objects.get(user_register=request.user)
        dr.Accept=request.POST['send']
        dr.save()
        return redirect(purshase)
        
        
        
                  

    return render(request,'Note_Send_Request.html' )    

def purchase_note(request,pk):
    di=reg.objects.get(usersname=request.user)
    print(di.usersname)
    dra=pic.objects.get(id=pk)
    # accept=accepts.objects.get(id=pk)
    print(dra.note_books.usersname)
    print(dra.account)
    print(di.Accept)
    if dra.note_books.Account=="Private": 
        if di.Accept=="Waiting for accept":
            print('helloss')
            note=pic.objects.get(id=pk) 
            show={
                'key':note,
                'keyy':di,
            }
            return render(request,'accept.html',show)
        elif di.Accept=="Accept":           
            note=pic.objects.get(id=pk)
            if note.rate==0:
                print(note.account)
                print('hai')
                context={
                        'key5':di,
                        'key4':note
                }
                return render(request,'download.html',context)
            elif note.rate>=0 :
                note=pic.objects.get(id=pk)
                print(note.account)
                print('h0i')
                context={
                        'key5':di,
                        'key4':note
                    }
            
            return render(request,'single_note_view.html',context)    
        else:
            return render(request,'purshase.html',{'key3':"Accpect"})        
    # Public     
    else:
        regg=reg.objects.get(usersname=request.user)
        assin=pic.objects.get(id=pk)
        print(assin.pk)
        print(regg.user_register.first_name)
                 
        note=pic.objects.get(id=pk)
        print(note.rate) 
        if note.rate==0  :
            print(note.account)
            print('hai')
            context={
                'key5':di,
                'key4':note
           }
            return render(request,'download.html',context)
       
        elif note.rate>=0 : 
            note=pic.objects.get(id=pk)         
            print(note.account)
            print('h0i')
            context={
                       'key5':di,
                       'key4':note
                    }
            return render(request,'single_note_view.html ',context)             
        
        return render(request,' download.html',context)        
        



def Rejectss (request,pk): 
    
    taabb=accepts.objects.filter(id=pk) 
    taabb.delete()  
    return redirect(Recive_send_request)
def Accept(request,pk):
    di=reg.objects.get(usersname=request.user)
    print(di.usersname)         
    accept=accepts.objects.get(id=pk)         
    accept.Accept='Accept' 
    accept.accepted.Accept='Accept'  
    print(accept.accepted.Accept)      
    accept.save()
    regg=reg.objects.get(usersname=accept.urnmae)
    regg.Accept='Accept'
    regg.save()
  
    return redirect(Recive_send_request) 

def Recive_send_request(request):
    usersi=reg.objects.get(usersname=request.user)
    view=accepts.objects.filter(name=usersi.usersname,Accept=None)
    # tab=accepts.objects.all()
    return render(request,'Recive_send_request.html',{'keyy':view})

def purchase_book(request,pk):
    di=reg.objects.get(usersname=request.user)
    print(di.usersname)
    dra=Books.objects.get(id=pk)    
    print(dra.brooks.usersname)
    print(dra.account)


    if dra.brooks.Account=="Private":              
        if di.Accept=="Waiting for accept":
            print('helloss')
            note=Books.objects.get(id=pk) 
            show={
                'key':note,
                'keyy':di,
            }
            return render(request,'accept.html',show)
        elif di.Accept=="Accept":
            note=Books.objects.get(id=pk)
            if note.rate==0:
                print(note.account)
                print('hai')
                context={
                        'key5':di,
                        'key4':note
           }
                return render(request,'download.html',context)
            elif note.rate>=0:
                note=Books.objects.get(id=pk)
                print(note.account)
                print('h0i')
                context={
                        'key5':di,
                        'key4':note
                    }
                return render(request,'single_book_view.html',context) 
                
            return render(request,'buy.html',context)    
        else:
            return render(request,'purshase.html',{'key3':"Accpect"})   


    # public     
    else: 
        regg=reg.objects.get(usersname=request.user)
        assin=Books.objects.get(id=pk)
        print(assin.pk)
        print(regg.user_register.first_name)
                
        note=Books.objects.get(id=pk)
        print(note.rate) 
        if note.rate==0  :
            print(note.account)
            print('hai')
            context={
                'key5':di,
                'key4':note
           }
            return render(request,'download.html',context)
       
        elif note.rate>=0 : 
            note=Books.objects.get(id=pk)         
            print(note.account)
            print('h0i')
            context={
                       'key5':di,
                       'key4':note
                    }
            return render(request,'single_book_view.html ',context)             
        
        return render(request,' download.html',context)       
       
 
    


def purchase_assigment(request,pk):
    di=reg.objects.get(usersname=request.user)
    print(di.usersname)
    dra=assignmentss.objects.get(id=pk)
    print(dra.assignment.usersname)
    print(dra.account)

   
    if dra.assignment.Account=="Private": 
        
        if di.Accept=="Waiting for accept":
            print('helloss')
            note=assignmentss.objects.get(id=pk) 
            show={
                'key':note,
                'keyy':di,
            }
            return render(request,'accept.html',show)
        elif di.Accept=="Accept":
            note=assignmentss.objects.get(id=pk)
            if note.rate==0:
                print(note.account)
                print('hai')
                context={
                        'key5':di,
                        'key4':note
           }
                return render(request,'download_assignment.html',context)
            elif note.rate>=0:
                note=assignmentss.objects.get(id=pk)
                print(note.account)
                print('h0i')
                context={
                        'key5':di,
                        'key4':note
                    }
                return render(request,'single_assignment_view.html',context) 
       
            return render(request,'single_assignment_view.html',context)    
        else:
            return render(request,'purshase.html',{'key3':"Accpect"})        
         
    else: 
        regg=reg.objects.get(usersname=request.user)
        assin=assignmentss.objects.get(id=pk)
        print(assin.pk)
        print(regg.user_register.first_name)
        # paysss=payments.objects.filter(urnmae=regg.user_register.first_name)           
        note=assignmentss.objects.get(id=pk)
        print(note.rate) 
        if note.rate==0:
            print(note.account)
            print('hai')
            context={
                'key5':di,
                'key4':note
           }
            return render(request,'download_assignment.html',context)
       
        elif note.rate>=0: 
            note=assignmentss.objects.get(id=pk)         
            print(note.account)
            print('h0i')
            context={
                       'key5':di,
                       'key4':note
                    }
            return render(request,'single_assignment_view.html ',context)             
        
        return render(request,' download_assignment.html',context)
        

def buy (request):  
    dra=reg.objects.get(user_register=request.user)
    if request.method=='POST':              
        ur_names=request.POST['namess']
        names=request.POST['urnamess']
        buy_rates=request.POST['buy_rate']
        comple=request.POST['compl']
        ssl_no=request.POST['ssll_noo'] 
        thingsss=request.POST['things']
        actrats=request.POST['actrat'] 
        urr_idd=request.POST['ur_id']      
             
        payments(payss=dra,urnmae=ur_names,uppname=names,rate=buy_rates,completes=comple,sl_id=ssl_no,thingss=thingsss,actrate=actrats,ur_id=urr_idd).save()
        return render(request,'scucess.html')
   
    
    return render(request,'buy.html') 
def scucess (request):
     return render(request,'scucess.html') 
def download(request):

    return render(request,'download.html')
def view_payment(request):
    di=reg.objects.get(usersname=request.user)
    print(di.id)
      
    tab=payments.objects.filter(ur_id=di.id,paid=None)
   
    return render(request,'view_payment.html',{'key':tab})

    
def download_assignment(request):
    return render(request,'download_assignment.html')    

  

def profile_single_view(request,pk):
    di=reg.objects.get(id=pk)
    print(di.usersname)
    assign=assignmentss.objects.filter (assignment=di.id)
    
    books=Books.objects.filter(brooks=di.id)
    notes=pic.objects.filter(note_books=di.id)
    context={
        'key':di,
        'key1':assign,
        'key2':books,
        'key3':notes
    }

    return render(request,'profile_single_view.html',context) 

def single_assignment_view(request):
   
    return render(request,'single_assignment_view.html')
def single_note_view(request):
   
    return render(request,'single_note_view.html')

def single_book_view (request):
     return render(request,'single_book_view.html')

def Buy_Assigments(request,pk):
    di=reg.objects.get(usersname=request.user)
    print(di.user_register.username)   
    if payments.objects.filter(payss=di.id,sl_id=pk).exists():
        pa=payments.objects.get(payss=di.id,sl_id=pk)
        if pa.completes=="completed":
            print("hai")
            if pa.paid=="IsPaid":
                print("h000")
                regg=reg.objects.get(usersname=request.user)
                note=assignmentss.objects.get(id=pk)         
                print(note.account)
                print('h0i')
                context={
                        'key5':regg,             
                        'key4':note
                    }
                return render(request,'download_assignment.html',context)
            return redirect(waiting_for_confirmation)        
    else:        
        regg=reg.objects.get(usersname=request.user)
        note=assignmentss.objects.get(id=pk)         
        print(note.account)
        print('h0i')
        context={
            'key5':regg,             
            'key4':note
            }
        return render(request,'buy.html',context) 

def Buy_Note(request,pk):
    di=reg.objects.get(usersname=request.user)
    print(di.user_register.username)   
    if payments.objects.filter(payss=di.id,sl_id=pk).exists():
        pa=payments.objects.get(payss=di.id,sl_id=pk)
        if pa.completes=="completed":
            print("hai")
            if pa.paid=="IsPaid":
                print("h000")
                regg=reg.objects.get(usersname=request.user)
                note=pic.objects.get(id=pk)         
                print(note.account)
                print('h0i')
                context={
                        'key5':regg,             
                        'key4':note
                    }
                return render(request,'download_assignment.html',context)
            return redirect(waiting_for_confirmation)        
    else:        
        regg=reg.objects.get(usersname=request.user)
        note=pic.objects.get(id=pk)         
        print(note.account)
        print('h0i')
        context={
            'key5':regg,             
            'key4':note
            }
        return render(request,'buy.html',context) 
              
def Buy_Book(request,pk):
    di=reg.objects.get(usersname=request.user)
    print(di.user_register.username)   
    if payments.objects.filter(payss=di.id,sl_id=pk).exists():
        pa=payments.objects.get(payss=di.id,sl_id=pk)
        if pa.completes=="completed":
            print("hai")
            if pa.paid=="IsPaid":
                print("h000")
                regg=reg.objects.get(usersname=request.user)
                note=Books.objects.get(id=pk)         
                print(note.account)
                print('h0i')
                context={
                        'key5':regg,             
                        'key4':note
                    }
                return render(request,'download_assignment.html',context)
            return redirect(waiting_for_confirmation)        
    else:        
        regg=reg.objects.get(usersname=request.user)
        note=Books.objects.get(id=pk)         
        print(note.account)
        print('h0i')
        context={
            'key5':regg,             
            'key4':note
            }
        return render(request,'buy.html',context) 
                     
    
def pay_accepts(request,pk):
    di=reg.objects.get(usersname=request.user)
    print(di.usersname) 
    payss=payments.objects.get(id=pk)
    payss.paid="IsPaid"
    payss.save()

    return redirect(view_payment)

def pay_Rejects (request,pk): 
    
    payys=payments.objects.filter(id=pk) 
    payys.delete()  
    return redirect(view_payment)
def waiting_for_confirmation(request):
    return render (request,'waiting_for_confirmation.html')

def user_notes(request):
    usersi=reg.objects.get(usersname=request.user)
    view=pic.objects.filter(note_books=usersi)
   
    return render(request,'user_notes.html',{'keys':view})
def note_update(request,pk):
    di=reg.objects.get(usersname=request.user)
    print(di.usersname)
    dra=pic.objects.get(note_books=di.id,id=pk) 
    if request.method=='POST':              
        ra=pic.objects.get(id=pk)        
        ra.bookss=request.POST['content']
        ra.subs=request.POST['sub']
        ra.pic=request.FILES['fil']
        ra.rate=request.POST['rat']        
        ra.account=request.POST['Acc']
        ra.save()
        return redirect(user_notes)  
    return render(request,'user_note_edit.html',{'key':dra})  
def user_note_dele (request,pk): 
    userss=reg.objects.get(usersname=request.user)
    print(userss.usersname)
    taabb=pic.objects.filter(note_books=userss,id=pk) 
    taabb.delete()  
    return redirect(user_notes)
def enlarge(request,pk):   
    dra=pic.objects.get(id=pk)
    return render(request,'enlarge.html',{'key':dra})

 
    

        

