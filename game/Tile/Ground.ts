import * as Phaser from 'phaser';
import TileBase, { ITileConfig } from './TileBase';
import {GC} from '../Scenes/GameConfig';
import Visualizator from '../Utils/Visualizator';

export default class Ground extends TileBase {
    createSprite():void {
        this.image = new Phaser.GameObjects.Image(this.scene,0, -GC.tileHeightMidle, this.imageKey);
        this.image.setName('ground_image');
        this.image.displayOriginY = 0;
    }
}
export { ITileConfig as IGroundConfig };   