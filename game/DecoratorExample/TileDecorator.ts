import * as Phaser from 'phaser';
import ITile from './ITile';
namespace Tile {
    export abstract class TileDecorator implements ITile {
        public get x(): number {
            return this.tile.x;
        }
        public get y(): number {
            return this.tile.y;
        }
        public get row(): number {
            return this.tile.row;
        }
        public get column(): number {
            return this.tile.column;
        }
        public get width(): number {
            return this.tile.width;
        }
        public get height(): number {
            return this.tile.height;
        }
        public get scene(): Phaser.Scene {
            return this.tile.scene;
        }
        public get container(): Phaser.GameObjects.Container {
            return this.tile.container;
        }
        public get image(): Phaser.GameObjects.Image {
            return this.tile.image;
        }
        public get id(): number {
            return this.tile.id;
        }
        public getTile():ITile {
            return this.tile.getTile();
        }
        tile: ITile
        constructor(tile: ITile) {
            this.tile = tile;
        }
        create(): void {
            this.tile.create();
            this.implementDecorator();
        }
        addToScene():void {
            this.tile.addToScene();
        }
        abstract implementDecorator(): void;

        disableInteractive():void {}
        enableInteractive():void {}


        getImageKey():string {
            return this.tile.getImageKey()
        }

        remove():void {
            this.tile.remove();
        }
        hide() {
            this.tile.hide();
        }

        show() {
            this.tile.show();
        }

        setDepth(depth:number) {
            this.tile.setDepth(depth);
        }

    }
}
export default Tile.TileDecorator;