import { IGroundConfig } from './Ground';
import { IWallConfig } from './Wall';
import { IPropsConfig } from './Props';
export default interface ITileEngine {
    columns:number;
    rows:number;
    ground:IGroundConfig[][];
    groundZone:number[][],
    wall:IWallConfig;
    wallZone:number[][];
    props:IPropsConfig;
    propsZone:number[][];
    resource:IResources[];
}
export interface IResources {
    image:string;
    key:string;
}
