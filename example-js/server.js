const net = require("net");
const server = net.createServer();

server.listen({ host: "0.0.0.0", port: 3000 });

handleConnection = (socket) => {
  socket.on("data", (chunk) => {
    console.log("Received chunk: " + chunk.toString());
    socket.write("Server got your message", () => server.close());
  });
}

server.on("connection", handleConnection);

console.log("Server is ready! Listening…");
