import { IRectangle } from '../Utils/IRectangle';
import { GC } from '../Scenes/GameConfig';
import PositionController from './PositionController';
import TileBase, { ITileConfig } from '../Tile/TileBase';
import ITile from '../Tile/ITile';
export interface IEntityZone {
    x:number;
    y:number;
}
export interface ISortResponse {
    wall:boolean;
    row:number;
    column:number;
}
export default class EntityWallSorting {
    static sort(entity:IEntityZone, grounds:ITile[] ,wallZone:any):ISortResponse {
        let character: IRectangle = {
            x: entity.x - GC.tileWidth / 4,
            y: entity.y - GC.tileHeight / 4,
            width: GC.tileWidth / 2,
            height: GC.tileHeight / 2
        }
        let groundsOnColide: ITile[] = PositionController.getGroundsOnCollide(character, grounds);
        let closestTile:ITile = PositionController.getClosestTile(character, groundsOnColide);
        let response:ISortResponse = {wall:false, row:0, column:0}
        if (closestTile != undefined) {
            if (wallZone[closestTile.row][closestTile.column] === 1) {
                response.wall = true;
            }else {
                response.wall = false;
                response.row = closestTile.row;
                response.column = closestTile.column;
            }
        }
        return response;
    }
}