
export interface IReactIntersect {
	x:number,
	y:number,
	width:number,
	height:number
}

export interface IRectangle {
	x:number,
	y:number,
	width:number,
	height:number
}


export default class Collider {

    static rangeIntersect(min0:number, max0:number, min1:number, max1:number):boolean {
    	return Math.max(min0, max0) >= Math.min(min1, max1) && Math.min(min0, max0) <= Math.max(min1, max1);
    }

    static rectIntersect(a:IReactIntersect, b:IReactIntersect):boolean {
		  return Collider.rangeIntersect(a.x, a.x + a.width, b.x, b.x + b.width) && Collider.rangeIntersect(a.y, a.y + a.height, b.y, b.y + b.height);
	}

	static isoDetection(a:any,b:any) {
		return a.y > b.y;
	}

}