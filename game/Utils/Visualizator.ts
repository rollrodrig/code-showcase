
import * as Phaser from 'phaser';

export default class Visualizator {
    static rectangle(scene:Phaser.Scene, x:number, y:number, w:number, h:number) {
        let rectangle:Phaser.Geom.Rectangle = new Phaser.Geom.Rectangle(x,y,w,h);
		let graphics:Phaser.GameObjects.Graphics = new Phaser.GameObjects.Graphics(scene,{ lineStyle: { width: 1, color: 0x0094ff }, fillStyle:{color:0x0094ff} })
            graphics.strokeRectShape(rectangle);
            scene.add.existing(graphics);
    }
}