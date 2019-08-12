import * as Phaser from 'phaser';
export default class Floor {
    scene:Phaser.Scene;
	isoWidth = 200;
    isoHeight = 100;
    imageFloorKey:string = 'floor';
    constructor(scene:Phaser.Scene) {
        this.scene = scene;
    }
    create() {
        var graphics = this.scene.add.graphics({ fillStyle: { color: 0xff0000 } });
        var floorTileAreaPoints = [
            new Phaser.Geom.Point(0, -50),
            new Phaser.Geom.Point(100, 0),
            new Phaser.Geom.Point(0, 50),
            new Phaser.Geom.Point(-100, 0)
        ];
        var floorTileHitArea = new Phaser.Geom.Polygon(floorTileAreaPoints);
        let floor = this.scene.add.image(0, 0, this.imageFloorKey)
        var container = this.scene.add.container(400, 300)
        container.add([floor]);
        container.setInteractive(floorTileHitArea, Phaser.Geom.Polygon.Contains);
        container.on('pointerover', function () {
            floor.setTint(0x44ff44);
        });
        container.on('pointerout', function () {
            floor.clearTint();
        });
        container.once('pointerup', function () {
            floor.destroy();
        });
    }
	drawFloorTiles(x:number,y:number) {
        this.scene.add.image(((x-y)*this.isoWidth/2)+450, (x+y)*this.isoHeight/2, this.imageFloorKey)
            .setInteractive();
    }
	drawTiles(x:number,y:number) {
		this.scene.add.isotriangle(((x-y)*this.isoWidth/2)+450 , (x+y)*this.isoHeight/2 ,this.isoWidth, this.isoHeight)
		.setInteractive({ cursor: 'pointer' });
    }
}