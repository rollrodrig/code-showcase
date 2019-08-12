/**
 * Given an array with nested arrays it return a one dimension array
 *
 * @param {any[]} arr               An array with optional nested arrays
 * @returns {number[]} flated       A new one dimention aray      
 */
function flatarray(arr:any[]) {
    if( !Array.isArray(arr)) throw new Error(`${arr} is not an array`); 
    let flated = [];
    let l = arr.length;
    for (let i = 0; i < l; i++) {
        // if element is array, call the function flatarray again with the current element.
        if(Array.isArray(arr[i])) {
            flated = flated.concat(flatarray(arr[i]));
        } else {
            flated.push(arr[i]);
        }
    }
    return flated;
}
import { assert, expect } from 'chai';
describe('flatarray', () => {
    it('should return the flated array', () => {
        expect(flatarray([1,2,3])).to.deep.eq([1,2,3]);
        expect(flatarray([1,[2],3])).to.deep.eq([1,2,3]);
        expect(flatarray([1,[2,3,4],5])).to.deep.eq([1,2,3,4,5]);
        expect(flatarray([1,[2,[[3],4]],5,6])).to.deep.eq([1,2,3,4,5,6]);
        expect(flatarray([1,[2,[[3],4]],5,[6,[7,[8]]],9])).to.deep.eq([1,2,3,4,5,6,7,8,9]);
    });
});