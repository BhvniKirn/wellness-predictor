from rest_framework import serializers

class WellnessInputSerializer(serializers.Serializer):
    heart_rate = serializers.FloatField()
    sleep_hours = serializers.FloatField()
    steps = serializers.IntegerField()
    calories = serializers.FloatField()
    screen_time = serializers.FloatField()
    hydration = serializers.FloatField()
    bmi = serializers.FloatField()
    age = serializers.IntegerField()
    exercise_minutes = serializers.FloatField()
    alcohol_units = serializers.FloatField()
    caffeine_mg = serializers.FloatField()
