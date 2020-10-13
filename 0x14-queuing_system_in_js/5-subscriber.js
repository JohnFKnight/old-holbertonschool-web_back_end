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

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    console.log(await getAsync(schoolName));
}


const achannel = 'holberton school channel';

subscriber.subscribe(achannel);

subscriber.on('message', function(channel, msg) {
    if (msg === 'KILL_SERVER') {
	subscriber.unsubscribe();
	subscriber.quit();
    }
    console.log(msg);
});
