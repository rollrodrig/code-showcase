import Builder from './Builder';
import {GC} from '../Scenes/GameConfig';
import GameScene from '../Scenes/GameScene';
import { Game } from 'phaser';
import Grid, { IGrid } from './Grid';
import ITile from './ITile';
import TileFactory, { TileType } from './TileFactory';
import TileBase from './TileBase';

export default class GridBuilder extends Builder {
    scene:GameScene;
	private static instance: GridBuilder;
    constructor() {
        super();
		if (GridBuilder.instance) { return GridBuilder.instance; } GridBuilder.instance = this;
        this.depthFactor = 100000;
        this.tileType = TileType.Grid;
    }

    setData(rows:number, columns:number) {
        this.scene = new GameScene;
        this.rows = rows;
        this.columns = columns;
    }
    
    build(){
		for(let row = 0; row < this.rows; row++) {
			for(let column = 0; column < this.columns; column++) {
                let x = ((column - row) * GC.tileWidth/2)+GC.canvasWidthMiddle;
                let y = (column + row) * GC.tileHeight/2;

                let elementData:IGrid = {
                    x:x,
                    y:y,
                    row:row,
                    column:column,
                    element:[],
                    id:Math.floor(Math.random()*10000),
                    depth: this.depthFactor,
                    debug:this.debug,
                    tileType: this.tileType,
                    empty: true,

                }

                let t:ITile = TileFactory.create(this.tileType, elementData);
                t.create();
                t.addToScene();
                this.store(t);
                t.hide(); // grid should start invisible
                
			}
        }
    }
}