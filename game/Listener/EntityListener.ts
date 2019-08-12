import IListener, { EventType } from "./IListener";
import EntityController from '../Controllers/EntityController';
// This class is not used
export default class EntityListener implements IListener {
    entityController:EntityController;
    onDragStart:OnDragStart = new OnDragStart;
    onDrag:OnDrag = new OnDrag;
    onDrangEnd:OnDrangEnd = new OnDrangEnd;
    onPointerDown:OnPointerDown = new OnPointerDown;
    onPointerUp:OnPointerUp = new OnPointerUp;
    onPointerOver:OnPointerOver = new OnPointerOver;
    onPointerOut:OnPointerOut = new OnPointerOut;

    constructor(){
        this.entityController = new EntityController;
    }
    
    listen(eventType:EventType, data:any): void {
        console.log('listen: EntityListener');
        switch(eventType) {
            // todo, should be updated
            // case EventType.dragstart:
            //     this.entityController.onDragStart(data);
            //     break;
        }

    }

}

abstract class OnEntityEvent {

}

class OnDragStart extends OnEntityEvent {

}

class OnDrag extends OnEntityEvent {

}

class OnDrangEnd extends OnEntityEvent {

}

class OnPointerDown extends OnEntityEvent {

}

class OnPointerUp extends OnEntityEvent {

}

class OnPointerOver extends OnEntityEvent {

}

class OnPointerOut extends OnEntityEvent {

}