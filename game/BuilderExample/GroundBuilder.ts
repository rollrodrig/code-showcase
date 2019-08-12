
import Builder from './Builder';
import {TileType} from './TileFactory';
export default class GroundBuilder extends Builder {
    private static instance: GroundBuilder;
    constructor() {
        super();
        if (GroundBuilder.instance) { return GroundBuilder.instance; } GroundBuilder.instance = this;
        this.depthFactor = 100;
        this.tileType = TileType.Ground;
    }
}