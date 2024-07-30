import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();


client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err)
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
};

const getPromisify = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const val = await getPromisify(schoolName);
    console.log(val);
  } catch (err) {
      console.log(err);
  }
};

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
