import IEntity, { IEntt } from '../Entity/IEntity';
import {IEntityZone} from '../Sorting/EntityWallSorting';
export default class EntityUtils {
    static getCurrentEntity(data:{entityId:number}, entities:IEntity[]):IEntity {
        let l = entities.length;
        let currentEntity:IEntity;
        for (let index = 0; index < l; index++) {
            currentEntity = entities[index];
            if(data.entityId === currentEntity.id) {
                break;
            }
        }
        return currentEntity;
    }
    static getEntityXY(currentEntity:IEntity):IEntityZone {
        return { x: currentEntity.getX(), y: currentEntity.getY()};
    }
}