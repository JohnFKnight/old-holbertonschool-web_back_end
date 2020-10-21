const kue = require('kue')
, queue = kue.createQueue();

// const kue = require('kue')
// , push_notification_code_2 = kue.createQueue();


// Data
const listProducts = [
  {
    'Id': 1,
    'name': 'Suitcase 250',
    'price': 50,
    'stock': 4
  },
  {
    'Id': 2,
    'name': 'Suitcase 450',
    'price': 100,
    'stock': 10
  },
  {
    'Id': 3,
    'name': 'Suitcase 650',
    'price': 350,
    'stock': 2
  },
  {
    'Id': 4,
    'name': 'Suitcase 1050',
    'price': 550,
    'stock': 5
  }
];


// Data access
function getItemById(id) {
  return (listProducts.find(x => x.Id === id));
}


// Server
const express = require('express');
const app = express();
const port = 1245;

app.listen(port, () => {
  console.log('app listening at http://localhost:${port}');
})


// Products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
})


// In stock in Redis
import redis from 'redis';
const client = redis.createClient();
const { promisify } = require('util');
const getAsync = promisify(client.get).bind(client);

function reserveStockById(itemId, stock) {
  const item = getItemById(itemId);
  // let onHand = item.stock;
  // client.set(item.reservedStock, stock);
  // client.set(item.stock, onHand - 1);
  client.set(item.stock, stock);
  getItemById(itemId);
}

// function getCurrentReservedStockById(itemId) {
async function getCurrentReservedStockById(itemId) {
  const item =  getItemById(itemId);
  return (await getAsync(item.stock));
}


// Product detail
app.get('/list_products/:itemId', (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (item == undefined )
    return (res.status(404).json({status: 'Product not found'}));
  return (res.json({item: getItemById(itemId), reserved: getCurrentReservedStockById(itemId).then(console.log)}));
  // res.json(getCurrentReservedStockById(itemId).then(console.log));
})


app.get('/reserve_product/:itemId', (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (item == undefined )
    return (res.status(404).json({status: 'Product not found'}));
  console.log('STOCK ', item.stock);
  if (item.stock < 1)
    return (res.status(403).json({status:'Not enough stock available', itemId: itemId}));

  reserveStockById(itemId, 1);
  res.status(200).json({status:'Reservation confirmed', itemId: itemId});
})
