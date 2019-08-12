import * as Phaser from 'phaser';
import Entity  from './Entity';
import {IEntt} from './IEntity';
export default class Hero extends Entity {
    constructor(){
        super();
    }
}
export { IEntt as IHero};