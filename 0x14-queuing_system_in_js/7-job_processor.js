// const kue = require('kue')
// , push_notification_code = kue.createQueue();

const kue = require('kue')
, queue = kue.createQueue();

queue.process('push_notification_code_2', function(job, done) {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
    // done();
});

const blacklist = [
    '4153518780',
    '4153518781'
];

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);
    if (blacklist.includes(phoneNumber)) {
	return done('Phone number %d is blacklisted', phoneNumber);
    }
    job.progress(50, 100);
    console.log('Sending notification %d to %d with message %s', job.id, phoneNumber, message);
    return done();
}
