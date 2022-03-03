import mongoose from "mongoose";
import dotenv from 'dotenv';

async function connect() {
  dotenv.config();
  await mongoose.connect(process.env.DB_URI)
}

export default connect();