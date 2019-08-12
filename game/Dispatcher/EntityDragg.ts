import IListener, { EventType } from "../Listener/IListener";
export default class EntityDragg {
    listeners: IListener[] = [];
    add(listener: IListener) {
        this.listeners.push(listener);
    }
    notify(eventType:EventType, data?:any) {
        this.listeners.map(listener => {
            listener.listen(eventType,data);
        });
    }
}
