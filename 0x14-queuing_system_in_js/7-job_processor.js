// const kue = require('kue')
// , push_notification_code = kue.createQueue();

const kue = require('kue')
, queue = kue.createQueue();

queue.process('notify2', function(job, done) {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
    // done();
});

const blacklist = [
    '4153518780',
    '4153518781'
];

function sendNotification(phoneNumber, message, job, done) {
    // console.log(job.data);
    let progress = 0;
    // job.progress(progress + 1, 50);
    function status() {
    	progress += 1;
    	job.progress(progress, 100);
    	if (progress >= 50) return done();
    }
    status();
    if (blacklist.includes(phoneNumber)) {
	return done('Phone number ' + phoneNumber + ' is blacklisted');
    }
    console.log('Sending notification ' + job.id + ' to ' + phoneNumber + ', with message: ' + message);
    done();
}

