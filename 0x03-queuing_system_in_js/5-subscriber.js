import { createClient, print } from 'redis';

const client = createClient();


client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err)
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.subscribe('holberton school channel', (err) => {
  if (err) {
    console.log(error);
  }
});

client.on('message', (channel, message) => {
  if (message == 'KILL_SERVER') {
    client.unsubscribe('holberton school channel', (err) => {
      if (err) {
        console.log(err);
      } else {
        client.quit((err) => {
          if (err) {
            console.log(err);
          }
        });
      }
    });
  } else {
    console.log(message);
  }
});
