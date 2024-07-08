/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/src/**/*.css',
    './node_modules/flowbite/**/*.js'
],

  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

