import { createClient } from 'redis';
import { print } from 'redis';

const client = createClient();

client.on('error', err => {
        console.log(`Redis client not connected to the server: ${err}`)
});

client.on('connect', () => {
        console.log('Redis client connected to the server');


        function setNewSchool(schoolName, value) {
                client.set(schoolName, value, (err, reply) => {
                        if (err) {
                                console.error(err);
                        } else {
                                console.log(`Reply: ${reply}`);
                        }
                });
        };

        function displaySchoolValue(schoolName) {
                client.get(schoolName, (err, value) => {
                        if (err) {
                                console.error(err);
                        } else {
                                console.log(value);
                        }
                });
        };
        setNewSchool('HolbertonSanFrancisco', '100');
        displaySchoolValue('HolbertonSanFrancisco');

});
