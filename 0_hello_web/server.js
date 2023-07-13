const net = require("net");
const server = net.createServer();

server.on("connection", handleConnection);
server.listen({ port: 3000 });
console.log("Server is ready! Listening on port 3000…")

function handleConnection(socket) {
  socket.on("data", (chunk) => {
    console.log("Received chunk: ");
    console.log(chunk.toString());
  });

  socket.write("HTTP/1.1 200 OK\nContent-Length: 11\n\nHello World");
}
