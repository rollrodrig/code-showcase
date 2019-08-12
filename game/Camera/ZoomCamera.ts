import * as Phaser from 'phaser';
import {EStates} from '../State/EStates';
import GameStateController from '../Controllers/GameStateController';
export default class ZoomCamera {
    private camera:Phaser.Cameras.Scene2D.Camera;
    private zoomFactor:number = 0.1;
    private zoomDelta:number;
    private onCanvas:boolean;
    gameStateController:GameStateController;
    constructor(camera:Phaser.Cameras.Scene2D.Camera) {
        this.camera = camera;
        this.gameStateController = new GameStateController;
        this.listenMouseScroll();
    }

    listenMouseScroll() {
        document.addEventListener("mousemove", this.mousemove.bind(this));
        document.addEventListener("wheel", this.wheel.bind(this));
    }
    mousemove(e:any) {
        if(e.clientX<900 && e.clientY < 600) {
            this.onCanvas = true;
        }else {
            this.onCanvas = false;
        }
    }
    wheel(e:any) {
        if(this.onCanvas) {
            if(this.gameStateController.state === EStates.PANNING) {
                this.zoom(e.wheelDeltaY);
            }
        }
    }
    zoom(delta:number){
        if(delta<0) {
            this.zoomDelta = 1;
        }else {
            this.zoomDelta = -1;
        }
        this.camera.zoom += this.zoomDelta*this.zoomFactor;
    }

}