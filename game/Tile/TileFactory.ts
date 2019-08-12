import TileBase, { ITileConfig} from './TileBase';
import Ground, {IGroundConfig} from '../Tile/Ground';
import Wall, {IWallConfig} from '../Tile/Wall';
import Props, {IPropsConfig} from '../Tile/Props';
import ITile from './ITile';

import TileBoxDecorator from './TileBoxDecorator';
import IsometricBoxDecorator from './IsometricBoxDecorator';
import GroundHoverInteractiveDecorator from './GroundHoverInterctiveDecorator';
import WallInteractiveDecorator from './WallInterctiveDecorator';
import PropInterctiveDecorator from './PropInterctiveDecorator';
import GridInterctiveDecorator from './GridInterctiveDecorator';
import InterctiveDecorator from './InterctiveDecorator';
import TilePointerUpDecorator from './TilePointerUpDecorator';
import GroundStandAreaDecorator from './GroundStandAreaDecorator';
import Grid from './Grid';

import TileDecorator from './TileDecorator';
import HoverInteractiveDecorator from './HoverInterctiveDecorator';

export enum TileType {
    Ground = 'ground',
    Wall = 'wall',
    Props = 'props',
    Grid = 'grid',
}

class TileInteractivityCommand {

    controlled: TileDecorator;
    constructor(controlled: TileDecorator) {
        this.controlled = controlled;
    }

    disableInteractive() {
        this.controlled.disableInteractive();
    }
    
    enableInteractive(){
        this.controlled.enableInteractive();
    }
}

export default class TileFactory {

    static create(type:TileType, config:ITileConfig):ITile {
        let tile:ITile;
        switch(type) {
            case TileType.Ground:
                tile = new Ground(config);
                tile = new TileBoxDecorator(tile);
                tile = new IsometricBoxDecorator(tile);
                tile = new GroundHoverInteractiveDecorator(tile);
                tile = new TilePointerUpDecorator(tile);
                tile = new GroundStandAreaDecorator(tile);
            break;
            case TileType.Wall:
                tile = new Wall(config);
                tile = new IsometricBoxDecorator(tile);
                tile = new WallInteractiveDecorator(tile);
                tile = new TilePointerUpDecorator(tile);
                break;
            case TileType.Props:
                tile = new Props(config);
                tile = new TileBoxDecorator(tile);
                tile = new IsometricBoxDecorator(tile);
                tile = new PropInterctiveDecorator(tile);
                tile = new TilePointerUpDecorator(tile);
            break;
            case TileType.Grid:
                tile = new Grid(config);
                tile = new TileBoxDecorator(tile);
                tile = new IsometricBoxDecorator(tile);
                tile = new InterctiveDecorator(tile);
                tile = new HoverInteractiveDecorator(tile);
                tile = new TilePointerUpDecorator(tile);
            break;
        }
        return tile;
    }
}