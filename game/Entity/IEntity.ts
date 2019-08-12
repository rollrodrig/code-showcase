import * as Phaser from 'phaser';
import GameScene from '../Scenes/GameScene';
export interface IEntt {
    x: number;
    y: number;
    width: number;
    height: number;
    imageKey: string;
    id: number;
}
export default interface IEntity {
    scene: Phaser.Scene;
    container: Phaser.GameObjects.Container;
    image: Phaser.GameObjects.Image;
    id: number;
    setConfig(config:IEntt): void;
    create():void;
    addToScene():void;
    setX(x:number):void;
    getX():number;
    setY(y:number):void;
    getY():number;
    setRow(row:number):void;
    setColumn(column:number):void;
    setDepth(depth:number):void;
    resetPosition():void;
    autoSetDepth():void;
    setTint():void;
    clearTint():void;
    getEntity():IEntity;
}