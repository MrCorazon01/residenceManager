from django.shortcuts import render, redirect
from .models import *
from .form import StudentForm, UserForm, PaymentForm
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q


# Create your views here.

def index_view(request):
    
    return render(request, "index.html")

def view_login(request):
    return render(request, "login.html")


def process_login(request):
    print(request.POST["student_number"])
    if request.method == 'POST':
        student_number = request.POST['student_number']
        try:
            data_user = StudentModel.objects.get(student_number=student_number)
        except StudentModel.DoesNotExist:
            return render(request, 'login.html', {'error': 'Numéro utilisateur ou mot de passe incorrect.'})
        password = request.POST['password']
        user = authenticate(request, username=data_user.user.username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html', {'error': 'Numéro utilisateur ou mot de passe incorrect.'})

def view_logout(request):
    logout(request)
    return redirect('login')


def view_register(request):
    form1 = StudentForm()
    form2 = UserForm()
    return render(request, "register.html", {"form1": form1, "form2": form2})

def view_add_user(request):
    if request.method == "POST":
        form1 = StudentForm(request.POST)
        form2 = UserForm(request.POST)
    
        if form2.is_valid():
            message = "Utilisateur Ajouté avec succès"
            data1 = {
                'student_number': form1['student_number'].value(),
                'telephone': form1['telephone'].value(),
                'department': form1['department'].value(),
            }
            print(data1)
            # Générer un nom d'utilisateur unique
            existing_users = User.objects.count()
            username = f'user_{existing_users + 1}'
            
            data2 = form2.cleaned_data
            try:
                if data2["password"] != data2["password2"]:
                    error = "Les deux mots de passes doivent être les mêmes"
                    return render(request, "register.html", {"form1": form1, "form2": form2, "error": error})
                elif len(data2["password"]) < 8:
                    error = "Le mot de passe doit contenir au minimum 8 caractères"
                    return render(request, "register.html", {"form1": form1, "form2": form2, "error": error})
                
                elif data1["department"] == "":
                    error = "Veuillez remplire le champs département"
                    return render(request, "register.html", {"form1": form1, "form2": form2, "error": error})

                user = User.objects.create( username=username,
                                        first_name=data2["first_name"], 
                                        last_name=data2["last_name"],
                                        email=data2["email"],
                                        )
                user.set_password(data2["password"])
                user.save()
                print("password------------------", data2["password"])
                print("user------------------", user)
                student = StudentModel.objects.create(user=user, student_number=data1["student_number"], telephone=data1["telephone"], department=data1["department"])
                student.save()
                return render(request, "register.html", {"form1": form1, "form2": form2, "message": message})
            except IntegrityError:
                error = "Cet numéro d'étudiant existe déjà!"
                return render(request, "register.html", {"form1": form1, "form2": form2, "error": error})
        

        else:
            print(form1.data, form2.data)
            error = "Il y'a eu une erreur lors du remplissage"
            return render(request, "register.html", {"form1": form1, "form2": form2, "error": error})
    else:
        form1 = StudentForm(request.POST)
        form2 = UserForm(request.POST)
        error = "La methode utilisée n'est pas POST"
        return render(request, "register.html", {"form1": form1, "form2": form2, "error": error})

@login_required
def view_room(request):
    return render(request, "room.html")

@login_required
def view_room_h1(request):
    rooms = RoomModel.objects.all()
    data = [room for room in rooms if "H1" in room.room_number]

    return render(request, "rooms/rooms.html", {"rooms": data})

@login_required
def view_room_h2(request):
    rooms = RoomModel.objects.all()
    data = [room for room in rooms if "H2" in room.room_number]

    return render(request, "rooms/rooms.html", {"rooms": data})

@login_required
def view_room_h3(request):
    rooms = RoomModel.objects.all()
    data = [room for room in rooms if "H3" in room.room_number]

    return render(request, "rooms/rooms.html", {"rooms": data})

@login_required
def view_room_h4(request):
    rooms = RoomModel.objects.all()
    data = [room for room in rooms if "H4" in room.room_number]

    return render(request, "rooms/rooms.html", {"rooms": data})

@login_required
def view_room_h5(request):
    rooms = RoomModel.objects.all()
    data = [room for room in rooms if "H5" in room.room_number]

    return render(request, "rooms/rooms.html", {"rooms": data})

@login_required
def view_dashboard(request):
    user = request.user
    print(user)
    if user.is_authenticated:
        try:
            student = StudentModel.objects.get(user=user)
        except StudentModel.DoesNotExist:
            student = None
        return render(request, 'dashboard.html', {'student': student})
    else:
        return redirect('login')

    return render(request, "dashboard.html")

@login_required
def view_complaint(request):
    return render(request, "complaint.html")

@login_required
def process_complaint(request):
    if request.method == "POST":
        subject = request.POST["subject"]
        description = request.POST["description"]
        if subject == "" or description == "":
            return render(request, "complaint.html", {"error": "Veulliez remplite tout les champs svp !"})
        user = request.user
        student = StudentModel.objects.get(user=user)
        complaint = ComplaintModel.objects.create(subject=subject, description=description, student=student)
        complaint.save()
        return render(request, "complaint.html", {"message": "Votre plainte à été enregistrer avec success"})


@login_required
def complaints_history(request):
    user = request.user
    student = StudentModel.objects.get(user=user)
    complaints = ComplaintModel.objects.filter(student=student)

    return render(request, "complaints/complaints.html", {"complaints": complaints})

@login_required
def complaint_contain(request):
    complaint_id = request.POST['complaint_id']
    print("-------------", complaint_id)
    complaint = ComplaintModel.objects.get(complaint_id=complaint_id)

    return render(request,'complaints/contain.html', {'complaint': complaint})


@login_required
def view_paiement(request):
    user = request.user
    student = StudentModel.objects.get(user=user)
    payment_status = []
    payments = PaymentModel.objects.filter(student=student)
    current_year = datetime.now().year

     # Liste des choix de mois
    MONTH_CHOICES = [
        ('1', 'Janvier'), ('2', 'Février'), ('3', 'Mars'),
        ('4', 'Avril'), ('5', 'Mai'), ('6', 'Juin'),
        ('7', 'Julliet'), ('8', 'Août'), ('9', 'Septembre'),
        ('10', 'Octobre'), ('11', 'Novembre'), ('12', 'Décembre')
    ]

    # Vérifier pour chaque mois s'il a été payé ou non
    for month_value, month_label in MONTH_CHOICES:
        status = student.get_payment_status(month_value)
        amount = next((payment.amount for payment in payments if payment.mounth == month_value), 0)
        payment_status.append((month_label, status, amount))
   
    return render(request, "paiement.html", {"payment": payments, "student":student, "payment_status": payment_status, "current_year":current_year})


@login_required
def reservation(request):
    if request.method == 'POST':
        student = StudentModel.objects.get(user=request.user)
        room_number = request.POST['room_number']
        room = RoomModel.objects.get(room_number=room_number)
        if student.reservation:
            error_message = "Désolé, vous avez dèja réserver la chambre " + student.reservation.room.room_number
            return render(request, 'room.html', {'error_message': error_message})


        if room.remaining_space > 0:
            # Créer une nouvelle instance de réservation
            reservation = ReservationModel(room=room)
            reservation.save()
            # Mis à jour le nombre de places restantes de la chambre
            room.remaining_space -= 1
            room.save()
            # Asscocitation de la réservation à l'étudiant connecté
            print(request.user)
            
            student.reservation = reservation
            student.save()

            message = "Félicitation, Vous avez réserver la chambre " + student.reservation.room.room_number
            return render(request, 'room.html', {'message': message})
        else:
            error_message = "Désolé, la chambre" + room.room_number + " est pleine"
            return render(request, 'room.html', {'error_message': error_message})
    else:
            return redirect('index')

@login_required
def delete_reservation(request):
    student = StudentModel.objects.get(user=request.user)
    if student.reservation_id:
        reservation = ReservationModel.objects.get(reservation_id=student.reservation.reservation_id)
        # Supprimer la réservation
        reservation.delete_reservation()
        # Rediriger l'utilisateur vers une page de confirmation ou une autre vue appropriée
        message = "Vous avez supprimer votre reservation avec success"
        student = StudentModel.objects.get(user=request.user)
        return render(request, 'dashboard.html', {"message": message, "student": student})
    else: 
        error = "Vous avez pas de reservation en cours"
        return render(request,'dashboard.html',{'error':error})

@login_required   
def search_room(request):
    room_number = request.GET.get("room_number").upper()
    room_list = []

    rooms = RoomModel.objects.all()
    if room_number:
        for room in rooms:
            if room_number in room.room_number:
                room_list.append(room)
        return render(request, "search_room.html", {"rooms": room_list})
    return render(request, "search_room.html", {"error": "Aucune chambre trouvée"})

@staff_member_required
def view_students(request):
    students = StudentModel.objects.all()
    return render(request, 'students.html', {"students": students})

@staff_member_required
def view_info_student(request):
    student_number = request.POST["student_number"]
    student = StudentModel.objects.get(student_number=student_number)
    return render(request, "info_student.html", {"student": student})

@staff_member_required
def view_payment_student(request):
    student_number = request.POST["student_number"]
    print("--------------------", student_number)
    student = StudentModel.objects.get(student_number=student_number)

    payment_status = []
    payments = PaymentModel.objects.filter(student=student)
    current_year = datetime.now().year

     # Liste des choix de mois
    MONTH_CHOICES = [
        ('1', 'Janvier'), ('2', 'Février'), ('3', 'Mars'),
        ('4', 'Avril'), ('5', 'Mai'), ('6', 'Juin'),
        ('7', 'Julliet'), ('8', 'Août'), ('9', 'Septembre'),
        ('10', 'Octobre'), ('11', 'Novembre'), ('12', 'Décembre')
    ]

    # Vérifier pour chaque mois s'il a été payé ou non
    for month_value, month_label in MONTH_CHOICES:
        status = student.get_payment_status(month_value)
        amount = next((payment.amount for payment in payments if payment.mounth == month_value), 0)
        payment_status.append((month_label, status, amount))

    return render(request, "paiement_student.html", {"payment": payments, "student":student, "payment_status": payment_status, "current_year":current_year})

@staff_member_required
def view_add_payment(request):
    form = PaymentForm()
    student_number = request.POST["student_number"]
    student = StudentModel.objects.get(student_number=student_number)

    return render(request, 'add_payment.html', {"form": form, "student": student})

@staff_member_required
def payment_register(request):
    if request.method == "POST":
        student_number = request.POST["student_number"]
        student = StudentModel.objects.get(student_number=student_number)
        form = PaymentForm(request.POST)
        amount = form['amount'].value()
        mounth = form['mounth'].value()
        payment_status = form['payment_statut'].value()

        payment = PaymentModel.objects.create(student=student, amount=amount, mounth=mounth, payment_statut=payment_status)
        payment.save()
        return render(request, 'add_payment.html', {"form": form, "student": student, "message": "Le paiement a été bien enregistrer"})

@staff_member_required
def search_student(request):
    search_query = request.GET.get('search_query', '')

    # Filtrer les étudiants en fonction de la recherche insensible à la casse
    students = StudentModel.objects.filter(
        Q(student_number__icontains=search_query) | 
        Q(user__first_name__icontains=search_query) |
        Q(user__last_name__icontains=search_query)
    )

    context = {
        'students': students
    }
    return render(request, "search_student.html", context)