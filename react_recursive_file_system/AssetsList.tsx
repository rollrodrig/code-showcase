import React, { Component } from 'react';
import TileSprite from './TileSprite';
import { TFile } from './Folder';
interface Props {
    files:TFile[]
    fn:string
}

interface State {

}
class AssetsList extends Component<Props, State> {
    render() {
        let tileSprites = this.props.files.map((f:TFile) => {
            return <TileSprite key={f.fid} file={f} fn={this.props.fn} />;
        });
        return (<div className="pnscroll">
            <div className="grd">
                {tileSprites}
            </div>
        </div>);
    }
}
export default AssetsList;