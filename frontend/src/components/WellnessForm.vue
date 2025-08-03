<template>
  <div class="max-w-xl mx-auto p-6">
    <h2 class="text-2xl font-bold mb-4">Wellness Risk Predictor</h2>

    <form @submit.prevent="submitData" class="space-y-3">
      <div v-for="(value, key) in form" :key="key">
        <label class="block capitalize font-semibold">{{ key.replace(/_/g, ' ') }}</label>
        <input
          type="number"
          step="any"
          v-model.number="form[key]"
          class="border p-2 rounded w-full"
        />
      </div>

      <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded">Predict</button>
    </form>

    <div v-if="result" class="mt-6">
      <h3 class="text-lg font-bold">Prediction Result</h3>
      <p>Stress Risk: <strong>{{ result.stress_risk === 1 ? "High" : "Low" }}</strong></p>
      <p>Probability: {{ result.probability.toFixed(2) }}</p>

      <!-- Chatbot Tips -->
      <div class="mt-4 p-4 border border-green-400 rounded bg-green-50">
        <p class="font-semibold">Wellness Assistant:</p>
        <p>{{ chatbotTip }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      form: {
        heart_rate: 72,
        sleep_hours: 7,
        steps: 8000,
        calories: 2200,
        screen_time: 5,
        hydration: 2.5,
        bmi: 22,
        age: 25,
        exercise_minutes: 30,
        alcohol_units: 1,
        caffeine_mg: 100
      },
      result: null
    };
  },
  computed: {
    chatbotTip() {
      if (!this.result) return "";
      const { stress_risk, probability } = this.result;

      if (stress_risk === 1) {
        if (probability > 0.9)
          return "Your stress level is critically high. Try breathing exercises, reduce screen time, and prioritize sleep.";
        if (probability > 0.7)
          return "You seem stressed. Consider taking a short walk, staying hydrated, or meditating.";
        return "Your stress risk is moderate. Maintain balance with regular exercise and mindful breaks.";
      } else {
        if (probability < 0.1)
          return "You're doing great! Keep up the healthy lifestyle.";
        return "Your wellness profile looks strong. Stay active and hydrated!";
      }
    }
  },
  methods: {
    async submitData() {
      try {
        const res = await axios.post("http://127.0.0.1:8000/api/predict/", this.form);
        this.result = res.data;
      } catch (err) {
        console.error(err);
        alert("Prediction failed. Make sure the Django server is running.");
      }
    }
  }
};
</script>
