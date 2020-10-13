// const redis = require('redis');
import redis from 'redis';
const client = redis.createClient();
const { promisify } = require('util');
const getAsync = promisify(client.get).bind(client);


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

// client.hset('HolbertonSchools', 
// 	    'Portland', 50,
// 	    'Seattle', 80,
// 	    'New York', 20,
// 	    'Bogota', 20,
// 	    'Cali', 40,
// 	    'Paris', 2
// 	   );

// Gary used async/await and a loop. Nice. What is main() at the bottom?
// He got Reply 0 too. Whew!
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

client.hgetall('HolbertonSchools', function(err, res) {
    console.log(res);
});
