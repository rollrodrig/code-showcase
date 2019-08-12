import * as Phaser from 'phaser';
import TileBase, { ITileConfig } from './TileBase';
import {GC} from '../Scenes/GameConfig';
export default class Grid extends TileBase {
    createSprite():void {
        this.image = new Phaser.GameObjects.Image(this.scene,0, -GC.tileHeightMidle, 'grid-image-helper');
        this.image.setName('grid-image-helper');
        // moving the origin to x = 0.5, y = 0
        this.image.displayOriginY = 0;
        
    }
}
export { ITileConfig as IGrid }

