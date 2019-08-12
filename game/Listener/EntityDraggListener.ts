import IListener, { EventType } from "./IListener";
import TileController from '../Controllers/TileController';
import GameStateController from '../Controllers/GameStateController';
import EntityController from '../Controllers/EntityController'
import { EStates } from "../State/EStates";

export default class EntityDraggListener implements IListener {
    tileController:TileController;
    gameStateController:GameStateController;
    entityController:EntityController;

    constructor() {
        this.tileController = new TileController;
        this.gameStateController = new GameStateController;
        this.entityController = new EntityController;
    }

    listen(eventType:EventType, data:any): void {
        switch(eventType) {
            case EventType.dragstart:
                //TODO, set game state entity
                this.gameStateController.state = EStates.ENTITY;
                this.entityController.onDragStart(data);
                this.tileController.onDragStart();
                break;
            case EventType.drag:
                this.entityController.onDrag(data);
                this.tileController.onDrag();
            break;
            case EventType.dragend:
                // this.gameStateController.setMapState();
                this.gameStateController.state = EStates.PANNING;
                this.entityController.onDragEnd(data);
                this.tileController.onDragEnd();
            break;
            case EventType.dragenter:
                this.tileController.onDragEnter();
            break;
            case EventType.dragleave:
                this.tileController.onDragLeave();
            break;
            case EventType.drop:
                this.tileController.onDrop();
            break;
        }
    }
}
