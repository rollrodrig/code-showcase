import React, { Component } from 'react';
import { connect } from 'react-redux';
import { TFile } from './Folder';
import { TileActions, TTilePayload } from '../../reducers/Tile';
interface Props {
    selection?:any
    UpdateTile:(type:TileActions, payload:TTilePayload)=> void
    file:TFile
    fn:string
}
interface State {

}
export interface TSpriteSelected {
    fn: string,
    fid: string, 
}
const HOST = "";
const ASSETS = "/assets/store/";
class EntitySprite extends Component<Props, State> {
    fn = this.props.fn+this.props.file.fn;
    fid = this.props.file.fid;
    onSelectSprite = () => {
        let type: TileActions = TileActions.TILE_SET_SPRITE;
        let payload: TTilePayload = {
            sprite:ASSETS+this.fn,
            asset_pack_name:"Angel Art Dungeon 2019",
            sprite_path:" angel_art_dungeons_2019 > walls > wall_dark",
        }
        this.props.UpdateTile(type, payload);
    }
    render() {
        return (
            <div className="grditm" onClick={this.onSelectSprite}>
                <div className="sprite">
                    <img src={HOST+ASSETS+this.fn} alt={this.fid} />
                </div>
            </div>
        );
    }
}
const mapStateToProps = (state:any) => {
	return {
	}
}
const mapDispatchToProps = (dispatch:any) => {
	return {
        UpdateTile: (type:TileActions, payload:TTilePayload) => dispatch({type, payload}),
	}
}
export default connect(mapStateToProps,mapDispatchToProps)(EntitySprite);