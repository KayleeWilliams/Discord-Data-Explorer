/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{html,js,vue}",
    "./app.vue",
  ],
  theme: {
    extend: {
      colors: {
        background: '#382D43',
        primary: '#E3C7E7',
        secondary: '#CC9EFA',
      },
    },
  },
  plugins: [],
}
