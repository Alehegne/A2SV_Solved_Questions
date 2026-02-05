def generate_subsets(elements):
  n = len(elements)
  subset = []
  result = []
  def search(k):# k is the current index
    if k == n:# all decisions made, add current subset to result
      result.append(subset.copy())
      return
    # choice 1: do not take arr[k]
    search(k + 1)
    # choice 2: take arr[k]
    subset.append(elements[k])
    search(k + 1) # include arr[k]
    subset.pop()# backtrack
  search(0)
  return result


print(sorted(generate_subsets([0,1,2]),key=lambda x:(len(x),x)))