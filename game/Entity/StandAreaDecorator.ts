import EntityDecorator from "./EntityDecorator";
import { GC } from "../Scenes/GameConfig";
export default class StandAreaDecorator extends EntityDecorator {
    implementDecorator(): void {
        console.log('Implement StandAreaDecorator');
        let ropts: any = {
            x: -GC.tileWidth / 4,
            y: -GC.tileHeight / 4,
            w: GC.tileWidth / 2,
            h: GC.tileHeight / 2
        }
        let rectangle = new Phaser.Geom.Rectangle(ropts.x, ropts.y, ropts.w, ropts.h);
        let graphics = new Phaser.GameObjects.Graphics(this.entity.scene, { lineStyle: { width: 1, color: 0xbbff00 } })
        graphics.strokeRectShape(rectangle);
        this.entity.container.add(graphics);
    }
}