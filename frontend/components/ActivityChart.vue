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
          backgroundColor: '#FF9375',
          borderColor: '#C65E44',
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
          backgroundColor: '#FF9375',
          borderColor: '#C65E44',
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
      x: { ticks: { color: '#382D43' } },
      y: {
        display: false,
        beginAtZero: false,
        ticks: { color: '#382D43', display: false } 
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
        data: weekly(this.activity)

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



<!-- <script>
import { Bar, Chart, Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, PointElement, LineElement, Filler} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, LineElement, PointElement, Filler)
let delayed = false; 

export default {
  props: {
    data: Object,
  },
  
  name: 'ActitivityChart',
  components: { Line },

  data() {
    return {
      chartData: {
        labels: this.data.weekly.map((item) => item[0]),
        datasets: [
          {
            type: 'line',
            order: 1,
            label: 'Average Activity',
            data: this.data.weekly.map((item) => item[1]),

            // Data styling
            backgroundColor: '#FF9375',
            borderColor: '#C65E44',
            tension: 0.5,
            fill: 'start',
            radius: 6,
          }
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: true,
        scales: {
          x: { ticks: { color: '#382D43' } },
          y: {
            // display: false,
            beginAtZero: false,
            display: false,
            ticks: { color: '#382D43', display: false } 
          },
        },
        plugins: {
          legend: {
            display: false
          }
        },

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
    }
  },

    methods: {
    updateData (type) {
      switch (type) {
        case 'avgPerWeekday':
          this.chartData.labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
          this.chartData.datasets[0].label = 'Avg Per Weekday'
          this.chartData.datasets[0].data = [...new Array(7)].map(() => Math.floor(Math.random() * 100))
          break
        case 'perMonth':
          this.chartData.labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
          this.chartData.datasets[0].label = 'Per Month'
          this.chartData.datasets[0].data = [0, 1, 2, 3, 4]
          break
        case 'perYear':
          this.chartData.labels = ['2020', '2021', '2022', '2023', '2024']
          this.chartData.datasets[0].label = 'Per Year'
          this.chartData.datasets[0].data = [...new Array(5)].map(() => Math.floor(Math.random() * 100))
          break
      }
    },
  }
}

</script> -->