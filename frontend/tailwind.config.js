/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./components/**/*.{html,js,vue}", "./app.vue"],
  theme: {
    extend: {
      colors: {
        background: "#131517",
        primary: "#EBEBF7",
        secondary: "#1E1F24",
        accent: "#4465F1",
      },
    },
  },
  plugins: [],
};
