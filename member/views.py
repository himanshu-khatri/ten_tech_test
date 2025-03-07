from django.shortcuts import render
from rest_framework.generics import ListAPIView

from member.models import Member
from member.serializers import MemberSerializer


# Create your views here.
class MemberListView(ListAPIView):
    """
        API to provide list of all members
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer