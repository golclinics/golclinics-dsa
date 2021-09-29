const SPACE = " ";

/**
 * Reverses the "words" (not individual characters) in-place
 * @param {string[]} wordsList - an array of characters representing words
 * @returns {string[]} modified, reversed wordsList array
 */
function reverseSentence(wordsList: string[]): string[] {
  let currentIdx = 0;
  const wordStack: string[] = [];

  while (currentIdx < wordsList.length) {
    if (wordsList[currentIdx] !== SPACE) {
      currentIdx = registerWord(wordsList, currentIdx, wordStack);
    }

    if (wordsList[currentIdx] === SPACE) {
      wordStack.push(SPACE);
    }

    currentIdx++;
  }

  wordsList.length = 0;

  while (wordStack.length > 0) {
    const currentWord = wordStack.pop();
    const currentWordArr = currentWord.split("");

    wordsList.push(...currentWordArr);
  }

  return wordsList;
}

/**
 * Build up a word from the wordsList and register it in wordStack
 * @param {string[]} wordsList - an array of characters representing words
 * @param {number} startIdx - index to start constructing a word
 * @param {string[]} wordStack - an array of individually registered words
 * @returns 
 */
function registerWord(
  wordsList: string[],
  startIdx: number,
  wordStack: string[]
): number {
  let currentIdx = startIdx;
  let currentWord = "";

  while (currentIdx < wordsList.length) {
    const currentChar = wordsList[currentIdx];

    if (currentChar === SPACE) break;

    currentWord += currentChar;

    currentIdx++;
  }

  wordStack.push(currentWord);

  return currentIdx;
}

const A = ["t", "h", "i", "s", " ", "i", "s", " ", "g", "o", "o", "d"];
reverseSentence(A);
// A = ['g','o','o','d',' ','i','s',' ','t','h','i','s'];
