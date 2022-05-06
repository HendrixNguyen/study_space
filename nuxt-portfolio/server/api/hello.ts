import { ClientRequest, IncomingMessage, OutgoingMessage, ServerResponse } from "http";


export const hello = (req: IncomingMessage, res: ServerResponse) => res.write("", () => "Hello World!");