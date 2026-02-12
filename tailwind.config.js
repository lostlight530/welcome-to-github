/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'google-blue': '#4285F4',
        'google-red': '#EA4335',
        'google-yellow': '#FBBC05',
        'google-green': '#34A853',
        'dark-bg': '#0F172A',
        'card-bg': '#1E293B',
      },
      fontFamily: {
        'sans': ['Inter', 'system-ui', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
