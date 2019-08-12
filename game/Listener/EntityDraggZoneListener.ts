import IListener, { EventType } from "./IListener";
import TileController from '../Controllers/TileController';
import GameStateController from '../Controllers/GameStateController';
import EntityController from '../Controllers/EntityController';

export default class EntityDraggZoneListener implements IListener {
    constructor() {
    }
    listen(eventType:EventType, data:any): void {
        switch(eventType) {
            case EventType.dragenter:
            break;
            case EventType.dragleave:
            break;
            case EventType.drop:
            break;
        }
    }
}
