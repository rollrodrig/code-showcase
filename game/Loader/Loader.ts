
import * as Phaser from 'phaser';
import TilesData from '../Data/TilesData';
import Request from './Request';
import GameScene from '../Scenes/GameScene';
export default class Loader {
    scene:Phaser.Scene;
    resources:{image:string, key:string}[];
    request:Request;
    constructor() {
        this.scene = new GameScene;
        this.resources = TilesData.resources;
        this.request = new Request;
    }

    staticLoadAssets(data:any) {
        this.loadAssets(data.resources);
    }
    private loadAssets(resources:{image:string, key:string}[]) {
        this.resources = resources;
        let l = this.resources.length;
        for(let i = 0; i < l; i++) {
            let res:{key:string, image:string;} = this.resources[i];
            this.scene.load.image(res.key, res.image);
        }
        this.scene.load.start();
    }
    
}
    