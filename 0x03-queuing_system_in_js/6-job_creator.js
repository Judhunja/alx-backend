const kue = require('kue');

const queue = kue.createQueue();

const jobDetails = {
  phoneNumber: '55555555',
  message: 'Welcome'
};

const job = queue.create('push_notification_code', jobDetails).save((err) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', (result) => {
  console.log('Notification job completed');
});

job.on('failed', (err) => {
  console.log('Notification job failed');
});
