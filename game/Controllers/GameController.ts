import EntityController from './EntityController';
import CameraController from './CameraController';
import TileController from './TileController';
import AssetsController from './AssetsController';
import GameStateController from './GameStateController';
import ToolController from './ToolController';
import Assets from '../Assets/Assets';
import ServerAssets from '../Assets/ServerAssets';
import DummyAssets from '../Assets/DummyAssets';
import LoaderEngine from '../Assets/LoaderEngine';
import GameScene from '../Scenes/GameScene';
import Controller from './Controller';
import { IHero } from '../Entity/Hero';
import ETools from '../Tool/ETool';
import GameStorage from '../Storage/GameStorage';
import { TGameBridgeTile } from "../Bridge/TGameBridgeTile";
import { TGameBridgeData } from "../Bridge/TGameBridgeData";
import { EGameBridgeEvent } from "../Bridge/EGameBridgeEvent";
import { EStates } from '../State/EStates';
import LoadingScene from '../Scenes/LoadingScene';
import TSceneData from '../Data/TSceneData';
import Bridge from '../Bridge/Bridge';

export default class GameController extends Controller {
    entityController:EntityController;
    cameraController:CameraController;
    tileController:TileController
    assetsController:AssetsController;
    gameStateController:GameStateController;
    toolController:ToolController;
    gameStorage:GameStorage
    loadingScene = new LoadingScene;
    private static instance: GameController;
    constructor() {
        super();
        if (GameController.instance) { return GameController.instance; } GameController.instance = this;
    }


    init():void {
        console.log("GameController init");
        
        this.gameStorage = new GameStorage;

        this.assetsController = new AssetsController; 
        this.assetsController.init();
        
        this.gameStateController = new GameStateController; // by default start with mapstate
        this.gameStateController.init();
        // this.gameStateController.setMapState();
        // this.gameStateController.setEntityState();

        this.cameraController = new CameraController;
        this.cameraController.init();

        this.tileController = new TileController;
        this.tileController.init();

        this.entityController = new EntityController;
        this.entityController.init();

        this.toolController = new ToolController;
        this.toolController.init();
        
        this.setTool(ETools.SELECT);

        // this.start();
    }

    setTool(tool:ETools) {
        this.toolController.setTool(tool);
        this.gameStorage.add('tool',tool);
        this.generateStateFromTool(tool)
    }

    private generateStateFromTool(tool:ETools) {
        let gameState: EStates;
        switch(tool) {
            case ETools.SELECT:
                gameState = EStates.PANNING;
                break;
            case ETools.GROUND:
                gameState = EStates.GROUNDING;
                break;
            case ETools.WALL:
                gameState = EStates.WALLING;
            break;
            case ETools.ERASER_GROUND:
                gameState = EStates.DELETING_GROUND;
            break;
            case ETools.ERASER_WALL:
                gameState = EStates.DELETING_WALL;
            break;
        }  
        this.setGameState(gameState);
    }

    setGameState(gameState:EStates) {
        this.gameStateController.setState(gameState);
        this.gameStorage.add('gamestate',gameState);
        this.updateGrid();
    }

    getGameState() {
        return this.gameStateController.getState();
    }

    private updateGrid() {
        let state:EStates = this.gameStateController.getState();
        state == EStates.PANNING? this.tileController.disableGrid():this.tileController.enableGrid();
        switch(state){
            case EStates.PANNING:
                break;
            case EStates.GROUNDING:
                this.tileController.setGridOnTop();
                break;
            case EStates.DELETING_GROUND:
                this.tileController.setGridOnTop();
                break;
            case EStates.WALLING:
                this.tileController.setGridOnMid();
                break;
            case EStates.DELETING_WALL:
                this.tileController.setGridOnMid();
            break;
        }
    }

    loadOneImage(sprite:TGameBridgeTile) {
        this.assetsController.loadOneImage(sprite);
        this.gameStorage.newTile(sprite.key);
        this.tileController.addKeyToResources(sprite);
    }
    
    start() {
        this.tileController.build();
    }
    eventFromInterface(data:TGameBridgeData) {
        switch(data.event) {
            case EGameBridgeEvent.GAME_SCENE_TILE_MAP:
                this.loadingScene.setJsonData(data.payload.map);
                this.loadingScene.loadImages();
            break;
            case EGameBridgeEvent.SELECT_TOOL:
                this.setTool(data.payload.tool);
            break;
            case EGameBridgeEvent.NEW_TILE:
                let sprite:TGameBridgeTile = {
                    path: data.payload.sprite.fn,
                    key: data.payload.sprite.fid,
                }
                //TODO, should implement callback
                this.loadOneImage(sprite);

            break;
            case EGameBridgeEvent.SAVE_SCENE_MAP:
                let sceneData:TSceneData = this.gameStorage.getMap();
                this.saveSceneMap(sceneData)
            break;
            
        }
    }
    saveSceneMap(sceneData:TSceneData) {
        Bridge.saveSceneMap(sceneData);
    }
}