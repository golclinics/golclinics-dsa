def reverse_by_copy(array)
  reversed = []
  for i in 1..array.size do
    reversed << array[-i]
  end
  reversed
end


def reverse_by_swapping(array)
  i = 0
  j = -1
  while i < array.size/2 do
    array[i], array[j] = array[j], array[i]
    i += 1
    j += -1
  end
  array
end

p(reverse_by_copy([1, 2, 3, 4, 5, 6]))

p(reverse_by_swapping([6, 7, 8, 9, 10]))