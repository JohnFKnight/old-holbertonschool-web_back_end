import redis from 'redis';
const client = redis.createClient();
const { promisify } = require('util');
const getAsync = promisify(client.get).bind(client);

function reserveSeat(number) {
  // console.log(number);
  client.set('available_seats', number);
  console.log('SEATS SET ', ('available_seats'));
}

async function getCurrentAvailableSeats() {
  // console.log(await getAsync('available_seats'));
  const seats = await getAsync('available_seats').then(function(reply) {
    console.log('REPLY ', reply);
    return reply;
  });
}

let reservationEnabled = true;

const kue = require('kue')
, queue = kue.createQueue();

const express = require('express');
const app = express();
const port = 1245;

app.listen(port, () => {
  console.log('app listening at http://localhost:${port}');
})

app.get('/available_seats', (req, res) => {
  reserveSeat(55);
  res.json({numberOfAvailableSeats: getCurrentAvailableSeats()});
})

app.get('/reserve_seat', (req, res) => {
  if (reservationEnabled === false)
    return (res.json({status: 'Reservation in process'}));

  const job = queue.create('reserve_seat').save(function(err) {
    if (err) return (res.json({status: 'Reservation failed'}));

    res.json({status: 'Reservation in process'});
  });
  job.on('complete', function ()  {
    console.log('Seat reservation job %d completed', job.id);
  }).on('failed', function (err) {
    console.log('Seat reservation job %d failed', job.id,  err)
  });
})

app.get('/process', (req, res) => {
  queue.process('reserve_seat', function(job, done) {
    let seats = getCurrentAvailableSeats();
    console.log(seats)
    let reserved = reserveSeat()
    done();
  });
})
