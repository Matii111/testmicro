require('dotenv').config();
const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.BACKEND_PORT;

app.use(express.static(path.join(__dirname, '../../frontend/public')));

app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, '../../frontend/public', 'index.html'));
});

// Inicia el servidor
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
