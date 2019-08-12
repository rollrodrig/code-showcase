import EntityDecorator from "./EntityDecorator";
import IEntity, { IEntt } from "./IEntity";
import { GC } from '../Scenes/GameConfig';
export default class TileBoxDecorator extends EntityDecorator {
    constructor(entity:IEntity) {
        super(entity)
    }
    create():void{
        this.entity.create();
        this.implementDecorator();
    }
    implementDecorator(): void {
        let ropts: any = {
            x: -GC.tileWidth / 2,
            y: -GC.tileHeight / 2,
            w: GC.tileWidth,
            h: GC.tileHeight
        }
        let rectangle = new Phaser.Geom.Rectangle(ropts.x, ropts.y, ropts.w, ropts.h);
        let graphics = new Phaser.GameObjects.Graphics(this.entity.scene, { lineStyle: { width: 1, color: 0xff0087 } })
        graphics.strokeRectShape(rectangle);
        this.entity.container.add(graphics);
    }
}