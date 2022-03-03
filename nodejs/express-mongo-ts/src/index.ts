import bodyParser from "body-parser";
import express from "express";


const app = express();
const PORT = 3000;

app.use(bodyParser)
app.use(express.urlencoded());

app.listen(PORT || 3000,() => {
  `this server is running on PORT:${PORT}`
})