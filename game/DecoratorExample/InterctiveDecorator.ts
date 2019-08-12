import * as Phaser from 'phaser';
import TileDecorator from './TileDecorator';
import { GC } from '../Scenes/GameConfig';
namespace Tile {
    export class InteractiveDecorator extends TileDecorator {
        implementDecorator() {
            let points = [
                new Phaser.Geom.Point(50, 0),
                new Phaser.Geom.Point(100, 25),
                new Phaser.Geom.Point(50, 50),
                new Phaser.Geom.Point(0, 25)
            ];
            var polygon = new Phaser.Geom.Polygon(points);
            this.tile.image.setInteractive(polygon, Phaser.Geom.Polygon.Contains);
        }
    }
}
export default Tile.InteractiveDecorator;