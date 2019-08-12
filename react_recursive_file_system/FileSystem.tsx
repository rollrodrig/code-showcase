import React, { Component } from 'react';
import Folder, {TFile} from './Folder';
interface Props {
	assets:TFile[],
}
interface State {
}
class FileSystem extends Component<Props, State> {
    render() {
		let { assets } = this.props;
		let fileStructure = assets.map((f:TFile) =><Folder key={f.fid} folder={f} fn={f.fn} />);
        return (
            <div>
				{fileStructure}
            </div>
        );
    }
}
export default FileSystem