const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  }
]

function getItemById(id) {
  for (item of listProducts) {
    if (item.id === id) {
      return item;
    }
  }
}

const express = require('express');

const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.send(listproducts);
});

app.get('list_products/:itemId', (req, res) => {
  try {
    res.send(getCurrentReservedStockById(itemId));
  } catch (error) {
    return {'status': 'Product not found'};
  }
});

app.get('reserve_product/:itemId', (req, res) => {
  try {
    getCurrentReservedStockById(itemId);
  } catch (error) {
    return {'status': 'Product not found'};
  }
});

app.listen(port, () => {
});

import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();


client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err)
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function reserveStockById(itemId, stock) {
  client.set(itemId, stock, print);
};

const getPromisify = promisify(client.get).bind(client);

async function getCurrentReservedStockById(itemId) {
  try {
    const val = await getPromisify(itemId);
    return val;
  } catch (err) {
      console.log(err);
  }
};
