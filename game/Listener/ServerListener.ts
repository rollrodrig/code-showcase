import IListener, { EventType } from "./IListener";
export default class ServerListener implements IListener {
    listen(eventType:EventType): void {
        console.log('listen: ServerListener');
    }
}