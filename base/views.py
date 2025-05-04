from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from django.contrib.auth.models import User
from .serializers import *

# Create your views here.

@api_view(["GET"])
def get_user_details(request):
    # if user is auth
        # get user details
    #else get generic

    user = User.objects.get(username = "jodoe")
    candidate = Candidate.objects.get(user = user)
    work_experience_list = WorkExperience.objects.filter(candidate = candidate).order_by("-date_start")
    
    
    candidateS = CandidateSerializer(candidate).data 
    
    work_expS = []
    for _ in work_experience_list:
        _keyRes = KeyResponsibilities.objects.filter(work_experience = _)
        keyRes = []
        for j in _keyRes:
            keyRes.append(j.key_responsibilities)
        workData = WorkExperienceSerializer(_).data
        workData['keyRes'] = keyRes
        work_expS.append(workData)

    education = EducationSerializer(Education.objects.filter(candidate = candidate), many = True).data

    skills = SkillSerializer(Skill.objects.filter(candidate = candidate), many = True).data
    languages = LanguageSerializer(Language.objects.filter(candidate = candidate), many = True).data
    certifications = CertificationSerializer(Certification.objects.filter(candidate = candidate), many = True).data
    refs = ReferenceSerializer(Reference.objects.filter(candidate = candidate), many = True).data

    user_data = {'candidate' : candidateS, "work_exps" : work_expS, "education" : education, "skills" : skills, "languages" : languages, "certs" : certifications, "refs" : refs}
    return Response(user_data, status = 200)
