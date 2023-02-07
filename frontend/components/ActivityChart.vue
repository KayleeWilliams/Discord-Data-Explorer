<template>
    <div class="w-full bg-secondary p-4 rounded-xl drop-shadow-lg">
    <p class="font-bold"> Activity </p>
    <div class="flex flex-row gap-2 font-medium justify-center">
      <button @click="updateData('Hourly')">Hourly</button>
      <button @click="updateData('Weekly')">Weekday</button>
      <!-- <button @click="updateData('perYear')">Per Year</button> -->
    </div>
    <Line ref="line" :data="data" :options="options" class="w-full"/>
  </div>
</template>

<script>
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, PointElement, LineElement, Filler} from 'chart.js'
  import { Line } from 'vue-chartjs'

  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, LineElement, PointElement, Filler)
  let delayed = false; 


  const weekly = (activity) => {
    return {
      labels: activity.weekly.map((item) => item[0]),
      datasets: [
        {
          label: 'Activity',
          data: activity.weekly.map((item) => item[1]),

          // Data styling
          borderColor: 'rgba(68, 101, 241, 1)',
          backgroundColor: 'rgba(68, 101, 241, 0.6)',
          pointStyle: false,
          tension: 0.5,
          fill: 'start',
          radius: 6,
        }
      ]
    }
  }

    const hourly = (activity) => {
    return {
      labels: activity.hourly.map((item) => item[0]),
      datasets: [
        {
          label: 'Activity',
          data: activity.hourly.map((item) => item[1])  ,

          // Data styling
          borderColor: 'rgba(255, 91, 159, 1)',
          backgroundColor: 'rgba(255, 91, 159, 0.6)',
          pointStyle: false,
          tension: 0.5,
          fill: 'start',
          radius: 6,
        }
      ]
    }
  }

  const options = {
    responsive: true,
    maintainAspectRatio: true,
    scales: {
      x: { ticks: { color: '#EBEBF7' } },
      y: {
        display: false,
        beginAtZero: false,
        ticks: { color: '#EBEBF7', display: false } 
      },
    },
    plugins: {
      legend: {
        display: false
      }
    },

    // Animate the graph on load
    animation: {
      onComplete: () => {
        delayed = true;
      },
      delay: (context) => {
        let delay = 0;
        if (context.type === 'data' && context.mode === 'default' && !delayed) {
          delay = context.dataIndex * 300 + context.datasetIndex * 100;
        }
        return delay;
      },
    }
  }

  export default {
    components: { Line },

    props: {
      activity: Object,
    },

    data() {
      return {
        options: options,
        data: hourly(this.activity)

      }
    },
    methods: {
      updateData(label) {
        switch (label) {
          case 'Weekly':
            this.data = weekly(this.activity)
            break
          case 'Hourly':
            this.data = hourly(this.activity)
            break
          // case 'Data Three':
          //   this.data = dataThree
          //   break
        }
      }
    }
  }
</script>