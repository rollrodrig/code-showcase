import * as Phaser from 'phaser';
import { GC } from '../Scenes/GameConfig';
import GameScene from '../Scenes/GameScene';
import ITile from './ITile';
import IJsonData, { IGroundZone, IWallZone, IPropsZone, ITileZone, ITileElemnt } from '../Data/TSceneData';
import { TileType } from './TileFactory';

export interface ITileConfig {
    row: number;
    column: number;
    element: ITileElemnt;
    id: number;
    depth: number;
    x: number;
    y: number;
    debug: boolean;
    tileType: TileType;
    empty: boolean;
}

export default abstract class TileBase implements ITile {


    private _scene: Phaser.Scene;
    public get scene(): Phaser.Scene {
        return this._scene;
    }
    public set scene(value: Phaser.Scene) {
        this._scene = value;
    }

    private _container: Phaser.GameObjects.Container;
    public get container(): Phaser.GameObjects.Container {
        return this._container;
    }
    public set container(value: Phaser.GameObjects.Container) {
        this._container = value;
    }

    private _image: Phaser.GameObjects.Image;
    public get image(): Phaser.GameObjects.Image {
        return this._image;
    }
    public set image(value: Phaser.GameObjects.Image) {
        this._image = value;
    }

    private _id: number;
    public get id(): number {
        return this._id;
    }
    public set id(value: number) {
        this._id = value;
    }

    tileType: TileType;

    isometricHelper: Phaser.Geom.Rectangle;

    tileWidth: number;
    tileHeight: number;

    key: string;
    imageKey: string;

    element: ITileElemnt;
    row: number;
    column: number;

    x: number;
    y: number;

    width: number;
    height: number;

    depth: number;
    depthFactor: number = 10;
    debug: boolean;
    empty: boolean = true;

    constructor(config: ITileConfig) {
        this._scene = new GameScene;
        this.x = config.x;
        this.y = config.y;
        this.width = GC.tileWidth;
        this.height = GC.tileHeight;
        this.row = config.row;
        this.column = config.column;
        this.element = config.element;
        this.imageKey = config.element.k;
        this.id = config.id;
        this.depth = config.depth;
        this.debug = config.debug;
        this.tileType = config.tileType;
        this.empty = config.empty;
        // this.create();
    }

    create(): void {
        this.createSprite();
        this.crateContainer();
    }

    abstract createSprite(): void;

    crateContainer(): void {
        // container origin es x= 0.5, y = 0.5
        // every element start at x= 0.5 y = 0.5 
        this._container = new Phaser.GameObjects.Container(this._scene, this.x, this.y);
        this._container.setSize(GC.tileWidth, GC.tileHeight);
        this._container.setDepth(this.depth);
        this._container.add(this._image);
    }

    addToScene(): void {
        this._scene.add.existing(this._container);
    }

    getTile(): ITile {
        return this;
    }
    getImageKey(): string {
        return this.imageKey;
    }

    remove() {
        this._container.destroy();
    }

    show() {
        this._container.setVisible(true);
    }

    hide() {
        this._container.setVisible(false);
    }
    
    setDepth(depth:number) {
        this._container.setDepth(depth);
    }
}