/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/src/**/*.css',
    './static/src/**/*.js',
    './node_modules/flowbite/**/*.js'
],

  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

