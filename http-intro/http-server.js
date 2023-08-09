const net = require("net");
const server = net.createServer();

server.on("connection", handleConnection);
server.listen({ host:"localhost", port: 3000 });
console.log("Server is ready! Listening…")

function handleConnection(socket) {
  socket.on("data", (chunk) => {
    console.log("Received chunk: ");
    console.log(chunk.toString());
  });

//define HTTP response 
start_line = `HTTP/1.0 200 OK\n`
            
//The extendable list of HTTP headers
headers = `Content-Type: text/html\n`

end_of_metadata=`\n`

//message payload, or body
http_body = `
<html>
<body>
<h1>Hello World</h1> 
<p>this is my server, hey.</p>
</body>
</html>
`
  http_response = start_line + headers + end_of_metadata + http_body

  socket.write(http_response);
}
