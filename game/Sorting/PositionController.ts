import TileBase from '../Tile/TileBase';
import { GC } from '../Scenes/GameConfig';
import Entity from '../Entity/Entity';
import { IRectangle } from '../Utils/IRectangle';
import Collider from '../Utils/Collider';
import Utils from '../Utils/Utils';
import ITile from '../Tile/ITile';
export default class PositionController {
    tiles:TileBase[] = []
    constructor() {

    }
    // return all tiles that the character have contact
    static getGroundsOnCollide(entity:IRectangle,grounds:ITile[]): ITile[] {
        let l:number = grounds.length;
        let groundsOnCollide:ITile[] = [];
        for(let i = 0; i < l; i++) {
            let currGround:ITile = grounds[i];
            let ground:IRectangle = {
                x: currGround.x - GC.tileWidth/4,
                y: currGround.y - GC.tileHeight/4,
                width: GC.tileWidth/2,
                height: GC.tileHeight/2
            }
            if(Collider.rectIntersect(entity,ground)) {
                groundsOnCollide.push(currGround);
            }
        }
        return groundsOnCollide;
    }

    static getClosestTile(entity:IRectangle,tiles:ITile[]):ITile {
        let l = tiles.length;
        let distances:number[] = [];
        let tile:ITile;
        if(l>0) {
            for(let i = 0; i < l; i++) {
                let tile = tiles[i];
                let obja = {x:entity.x, y:entity.y};
                let objb = {x:tile.x - GC.tileWidth/4 , y:tile.y - GC.tileHeight/4};
                distances.push(Utils.distBetweenTwoObjs(obja,objb));
            }
            distances.push(100000); 
            if(distances[1]>=distances[0]) {
                tile = tiles[0];
            }else {
                tile = tiles[1];
            }
        }
        return tile;
    }

}