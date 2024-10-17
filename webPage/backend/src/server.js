require('dotenv').config();
const express = require('express');
const cors = require('cors');
const path = require('path');
const app = express();
const { createProxyMiddleware } = require('http-proxy-middleware');
const PORT = process.env.BACKEND_PORT;
const JSON = process.env.JSON_PORT;

const corsConfig = {
    origin: `http://localhost:${JSON}`,
    methods: ['GET', 'POST'],
    credentials: false
}

app.use(cors(corsConfig));

app.use('/api', createProxyMiddleware({
    target: `http://localhost:${JSON}`,
    changeOrigin: true,
    pathRewrite: {
        '^/api': '',
    },
}));

app.use(express.static(path.join(__dirname, '../../frontend/public')));

app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, '../../frontend/public', 'index.html'));
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
