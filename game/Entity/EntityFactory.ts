import Entity from './Entity';
import Hero from './Hero';
export enum EntityType {
    Hero,
    Enemy,
}
export default class EntityFactory {
    create(type:EntityType):Entity {
        let entity:Entity;
        switch(type) {
            case EntityType.Hero:
                entity = new Hero;
            break;
            case EntityType.Enemy:

            break;
        }
        return entity;
    }
}