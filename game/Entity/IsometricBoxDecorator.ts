import EntityDecorator from "./EntityDecorator";
import { IEntt } from "./IEntity";
export default class IsometricBoxDecorator extends EntityDecorator {
    create():void{
        this.entity.create();
        this.implementDecorator();
    }
    implementDecorator(): void {
        console.log('Implement IsometricBoxDecorator');
    }
}