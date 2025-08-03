from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WellnessInputSerializer
import xgboost as xgb
import numpy as np

# Load model once
model = xgb.Booster()
model.load_model("wellness_model.json")

FEATURE_ORDER = [
    'heart_rate', 'sleep_hours', 'steps', 'calories', 'screen_time',
    'hydration', 'bmi', 'age', 'exercise_minutes', 'alcohol_units', 'caffeine_mg'
]

class PredictStressView(APIView):
    def post(self, request):
        serializer = WellnessInputSerializer(data=request.data)
        if serializer.is_valid():
            features = serializer.validated_data
            input_array = np.array([[features[feat] for feat in FEATURE_ORDER]])
            dmatrix = xgb.DMatrix(input_array, feature_names=FEATURE_ORDER)
            prob = model.predict(dmatrix)[0]
            result = int(prob > 0.5)
            return Response({
                "stress_risk": result,
                "probability": float(prob)
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
