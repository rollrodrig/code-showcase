import IListener, { EventType } from "./IListener";
import AssetsController from '../Controllers/AssetsController';
import GameStateController from '../Controllers/GameStateController';
import TileBase from "../Tile/TileBase";
import { TileType } from "../Tile/TileFactory";
import { EStates } from "../State/EStates";
import { GameState } from "../State/GameState";
import GameScene from '../Scenes/GameScene';
import GameStorage from '../Storage/GameStorage';
import Controller from "../Controllers/Controller";
import TileController from '../Controllers/TileController';

export default class TileListener implements IListener {
    
    assetsController: AssetsController = new AssetsController;
    gameStateController: GameStateController = new GameStateController;
    tileController:TileController = new TileController;
    scene: GameScene = new GameScene;
    
    gameState:EStates;
    row:number;
    column:number;
    gameStorage = new GameStorage;

    private static instance: TileListener;
    constructor() {
        if (TileListener.instance) { return TileListener.instance;}TileListener.instance = this;
    }

    listen(eventType:EventType, tile:TileBase): void {
        console.log('listen: InterfaceListener', tile);
        this.tileController.action(tile);
    }

}
