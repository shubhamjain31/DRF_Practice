from asyncore import read
from rest_framework import serializers
from .models import Course, Instructor, Subject

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields ="__all__"

# class SubjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subject
#         fields ="__all__"
        
# class InstructorSerializer(serializers.ModelSerializer):
#     subjects = SubjectSerializer(read_only=True, many=True)
    
#     class Meta:
#         model = Instructor
#         fields ="__all__"

# ======================================================= HyperLinkedModelSerializer ============================================
class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields ="__all__"
        
class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    subject = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='subject-details')
    
    class Meta:
        model = Instructor
        fields = "__all__"