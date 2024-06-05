from rest_framework import serializers
from apps.parteevento.models import ParteEvento
from apps.evento.models import Evento
from apps.evento.api.serializers import EventoSerializer

from apps.evento.models import Evento

class ParteEventoSerializer(serializers.ModelSerializer):
    fk_evento = EventoSerializer()

    class Meta:
        model = ParteEvento
        fields = ['id', 'fk_evento', 'orden', 'timecap', 'descanso', 'date_created']

    def create(self, validated_data):
        fk_evento_data = validated_data.pop('fk_evento')
        fk_evento = Evento.objects.create(**fk_evento_data)
        parte_evento = ParteEvento.objects.create(fk_evento=fk_evento, **validated_data)
        return parte_evento
    

class ParteEvento_por_id(serializers.ModelSerializer):
    fk_evento = serializers.PrimaryKeyRelatedField(queryset=Evento.objects.all())

    class Meta:
        model = ParteEvento
        fields = ['id', 'fk_evento', 'orden', 'timecap', 'descanso', 'date_created']
