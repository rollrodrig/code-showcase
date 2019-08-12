import * as Phaser from 'phaser';
import TileDecorator from './TileDecorator';
import { GC } from '../Scenes/GameConfig';
namespace Tile {
    export class IsometricBoxDecorator extends TileDecorator {
        implementDecorator() {
            let points = [
                new Phaser.Geom.Point(50, 0),
                new Phaser.Geom.Point(100, 25),
                new Phaser.Geom.Point(50, 50),
                new Phaser.Geom.Point(0, 25)
            ];
            var polygon = new Phaser.Geom.Polygon(points);
            let graphics:Phaser.GameObjects.Graphics = new Phaser.GameObjects.Graphics(this.tile.scene,{ lineStyle: { width: 1, color: 0x0094ff }, fillStyle:{color:0x0094ff} })
            graphics.setName('isometric_helper');
            graphics.strokePoints(polygon.points,true);
            graphics.x = -GC.tileWidth/2;
            graphics.y = -GC.tileHeight/2;
                // isometricGraphic.setActive(false);
            this.tile.container.add(graphics);                
        }
    }
}
export default Tile.IsometricBoxDecorator;