from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudenDetail, StudentData, UniversityDetail, EducationDetail
from datetime import datetime


class Apply(APIView):
    def post(self, request):
        try:
            student = request.data['passport']
            student_email_address = request.data['student_email_address']
            StudentData.objects.create(Student_id=student, student_email_address=student_email_address)
            return Response({'Status': 'Success', "Message": "Student Id created Successfully", "Student Id": student},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Status': 'Failed', "Error": "Some Internal Error Occured" + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request):
        pass



class PersonalInformation(APIView):
    def post(self, request):
        try:
            data = StudenDetail.objects.get(Student_id = request.data['student_id'])
            if not data:
                data.student_id = request.data['student_id']
                data.firstname = request.data['firstname']
                data.lastname = request.data['lastname']
                data.email = request.data['email']
                data.contact = request.data['contact']
                data.gender = request.data['gender']
                data.date_of_birth = convert_date_time(request.date['date_of_birth'])
                data.nationality = request.data['nationality']
                data.country_of_birth = request.data['country_of_birth']
                data.city_of_birth = request.data['city_of_birth']
                data.address_line_1 = request.data['address_line_1']
                data.address_line_2 = request.data['address_line_2']
                data.city = request.data['city']
                data.state = request.data['state']
                data.postalcode = request.data['postalcode']
                data.mailing_address_line_1 = request.data['mailing_address_line_1']
                data.mailing_address_line_2 = request.data['mailing_address_line_2']
                data.mailing_address_city = request.data['mailing_address_city']
                data.mailing_address_state = request.data['mailing_address_state']
                data.mailing_address_postal_code = request.data['mailing_address_postal_code']
                
                data.save()
                return Response({'Status': 'Success', "Message": "Personal Information has been save successfully"},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Status': 'Failed', "Error": "Some Internal Error Occured" + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UniversityInformation(APIView):
    def post(self, request):
        try:
            data = UniversityDetail.objects.get(Student_id = request.data['student_id'])
            if not data:
                data.student_id = request.data['student_id']
                data.university_data = request.data['university_data']
                data.save()
                return Response({'Status': 'Success', "Message": "University Information has been save successfully"},
                            status=status.HTTP_200_OK)
        except:
            return Response({'Status': 'Failed', "Error": "Some Internal Error Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
class EducationInformation(APIView):
    def post(self, request):
        try:
            data = EducationDetail.objects.get(Student_id = request.data['student_id'])
            if not data:
                data.student_id = request.data['student_id']
                data.ielts = request.data['ielts']
                data.toefl = request.data['toefl']
                data.duolingo = request.data['duolingo']
                data.pte = request.data['pte']
                data.others = request.data['others']
                data.level_of_education = request.data['level_of_education']
                data.institute_name = request.data['institute_name']
                data.country_of_education = request.data['country_of_education']
                data.course_studied = request.data['course_studied']
                data.start_date = convert_date_time(request.data['start_date'])
                data.end_date = convert_date_time(request.data['end_date'])
                data.post_level_of_educaion = request.data['post_level_of_educaion']
                data.post_institute_name = request.data['post_institute_name']
                data.post_country_of_education = request.data['post_country_of_education']
                data.post_course_studied = request.data['post_course_studied']
                data.post_start_date =convert_date_time(request.data['post_start_date'])
                data.post_end_date = convert_date_time(request.data['post_end_date'])
                data.academic_miscoduct = request.academic_miscoduct['ielts']
                data.crimal_preceeding = request.data['criminal_preceeding']
                data.save()
                return Response({'Status': 'Success', "Message": "Education Information has been save successfully"},
                            status=status.HTTP_200_OK)
        except:
            return Response({'Status': 'Failed', "Error": "Some Internal Error Occured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
class UploadDocumnts(APIView):
    def post(self, request):
        pass

def convert_date_time(time):
 
    format_data = "%d-%m-%y"
 
    date = datetime.strptime(time, format_data)

    return date
 

