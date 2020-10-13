// const kue = require('kue')
// , push_notification_code = kue.createQueue();

const kue = require('kue')
, queue = kue.createQueue();

queue.process('notify', function(job, done) {
    // console.log(job.data.phoneNumber, job.data.message);
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
});

function sendNotification(phoneNumber, message) {
    console.log('Sending notification to ' + phoneNumber + ', with message: ' + message);
    // done();
}
