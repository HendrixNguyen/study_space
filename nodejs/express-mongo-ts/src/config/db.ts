import mongoose from "mongoose";
import dotenv from 'dotenv';

  const env = dotenv.config({path: '../.env.dev'});

async function connect() {
  await mongoose.connect(env.DB_URI)
}

export default connect();