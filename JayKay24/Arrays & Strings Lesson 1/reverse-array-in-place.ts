/**
 * Takes in an array of items and reverses it in-place
 * @param items - an array of items
 * @returns items - original array
 */
function reverseArray<T>(items: T[]): T[] {
  let leftIdx = 0,
    rightIdx = items.length - 1;

  while (leftIdx < rightIdx) {
    swap<T>(items, leftIdx, rightIdx);
    leftIdx++;
    rightIdx--;
  }

  return items;
}

/**
 * Swap items at indexes provided with each other
 * @param arr - an array of items
 * @param idx1 - first index
 * @param idx2 - second index
 */
function swap<T>(arr: T[], idx1: number, idx2: number): void {
  [arr[idx2], arr[idx1]] = [arr[idx1], arr[idx2]];
}

const A = [10, 5, 6, 9];
console.log(reverseArray<number>(A));
// A = [9, 6, 5, 10]