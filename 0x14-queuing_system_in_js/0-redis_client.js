// const redis = require('redis');
import redis from 'redis';
const client = redis.createClient();

client.on('error', function(err) {
    console.log('Redis client not connected to the server: ' + err);
})
client.on('ready', function() {
    console.log('Redis client connected to the server');
})
