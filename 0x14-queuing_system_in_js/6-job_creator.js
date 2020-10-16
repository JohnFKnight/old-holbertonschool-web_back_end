const kue = require('kue')
, queue = kue.createQueue();

// const kue = require('kue')
// , push_notification_code = kue.createQueue();

const notification = {
    phoneNumber: '123.456.7890',
    message: 'hello',
};

const job = queue.create('push_notification_code', notification).save(function(err) {
    if (!err) console.log('Notification job created: ' +  job.id);
});

job.on('complete', function() {
    console.log('Notification job completed');
}).on('failed', function() {
    console.log('Notification job failed');
});
