import * as Phaser from 'phaser';
import CharacterDepthSorting from '../Sorting/CharacterDepthSorting';
import EntityController from '../Controllers/EntityController';
import GameScene from '../Scenes/GameScene';
import { GC } from '../Scenes/GameConfig';
import TileEngine from '../Tile/TileEngine';
import Collider from '../Utils/Collider';
import TileBase from '../Tile/TileBase';
import Ground from '../Tile/Ground';
import Utils from '../Utils/Utils';
import { IRectangle } from '../Utils/IRectangle';
import PositionController from './PositionController';
import GridBuilder from '../Tile/GridBuilder';
import WallBuilder from '../Tile/WallBuilder';
import GroundBuilder from '../Tile/GroundBuilder';
import Observer from '../Observer/Observer';
import IEntity, { IEntt } from './IEntity';
import ITile from '../Tile/ITile';
export default abstract class Entity implements IEntity {
    private _scene: Phaser.Scene;
    public get scene(): Phaser.Scene {
        return this._scene;
    }
    private _container: Phaser.GameObjects.Container;
    public get container(): Phaser.GameObjects.Container {
        return this._container;
    }
    private _image: Phaser.GameObjects.Image;
    public get image(): Phaser.GameObjects.Image {
        return this._image;
    }
    prevRow: number;
    prevColumn: number;
    row: number = 0;
    column: number = 0;
    config: IEntt;
    x: number;
    y: number;
    width: number;
    height: number;
    imageKey: string;
    id: number;
    groundTiles: ITile[];
    depthOnDrag: number = 50000;
    depthIddle: number = 20000;
    depth: number;
    dragDistanceThreshold: number = 0;
    tileEngine: TileEngine;
    gridBuilder: GridBuilder;
    wallBuilder: WallBuilder;
    observers: Observer[] = [];
    tilePositionHelper: Phaser.GameObjects.Image;
    prevTilePositionHelper: Phaser.GameObjects.Image;
    constructor() {
        this._scene = new GameScene;
        this.tileEngine = new TileEngine;
        this.groundTiles = this.tileEngine.groundBuilder.getTiles();
        this.gridBuilder = new GridBuilder;
        this.wallBuilder = new WallBuilder;
    }
    setConfig(config: IEntt) {
        this.config = config;
        this.x = this.config.x;
        this.y = this.config.y;
        this.width = this.config.width;
        this.height = this.config.height;
        this.imageKey = this.config.imageKey;
        this.id = this.config.id;
    }
    create(): void {
        // container origin is in x=0.5, y=0.5
        this._container = new Phaser.GameObjects.Container(this._scene, this.x, this.y);
        this._image = new Phaser.GameObjects.Image(this._scene, 0, 0, this.imageKey);
        this._image.displayOriginY = this._image.height - GC.tileHeight / 2;
        this._container.setSize(GC.tileWidth, GC.tileHeight);
        let rect: Phaser.Geom.Rectangle = new Phaser.Geom.Rectangle(0, -(this._image.width - GC.tileHeight / 2), this._image.width, this._image.height);
        this._container.setInteractive(rect, Phaser.Geom.Rectangle.Contains);
        this._container.add(this._image);
        this.setDepth(this.depthIddle);
    }
    addToScene(): void {
        this._scene.add.existing(this._container);
    }
    setDepthOnDragg() {

    }
    autoSetDepth() {
        this.depth = 10000 * (this.row + 1) + 100 * (this.column + 1) + 1; 
        this._container.setDepth(this.depth);
    }
    setDepth(depth:number) {
        this.depth = depth;
        this._container.setDepth(depth);
    }
    setX(x:number):void {
        this.container.x = this.x = x;
    }
    getX():number {
        return this.x;
    }
    setY(y:number):void {
        this.container.y = this.y = y;
    }
    getY():number {
        return this.y;
    }
    setRow(row:number):void {
        this.row = row;
    }
    setColumn(column:number):void {
        this.column = column;
    }
    resetPosition() {
        this.container.x = this.container.input.dragStartX;
        this.container.y = this.container.input.dragStartY;
        this.autoSetDepth();
    }
    setTint():void {
        this._image.setTint(0xff0000);
    }
    clearTint():void {
        this._image.clearTint();
    }
    getEntity(): IEntity {
        return this;
    }
}