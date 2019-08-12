import * as Phaser from 'phaser';
import Entity from './Entity';
import IEntity, { IEntt } from './IEntity';
import { GC } from '../Scenes/GameConfig';
import GameScene from '../Scenes/GameScene';
export default abstract class EntityDecorator implements IEntity {
    entity: IEntity
    constructor(entity: IEntity) {
        this.entity = entity;
    }
    abstract implementDecorator(): void;
    create(): void {
        this.entity.create();
        this.implementDecorator();
    }
    setConfig(config: IEntt): void {
        this.entity.setConfig(config);
    };
    addToScene(): void {
        this.entity.addToScene();
    }
    public get scene(): Phaser.Scene {
        return this.entity.scene;
    }
    public get container(): Phaser.GameObjects.Container {
        return this.entity.container;
    }
    public get image(): Phaser.GameObjects.Image {
        return this.entity.image;
    }
    public get id(): number {
        return this.entity.id;
    }
    setX(x:number):void {
        this.entity.setX(x);
    }
    getX():number {
        return this.entity.getX();
    }
    setY(y:number):void {
        this.entity.setY(y);
    }
    getY():number {
        return this.entity.getY();
    }
    setRow(row:number):void {
        this.entity.setRow(row);
    }
    setColumn(column:number):void {
        this.entity.setColumn(column);
    }
    setDepth(depth: number) {
        this.entity.setDepth(depth);
    }
    resetPosition():void {
        this.entity.resetPosition();
    }
    autoSetDepth():void {
        this.entity.autoSetDepth();
    }
    setTint():void {
        this.entity.setTint();
    }
    clearTint():void {
        this.entity.clearTint();
    }
    getEntity(): IEntity {
        return this.entity.getEntity();
    }
}