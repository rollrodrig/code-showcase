import GameScene from '../Scenes/GameScene';

export default abstract class Controller {
    scene:GameScene;
    constructor() {
        this.scene = new GameScene;
    }
    abstract init():void;
}