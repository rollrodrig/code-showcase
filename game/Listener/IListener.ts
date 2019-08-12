export enum EventType {
    pointerdown,
    pointerup,
    pointerover,
    pointerout,
    dragstart,
    drag,
    dragend,
    dragenter,
    dragleave,
    drop,
}
export default interface IListener {
    listen(eventType:EventType, data?:any): void;
}
