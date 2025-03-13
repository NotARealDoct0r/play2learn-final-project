// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })
module.exports = {
  publicPath: '/', // Change this to '/' so it works in both dev & production
  outputDir: '../static/dist', // Keep built files in static folder
  indexPath: '../static/dist/index.html', // Store Vue’s index.html in static, NOT templates!

  configureWebpack: {
    devServer: {
      devMiddleware: {
        writeToDisk: true
      }
    }
  }
};