const { createProxyMiddleware } = require('http-proxy-middleware')

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: import.meta.env.VITE_REACT_APP_BACK_END_URL,
      changeOrigin: true,
    })
  )

  app.use(
    '/auth',
    createProxyMiddleware({
      target: import.meta.env.VITE_REACT_APP_BACK_END_URL,
      changeOrigin: true,
    })
  )
}
