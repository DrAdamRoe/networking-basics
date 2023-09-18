const net = require('net');

const HOST = '0.0.0.0'; // Standard loopback interface address (localhost)
const port_number = 65432; // Port to listen on (non-privileged ports are > 1023)

const server = net.createServer((socket) => {
  console.log(`Server started at address ${HOST} on port ${port_number}`);
  socket.on('data', (data) => {
    console.log('Client connected from: ', socket.remoteAddress, socket.remotePort);
    const requestData = data.toString();

    // Log received message from client
    console.log('Message from client:\n', requestData);
    console.log(' -- end message from client -- ');

    // HTTP Response
    const httpStatusLine = 'HTTP/1.0 200 OK';
    const httpHeaders = 'Content-Type: text/html\r\nContent-Length: 44'; // Modify Content-Length accordingly
    const httpBody = `
<html>
<body>
<h1>Hello World</h1> 
<p>This is my server, hey.</p>
</body>
</html>
`;

    const httpResponse = `${httpStatusLine}\r\n${httpHeaders}\r\n\r\n${httpBody}`;
    socket.write(httpResponse, 'utf-8', () => {
      // Close the connection after sending the response
      socket.end();
      console.log('Connection closed');
    });
  });

  socket.on('error', (err) => {
    console.error('Socket error:', err);
  });
});

server.listen(port_number, HOST);