import React, { Component } from 'react';
import FolderHeader from './FolderHeader';
import AssetsList from './AssetsList';
export interface TFile {
    id?: string
    uuid?: string
    user_id?: string
    enabled?: boolean
    assets_name?: string
    fn: string
    fid:string
    sf: number
    f?:TFile[]
}
interface Props {
    folder:TFile
    fn:string
}
interface State {
    open:any
}
class Folder extends Component<Props, State> {
    //@ts-ignore
    files:TFile[] = this.props.folder.f;
    state = {
        open:false
    }
    onClickFolder = () => {
        this.setState( prevProps => {
            return {
                open: !prevProps.open
            }
        });
    }    
    render() {
        let subcontent;
        if(this.state.open) {
            if(this.props.folder.sf) {
                subcontent = this.files.map((f:TFile) => {
                    return(<Folder key={f.fid} folder={f} fn={this.props.fn+"/"+f.fn+"/"} />);
                });
            }else {
                subcontent = <AssetsList files={this.files} fn={this.props.fn} />;
            }
        }
        return (
            <div className="fs">
                <FolderHeader t={this.props.folder.fn} onClickFolder={this.onClickFolder} open={this.state.open} />
                <div className="fs_b">
                    {subcontent}
                </div>
            </div>
        );
    }
}
export default Folder;