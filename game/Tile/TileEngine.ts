import * as Phaser from 'phaser';
import GameScene from '../Scenes/GameScene';
import Ground from '../Tile/Ground';
import Props from '../Tile/Props';
import TileBase from './TileBase';
import Wall from '../Tile/Wall';
import GridBuilder from './GridBuilder';
import GroundBuilder from './GroundBuilder';
import ITileEngine from './ITileEngine';
import TSceneData, { IGround, IWall } from '../Data/TSceneData';
import PropsBuilder from './PropsBuilder';
import WallBuilder from './WallBuilder';
import ITile from './ITile';
import TileFactory, {TileType} from './TileFactory';
import GameStorage from '../Storage/GameStorage';


export default class TileEngine {
    private static instance: TileEngine;

    scene: Phaser.Scene;
    rows: number;
    columns: number;
    groundBuilder: GroundBuilder;
    wallBuilder: WallBuilder;
    propsBuilder: PropsBuilder;
    gridBuilder: GridBuilder;
    showGrid: boolean = false;
    gameStorage = new GameStorage;
    constructor() {
        if (TileEngine.instance) { return TileEngine.instance; } TileEngine.instance = this;

        this.scene = new GameScene;
        this.groundBuilder = new GroundBuilder;
        this.wallBuilder = new WallBuilder;
        this.propsBuilder = new PropsBuilder;
        this.gridBuilder = new GridBuilder;
    }

    build() {
        let data:TSceneData  = this.gameStorage.get('map');
        
        this.rows = data.rows;
        this.columns = data.columns;

        this.groundBuilder.setData(this.rows, this.columns, data.groundZone, data.ground);
        this.groundBuilder.build();

        this.wallBuilder.setData(this.rows, this.columns, data.wallZone, data.wall);
        this.wallBuilder.build();

        this.propsBuilder.setData(this.rows, this.columns, data.propsZone, data.props);
        this.propsBuilder.build();

        this.gridBuilder.setData(this.rows, this.columns)
        this.gridBuilder.build();

    }

    getGroundTiles(): ITile[] | Ground[] {
        return this.groundBuilder.getTiles();
    }

    getWallTiles(): ITile[] | Wall[] {
        return this.wallBuilder.getTiles();
    }

    getPropsTiles(): ITile[] | Props[] {
        return this.propsBuilder.getTiles();
    }

    getGridTiles(): ITile[] | Props[] {
        return this.gridBuilder.getTiles();
    }

    addGround(row:number, column:number, element: IGround) {
        this.groundBuilder.buildOne(row, column, element)
    }
    
    updateGround(row:number, column:number, element: IGround) {
        this.groundBuilder.updateOne(row, column, element.k)
    }

    removeGround(row:number, column:number) {
        this.groundBuilder.removeOne(row, column);
    }

    addWall(row:number, column:number, element: IWall) {
        this.wallBuilder.buildOne(row, column, element)
    }
    updateWall(row:number, column:number, element: IWall) {
        this.wallBuilder.updateOne(row, column, element.k);
    }
    removeWall(row:number, column:number) {
        this.wallBuilder.removeOne(row, column);
    }
    onDragStart() {
        let w: ITile[] = this.getWallTiles();
        let ll = w.length;
        for (let i = 0; i < ll; i++) {
            let wc = w[i];
            wc.container.alpha = 0.5;
        }
    }
    onDragEnd() {
        let w: ITile[] = this.getWallTiles();
        let ll = w.length;
        for (let i = 0; i < ll; i++) {
            let wc = w[i];
            wc.container.alpha = 1;
        }
    }
    onDrop() {
        console.log('TileEngine onDrop');
        
    }

    disableGrid() {
        this.gridBuilder.disable();
    }
    enableGrid() {
        this.gridBuilder.enable();
    }
    setGridOnTop() {
        this.gridBuilder.setDepth(100000);
    }
    setGridOnMid() {
        this.gridBuilder.setDepth(1000);
    }
}