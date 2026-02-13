/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        'tech-black': '#05070A',
        'tech-surface': '#0D1117',
        'laser-blue': '#00D1FF',
        'signal-orange': '#FF4D00',
        'machine-grey': '#30363D',
        'data-green': '#00FF41'
      },
      fontFamily: {
        'mono': ['"JetBrains Mono"', 'monospace'],
        'sans': ['Inter', 'sans-serif']
      },
      letterSpacing: {
        'widest': '.25em',
      }
    },
  },
  plugins: [],
}
