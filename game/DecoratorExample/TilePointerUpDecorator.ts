import * as Phaser from 'phaser';
import TileDecorator from './TileDecorator';
import TilePointerUp from '../Dispatcher/TilePointerUp';
import TilePointerUpListener from '../Listener/TilePointerUpListener'; // Este listener no tiene mucho sentido
import InterfaceListener from '../Listener/InterfaceListener';
import { EventType } from '../Listener/IListener';

import ITile from './ITile';

import { GC } from '../Scenes/GameConfig';
import AssetsController from '../Controllers/AssetsController';
import TileListener from '../Listener/TileListener';

namespace Tile {
    export class TilePointerUpDecorator extends TileDecorator {
        tilePointerUp:TilePointerUp;
        assetsController = new AssetsController;
        
        constructor(tile: ITile) {
            super(tile);
            this.tilePointerUp = new TilePointerUp;
            this.tilePointerUp.add(new TileListener);
        }

        implementDecorator() {
            this.tile.image.on('pointerdown', (pointer:Phaser.Input.Pointer) => {
            });
            this.tile.image.on('pointerup', (pointer:Phaser.Input.Pointer) => {
                this.tilePointerUp.notify(EventType.pointerup, this.tile.getTile());
            })
        }
    }
}
export default Tile.TilePointerUpDecorator;