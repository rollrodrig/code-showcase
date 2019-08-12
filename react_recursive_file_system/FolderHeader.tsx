import React, { Component } from 'react';
interface Props {
    open:any
    t:any
    onClickFolder: ()=> void
}

interface State {

}
class FolderHeader extends Component<Props, State> {
    render() {
        let k = this.props.open ? "down" : "right";
        let f = this.props.open ? "-open" : "";
        return (<div className="fs_h" onClick={this.props.onClickFolder}>
            <i className={"fas fa-caret-" + k}></i>&nbsp;
                <i className={"fas fa-folder" + f}></i>&nbsp;
                {this.props.t}
        </div>);
    }
}
export default FolderHeader;