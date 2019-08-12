import * as Phaser from 'phaser';
import TileDecorator from './TileDecorator';
import { GC } from '../Scenes/GameConfig';
namespace Tile {
    export class GroundStandAreaDecorator extends TileDecorator {
        implementDecorator() {
            let ropts:any = {
                x: -GC.tileWidth/4,
                y: -GC.tileHeight/4,
                w: GC.tileWidth/2,
                h: GC.tileHeight/2
            }
            let rectangle = new Phaser.Geom.Rectangle(ropts.x,ropts.y,ropts.w,ropts.h);
            let graphics = new Phaser.GameObjects.Graphics(this.tile.scene,{ lineStyle: { width: 1, color: 0x0094ff }, fillStyle:{color:0x0094ff} })
                graphics.strokeRectShape(rectangle);
                graphics.fillRectShape(rectangle);
                this.tile.container.add(graphics);           
        }
    }
}
export default Tile.GroundStandAreaDecorator;