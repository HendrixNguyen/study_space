import express from "express";


const app = express();
const PORT = 3000;

app.use(PORT)

app.listen(PORT || 3000,() => {
  `this server is running on PORT:${PORT}`
})