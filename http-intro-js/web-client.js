const net = require('net');

const HOST = '0.0.0.0'; // The server's hostname or IP address
const port_number = 65432; // The port used by the server

const client = new net.Socket();

client.connect(port_number, HOST, () => {
  console.log('Connected to the server');
  const msg = 'GET / HTTP/1.0';
  console.log('Sending to the server: ', msg);
  client.write(msg, 'utf-8'); // send your message with utf-8 encoding
});

client.on('data', (data) => {
  console.log('Received from server: ', data.toString('utf-8'));
  client.end(); // Close the connection when done
});

client.on('close', () => {
  console.log('Connection closed');
});