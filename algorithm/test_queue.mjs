import { Queue } from "./Queue.mjs";

let queue = new Queue();

console.log("========= 첫 번째 출력 ==========");
queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3);

console.log(queue.front());

console.log("========= 두 번째 출력 ==========");
console.log(queue.dequeue());
console.log(queue.dequeue());
console.log(queue.dequeue());
console.log(queue.dequeue());

console.log(`isEmpay: ${queue.isEmpty()}`);
