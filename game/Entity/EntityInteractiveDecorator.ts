import * as Phaser from 'phaser';
import EntityDecorator from "./EntityDecorator";
import IEntity, { IEntt } from "./IEntity";
import { GC } from '../Scenes/GameConfig';
import EntityMouseHover from "../Dispatcher/EntityMouseHover";
import EntityPointerUp from "../Dispatcher/EntityPointerUp";
import EntityDragg from "../Dispatcher/EntityDragg";
import ServerListener from '../Listener/ServerListener';
import InterfaceListener from '../Listener/InterfaceListener';
import EntityDraggListener from '../Listener/EntityDraggListener';
import EntityClickListener from '../Listener/EntityClickListener';
import { EventType } from '../Listener/IListener';
import GameStateController from '../Controllers/GameStateController';
import {EStates} from '../State/EStates';
export default class EntityInteractiveDecorator extends EntityDecorator {
    entityMouseHover:EntityMouseHover;
    entityPointerUp:EntityPointerUp;
    entityDragg:EntityDragg;
    gameStateController:GameStateController;
    constructor(entity: IEntity){
        super(entity);
        this.entityMouseHover = new EntityMouseHover;
        this.entityPointerUp = new EntityPointerUp;
        this.entityDragg = new EntityDragg;
        this.gameStateController = new GameStateController;
    }
    implementDecorator(): void {
        this.interactiveZone();
        this.draggable();
        this.pointerEvents();
        this.draggEvents();
        this.addListeners();
    }
    addListeners(): void {
        // this.entityMouseHover.add(new ScenaryListener);
        this.entityPointerUp.add(new ServerListener);
        this.entityPointerUp.add(new InterfaceListener);
        this.entityPointerUp.add(new EntityClickListener);
        this.entityDragg.add(new EntityDraggListener);
    }
    interactiveZone(): void {
        let opts = {
            x: 0,
            y: -(this.entity.image.width - GC.tileHeight / 2),
            width: this.entity.image.width,
            height: this.entity.image.height,
        }
        let interactiveZone: Phaser.Geom.Rectangle = new Phaser.Geom.Rectangle(opts.x, opts.y, opts.width, opts.height);
        this.entity.container.setInteractive(interactiveZone, Phaser.Geom.Rectangle.Contains);
    }
    draggable(): void {
        this.entity.scene.input.setDraggable(this.entity.container);
    }
    pointerEvents():void {
        this.entity.container.on('pointerdown', () => {
            console.log('entity pointerdown');
            // this.entityPointerUp.notify(EventType.pointerdown, {entity:this.entity});
        });
        this.entity.container.on('pointerup', () => {
            console.log('entity pointerup');
            this.entityPointerUp.notify(EventType.pointerup, this.entity.getEntity());
        });
        this.entity.container.on('pointerover', () => {
            // console.log('pointerover');
            // this.entityMouseHover.notify(EventType.pointerover, {entity:this.entity});
        });
        this.entity.container.on('pointerout', () => {
            // console.log('pointerout');
            // this.entityMouseHover.notify(EventType.pointerout, this.entity.getEntity());
        });
    }
    draggEvents(): void {
        this.entity.container.on('dragstart', (pointer: Phaser.Input.Pointer) => {
            this.entityDragg.notify(EventType.dragstart,{entity:this.entity});
        });
        this.entity.container.on('drag', (pointer: Phaser.Input.Pointer, dragX: number, dragY: number) => {
            this.entityDragg.notify(EventType.drag,{entity:this.entity, x:dragX, y:dragY});
        });
        this.entity.container.on('dragend', (pointer: Phaser.Input.Pointer) => {
            this.entityDragg.notify(EventType.dragend,{entity:this.entity});
        });
        this.entity.container.on('dragenter', (pointer: Phaser.Input.Pointer, dropZone: Phaser.GameObjects.Zone) => {
            this.entityDragg.notify(EventType.dragenter);
        });
        this.entity.container.on('dragleave', (pointer: Phaser.Input.Pointer, dropZone: Phaser.GameObjects.Zone) => {
            this.entityDragg.notify(EventType.dragleave);
        });
        this.entity.container.on('drop', (pointer: Phaser.Input.Pointer, dropZone: Phaser.GameObjects.Zone) => {
            this.entityDragg.notify(EventType.drop, {a:'drop'});
        });
    }
}