// const redis = require('redis');
import redis from 'redis';
const client = redis.createClient();
const { promisify } = require('util');
const getAsync = promisify(client.get).bind(client);
const subscriber = redis.createClient();
const publisher = redis.createClient();


client.on('error', function(err) {
    console.log('Redis client not connected to the server: ' + err);
})
client.on('connect', function() {
    console.log('Redis client connected to the server');
})

function publishMessage(message, time) {
    setTimeout(() => {
	const achannel = 'holberton school channel';
	console.log('About to send ' + message);
	publisher.publish(achannel, message);
    }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
