const net = require('net');

const HOST = '0.0.0.0'; // Standard loopback interface address (localhost)
const port_number = 65432; // Port to listen on (non-privileged ports are > 1023)

function formHttpBody() {
  // Message payload, or body
  const httpBody = `
<html>
<body>
<h1>Hello World</h1>
<p>This is my server, hey.</p>
</body>
</html>
`;

  return httpBody;
}

function formHttpResponse() {
  // HTTP start line
  const startLine = 'HTTP/1.0 200 OK';

  // The extendable list of HTTP headers
  const headers = 'Content-Type: text/html';

  // Break between head and body - the neck, if you will.
  const endOfMetadata = '';

  // Message payload, or body
  const httpBody = formHttpBody();

  // Set body length in header, using body function
  const contentLength = Buffer.byteLength(httpBody, 'utf-8');
  const headersWithContentLength = `${headers}\r\nContent-Length: ${contentLength}`;

  // The "head": start-line + headers
  const httpHead = `${startLine}\r\n${headersWithContentLength}`;

  const httpResponse = `${httpHead}\r\n${endOfMetadata}${httpBody}`;

  return httpResponse;
}

const server = net.createServer((socket) => {
  console.log(`Server started at address ${HOST} on port ${port_number}`);
  socket.on('data', (data) => {
    console.log('Client connected from: ', socket.remoteAddress, socket.remotePort);
    const requestData = data.toString();

    // Log received message from client
    console.log('Message from client:\n', requestData);
    console.log(' -- end message from client -- ');

    // Send encoded HTTP response
    const httpResponse = formHttpResponse();
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
