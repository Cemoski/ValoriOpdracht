""""
Django's serialization framework provides a mechanism for “translating” Django models into' 
other formats. Usually these other formats will be text-based and used for sending Django' data over a wire, but it's 
possible for a serializer to handle any format (text-based or not).

Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first 
validating the incoming data. The serializers in REST framework work very similarly to Django's Form and ModelForm classes

"""""

from rest_framework import serializers
from .models import Intern


class InternSerializer(serializers.ModelSerializer):
	class Meta:
		model = Intern
		fields ='__all__'
