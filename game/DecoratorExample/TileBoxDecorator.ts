import * as Phaser from 'phaser';
import TileDecorator from './TileDecorator';
import { GC } from '../Scenes/GameConfig';

namespace Tile {
    export class TileBoxDecorator extends TileDecorator {
        implementDecorator() {
            let ropts:any = {
                x: -GC.tileWidthMiddle,
                y: -GC.tileHeightMidle,
                w: GC.tileWidth,
                h: GC.tileHeight
            }
            let rectangle = new Phaser.Geom.Rectangle(ropts.x,ropts.y,ropts.w,ropts.h);
            let graphics = new Phaser.GameObjects.Graphics(this.tile.scene,{ lineStyle: { width: 1, color: 0xae00ff } })
                graphics.strokeRectShape(rectangle);
                this.tile.container.add(graphics);

            // let t = new Phaser.GameObjects.Text(this.scene,0,0,this.row+' '+this.column,{});
            // this.container.add(t);
        }
    }
}
export default Tile.TileBoxDecorator;