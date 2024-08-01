import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();


client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err)
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
  const number = 50;
});

function reserveSeat(number) {
  client.set(available_seats, number, print);
};

const getPromisify = promisify(client.get).bind(client);

async function getCurrentAvailableSeats() {
  try {
    const val = await getPromisify(available_seats);
    let reservationEnabled = true;
    return val;
  } catch (err) {
    let reservationEnabled = false;
    console.log(err);
  }
};

const kue = require('kue');
const queue = kue.createQueue();

const express = require('express');

const app = express();
const port = 1245;

app.get('/available_seats', (req, res) => {
  return {'numberOfAvailableSeats': getCurrentAvailableSeats()};
});

app.get('reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return { "status": "Reservation are blocked" };
  }
  const job = queue.create('reserve_seat').save(err => {
    if (!err) {
      return {'status': 'Reservation in process'};
    } else {
      return { "status": "Reservation failed" };
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
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
