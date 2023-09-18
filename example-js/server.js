const net = require("net");
const server = net.createServer();

server.on("connection", handleConnection);
server.listen({ host:"0.0.0.0", port: 3000 });
console.log("Server is ready! Listening…")

function handleConnection(socket) {
  socket.on("data", (chunk) => {
    console.log("Received chunk: ");
    console.log(chunk.toString());
  });

  socket.write("Server got your message");
}
