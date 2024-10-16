const { readFileSync, writeFileSync, existsSync } = require('fs');
const express = require('express');
const app = express();

// Verifica si el archivo count.txt existe, si no, crea uno con 0
if (!existsSync('./count.txt')) {
    writeFileSync('./count.txt', '0');
}

app.get('/', (req, res) => {
    try {
        // Lee el conteo actual desde count.txt
        const count = readFileSync('./count.txt', 'utf-8');
        console.log('count:', count);

        // Incrementa el conteo
        const newCount = parseInt(count) + 1;

        // Escribe el nuevo conteo en count.txt
        writeFileSync('./count.txt', newCount.toString());

        // Envía la respuesta HTML
        res.send(`
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8"/>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>TEST</title>
            </head>
            <body>
                <h1>TEST</h1>
                <p>Visits: ${newCount}</p>
            </body>
            </html>
        `);
    } catch (error) {
        console.error('Error reading/writing count.txt:', error);
        res.status(500).send('Error in the server.');
    }
});

app.listen(5000, () => console.log('Server running at http://localhost:5000/'));
