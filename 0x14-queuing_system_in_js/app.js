const express = require('express');
const app = express();
const port = 1245;
const listProducts = require('

app.listen(port, () => {
    console.log('app listening at http://localhost:${port}');
})

app.get('/list_products', (req, res) => {
    res.json({});
})

// function getItemById(id) {
