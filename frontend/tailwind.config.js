/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./components/**/*.{html,js,vue}",
    "./app.vue",
  ],
  theme: {
    extend: {
      colors: {
        background: '#3A3238',
        primary: '#E3C7E7',
        secondary: '#D282A6',
      },
    },
  },
  plugins: [],
}
