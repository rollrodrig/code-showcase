import IListener, { EventType } from "./IListener";
export default class GameSceneListener implements IListener {
    listen(eventType:EventType): void {
        throw new Error("Method not implemented.");
    }
}
