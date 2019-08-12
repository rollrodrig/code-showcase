
export default interface ITile {
    scene: Phaser.Scene;
    container: Phaser.GameObjects.Container;
    image: Phaser.GameObjects.Image;
    id: number;
    x:number;
    y:number;
    row:number;
    column:number;
    width:number;
    height:number;
    getTile():ITile;
    create():void;
    addToScene():void;
    remove():void;
    getImageKey():string;
    show():void;
    hide():void;
    setDepth(depth:number):void;
    
}