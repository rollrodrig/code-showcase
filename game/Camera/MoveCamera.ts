import * as Phaser from 'phaser';
import {EStates} from '../State/EStates';
import GameStateController from '../Controllers/GameStateController';

class MoveCamera {
    mouseDown:boolean = false;
    mouseUp:boolean = true;
    draggin:boolean = false;
    camera:Phaser.Cameras.Scene2D.Camera;
    prevMouseX:number;
    prevMouseY:number;
    gameStateController:GameStateController;
    gameState:EStates;

    private _x: number;
    public get x(): number {
        return this._x;
    }
    public set x(value: number) {
        this._x = value;
    }

    private _y: number;
    public get y(): number {
        return this._y;
    }
    public set y(value: number) {
        this._y = value;
    }

    private _cameraMovementSpeed: number = 0.5;
    public get cameraMovementSpeed(): number {
        return this._cameraMovementSpeed;
    }
    public set cameraMovementSpeed(value: number) {
        this._cameraMovementSpeed = value;
    }

    constructor(camera:Phaser.Cameras.Scene2D.Camera){
        this.camera = camera;
        this.gameStateController = new GameStateController;
        this.listenMouseActions();
        // this.removeEventListener();
    }

    private movementX(x:number):number {
        return (x-this.prevMouseX)*this.cameraMovementSpeed;
    }

    private movementY(y:number):number {
        return (y-this.prevMouseY)*this.cameraMovementSpeed;
    }

    listenMouseActions() {
        document.addEventListener("mousedown",this.mousedown.bind(this));
        document.addEventListener("mouseup", this.mouseup.bind(this));
        document.addEventListener("mousemove", this.mousemove.bind(this));
    }
    removeEventListener() {
        document.getElementById("gamecanvas").removeEventListener("mousedown",this.mousedown);
        document.getElementById("gamecanvas").removeEventListener("mouseup", this.mouseup);
        document.getElementById("gamecanvas").removeEventListener("mousemove", this.mousemove);
    }
    mousedown(e:any) {
        if(e.target.tagName === 'CANVAS') {
            this.mouseUp = false;
            this.mouseDown = true;
        }
    }
    mouseup(e:any) {
        this.mouseUp = true;
        this.mouseDown = false;
    }
    mousemove(e:any){
        if(this.gameStateController.state === EStates.PANNING) {
            this.moveCamera(e);
        }
    }

    moveCamera(e:any) {

        if(this.mouseDown) {
            this.camera.scrollX -= this.movementX(e.clientX);
            this.camera.scrollY -= this.movementY(e.clientY);
            this.updateCameraPosition();
        }
        this.prevMouseX = e.clientX;
        this.prevMouseY = e.clientY;
    }
    updateCameraPosition(){
        this._x = this.camera.scrollX;
        this._y = this.camera.scrollY;
    }
    
}

export default MoveCamera;