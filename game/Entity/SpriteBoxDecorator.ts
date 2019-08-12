
import * as Phaser from 'phaser';
import EntityDecorator from "./EntityDecorator";
import IEntity, { IEntt } from "./IEntity";
import { GC } from '../Scenes/GameConfig';
export default class SpriteBoxDecorator extends EntityDecorator {
    create():void {
        this.entity.create();
        this.implementDecorator();
    }
    implementDecorator(): void {
        let ropts: any = {
            x: -GC.tileWidth / 2,
            y: -(this.entity.image.height - GC.tileHeight / 2),
            w: this.entity.image.width,
            h: this.entity.image.height
        }
        let rectangle = new Phaser.Geom.Rectangle(ropts.x, ropts.y, ropts.w, ropts.h);
        let graphics = new Phaser.GameObjects.Graphics(this.entity.scene, { lineStyle: { width: 1, color: 0x10ff00 } })
        graphics.strokeRectShape(rectangle);
        this.entity.container.add(graphics);
    }
}