import Controller from "./Controller";
import TileEngine from '../Tile/TileEngine';
import TileBase, { ITileConfig } from '../Tile/TileBase';
import ITile from '../Tile/ITile';
import GameStateController from './GameStateController';
import { TileType } from "../Tile/TileFactory";
import TSceneData, {IGroundZone, IGround, IWallZone, IWall, IPropsZone, IProps, IResources } from '../Data/TSceneData';
import GameStorage from '../Storage/GameStorage';
import { EStates } from "../State/EStates";
import { EGameBridgeEvent } from "../Bridge/EGameBridgeEvent";
import Bridge from '../Bridge/Bridge';
import * as _ from 'lodash';
import { TGameBridgeTile } from "../Bridge/TGameBridgeTile";
import Utils from '../Utils/Utils';

export interface  TDataToInterface {
    row:number 
    column:number 
    type: TileType
    id:number
    action: EStates
    info:{
        k:string
    }
}

export interface TSelectTile {
    row:number 
    column:number 
    type: TileType
    id:number
    action: EStates
    info:{
        k:string
    } 
}

export default class TileController extends Controller {
    private static instance: TileController;
    tileEngine:TileEngine;
    // gameStateController = new GameStateController;
    gameStorage = new GameStorage;
    sceneData:TSceneData;
    gridEnabled:boolean = false;

    constructor() {
        super();
		if (TileController.instance) {return TileController.instance;}
        TileController.instance = this;
        this.sceneData = this.gameStorage.getMap();

    }

    init():void{
        this.tileEngine = new TileEngine;
    }
    build() {
        console.log('Buildng tiles...');
        this.tileEngine.build();
    }
    
    getGroundTiles():ITile[] {
        return this.tileEngine.getGroundTiles();
    }
    getWallTiles():ITile[] {
        return this.tileEngine.getWallTiles();
    }
    getPropsTiles():ITile[] {
        return this.tileEngine.getPropsTiles();
    }

    onDragStart() {
        console.log('onDragStart()...');
        this.tileEngine.onDragStart();
    }
    onDrag() {
        console.log('onDrag()...');
    }
    onDragEnd() {
        console.log('onDragEnd()...');
        this.tileEngine.onDragEnd();
    }
    onDragEnter() {
        console.log('onDragEnter()...');
    }
    onDragLeave() {
        console.log('onDragLeave()...');
    }
    onDrop() {
        console.log('onDrop()...');
        this.tileEngine.onDrop();
    }

    action(tile:TileBase) {
        console.log("action ", tile);
        let gameState: EStates = this.gameStorage.get('gamestate');
        let row = tile.row;
        let column = tile.column;
        switch(gameState) {
            case EStates.PANNING:
                // this.actionOnGround(row, column);
                let tileSelected:TSelectTile = {
                    row: tile.row,
                    column: tile.column,
                    type: tile.tileType,
                    id: tile.id,
                    action: gameState,
                    info:{k: tile.getImageKey()}
                }
                Bridge.selectTile(tileSelected)
            break;
            case EStates.GROUNDING:
                this.actionOnGround(row, column);
            break;
            case EStates.DELETING_GROUND:
                this.actionDeleteGround(row, column);
            break;
            case EStates.WALLING:
                this.actionOnWall(row, column);
            break;
            case EStates.DELETING_WALL:
                this.actionDeleteWall(row, column);
            break;
        }
        

    }

    searchForTile() {

    }

    actionOnGround(row:number, column:number) {
        let groundZone:IGroundZone[] = this.gameStorage.groundZone();
        let newTileKey: IGround = this.gameStorage.getNewTileData();
        // exist tile
        if(groundZone[row][column]) {
            this.tileEngine.updateGround(row, column,newTileKey);
        // add new tile
        }else {
            this.tileEngine.addGround(row, column, newTileKey);
            groundZone[row][column] = 1;
            this.gameStorage.groundZoneUpdate(groundZone);
        }
        let ground:IGround[][] = this.gameStorage.ground();
        ground[row][column] = newTileKey;
        this.gameStorage.groundUpdate(ground);
    }

    actionDeleteGround(row:number, column:number) {
        let groundZone:IGroundZone[] = this.gameStorage.groundZone();
        let ground:IGround[][] = this.gameStorage.ground();
        if(groundZone[row][column]) {
            this.tileEngine.removeGround(row, column);
            groundZone[row][column] = 0;
            this.gameStorage.groundZoneUpdate(groundZone);
            ground[row][column] = {k:null}
            this.gameStorage.groundUpdate(ground);
        }
    }

    actionOnWall(row:number, column:number) {
        let wallZone:IWallZone[] = this.gameStorage.wallZone();
        let newTileKey: IWall = this.gameStorage.getNewTileData();
        if(wallZone[row][column]) {
            this.tileEngine.updateWall(row, column, newTileKey);
        }else {
            this.tileEngine.addWall(row, column, newTileKey);
            wallZone[row][column] = 1;
            this.gameStorage.wallZoneUpdate(wallZone);
        }
        let wall:IWall[][] = this.gameStorage.wall();
        wall[row][column] = newTileKey;
        this.gameStorage.wallUpdate(wall);
    }

    actionDeleteWall(row:number, column:number) {
        let wallZone:IWallZone[] = this.gameStorage.wallZone();
        let wall:IWall[][] = this.gameStorage.wall();
        if(wallZone[row][column]) {
            this.tileEngine.removeWall(row, column);
            wallZone[row][column] = 0;
            this.gameStorage.wallZoneUpdate(wallZone);
            wall[row][column] = {k:null}
            this.gameStorage.wallUpdate(wall);
        }
    }

    addKeyToResources(sprite:TGameBridgeTile) {
        let resources:IResources[] = this.gameStorage.getResources();
        Utils.log(resources);
        let found =  _.findIndex(resources,(resource:IResources) => resource.k === sprite.key)
        if(found === -1) {
            resources.push({k:sprite.key, i: sprite.path});
            Utils.log(resources);
            this.gameStorage.setResources(resources);
        }
    }

    removeKeyFromResources(key:string) {

    }

    disableGrid() {
        if(this.gridEnabled) {
            this.tileEngine.disableGrid();
            this.gridEnabled = false;
        }
    }
    enableGrid() {
        if(this.gridEnabled === false)  {
            this.tileEngine.enableGrid();
            this.gridEnabled = true;
        }
    }
    setGridOnTop() {
        this.tileEngine.setGridOnTop();
    }
    setGridOnMid() {
        this.tileEngine.setGridOnMid();
    }


    addTile(tile:TileBase){
        console.log("adding tile", tile);
        
    }

    updateTile(tile:TileBase){
        console.log("updateTile tile", tile);
        
    }

    removeTile(tile:TileBase){
        console.log("remove tile", tile);
        
    }
}