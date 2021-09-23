function getTotalX(a, b) {
    let nums=0;
    for (let x = 0; x <= 100; x++) {
        if (a.every(int => (x % int === 0))) {
            if (b.every(int => (int % x === 0))) {
                nums++;
            }
        }
    }
    return nums;
}

//solution gotten from discussion area. Learnt to put the constraints provided into consideration for the algorith7
