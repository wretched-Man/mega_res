/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {
        screens : {
            'mobile': '600px',
        }
    },
  },
  plugins: [],
}

