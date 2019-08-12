import TSceneData, { IGroundZone, IGround, IWallZone, IWall, IPropsZone, IProps, IResources } from "../Data/TSceneData";

class GameStorage {
    mapKey:string = 'map';
    bag:{[key:string]:any} = {}
    private static instance: GameStorage;
    constructor() {
      if (GameStorage.instance) {return GameStorage.instance;}GameStorage.instance = this;
      this.bag['newtile'] = 'sprite-template';
    }

    addMap(value:TSceneData) {
      this.add(this.mapKey, value);
    }
    getMap():TSceneData {
      return this.get(this.mapKey);
    }

    newTile(key:string) {
      this.add('newtile', key);
    }

    getNewTile():string {
      return this.get('newtile');
    }
    getNewTileData():IGround {
      return {k:this.get('newtile')};
    }

    add(key:string, value:any) {
        this.bag[key] = value;
    }
    
    get(key:string):any {
      return this.bag[key];
    }

    remove(key:string) {

    }

    groundZone():IGroundZone[] {
      return this.bag[this.mapKey].groundZone;
    }
    groundZoneUpdate(grounZone:IGroundZone[]) {
      this.bag[this.mapKey].groundZone = grounZone;
    }
    ground():IGround[][] {
      return this.bag[this.mapKey].ground;
    }
    groundUpdate(ground:IGround[][]) {
      this.bag[this.mapKey].ground = ground;
    }
    wallZone():IWallZone[] {
      return this.bag[this.mapKey].wallZone;
    }
    wallZoneUpdate(wallZone:IWallZone[]) {
      this.bag[this.mapKey].wallZone = wallZone;
    }
    wall():IWall[][] {
      return this.bag[this.mapKey].wall;
    }
    wallUpdate(wall:IWall[][]) {
      return this.bag[this.mapKey].wall = wall;
    }
    propsZone() {

    }
    props() {

    }

    getResources():Array<IResources>{
      return this.bag[this.mapKey].resources;
    }
    setResources(resources:IResources[]) {
      this.bag[this.mapKey].resources = resources;
    }

    

}

export default GameStorage;