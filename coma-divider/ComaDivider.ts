export const comaDivider = (string: string) => {
    let braces: number = 0;
    const indexes: number[] = [];
    const divided: string[] = [];
    const l = string.length;
    for (let i = 0; i < l; i++) {
        const c = string.charAt(i);
        if (c === "{") {
            braces++;
        }
        if (c === "}") {
            braces--;
        }
        if (c === "," && braces === 0) {
            indexes.push(i);
        }
    }
    indexes.push(string.length);
    indexes.reduce((prev: number, next: number) => {
        divided.push(string.substring(prev, next));
        return next + 1;
    }, 0);
    return divided;
};