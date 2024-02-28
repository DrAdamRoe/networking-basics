const net = require("net");
const server = net.createServer();

//define HTTP response
const http_status_code = "HTTP/1.0 200 OK\n";

//The extendable list of HTTP headers
const http_headers = "Content-Type: text/html\n";

const http_end_of_metadata="\n";

//message payload, or body
const http_body = `
<html>
  <body>
    <h1>Hello World</h1> 
    <p>this is my server, hey.</p>
  </body>
</html>
`;

const http_response = http_status_code + http_headers + http_end_of_metadata + http_body;

server.listen({ host:"0.0.0.0", port: 3000 });

handleConnection = (socket) => {
  socket.on("data", (chunk) => {
    console.log("Received chunk: " + chunk.toString());
    socket.write(http_response, () => socket.end());
  });
};

server.on("connection", handleConnection);

console.log("Server is ready! Listening ...");
