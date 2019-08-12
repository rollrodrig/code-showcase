import IListener, { EventType } from "./IListener";
import TileController from '../Controllers/TileController';
import GameStateController from '../Controllers/GameStateController';

export default class EntityClickListener implements IListener {
    tileController:TileController;
    gameStateController:GameStateController;

    constructor() {
        this.tileController = new TileController;
        this.gameStateController = new GameStateController;
    }

    listen(eventType:EventType): void {
        switch(eventType) {
            case EventType.pointerdown:
                // this.gameStateController.setEntityState();
            break;
            case EventType.pointerup:
                // this.gameStateController.setMapState();
            break;
        }
    }
}
