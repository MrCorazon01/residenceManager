from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class RoomModel(models.Model):
    room_number = models.CharField(max_length=255, primary_key=True)
    capacite = models.IntegerField()
    remaining_space = models.IntegerField()

    def __str__(self):
        return self.room_number
    

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"


class ReservationModel(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    reservation_date = models.DateTimeField(auto_now=True)
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reservation_id} : {self.room} - {self.reservation_date}"
    
    def delete_reservation(self):
        # Mettre à jour le nombre de places restantes de la chambre
        self.room.remaining_space += 1
        self.room.save()
        # Supprimer la réservation
        self.delete()

    class Meta:
        verbose_name = "Rerservation"
        verbose_name_plural = "Rerservations"







class StudentModel(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=255, primary_key=True)
    telephone = models.CharField(max_length=255)
    reservation = models.ForeignKey(ReservationModel, on_delete=models.CASCADE, null=True)
    
    department = models.CharField(max_length=50, default="" , blank=True)
    #complaint = models.ForeignKey(ComplainteModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} : {self.student_number}"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural= "Students"

    def get_payment_status(self, month_value):
        try:
            payment = PaymentModel.objects.get(student=self, mounth=str(month_value))
            return payment.payment_statut
        except PaymentModel.DoesNotExist:
            return False


class PaymentModel(models.Model):
    MOUNTH_CHOICE = [
        ('1', 'Janvier'), ('2','Février'), ('3', 'Mars'),
        ('4','Avril'),('5',"Mai"),('6',"Juin") ,('7',"Julliet"),
        ('8',"Août"),('9', "Septembre"), ('10', "Octobre"), 
        ('11', "Novembre"), ('12', "Decembre")
    ]
    payment_id = models.AutoField(primary_key=True)
    amount = models.FloatField(default=3000)
    mounth = models.CharField(choices=MOUNTH_CHOICE, max_length=255)
    payment_statut = models.BooleanField()
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE, default="null")

    def __str__(self):
        return f'{self.payment_id} : {self.mounth} - {self.amount}'
    

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"


class ComplaintModel(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.complaint_id} : {self.subject}'
    

    class Meta:
        verbose_name = "Complaint"
        verbose_name_plural = "Complaints"