import * as Phaser from 'phaser';
import TileDecorator from './TileDecorator';
import { GC } from '../Scenes/GameConfig';
namespace Tile {
    export class HoverInteractiveDecorator extends TileDecorator {
        implementDecorator() {
            this.tile.image.on('pointerover', (pointer:Phaser.Input.Pointer) => {
                this.tile.image.setTint(0x00ff37);
            });
            this.tile.image.on('pointerout', (pointer:Phaser.Input.Pointer) => {
                this.tile.image.clearTint();
            })
        }
    }
}
export default Tile.HoverInteractiveDecorator;