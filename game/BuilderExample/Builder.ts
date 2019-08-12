import * as Phaser from 'phaser';
import GameScene from '../Scenes/GameScene';
import TileBase, { ITileConfig } from './TileBase';
import ITile from './ITile';
import { GC } from '../Scenes/GameConfig';
import TileFactory, { TileType } from './TileFactory';
import IJsonData, { IGroundZone, IWallZone, IPropsZone, ITileZone, ITileElemnt } from '../Data/TSceneData';
import { findIndex } from 'lodash';

import Utils from '../Utils/Utils';


export default abstract class Builder {
    rows: number;
    columns: number;
    zone: ITileZone[];
    element: ITileElemnt[][];
    scene: Phaser.Scene;
    tiles: ITile[] = [];
    debug: boolean = false;
    depthFactor: number;
    tileType: TileType;

    setData(rows: number, columns: number, zone: ITileZone[], element: ITileElemnt[][]) {
        this.scene = new GameScene;
        this.rows = rows;
        this.columns = columns;
        this.zone = zone;
        this.element = element;
    }

    store(tile: ITile): void {
        this.tiles.push(tile);
    }

    getTiles(): ITile[] {
        return this.tiles;
    }

    tileOptions(row: number, column: number, depth: number, type: TileType, element: ITileElemnt): ITileConfig {
        let x = ((column - row) * GC.tileWidth / 2) + GC.canvasWidthMiddle;
        let y = (column + row) * GC.tileHeight / 2;
        let _depth = this.depthFactor * (row + 1) + (this.depthFactor / 100) * (column + 1);
        let config: ITileConfig = {
            x: x,
            y: y,
            row: row,
            column: column,
            element: element,
            id: Math.floor(Math.random() * 10000),
            depth: _depth,
            debug: this.debug,
            tileType: this.tileType,
            empty: false,
        }
        return config;
    }

    build(): void {
        // let isEmpty = true;
        for (let row = 0; row < this.rows; row++) {
            for (let column = 0; column < this.columns; column++) {
                // isEmpty = this.zone[row][column]?false:true;
                if (this.zone[row][column]) {
                    let tileOptions = this.tileOptions(row, column, this.depthFactor, this.tileType, this.element[row][column]);
                    let t: ITile = TileFactory.create(this.tileType, tileOptions);
                    t.create();
                    t.addToScene();
                    this.store(t);
                }
            }
        }
    }

    buildOne(row: number, column: number, element: ITileElemnt): void {
        let tileOptions = this.tileOptions(row, column, this.depthFactor, this.tileType, element);
        let t: ITile = TileFactory.create(this.tileType, tileOptions);
        t.create();
        t.addToScene();
        this.store(t);
    }

    updateOne(row: number, column: number, k: string) {
        let index = this.getIndex(row, column);
        if (index != -1) {
            let tile = this.tiles[index];
            tile.image.setTexture(k);
        } else {
            throw new Error("tile id not found row:" + row + " column:" + column);
        }
    }

    removeOne(row: number, column: number) {
        let index = this.getIndex(row, column);
        if (index != -1) {
            let tile = this.tiles[index];
            tile.remove();
            this.tiles.splice(index, 1);
        }
    }

    getIndex(row: number, column: number) {
        return findIndex(this.tiles, (t: TileBase) => { return t.row == row && t.column == column });
    }

    disable() {
        this.tiles.map((tile: ITile) => {
            tile.hide();
        })
    }

    enable() {
        this.tiles.map((tile: ITile) => {
            tile.show();
        })
    }

    setDepth(depth: number) {
        this.tiles.map((tile: ITile) => {
            tile.setDepth(depth);
        })
    }

}