from django.db import models

class StudentData(models.Model):
    Student_id = models.CharField(primary_key=True, max_length=100)
    student_email_address = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.Student_id}"


class UniversityDetail(models.Model):
    student_id = models.ForeignKey(StudentData, on_delete=models.CASCADE)
    university_data = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return f"{self.Student_id}"

class StudenDetail(models.Model):
    student_id = models.ForeignKey(StudentData, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    gender = models.BooleanField(choices=[('Male', 'Male'), ('Female','Female')])
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    country_of_birth = models.CharField(max_length=100)
    city_of_birth = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postalcode = models.CharField(max_length=100)
    mailing_address_line_1 = models.CharField(max_length=100)
    mailing_address_line_2 = models.CharField(max_length=100)
    mailing_address_city = models.CharField(max_length=100)
    mailing_address_state = models.CharField(max_length=100)
    mailing_address_postal_code = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.Student_id}"


class EducationDetail(models.Model):
    student_id = models.ForeignKey(StudentData, on_delete=models.CASCADE)
    ielts = models.CharField(max_length=1000)
    toefl = models.CharField(max_length=1000)
    duolingo = models.CharField(max_length=1000)
    pte = models.CharField(max_length=1000)
    others = models.CharField(max_length=1000)
    level_of_education = models.CharField(max_length=1000)
    institute_name = models.CharField(max_length=1000)
    country_of_education = models.CharField(max_length=1000)
    course_studied = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    post_level_of_educaion = models.CharField(max_length=1000)
    post_institute_name = models.CharField(max_length=1000)
    post_country_of_education = models.CharField(max_length=1000)
    post_course_studied = models.CharField(max_length=1000)
    post_start_date = models.DateField()
    post_end_date = models.DateField()
    academic_miscoduct =  models.BooleanField(choices=[('Yes', 'Yes'), ('No','No')])
    behaviour_misconduct =  models.BooleanField(choices=[('Yes', 'Yes'), ('No','No')])
    crimal_preceeding=  models.BooleanField(choices=[('Yes', 'Yes'), ('No','No')])