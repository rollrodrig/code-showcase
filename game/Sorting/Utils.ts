export default class Utils {
    static distBetweenTwoObjs(o1:{x:number,y:number},o2:{x:number,y:number}) {
        let a = o1.x - o2.x;
        let b = o1.y - o2.y;
        let d = Math.sqrt((a*a) + (b*b));
        return d;
    }
    static splice1(array:any[],index:number){
        var l:number = array.length;
        if (l){
            while (index<l){
                array[index++] = array[index];
            }
            --array.length;
        }
    }
}