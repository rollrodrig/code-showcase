import * as Phaser from 'phaser';
import Hero, { IHero } from '../Entity/Hero';
import Entity from '../Entity/Entity';
import GameScene from '../Scenes/GameScene';
import EntityFactory, { EntityType } from '../Entity/EntityFactory';
import Controller from './Controller';
import TileBoxDecorator from '../Entity/TileBoxDecorator';
import IsometricBoxDecorator from '../Entity/IsometricBoxDecorator';
import SpriteBoxDecorator from '../Entity/SpriteBoxDecorator';
import StandAreaDecorator from '../Entity/StandAreaDecorator';
import EntityInteractiveDecorator from '../Entity/EntityInteractiveDecorator';
import IEntity, { IEntt } from '../Entity/IEntity';
import EntityUtils from '../Utils/EntityUtils';
import EntityWallSorting, {IEntityZone, ISortResponse} from '../Sorting/EntityWallSorting';
import TileController from './TileController';
import TileBase, { ITileConfig } from '../Tile/TileBase';
import ITile from '../Tile/ITile';
import GameStorage from '../Storage/GameStorage';
export default class EntityController extends Controller {
    private static instance: EntityController;
    entities: IEntity[] = [];
    boxHelper: boolean = false;
    groundHelper: boolean = false;
    entityFactory: EntityFactory;
    tileController: TileController;
    gameStorage = new GameStorage;
    constructor() {
        super();
        if (EntityController.instance) { return EntityController.instance; }
        EntityController.instance = this;
        this.entityFactory = new EntityFactory;
        this.tileController = new TileController;
        console.log('EntityController ready.......');
    }

    init(): void {
    }
    addHero(config: IHero) {
        console.log('addHero');
        let h: IEntity = this.entityFactory.create(EntityType.Hero);
        h = new EntityInteractiveDecorator(h);
        if (this.boxHelper) {
            h = new SpriteBoxDecorator(h);
            h = new TileBoxDecorator(h);
            h = new IsometricBoxDecorator(h);
            h = new StandAreaDecorator(h);
        }
        h.setConfig(config);
        h.create();
        h.addToScene();
        this.push(h);
    }

    addEnemy() {

    }

    removeHero() {

    }

    removeEnemy() {

    }

    push(entity: IEntity) {
        this.entities.push(entity);
    }

    getEntities() {
        return this.entities;
    }

    onDragStart(data:{entity:IEntity}) {
        data.entity.setTint();
    }
    onDrag(data:{entity:IEntity,x:number, y:number}) {
        data.entity.setX(data.x);
        data.entity.setY(data.y);
    }
    onDragEnd(data:{entity:IEntity}) {
        console.log('onDragEnd()... start eval wall sorting');
        this.onEntityMovementEnd(data.entity);
    }
    onDragEnter() {
        console.log('onDragEnter()...');
    }
    onDragLeave() {
        console.log('onDragLeave()...');
    }
    onDrop() {
    }
    onEntityMovementEnd(entity:IEntity) {
        entity.clearTint()
        let entityZone: IEntityZone = EntityUtils.getEntityXY(entity);
        let groundTiles:ITile[] = this.tileController.getGroundTiles();
        let jsondata = this.gameStorage.get('map');
        let response:ISortResponse = EntityWallSorting.sort(entityZone, groundTiles, jsondata.wallZone );
        if(response.wall) {
            entity.resetPosition();
        }else {
            entity.setRow(response.row);
            entity.setColumn(response.column);
            entity.autoSetDepth();
        }
    }
}