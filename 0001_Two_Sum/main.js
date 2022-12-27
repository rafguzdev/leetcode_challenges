let nums = [-1, -2, -3, -4, -5]
let target = -8

const fun = (nums, target) => {
  let idx = undefined
  for (const [idy, num] of nums.entries()) {
    const val = target - num
    idx = nums.indexOf(val, idy + 1)
    if (idx >= 0) {
      return [idy, idx]
    }
  }
}

console.log(fun(nums, target))
