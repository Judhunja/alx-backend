import kue from 'kue';

import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

queue.testMode.enter();

const list = [
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
    }
];

const result = createPushNotificationsJobs(list, queue);

import { expect } from 'chai';

expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');

queue.testMode.exit();
