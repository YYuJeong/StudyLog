import heapq


def solution(scoville, k):
  answer = 0
  scoville.sort()
  heapq.heapify(scoville)

  if scoville[0] >= k:
    return answer
  while scoville[0] < k:
    if len(scoville) == 1:
      return -1
    a = heapq.heappop(scoville)
    b = heapq.heappop(scoville)
    heapq.heappush(scoville, a + (b * 2))
    answer += 1
  return answer
