import * as Phaser from 'phaser';
import MoveCamera from './MoveCamera';
import ZoomCamera from './ZoomCamera';
import GameScene from '../Scenes/GameScene';
export default class Camera {
    scene:GameScene;
    private camera:Phaser.Cameras.Scene2D.Camera;
    private moveCamera:MoveCamera;
    private zoomCamera:ZoomCamera;
    constructor() {
        this.scene = new GameScene;
        this.camera = this.scene.cameras.main;
        this.moveCamera = new MoveCamera(this.camera);
        this.zoomCamera = new ZoomCamera(this.scene.cameras.main);
    }
    setBgColor(r:number,g:number,b:number) {
		this.camera.backgroundColor.setTo(r,g,b);
    }
    
    getCamera():Phaser.Cameras.Scene2D.Camera {
        return this.camera;
    }

    setCamera(camera:Phaser.Cameras.Scene2D.Camera):void {
        this.camera = camera;
    }
}