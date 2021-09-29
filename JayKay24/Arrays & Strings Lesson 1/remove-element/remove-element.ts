/**
 * Remove all occurrences of val in nums in-place
 * @param {number[]} nums - sorted/unsorted array of integers
 * @param {number} val - integer to remove
 * @returns number of remaining items not equal to val after
 * removal of val
 */
function removeElement(nums: number[], val: number): number {
  let currentStart = 0,
    valCount = 0,
    remainingCount = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === val) {
      valCount++;
      currentStart = i;

      while (nums[i] === val && i < nums.length) {
        swap(nums, i, i + 1 >= nums.length ? i : i + 1);

        if (nums[i] !== val) {
          swap(nums, i, currentStart);
          i = currentStart;
          break;
        }

        i++;
      }
    }
  }

  for (let j = 0; j < nums.length; j++) {
    const currentVal = nums[j];

    if (currentVal !== val) remainingCount++;
  }

  return valCount > 0 ? remainingCount : nums.length;
}

/**
 * Swap items at indexes provided with each other
 * @param {number[]} arr - an array of integers that need swapping
 * @param {number} idx1 index to swap with idx2
 * @param {number} idx2 index to swap with idx1
 */
function swap(arr: number[], idx1: number, idx2: number): void {
  [arr[idx2], arr[idx1]] = [arr[idx1], arr[idx2]];
}

const A = [3, 2, 2, 3];
console.log(removeElement(A, 2)); // []
