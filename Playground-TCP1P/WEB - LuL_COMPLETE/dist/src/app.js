const express = require('express')

const port = process.env.PORT || 3000

const app = express()
app.use((_req, res, next) => {
        res.setHeader('Content-Security-Policy', "default-src 'self'")
        next()
})
app.use(
        express.static('static', {
                index: 'index.html'
        })
)

app.use((req, res) => {
        res.type('text').send(`${req.path}`)
})

app.listen(port, async () => {
        console.log(`Listening on http://0.0.0.0:${port}`)
        console.log('Browser launched')
})
