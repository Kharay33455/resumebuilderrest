from rest_framework import serializers
from .models import *


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        exclude = ['id', 'user']

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        exclude = ['id', 'candidate']
    
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ['id', 'candidate']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ['candidate','id']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        exclude = ['candidate','id']
    exclude = ['candidate','id']

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        exclude = ['id','candidate']