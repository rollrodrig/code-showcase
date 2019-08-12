import IListener, { EventType } from "./IListener";
import { EGameBridgeEvent } from "../Bridge/EGameBridgeEvent";
import { TileType } from "../Tile/TileFactory";
import TileBase from "../Tile/TileBase";


export default class InterfaceListener implements IListener {
    listen(eventType:EventType, tile:TileBase): void {
        console.log(tile);
        let data:{event:EGameBridgeEvent, data:{column:number, row:number, type:TileType }} = {
            event: EGameBridgeEvent.TILE_UPDATED,
            data: {
                column: tile.column,
                row: tile.row,
                type: tile.tileType,
            }
        }
    }
}
